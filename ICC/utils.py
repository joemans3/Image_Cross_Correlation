import numpy as np


# function to find the intensity radially from the center of the image
def radial_intensity(img: np.ndarray, center: tuple)->np.ndarray:
    '''
    Parameters:
    -----------
    img: np.ndarray
        The image to find the radial intensity
    center: tuple
        The center of the image
    Returns:
    --------
    intensity: np.ndarray
        The intensity radially from the center of the image
    '''
    x, y = np.meshgrid(np.arange(img.shape[1]), np.arange(img.shape[0]))
    r = np.sqrt((x - center[0])**2 + (y - center[1])**2)
    # convert r to integers
    r = r.astype(int)
    unique_r = np.unique(r)
    intensity = np.zeros(len(unique_r))
    for i in range(len(unique_r)):
        intensity[i] = np.mean(img[r == i])
    return intensity