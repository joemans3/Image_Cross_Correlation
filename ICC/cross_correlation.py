# cross correlation functionality

import numpy as np
from scipy import signal


# calculate the cross-correlation of two images
def cross_correlation(img1: np.ndarray, img2: np.ndarray)-> np.ndarray:
    ''' Calculate the cross-correlation of two images

    Parameters:
    -----------
    img1: np.ndarray
        The first image
    img2: np.ndarray
        The second image

    Returns:
    --------
    np.ndarray
        The cross-correlation of the two images
    '''
    return signal.correlate2d(img1, img2, mode='same', boundary='wrap')


# auto-correlation of an image with translation
def auto_correlation(img: np.ndarray, x: int, y: int)-> np.ndarray:
    ''' Calculate the auto-correlation of an image with translation

    Parameters:
    -----------
    img: np.ndarray
        The image to be auto-correlated
    x: int
        The x-translation
    y: int
        The y-translation

    Returns:
    --------
    np.ndarray
        The auto-correlation of the image with translation
    '''
    return signal.correlate2d(img, np.roll(img, (x, y), axis=(0, 1)), mode='same', boundary='wrap')


# peak of correlation
def correlation_peak_detection(cross_corr: np.ndarray, closeness_threshold: float)-> np.ndarray:
    ''' Detect the peak of the cross-correlation

    Parameters:
    -----------
    cross_corr: np.ndarray
        The cross-correlation of two images
    closeness_threshold: float
        The threshold for finding peak (s) near the maximum
    
    Returns:
    --------
    np.ndarray
        The peak of the cross-correlation
    '''
    # find the maximum value in the cross-correlation
    max_val = np.max(cross_corr)
    # find the indices of the maximum value aslong as it is within the closeness_threshold
    indx = np.where(cross_corr >= max_val - closeness_threshold)
    return np.array(indx).T