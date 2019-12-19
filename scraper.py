import pandas as pd
import pyttsx3
from random import seed
from random import randint
import requests
from bs4 import BeautifulSoup

def listSongs():
    req = requests.get('https://www.metrolyrics.com/death-grips-lyrics.html');
    if req.status_code == 200:
        print("successful request")
        content = req.content
    soup = BeautifulSoup(content,'html.parser')
    links = {}
    links = soup.find_all('a',attrs={'class':'title'})
    i = randint(0,len(links)-1)
    lyricLink = links[i]['href']
    return lyricLink

def getLyric(lyricLink):
    voz = pyttsx3.init()
    voz.setProperty('rate',100)
    req = requests.get(lyricLink)
    if req.status_code == 200:
        print("successful request")
        content = req.content

    soup = BeautifulSoup(content,'html.parser')
    lyric = {}
    lyric = soup.find_all('p',attrs={'class':'verse'})
    i = randint(0, len(lyric)-1)
    stanza = lyric[i].text.strip()
    verseList = {}
    verseList = stanza.splitlines()
    j = randint(0, len(verseList)-1)
    verse = verseList[j]
    print(verse)
    voz.say(verse)
    voz.runAndWait()
    voz.stop()

def main():
    lyricLink = listSongs();
    getLyric(lyricLink)

if __name__ == "__main__" :
    main()
