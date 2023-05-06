import wave
import sys

import pyaudio

# Default values
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
FILENAME = 'output.wav'


class Record:
    def __init__(self):
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1 if sys.platform == 'darwin' else 2
        self.rate = 44100
        self.is_open = False
        self.file = ""

    def record_secs(self, duration):
        with wave.open('output.wav', 'wb') as wf:
            p = pyaudio.PyAudio()
            wf.setnchannels(self.channels)
            wf.setsampwidth(p.get_sample_size(self.format))
            wf.setframerate(self.rate)

            stream = p.open(format=self.format,
                            channels=self.channels, rate=self.rate, input=True)

            print('Recording ...')
            for _ in range(0, self.rate // self.chunk * duration):
                wf.writeframes(stream.read(self.chunk))
            print('Done')

            stream.close()
            p.terminate()

            return 'output.wav'

    def open(self, file=FILENAME, channels=CHANNELS, format=FORMAT, rate=RATE):
        self.file = file
        self.wav = wave.open(self.file, 'wb')
        self.py_audio = pyaudio.PyAudio()
        self.wav.setnchannels(channels)
        self.wav.setsampwidth(self.py_audio.get_sample_size(format))
        self.wav.setframerate(rate)

        self.stream = self.py_audio.open(
            format=format, channels=channels, rate=rate, input=True)

        self.is_open = True

    def start(self, duration, chunk=CHUNK):
        if (not self.is_open):
            print('Stream is not opened, use .open before using .start')
            return -1
        print('Recording...')
        print('Press space to end')

        for _ in range(0, self.wav.getframerate() // chunk * duration):
            self.wav.writeframes(self.stream.read(chunk))

        print('Done')
        return self.file

    def close(self):
        if (not self.is_open):
            print('Stream is not open')
            return -1

        self.stream.close()
        self.py_audio.terminate()
