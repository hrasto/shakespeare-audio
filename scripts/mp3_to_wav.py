import subprocess, os, sys

def run(*test_files):
    os.makedirs('wav', exist_ok=True)

    if not os.path.isdir('mp3'): 
        print(f"{os.path.basename(__file__)}: cant find the mp3 folder => exiting")
        return

    # 1. we convert all mp3s to 16kHz/16bit wav which the whisper model can work with 
    for fname in os.listdir('mp3'):
        if fname[-4:] != '.mp3' or fname == 'zip': continue
        fname_wav = fname.replace('.mp3', f'.pcm_s16le.16000.wav')
        args = f"ffmpeg -y -i mp3/{fname} -ar 16000 -ac 1 -c:a pcm_s16le wav/{fname_wav}"
        subprocess.call(args.split())

    # 2. we create a single wav for train/test by concatenating single wavs
    files = sorted(os.listdir('wav'))
    train = ['wav/'+files[i] for i in range(len(files)) if i not in test_files]
    test = ['wav/'+files[i] for i in test_files]
    print(f"{os.path.basename(__file__)}: train resources: ", ", ".join(train))
    print(f"{os.path.basename(__file__)}: test resources: ", ", ".join(test))
    args = f"sox {' '.join(train)} train.16kHz.16bit.wav"
    subprocess.call(args.split())
    args = f"sox {' '.join(test)} test.16kHz.16bit.wav"
    subprocess.call(args.split())

    # 3. we downsample to 8kHz/8bit    
    args = f"ffmpeg -y -i train.16kHz.16bit.wav -ar 8000 -ac 1 -acodec pcm_u8 train.8kHz.8bit.wav"
    subprocess.call(args.split())
    args = f"ffmpeg -y -i test.16kHz.16bit.wav -ar 8000 -ac 1 -acodec pcm_u8 test.8kHz.8bit.wav"
    subprocess.call(args.split())

if __name__=="__main__":
    os.chdir("../")
    run(*sys.args[1:])