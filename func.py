import os
from time import sleep
import requests
from moviepy.editor import * 

def mp4(url_video):
    url = f'{url_video}'
    r = requests.get(url, allow_redirects=True)
    open('video.mp4', 'wb').write(r.content)
    video = VideoFileClip(r"video.mp4")
    audio = video.audio
    audio.write_audiofile(r"audio.mp3")

    audio.close()
    video.close()
    sleep(30.0)
    os.remove('video.mp4')
    os.remove('audio.mp3')


# mp4('https://uzhits.net/dl3/mobile/Ummon_guruhi_-_Yettinchi_qavat_uzhits.net.mp4')



