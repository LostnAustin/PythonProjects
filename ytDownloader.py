from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)


print("Title: ", yt.title)
print("View: ", yt.views)

#Get title and views of supplied YouTube video link
#EG) python3 ytDownloader.py "youtube.com/adfsf"

yd = yt.streams.get_highest_resolution()

#Download and add to specified folder
yd.download('/Users/chadlengefeld/Desktop/youTubeDLs')