from gtts import gTTS
mytext = 'ami tumake valo bashi'
language = 'bn'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")