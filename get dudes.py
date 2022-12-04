import os, whisper, threading

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

def checkDudes(input):
    transscription = transcribeVideo(f'./data/xqc-audio/{file}')
    transscription = transscription["text"]
    transscription = transscription.split()
    
    for i in transscription:
        if hasDude(i):
            total_dudes += 1
            print(f'Found: {total_dudes} dudes.')

total_dudes = 0
threads = []

for i in range(len(files)):
    file = files[i]
    print(f'\n\nStarting thread for file: {file}')
    print(f'Progress: {i+1}/{len(files)}')

    t = threading.Thread(target=checkDudes, args=(file,))
    threads.append(t)
    t.start()
    
