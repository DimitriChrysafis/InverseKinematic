import numpy as np
from numba import njit

@njit
def c(v, min_v, max_v):
    return max(min_v, min(v, max_v))

@njit
def i(x, y, z, l1, l2):
    d = np.sqrt(x ** 2 + y ** 2)
    ct2 = (d ** 2 + z ** 2 - l1 ** 2 - l2 ** 2) / (2 * l1 * l2)
    ct2 = c(ct2, -1.0, 1.0)
    st2 = np.sqrt(1 - ct2 ** 2)
    t2 = np.arctan2(st2, ct2)
    k1 = l1 + l2 * ct2
    k2 = l2 * st2
    t1 = np.arctan2(z, d) - np.arctan2(k2, k1)
    t3 = np.arctan2(y, x)
    return t1, t2, t3

@njit
def f(t1, t2, t3, l1, l2):
    x1 = l1 * np.cos(t1) * np.cos(t3)
    y1 = l1 * np.cos(t1) * np.sin(t3)
    z1 = l1 * np.sin(t1)
    x2 = x1 + l2 * np.cos(t1 + t2) * np.cos(t3)
    y2 = y1 + l2 * np.cos(t1 + t2) * np.sin(t3)
    z2 = z1 + l2 * np.sin(t1 + t2)
    return np.array([[0, x1, x2], [0, y1, y2], [0, z1, z2]])
