# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#######Usage snippets##############
# import youtube_dl
#
# ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
#
# with ydl:
#     result = ydl.extract_info(
#         'http://www.youtube.com/watch?v=BaW_jenozKc',
#         download=False # We just want to extract the info
#     )
#
# if 'entries' in result:
#     # Can be a playlist or a list of videos
#     video = result['entries'][0]
# else:
#     # Just a video
#     video = result
#
# print(video)
# video_url = video['url']
# print(video_url)
####################################

ALBUMNAME = "Myalbum/"

import yt_dlp

def downloadVideo(address,index):
    with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': ALBUMNAME+"/"+'%(title)s.mp3'}) as video:
        info_dict = video.extract_info(address, download=True)
        video_title = info_dict['title']
        print(video_title)
        video.download(address)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open("videolist.txt")
    i = 1
    videolist = file.readlines()
    ALBUMNAME = videolist[0].rstrip()
    videolist = videolist[1:]

    for line in videolist:
        downloadVideo(line.rstrip(),i)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

