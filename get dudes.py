#!pip install git+https://github.com/openai/whisper.git

import whisper
import os

import os

files = os.listdir("./data/xqc-audio/")

def transcribeVideo(path):
    model = whisper.load_model('tiny')
    out = model.transcribe(path, fp16=False)
    
    return out

def hasDude(input):
    if "dude" in input.lower():
        return True
    else:
        return False

total_dudes = 0

for i in range(len(files)):
    file = files[i]
    print(f'\n\nTrying file: {file}')
    print(f'Progress: {i+1}/{len(files)}')
    transscription = transcribeVideo(f'./data/xqc-audio/{file}')
    transscription = transscription["text"]
    transscription = transscription.split()
    
    for i in transscription:
        if hasDude(i):
            total_dudes += 1
            print(f'Found: {total_dudes} dudes.')