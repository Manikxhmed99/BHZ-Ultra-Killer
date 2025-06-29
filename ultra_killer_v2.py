# BHZ Ultra Killer v2 - Python Script for Termux
# Admin: Md Manik Ahmed

import os
import subprocess
import time

def banner():
    os.system("clear")
    print("\033[1;32m")
    print("██████╗ ██╗  ██╗███████╗    ██╗   ██╗██╗     ██████╗ ██████╗  █████╗")
    print("██╔══██╗██║  ██║██╔════╝    ██║   ██║██║     ██╔══██╗██╔══██╗██╔══██╗")
    print("██████╔╝███████║█████╗      ██║   ██║██║     ██████╔╝██████╔╝███████║")
    print("██╔═══╝ ██╔══██║██╔══╝      ╚██╗ ██╔╝██║     ██╔═══╝ ██╔═══╝ ██╔══██║")
    print("██║     ██║  ██║███████╗     ╚████╔╝ ███████╗██║     ██║     ██║  ██║")
    print("╚═╝     ╚═╝  ╚═╝╚══════╝      ╚═══╝  ╚══════╝╚═╝     ╚═╝     ╚═╝  ╚═╝")
    print("\n\033[1;31m         ⚠️ BHZ Ultra Copyright Killer Loaded ⚠️")
    print("\033[0m")

def process_video(input_path, output_path):
    print("\033[1;36m[•] Processing video for copyright bypass...\033[0m")
    try:
        # Modify video using ffmpeg to bypass copyright
        command = [
            "ffmpeg",
            "-i", input_path,
            "-vf", "scale=1280:720,hue=s=0,eq=brightness=0.06:saturation=1.2",
            "-af", "asetrate=44100*1.05,aresample=44100,atempo=1.1",
            "-metadata", "title=Custom",
            "-metadata", "author=BHZ-ADMIN",
            "-preset", "ultrafast",
            output_path
        ]
        subprocess.run(command, check=True)
        print("\033[1;32m[✔] Video processed and saved to:", output_path, "\033[0m")
    except subprocess.CalledProcessError:
        print("\033[1;31m[✘] Failed to process the video. Check if ffmpeg is installed.\033[0m")

def main():
    banner()
    input_path = input("\033[1;34m[📥] Enter input video path (e.g., input/video.mp4): \033[0m")
    output_path = input("\033[1;35m[📤] Enter output path (e.g., output/video-edited.mp4): \033[0m")

    if not os.path.exists(input_path):
        print("\033[1;31m[✘] Input file not found!\033[0m")
        return

    process_video(input_path, output_path)

if __name__ == "__main__":
    main()
