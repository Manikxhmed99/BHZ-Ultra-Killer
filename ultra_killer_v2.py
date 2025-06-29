import os
import time

# Color codes
G = "\033[1;32m"  # Green
R = "\033[1;31m"  # Red
Y = "\033[1;33m"  # Yellow
B = "\033[1;34m"  # Blue
C = "\033[1;36m"  # Cyan
M = "\033[1;35m"  # Magenta
RESET = "\033[0m"

def typewrite(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def banner():
    os.system("clear")
    print(G)
    typewrite("╔══════════════════════════════════════════════╗", 0.002)
    typewrite("║         🔥 BHZ ULTRA COPYRIGHT KILLER        ║", 0.005)
    typewrite("║            ADMIN: MD MANIK AHMED             ║", 0.005)
    typewrite("╚══════════════════════════════════════════════╝", 0.002)
    print(RESET)

def ensure_folders():
    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)

def get_inputs():
    print(f"{C}📥 Enter your video filename (inside 'input/'): {RESET}")
    video = input("🎞️ Filename: ")
    print(f"{C}🎵 Optional background music (inside 'input/') or press Enter: {RESET}")
    music = input("🎧 Music File: ")
    return f"input/{video}", (f"input/{music}" if music else ""), f"output/safe_{video}"

def process_video(video_in, music_in, video_out):
    print(f"\n{B}🔄 Processing your video with ultra filters... Please wait...{RESET}\n")

    video_filter = (
        f'-vf "scale=1280:720,eq=brightness=0.08:saturation=1.4:contrast=1.1" '
        f'-af "asetrate=44100*1.04,atempo=1.08,volume=1.2" '
    )

    if music_in:
        filter_complex = (
            f'-i "{video_in}" -i "{music_in}" '
            f'-filter_complex "[0:a]volume=1.0[a0];[1:a]volume=0.5[a1];[a0][a1]amix=inputs=2:duration=shortest[a]" '
            f'-map 0:v -map "[a]"'
        )
    else:
        filter_complex = f'-i "{video_in}"'

    cmd = (
        f'ffmpeg -y {filter_complex} '
        f'{video_filter} '
        f'-map_metadata -1 '
        f'-metadata title="" -metadata artist="" -metadata comment="" '
        f'-c:v libx264 -c:a aac -preset ultrafast -crf 28 "{video_out}"'
    )

    os.system(cmd)
    print(f"\n{G}✅ Successfully processed!\n📁 Output saved to: {Y}{video_out}{RESET}\n")

def main():
    banner()
    ensure_folders()
    video_in, music_in, video_out = get_inputs()

    if not os.path.exists(video_in):
        print(f"{R}[✘] Error: Video file not found in 'input/' folder.{RESET}")
        return

    if music_in and not os.path.exists(music_in):
        print(f"{Y}[!] Warning: Music file not found. Proceeding without music...{RESET}")
        music_in = ""

    process_video(video_in, music_in, video_out)

if __name__ == "__main__":
    main()
