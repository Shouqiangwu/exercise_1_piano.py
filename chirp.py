import math
import matplotlib.pyplot as plt
import numpy as np
def createChirpSignal(samplingrate: int, duration: int, freqfrom: int, freqto: int, linear: bool):
    # returns the chirp signal as list or 1D-array
    # TODO
    x = np.linspace(0, duration, duration*samplingrate)
    y = []
    if linear == True:
        for t in x:
            k = (freqto-freqfrom)/duration
            y.append(np.sin(2 * np.pi * (0.5 * k * t * t + freqfrom * t)))
    else:
        for t in x:
            a = pow((freqto/freqfrom), 1/duration)
            c = math.log(a)
            y.append(np.sin(2 * np.pi * freqfrom * (pow(a, t)-1) / c))
    Y = np.array(y)
    plt.plot(x, y)
    plt.show()
    return Y
