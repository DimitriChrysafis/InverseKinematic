import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from processing import prepare_interpolated_points, process_frame

def c(sp, ip, n, sf, l1, l2):
    def u(f_idx):
        a, px, py, pz, x, y, z = process_frame(f_idx, ip, l1, l2)
        for ln, pt, tg, org, ax in zip(ls, ps, ts, os, axs.flat):
            ln.set_data(a[0], a[1])
            ln.set_3d_properties(a[2])
            pt.set_data(px, py)
            pt.set_3d_properties(pz)
            tg.set_data([x], [y])
            tg.set_3d_properties([z])
            if f_idx == 0 or f_idx % (n // len(sp)) == 0:
                prev_x, prev_y, prev_z = ip[f_idx]
                org.set_data([prev_x], [prev_y])
                org.set_3d_properties([prev_z])
            ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.1)
            ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.1)
            ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.1)
        print(f"Rendering frame {f_idx + 1}/{len(sf)}")
        return ls + ps + ts + os

    def i():
        for ln, pt, tg, org in zip(ls, ps, ts, os):
            ln.set_data([], [])
            ln.set_3d_properties([])
            pt.set_data([], [])
            pt.set_3d_properties([])
            tg.set_data([], [])
            tg.set_3d_properties([])
            org.set_data([], [])
            org.set_3d_properties([])
        return ls + ps + ts + os

    fig, axs = plt.subplots(2, 2, subplot_kw={'projection': '3d'}, figsize=(10, 10))
    ags = [(30, 30), (30, 150), (60, 60), (60, 240)]
    for ax, ag in zip(axs.flat, ags):
        ax.set_xlim([-4, 4])
        ax.set_ylim([-4, 4])
        ax.set_zlim([-4, 4])
        ax.view_init(elev=ag[0], azim=ag[1])
        ax.set_box_aspect([1, 1, 1])
        ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.1)
        ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.1)
        ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.1)

    ls = [ax.plot([], [], [], 'o-', lw=6, color='#1f77b4')[0] for ax in axs.flat]
    ps = [ax.plot([], [], [], '-', lw=2, color='#ff7f0e')[0] for ax in axs.flat]
    ts = [ax.plot([], [], [], 'ro', markersize=8)[0] for ax in axs.flat]
    os = [ax.plot([], [], [], 'bo', markersize=8)[0] for ax in axs.flat]

    ani = animation.FuncAnimation(
        fig, u,
        frames=sf,
        init_func=i,
        blit=True
    )
    ani.save('robotic_arm_ik_demo_3d_spiral_cone.mp4', writer='ffmpeg', fps=20)
