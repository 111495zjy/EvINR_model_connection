import numpy as np

txt_file_path = '/content/EvINR_model_connection/gun_bullet_gnome.txt'
npy_file_path = '/content/EvINR_model_connection/gun_bullet_gnome.npy'

events = []
with open(txt_file_path, 'r') as f:
    #next(f)  # 跳过第一行
    for line in f:
        t, x, y, p = map(float, line.strip().split())
        events.append([t, x, y, p])

events_array = np.array(events)
np.save(npy_file_path, events_array)
