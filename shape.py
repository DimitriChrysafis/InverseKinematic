import numpy as np

def g(A, B, C, a, b, c, d, n):
    t = np.linspace(0, 2 * np.pi, n)
    x = A * np.sin(a * t + d)
    y = B * np.sin(b * t)
    z = C * np.sin(c * t)
    return np.stack([x, y, z], axis=1)
