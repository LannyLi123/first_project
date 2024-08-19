from pytube import YouTube
import os
import subprocess

def download_youtube_video(url, output_path):
    yt = YouTube(url)
    
    # 获取最高分辨率的视频流和音频流
    video_stream = yt.streams.filter(adaptive=True, file_extension='mp4').order_by('resolution').desc().first()
    audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()

    # 下载视频和音频流
    video_path = video_stream.download(output_path=output_path, filename='video.mp4')
    audio_path = audio_stream.download(output_path=output_path, filename='audio.mp4')
    
    return video_path, audio_path

import subprocess
import os

def merge_video_audio(video_path, audio_path, output_path):
    # 构建输出文件的完整路径
    output_file = os.path.join(output_path, 'final_output.mp4')
    command = [
        r'C:\ffmpeg\bin\ffmpeg.exe',  # 使用 FFmpeg 的绝对路径
        '-i', video_path,
        '-i', audio_path,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-strict', 'experimental',
        output_file
    ]
    try:
        # 执行 FFmpeg 命令合并视频和音频
        subprocess.run(command, check=True)
        print(f"合并完成，输出文件保存在：{output_file}")
    except subprocess.CalledProcessError:
        print("合并失败，请检查输入文件和参数")
    except FileNotFoundError:
        print("未找到 ffmpeg 可执行文件，请确保已安装并将其添加到系统 PATH 中")



def main():
    url = input("请输入 YouTube 视频的 URL: ")
    output_path = r'C:\Users\Lanny\Desktop\Lanny\youtube视频搬运'
    
    # 下载视频和音频
    video_path, audio_path = download_youtube_video(url, output_path)
    print(f'视频已下载到: {video_path}')
    print(f'音频已下载到: {audio_path}')
    
    # 合并视频和音频
    merge_video_audio(video_path, audio_path, output_path)

    if os.path.exists(r'C:\Users\Lanny\Desktop\Lanny\youtube视频搬运\video.mp4'):
        os.remove(r'C:\Users\Lanny\Desktop\Lanny\youtube视频搬运\video.mp4')
    if os.path.exists(r'C:\Users\Lanny\Desktop\Lanny\youtube视频搬运\audio.mp4'):
        os.remove(r'C:\Users\Lanny\Desktop\Lanny\youtube视频搬运\audio.mp4')
    return 0

if __name__ == '__main__':
    main()
