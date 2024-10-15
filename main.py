import numpy as np
from shape import generate_lissajous_curve_points
from processing import prepare_interpolated_points
from animate import create_animation


A = 2
B = 2
C = 2
a = 3
b = 2
c = 4
delta = np.pi / 2
num_points = 100
l1 = 3.0
l2 = 1.5
n_frames = 100
n_skip = 300


lissajous_points = generate_lissajous_curve_points(A, B, C, a, b, c, delta, num_points)
interpolated_points = prepare_interpolated_points(lissajous_points, n_frames)
selected_frames = np.arange(0, len(interpolated_points), n_skip)

if __name__ == "__main__":
    create_animation(lissajous_points, interpolated_points, n_frames, selected_frames, l1, l2)
