from urllib.request import Request, urlopen

import urllib

ad2="http://www.institutomendoza.com/audio/starter/classaudio2/AEF2CLASSAUDIO2/5.1.mp3"



import urllib.request
with urllib.request.urlopen(ad2) as url:
    s = url.read()
#I'm guessing this would output the html source code?
print(s)