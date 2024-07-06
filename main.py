import sys
import scripts.download_mp3
import scripts.install_whisper
import scripts.mp3_to_wav
import scripts.wav_to_text
import scripts.cleanup

kwargs = dict(
    model="base.en", 
    test_files=[3],
    resources=[],
)

for arg in sys.argv[1:]: 
    if arg[:2]=='--': 
        if arg[2:]=='model': 
            kwargs['model']=arg[2:]
        if arg[2:]=='test_files': 
            kwargs['test_files']=[int(a) for a in arg[2:].split(',')]
    else: 
        kwargs['resources'].append(arg)
    
if not kwargs['resources']: 
    kwargs['resources'] = scripts.download_mp3.default_resources

scripts.download_mp3.run(*kwargs['resources'])
scripts.install_whisper.run(kwargs['model'])
scripts.mp3_to_wav.run(*kwargs['test_files'])
scripts.wav_to_text.run(*kwargs['test_files'], model=kwargs['model'])
scripts.cleanup.run()
