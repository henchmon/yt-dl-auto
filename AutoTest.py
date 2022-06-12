##Script for crontab task automation
from datetime import datetime
from yt_dlp import YoutubeDL

#Shows current time
print("Current Time: " + datetime.now().strftime("%H:%M"))


#Opens URLS.txt
URLS = open('/home/marcus/Desktop/URLS.txt', 'r')

#Parses URLS.txt and runs yt-dlp each loop with the current line as an argument
for line in URLS:
	print("\n" + line)
	html = line
	#runs yt-dlp for URL
	with YoutubeDL() as ydl:
		ydl.download(html)
