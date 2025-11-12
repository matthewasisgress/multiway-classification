import numpy as np
import h5py
import sys
NPZ_FILE = 'organmnist3d.npz'
H5_FILE = 'organmnist3d.h5'
try:
    npz_data = np.load(NPZ_FILE)
except Exception as e:
    sys.exit(1)
try:
    with h5py.File(H5_FILE, 'w') as hf:
        for key in npz_data.files:
            print(f"  -> Writing dataset: {key}")
            hf.create_dataset(key, data=npz_data[key])
except Exception as e:
    sys.exit(1)