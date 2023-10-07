ALBUMNAME = "Myalbum"



import yt_dlp
import mutagen
from mutagen.easyid3 import EasyID3

def getFilename(title):
    filename = ALBUMNAME + "/" + title + ".mp3"
    return filename

def setAlbumIndex(file,index):
    try:
        metatag = EasyID3(file)
    except mutagen.id3.ID3NoHeaderError:
        metatag = mutagen.File(file, easy=True)
        metatag.add_tags()
    metatag['album'] = ALBUMNAME
    metatag['tracknumber'] = str(index)
    metatag.save()


def sanitizeFilename(string):
    prefix = len(ALBUMNAME) + 1
    substring = string[prefix:]
    substring = substring.replace("|","｜").replace(":","：").replace("/","⧸")
    return ALBUMNAME + "/" + substring

def downloadVideo(address,index):

    options = {'extract_audio': True,
               'restrict-filenames' : True,
               'format': 'bestaudio',
               'outtmpl': ALBUMNAME + "/" + '%(title)s',
               'postprocessors': [{
                   'key': 'FFmpegExtractAudio',
                   'preferredcodec': 'mp3',
                   'preferredquality': '192',
               },
                   {
                       'key': 'FFmpegMetadata'
                   }]
               }

    with yt_dlp.YoutubeDL(options) as video:
        info_dict = video.extract_info(address, download=False)
        video_title = info_dict['title']
        print(video_title)
        video.download(address)
        setAlbumIndex(sanitizeFilename(getFilename(video_title)),index)

if __name__ == '__main__':
    file = open("videolist.txt")
    i = 1
    videolist = file.readlines()
    ALBUMNAME = videolist[0].rstrip()
    videolist = videolist[1:]

    for line in videolist:
        downloadVideo(line.rstrip(),i)
        i+=1


def metadataTest():
    filepath = "2024/Bury the Light - Vergil's battle theme from Devil May Cry 5 Special Edition.mp3"
    try:
        audio = EasyID3(filepath)
    except mutagen.id3._util.ID3NoHeaderError:
        audio = mutagen.File(filepath, easy=True)
        audio.add_tags()
    audio['album'] = u"2024"
    audio.save()
    audio = EasyID3("2024/Bury the Light - Vergil's battle theme from Devil May Cry 5 Special Edition.mp3")
    print(audio['album'])

