import os
import subprocess

# files = os.listdir('C:/Projects/AI/resources/Tutorial')
files = os.listdir('resources/Tutorial')
for file in files[1:]:
	tutorial_number = file.split(" ")[0]
	tutorial_name = file.split("- ")[1].split(" Project 3")[0]
	print(tutorial_number)
	print(tutorial_name)
	subprocess.run(["ffmpeg", "-i", f"resources/Tutorial/{file}", f"resources/Tutorial_Audio/{tutorial_number}_{tutorial_name}.mp3"])