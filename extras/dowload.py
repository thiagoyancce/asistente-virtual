from pytube import YouTube
import os 
import pywhatkit
import requests
def dowloadVideo(name):
    y=pywhatkit.playonyt(name,open_video=False)
    url =requests.get(y).url
    video=YouTube(url)
    descarga=video.streams.get_highest_resolution()
    descarga.download()


def dowloadMp3(name):
    y=pywhatkit.playonyt(name)
    url =requests.get(y).url
    video=YouTube(url)
    out_path=video.streams.filter(only_audio=True).first().download()
    new_name=os.path.splitext(out_path)
    os.rename(out_path,new_name[0]+'.mp3')
'''
name=input("Enter the name of the video:")
y=pywhatkit.playonyt(name)
url =requests.get(y).url
dowloadMp3(url)
print(url)'''