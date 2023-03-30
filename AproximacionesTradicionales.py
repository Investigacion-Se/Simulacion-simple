import numpy as np

def AproximacionTradicional(x, dx):
    largo = len(x)
    puntoMedio = int(np.floor(largo / 2))

    y = np.zeros(largo)
    
    y[puntoMedio + 3] = -1 / 60
    y[puntoMedio + 2] = 3 / 20
    y[puntoMedio + 1] = -3 / 4

    y[puntoMedio - 1] = 3 / 4
    y[puntoMedio - 2] = -3 / 20
    y[puntoMedio - 3] = 1 / 60

    return np.fft.fft(np.fft.ifftshift(y / dx))

def AproximacionSegundaTradicional(x, dx):
    largo = len(x)
    puntoMedio = int(np.floor(largo / 2))

    y = np.zeros(largo)
    
    y[puntoMedio + 3] = 1 / 90
    y[puntoMedio + 2] = -3 / 20
    y[puntoMedio + 1] = 3 / 2
    y[puntoMedio + 0] = -49 / 18
    y[puntoMedio - 1] = 3 / 2
    y[puntoMedio - 2] = -3 / 20
    y[puntoMedio - 3] = 1 / 90    

    return np.fft.fft(np.fft.ifftshift(y / dx ** 2))