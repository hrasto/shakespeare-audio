# Shakespeare audio

Repo containing Python scripts for building a dataset of parallel audio and text suitable for machine learning experiments (e.g. language modeling).

By default, it downloads 3 shakespeare plays from [LibriVox](https://librivox.org) ([Romeo & Juliet](https://librivox.org/romeo-and-juliet-version-4-by-william-shakespeare/), [Hamlet](https://librivox.org/hamlet-version-3-by-william-shakespeare/) and [As You Like It](https://librivox.org/as-you-like-it-version-3-by-william-shakespeare/https:/)), and transcribes them using [whisper.cpp](https://github.com/ggerganov/whisper.cpp).

Quick start:

1. `git clone https://github.com/hrasto/shakespeare-audio`
2. `cd shakespeare-audio && pip install -r requirements.txt && python main.py `

The script may run for several minutes, as it needs to download and extract the archives, convert the mp3s to wavs, and run whisper to transcribe word by word, so that we can align the waveforms with the text via precise timestamps.
