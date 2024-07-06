import os, shutil

def run():
    shutil.rmtree('wav', ignore_errors=True)
    shutil.rmtree('mp3', ignore_errors=True)
    shutil.rmtree('txt', ignore_errors=True)
    shutil.rmtree('whisper.cpp', ignore_errors=True)

if __name__=="__main__": 
    run()