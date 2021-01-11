import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

from pydub import AudioSegment
from pytube import YouTube
import os
import random


class Converter:

    def convert_yt_to_mel_spec(self, yt_link):
        yt = YouTube(yt_link)

        stream = yt.streams.filter(only_audio=True, mime_type='audio/mp4')
        print(f"name: {yt.title}, stream: {stream}")

        audio_mp4_stream = yt.streams.get_by_itag(140)  # 140 is always mp4 audio
        mp4_audio_path = audio_mp4_stream.download(output_path='tmp', skip_existing=True)

        mp4 = AudioSegment.from_file(mp4_audio_path, "mp4")
        excerpt = mp4[60000:90000]
        excerpt = excerpt.set_frame_rate(22050)
        excerpt.export("tmp/song.wav", format="wav")
        print(excerpt.frame_rate)

        y, sr = librosa.load('tmp/song.wav')

        fig, ax = plt.subplots()
        M = librosa.feature.melspectrogram(y=y, sr=sr)
        M_db = librosa.power_to_db(M, ref=np.max)
        img = librosa.display.specshow(M_db)

        plt.axis('off')  # this rows the rectangular frame
        ax.get_xaxis().set_visible(False)  # this removes the ticks and numbers for x axis
        ax.get_yaxis().set_visible(False)  # this removes the ticks and numbers for y axis
        name = random.randrange(0,100)
        plt.savefig(f'app/static/spectrogram/{name}.png', bbox_inches='tight',
                    pad_inches=0)

        os.remove(mp4_audio_path)
        os.remove('tmp/song.wav')

        return name
