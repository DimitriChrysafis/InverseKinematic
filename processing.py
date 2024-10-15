import numpy as np
from kinematics import inverse_kinematics, forward_kinematics

def i(p1, p2, n):
    return np.linspace(p1, p2, n)

def p(pts, n):
    return np.concatenate([i(pts[i], pts[i + 1], n) for i in range(len(pts) - 1)])

def f(idx, pts, l1, l2):
    x, y, z = pts[idx]
    t1, t2, t3 = inverse_kinematics(x, y, z, l1, l2)
    a = forward_kinematics(t1, t2, t3, l1, l2)
    px = pts[:idx + 1, 0]
    py = pts[:idx + 1, 1]
    pz = pts[:idx + 1, 2]
    return a, px, py, pz, x, y, z
