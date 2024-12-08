import requests,json
def count_lines(input_string):
    if not input_string:
        return 0  # Handle empty strings
    return len(input_string.splitlines())
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
data = '{"model": "gemma:2b", "prompt": "hi how are you"}'
response = requests.post('http://localhost:11434/api/generate', headers=headers, data=data)
data = response.text
# Split the string by newline and parse each part as JSON
json_objects = [json.loads(line) for line in data.splitlines()]

# Access and print the value of 'love_2' from the second JSON object
# print(json_objects[0]["response"])
lines = count_lines(data)
result = ''
for new in range(0,lines):
    # print(json_objects[new]["response"], end='')
    result += json_objects[new]["response"]


result = str(result)
print(result)

from gtts import gTTS
mytext = result
language = 'bn'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")



from pydub import AudioSegment

# Specify file paths
mp3_file = "welcome.mp3"  # Replace with your MP3 file path
wav_file = "output_8bit.wav"  # Replace with desired WAV file path

# Load MP3 and export as 8-bit WAV
audio = AudioSegment.from_mp3(mp3_file)
audio = audio.set_sample_width(1)  # 8-bit audio has 1 byte per sample
audio.export(wav_file, format="wav")

print(f"Conversion to 8-bit WAV complete. Saved as {wav_file}.")



