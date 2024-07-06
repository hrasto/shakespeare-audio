import os, subprocess, re, sys

def run(*test_files, model="base.en"): 

    os.makedirs('txt', exist_ok=True)

    files = sorted(f.replace('.wav', '') for f in os.listdir("wav"))

    for fname in files:
        if not os.path.isfile('txt/'+fname+'.csv'): 
            print('transcribing', fname)
            subprocess.call(f"whisper.cpp/main -f wav/{fname}.wav -of txt/{fname} -ocsv -ml 1 -m whisper.cpp/models/ggml-{model}.bin".split())

    with open('test.csv', 'w') as out: 
        for i in test_files: 
            with open(f"txt/{files[i]}.csv", "r") as f: 
                for i, line in enumerate(f): 
                    if i == 0: continue
                    out.write(line)

    with open('train.csv', 'w') as out: 
        for i in range(len(files)): 
            if i in test_files: continue
            with open(f"txt/{files[i]}.csv", "r") as f: 
                for i, line in enumerate(f): 
                    if i == 0: continue
                    out.write(line)

    with open('train.txt', 'w') as out: 
        for i, fname in enumerate(files): 
            if i in test_files: continue
            with open(f'txt/{fname}.csv', 'r') as f: 
                for line in f: 
                    if line == 'start,end,text\n': continue
                    line = line[:-1] # delete the newline
                    line = re.sub(pattern=r"[0-9]+,[0-9]+,", repl="", string=line) # delete the timestamps
                    line = line[1:-1] # delete the quotation marks
                    out.write(line)

    with open('test.txt', 'w') as out: 
        for i in test_files:
            fname = files[i]
            print(fname)
            with open(f'txt/{fname}.csv', 'r') as f: 
                for line in f: 
                    if line == 'start,end,text\n': continue
                    line = line[:-1] # delete the newline
                    line = re.sub(pattern=r"[0-9]+,[0-9]+,", repl="", string=line) # delete the timestamps
                    line = line[1:-1] # delete the quotation marks
                    out.write(line)

if __name__=="__main__":
    os.chdir("../")
    run(*sys.args[1:])