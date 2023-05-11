import numpy as np
import matplotlib.pyplot as plt

def createTriangleSignal(samples: int, frequency: int, k_max: int):
    # returns the signal as 1D-array (np.ndarray)
    # TODO
    t = np.linspace(0, 1, samples)
    k = 0
    s = 0
    while k <= k_max:
        s1 = pow(-1, k) * (np.sin(2 * np.pi * (2 * k + 1) * frequency * t)) / ((2 * k + 1) ** 2)
        s = s + s1
        k = k + 1

    f_triangle = 8 * s / (np.pi ** 2)
    plt.plot(t, f_triangle)
    plt.title('TriangleSignal')
    plt.show()
    return f_triangle


def createSquareSignal(samples: int, frequency: int, k_max: int):
    # returns the signal as 1D-array (np.ndarray)
    # TODO
    t = np.linspace(0, 1, samples)
    k = 1
    s = 0
    while k <= k_max:
        s1 = (np.sin(2 * np.pi * (2 * k - 1) * frequency * t)) / (2 * k - 1)
        s = s + s1
        k = k + 1

    f_square = 4 * s / np.pi
    plt.plot(t, f_square)
    plt.title('SquareSignal')
    plt.show()
    return f_square


def createSawtoothSignal(samples: int, frequency: int, k_max: int, amplitude: int):
    # returns the signal as 1D-array (np.ndarray)
    # TODO
    t = np.linspace(0, 1, samples)
    k = 1
    s = 0
    while k <= k_max:
        s1 = (np.sin(2 * np.pi * k * frequency * t)) / k
        s = s + s1
        k = k + 1

    f_sawtooth = amplitude / 2 - amplitude * s / np.pi
    plt.plot(t, f_sawtooth)
    plt.title('SawtoothSignal')
    plt.show()
    return f_sawtooth
