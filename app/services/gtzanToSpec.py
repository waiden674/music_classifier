import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

import os

# Script used to convert the gtzan dataset wav to mel spectograms
# Although there were mel spectograms available in the dataset, I was
# not able to reproduce the spectogram in a fashion similar to theirs
# and as such, I decided to produce my own.

dir_path = "/home/wzhang/Downloads/archive/Data/genres_original/pop"  # change here


def convert(path, filename):
    y, sr = librosa.load(path)

    fig, ax = plt.subplots()
    M = librosa.feature.melspectrogram(y=y, sr=sr)
    M_db = librosa.power_to_db(M, ref=np.max)
    img = librosa.display.specshow(M_db)

    plt.axis('off')  # this rows the rectangular frame
    ax.get_xaxis().set_visible(False)  # this removes the ticks and numbers for x axis
    ax.get_yaxis().set_visible(False)  # this removes the ticks and numbers for y axis

    plt.savefig(f'pop/{filename}.png', bbox_inches='tight', pad_inches=0)  # change here
    plt.close()

    return None


i = 0

for filenames in os.listdir(dir_path):
    convert(dir_path + '/' + filenames, i)
    print(f"file {i} is completed")
    i += 1
