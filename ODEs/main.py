# %%%%
# Goal: create a simple ODE solver

import numpy as np
import scipy as sp
import numpy.linalg as npl
from scipy import (integrate, interpolate, optimize, signal, ndimage, misc, linalg as spl)
import scipy.linalg as spl
np.set_printoptions(2, suppress=True)


class ODE:
    """
    Class for solving ODEs
    """
    def __init__(self, function: callable) -> None:
        self.function = function
        pass


def ForwardEuler(f: callable, t: np.ndarray, y0: np.ndarray, h: float) -> np.ndarray:
    """
    Solve ODE using Forward Euler method
    """
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for i in range(1, n):
        y[i] = y[i-1] + h*f(y[i-1], t[i-1], 1)
    return y

def demo():
    
    def func(y, t, w):
        return y*w / (1 + y**2)

    