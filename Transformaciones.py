import numpy as np

def TransformacionDelCampo(campoActual):
    return np.fft.fft(campoActual)

def DestransformacionDelCampo(campoTransformado):
    return np.fft.ifft(campoTransformado)