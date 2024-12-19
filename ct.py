import os
import sys
import torch

from faster_whisper import WhisperModel
faster_whisper_model = 'nyrahealth/faster_CrisperWhisper'


device = "cuda" if torch.cuda.is_available() else "cpu"
torch_dtype = "float16" if torch.cuda.is_available() else "float32"
model = WhisperModel(faster_whisper_model, device=device, compute_type="float32")

import librosa

# Load the audio file
audio_file = "test60.mp3"
y, sr = librosa.load(audio_file)

# y is now a numpy array containing the audio data as floats
print(sr)
print(y)

segments, info = model.transcribe(y, beam_size=1, language='en', word_timestamps = True, without_timestamps= True)

for segment in segments:
    print(segment)