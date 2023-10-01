ALBUMNAME = "Myalbum"

import yt_dlp

def downloadVideo(address,index):
    with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': ALBUMNAME+"/"+'%(title)s.mp3'}) as video:
        info_dict = video.extract_info(address, download=True)
        video_title = info_dict['title']
        print(video_title)
        video.download(address)

if __name__ == '__main__':
    file = open("videolist.txt")
    i = 1
    videolist = file.readlines()
    ALBUMNAME = videolist[0].rstrip()
    videolist = videolist[1:]

    for line in videolist:
        downloadVideo(line.rstrip(),i)


