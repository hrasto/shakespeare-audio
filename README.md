# Shakespeare audio

Python scripts for building a dataset of parallel audio and text suitable for machine learning experiments (e.g. language modeling).

By default, it downloads 3 shakespeare plays from [LibriVox](https://librivox.org) ([Romeo & Juliet](https://librivox.org/romeo-and-juliet-version-4-by-william-shakespeare/), [Hamlet](https://librivox.org/hamlet-version-3-by-william-shakespeare/) and [As You Like It](https://librivox.org/as-you-like-it-version-3-by-william-shakespeare/)), and transcribes them using [whisper.cpp](https://github.com/ggerganov/whisper.cpp).
These recordings were created by volunteers, contain several male and female voices, and a variety of English accents.

## Quick start

You need to have [ffmpeg](https://ffmpeg.org) and [sox](https://sourceforge.net/projects/sox/) installed.
If you have them, you can clone the repository and run the main.py script: 

```
git clone https://github.com/hrasto/shakespeare-audio
cd shakespeare-audio
pip install -r requirements.txt
python main.py
```

The script may run for several minutes, as it needs to download and extract the archives, convert the mp3s to wavs, and run whisper to transcribe word by word, so that we can align the waveforms with the text via precise timestamps.

To delete the downloaded files that we used to build the corpus, run `python cleanup.py`.

The directory should now contain the following files: 
- `train.16kHz.16bit.wav`: training waveform at 16000 16bit samples per second
- `train.csv`: comma-separated file containing token timestamps back-to-back (w.r.t. samples in `train.16kHz.16bit.wav`)
- `train.txt`: textfile containing the bare text
- `train.8kHz.8bit.wav`: a low-resolution version of the waveform
- the same for `test` files

## Slow start

The main.py script accepts several arguments. You can: 

- `--model` specify the whisper model to be used for transcription (see [whisper.cpp](https://github.com/ggerganov/whisper.cpp/tree/master/models) for more info)
- `--test_files` specify the indices of (sorted) files to be used for the test set (corresponds with recordings per act) separated by comma, e.g. `--test_files=3,7,12`
- specify the audio resources via non-keyword arguments (separated by blank space)
