import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline


def smoothline(x, y, xlabel, ylabel, color, label):
    """draw a smooth line.

    :param x:
    :param y:
    :param xlabel:
    :param ylabel:
    :param color:
    :param label:
    """
    x_smooth = np.linspace(x.min(), x.max(), 300)
    y_smooth = make_interp_spline(x, y)(x_smooth)
    plt.plot(x_smooth, y_smooth, color=color, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
