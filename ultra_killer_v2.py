import os
import subprocess
from datetime import datetime

# 📁 Folder prepare
os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

print("🎬 BHZ Ultra Copyright Killer")
videofile = input("🎞️ ভিডিও ফাইল নাম দিন (input ফোল্ডারে রাখুন): ")
musicfile = input("🎵 ব্যাকগ্রাউন্ড মিউজিক ফাইল দিন (input ফোল্ডারে): ")

invid = f"input/{videofile}"
inmus = f"input/{musicfile}"
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
outvid = f"output/ultra_safe_{videofile.split('.')[0]}_{timestamp}.mp4"

# 💥 Advanced FFmpeg Command
command = [
    "ffmpeg",
    "-y",
    "-i", invid,
    "-i", inmus,
    "-filter_complex",
    "[0:v]scale=1280:720,setpts=PTS-STARTPTS,eq=brightness=0.04:saturation=1.2,"
    "zoompan=z='if(lte(zoom,1.0),1.001,zoom+0.001)':d=1:x='iw/2':y='ih/2',"
    "drawbox=x=30:y=30:w=250:h=80:color=black@0.3:t=fill[vid];"
    "[1:a]volume=0.3,asetrate=44100*0.97,atempo=1.04,"
    "aecho=0.8:0.88:60:0.4,firequalizer=gain_entry='entry(0,-25);entry(250,-13);entry(6000,5)',"
    "highpass=f=200,lowpass=f=800[aud]",
    "-map", "[vid]",
    "-map", "[aud]",
    "-c:v", "libx264",
    "-c:a", "aac",
    "-b:v", "1400k",
    "-b:a", "128k",
    "-preset", "ultrafast",
    "-crf", "27",
    "-shortest",
    "-metadata", "title=",
    "-metadata", "artist=",
    "-metadata", "comment=",
    "-metadata", "composer=",
    "-metadata", "encoded_by=",
    "-metadata", "publisher=",
    outvid
]

print("\n⏳ প্রক্রিয়া চলছে... কিছু সময় লাগবে...")
subprocess.run(command)

print(f"\n✅ সফলভাবে তৈরি: {outvid}")