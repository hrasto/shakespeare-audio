import os, subprocess, sys

def run(model="base.en"):
    # download whisper
    if not os.path.isdir('whisper.cpp'): 
        print(f"{os.path.basename(__file__)}: cloning the git repository...")
        subprocess.call("git clone https://github.com/ggerganov/whisper.cpp.git".split())

    # download the model
    if not os.path.isfile(f"whisper.cpp/models/ggml-{model}.bin"):
        subprocess.call(f"bash ./whisper.cpp/models/download-ggml-model.sh {model}".split())
    else: 
        print(f"{os.path.basename(__file__)}: model {model} found => skipping download")

    # install whisper in this directory
    process = subprocess.Popen(["make"], stdout=subprocess.PIPE, cwd="whisper.cpp/")
    process.wait()

if  __name__=="__main__": 
    os.chdir("../")
    run(*sys.argv[1:])