from chirp import createChirpSignal
from decomposition import createTriangleSignal, createSquareSignal, createSawtoothSignal

#createChirpSignal(200, 1, 1, 10, False)
#createChirpSignal(200, 1, 1, 10, True)
#createTriangleSignal(200, 2, 10000)
#createSquareSignal(200, 2, 10000)
createSawtoothSignal(200, 2, 10000, 1)
#TODO: Test the functions imported in lines 1 and 2 of this file.
