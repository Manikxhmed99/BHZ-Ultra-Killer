#!/usr/bin/env python3 import os import subprocess import time from termcolor import cprint

🔥 Colorful Banner

def banner(): os.system("clear") banner_lines = [ "\n", "\033[1;32m██████╗ ██████╗ ██╗\033[0m", "\033[1;32m██╔══██╗██╔══██╗██║\033[0m", "\033[1;32m██████╔╝██████╔╝██║\033[0m", "\033[1;32m██╔═══╝ ██╔═══╝ ██║\033[0m", "\033[1;32m██║     ██║     ██║\033[0m", "\033[1;32m╚═╝     ╚═╝     ╚═╝\033[0m", "\033[1;34m🔥 BHZ - COPYRIGHT KILLER TOOL\033[0m", "\033[1;34m👑 ADMIN: MANIK AHMED\033[0m", "\033[1;30m====================================\033[0m\n" ] for line in banner_lines: print(line) time.sleep(0.1)

🧠 Auto process all videos in input/

def process_all_videos(): input_folder = "input" output_folder = "output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(input_folder)
video_files = [f for f in files if f.lower().endswith((".mp4", ".mkv", ".mov", ".avi"))]

if not video_files:
    cprint("\n⚠️ No videos found in 'input/' folder!", "red")
    return

total = len(video_files)

for i, file in enumerate(video_files):
    input_path = os.path.join(input_folder, file)
    output_path = os.path.join(output_folder, f"edited_{file}")

    percent = int(((i + 1) / total) * 100)
    cprint(f"\n🎬 Editing: {file}  [{percent}% done]", "cyan")
    time.sleep(1)

    cmd = [
        "ffmpeg", "-i", input_path,
        "-vf", "scale=1280:720,eq=contrast=1.2:brightness=0.06:saturation=1.3,hue=s=0.8,drawbox=x=10:y=10:w=100:h=60:color=black@0.3:t=fill",
        "-af", "asetrate=44100*1.04,atempo=1.05,volume=0.8,highpass=f=200,lowpass=f=3000",
        "-metadata", "title=", "-metadata", "comment=", "-metadata", "author=",
        "-map_metadata", "-1",
        "-c:v", "libx264", "-c:a", "aac", "-crf", "28",
        output_path, "-y"
    ]

    subprocess.run(cmd)
    cprint(f"✅ Saved: {output_path}", "green")

cprint("\n🎉 All videos processed successfully!", "yellow", attrs=["bold"])

🚀 Run Script

if name == "main": banner() process_all_videos()
