from gtts import gTTS
import os
import playsound
import pypandoc
#This is just sample code but it can be refactored and made more efficient
#converting different formats using pandocs
doc = pypandoc.convert_file('/Users/nikhilgautam/PycharmProjects/pandoctester/test.html','plain',outputfile='test.plain')
doc2 = pypandoc.convert_file('/Users/nikhilgautam/PycharmProjects/pandoctester/Sway.epub','plain',outputfile='test2''.plain')
file1 = open("/Users/nikhilgautam/PycharmProjects/pandoctester/test.plain", "r")
file2 = open("/Users/nikhilgautam/PycharmProjects/pandoctester/test2.plain", "r")

file = "file.mp3"
filex = "file2.mp3"

# initialize tts, create mp3 and play
tts = gTTS(text=file1.read(), lang='en-uk', slow=False)
tts.save(file)
tts2 = gTTS(text=file2.read(), lang='en-uk', slow=False)
tts2.save(filex)

# playing the sound
playsound.playsound(file)
playsound.playsound(filex)

