from pytube import YouTube

link = YouTube('https://www.youtube.com/watch?v=l4BSJZnEX_c&list=RDeM8Mjuq4MwQ&index=2')
video = link.streams.get_highest_resolution()
video.download()
