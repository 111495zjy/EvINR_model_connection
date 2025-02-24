import numpy as np

txt_file_path = '/content/EvINR/ECD/dynamic_6dof/events.txt'
npy_file_path = '/content/EvINR/ECD/dynamic_6dof/events.npy'
events = []
with open(txt_file_path, 'r') as f:
    for line in f:
        t, x, y, p = map(float, line.strip().split())
        events.append([t, x, y, p])
events_array = np.array(events)
np.save(npy_file_path, events_array)
