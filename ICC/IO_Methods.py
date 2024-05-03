# functions for input/output of images/masks and output of results

import os
import numpy as np
from skimage import io


# import .npy files
def import_npy(path: str) -> np.ndarray:
    return np.load(path)

# import .tif files


def import_tif(path: str) -> np.ndarray:
    return io.imread(path)


# load image masks
def load_mask(path: str) -> np.ndarray:
    if path.endswith('.npy'):
        return import_npy(path)
    elif path.endswith('.tif'):
        return import_tif(path)
    elif path.endswith('.tiff'):
        return import_tif(path)
