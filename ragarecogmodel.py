# -*- coding: utf-8 -*-
"""RagaRecogModel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/

**Import Section**
"""

from google.colab import drive
drive.mount('/content/gdrive')

import pandas as pd
import numpy as np
import librosa
import os

"""**Literals**"""

folderpath = '/gdrive/MyDrive/audio'

"""**Audio Features from Librosa**"""

def get_harmonic_percussive(audio):
    return librosa.effects.hpss(audio)

def get_spectral_centroid(audio, sr):
    return librosa.feature.spectral_centroid(y=audio, sr=sr)

def get_spectral_contrast(audio, sr):
    return librosa.feature.spectral_contrast(y=audio,sr=sr)

def get_chroma_power(audio, sr):
    return librosa.feature.chroma_stft(y=audio, sr=sr)

def get_chroma_energy(audio, sr):
    s = np.abs(librosa.core.stft(audio))
    return librosa.feature.chroma_stft(S=s, sr=sr)

def get_chroma_cens(audio, sr):
    return librosa.feature.chroma_cens(y=audio, sr=sr)

def get_mfcc(audio, sr):
    return librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=12)

def load_features(ragam, audio, sr):
    y_harmonic, _ = get_harmonic_percussive(audio)
    spectral_centroids = get_spectral_centroid(audio, sr)
    contrast = get_spectral_contrast(y_harmonic, sr)
    chroma_cens = get_chroma_cens(y_harmonic, sr)
    mfcc = get_mfcc(y_harmonic, sr)

    elem = {'ragam': ragam, 
          'spectral_centroids': spectral_centroids, 
          'spectral_contrast': contrast, 
          'chroma_cens': chroma_cens, 
          'mfcc': mfcc}
  
    return elem

"""**Build Feature Dataset**"""

def load_audio():
    print("Loading audio data ...")

    flst = os.listdir(os.getcwd() + folderpath)
    total = len(flst)

    data = []

    for i, file in enumerate(flst):
      if file.endswith(".mp3"):
        audio, sr = librosa.core.load(os.getcwd() + folderpath + "/" + file)
        ragam = file.split(sep='-')[0]

        data.append(load_features(ragam, audio, sr))
          
        print("Completed: " + str(i + 1) + " of " + str(total) + " ...")
    
    return pd.DataFrame(data)

"""**ML Section**"""
#to be done
