from math import ceil
import matplotlib.pyplot as plt
import numpy as np
import os
# from tqdm import tqdm

def load_sample(filename, duration=4*44100, offset=44100//10):
    signal = np.load(filename)
    # plt.plot(signal)
    # plt.show()
    Position = np.argmax(signal)
    start = Position + offset
    signal_short = signal[start: start+duration]
    np.save('signals_short.npy', signal_short)
    return signal_short

def compute_frequency(signal, min_freq=20):
    sampling_freq = 44100
    A = np.fft.fft(signal)  # Amplitude array
    positiveA = np.abs(A)  # Amplitude absolute
    f = np.fft.fftfreq(signal.size, 1 / sampling_freq)  # frequency array
    freq = f[np.argmax(positiveA)]  # find the highest peak and corresponding frequency
    if freq < min_freq:
        f[np.argmax(positiveA)] = 0
        freq = f[np.argmax(positiveA)]  # return the frequency corresponding to this peak
    plt.plot(f, positiveA)
    plt.show()
    print(freq)
    return freq

signal = np.load('C:/Users/shouq/Desktop/intro_ML/Exercise/ex2/ex2/exercise1/sounds/Piano.ff.A4.npy')
sampling_freq = 44100
min_freq = 20

f0 = np.fft.fftfreq(signal.size, 1 / sampling_freq)  # frequency array
i = int(np.argwhere(f0 == min_freq))
f = f0[i:]
#print(type(f))

A = np.fft.fft(signal)# magnitude array
magnitude = np.abs(A) #absolute
m = magnitude[i:]


freq = f[np.argmax(m)] #find the highest peak corresponding to a frequency
print(abs(freq))
plt.plot(f0, magnitude)
plt.show()



if __name__ == '__main__':
    for i in ('A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'XX'):
        signal = load_sample('sounds/Piano.ff.' + i + '.npy')
        freq = compute_frequency(signal, min_freq=20)
        #print(type(freq))
        print('The max. frequency in ' + i + ' is ' + str(freq) + ' Hz')
    print('According to the following wikipedia link, the signal XX with frequency ' + str(freq) + ' Hz is D6')
# https://en.wikipedia.org/wiki/Piano_key_frequencies'''
