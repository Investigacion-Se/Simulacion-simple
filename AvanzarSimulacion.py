import numpy as np

def AvanzarSimulacion(campoActual, dt, coeficiente, kernel):
    return campoActual / (1 - dt * coeficiente * kernel)
