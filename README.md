# verse_grabber

A super simple Python3 script that grabs and says out loud a random verse from a random song from Death Grips.
Has some bugs, but it's reliable most of the time.
All lyrics are grabbed from MetroLyrics (https://www.metrolyrics.com/).

#### Libraries used:
* pyttsx3;
* random;
* requests;
* BeautifulSoup4. 

#### Known Bugs:
* sometimes it doesn't have a range to generate a random number;
* it may grab and say text that isn't part of the lyrics (like "Song by Death Grips")
