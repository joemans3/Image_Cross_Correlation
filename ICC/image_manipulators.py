# operations done to images pre- and post- processing

import numpy as np


# create a sub-image from a larger image in either 2D or 3D
def sub_space_img_2D(input_img: np.ndarray, x: int, y: int, width: int, height: int)-> np.ndarray:
    ''' Create a 2D sub-image from a larger image

    Parameters:
    -----------
    input_img: np.ndarray
        The image to be cropped
    x: int
        The x-coordinate of the top-left corner of the sub-image
    y: int
        The y-coordinate of the top-left corner of the sub-image
    width: int
        The width of the sub-image
    height: int
        The height of the sub-image

    Returns:
    --------
    np.ndarray
        The sub-image
    '''
    # x,y,w,h need to not exceed the bounds of the input_img
    if x + width > input_img.shape[0] or y + height > input_img.shape[1]:
        raise ValueError('The sub-image is out of bounds of the input image')
    return input_img[x:x + width, y:y + height]


def sub_space_img_3D(input_img: np.ndarray, x: int, y: int, z: int, width: int, height: int, depth: int)-> np.ndarray:
    ''' Create a 3D sub-image from a larger image

    Parameters:
    -----------
    input_img: np.ndarray
        The image to be cropped
    x: int
        The x-coordinate of the top-left corner of the sub-image
    y: int
        The y-coordinate of the top-left corner of the sub-image
    z: int
        The z-coordinate of the top-left corner of the sub-image
    width: int
        The width of the sub-image
    height: int
        The height of the sub-image
    depth: int
        The depth of the sub-image

    Returns:
    --------
    np.ndarray
        The sub-image
    '''
    # x,y,z,w,h,d need to not exceed the bounds of the input_img
    if x + width > input_img.shape[0] or y + height > input_img.shape[1] or z + depth > input_img.shape[2]:
        raise ValueError('The sub-image is out of bounds of the input image')
    return input_img[x:x + width, y:y + height, z:z + depth]


# subtract mean background from an image
def image_background_subtraction(img: np.ndarray, background: float)-> np.ndarray:
    ''' Subtract the mean background from an image

    Parameters:
    -----------
    img: np.ndarray
        The image to be processed
    background: float
        The mean background value

    Returns:
    --------
    np.ndarray
        The image with the mean background subtracted
    '''
    return img - background


# convert image to int 64
def convert_img_int64(img: np.ndarray)-> np.ndarray:
    ''' Convert an image to int64

    Parameters:
    -----------
    img: np.ndarray
        The image to be converted

    Returns:
    --------
    np.ndarray
        The image converted to int64
    '''
    return img.astype(np.int64)


# normalize an image
def normalize_img(img: np.ndarray, lower: float, upper: float, ignore_zeros: bool)-> np.ndarray:
    ''' Normalize an image

    Parameters:
    -----------
    img: np.ndarray
        The image to be normalized
    lower: float
        The lower bound of the normalization
    upper: float
        The upper bound of the normalization
    ignore_zeros: bool
        Whether to ignore zeros in the normalization


    Returns:
    --------
    np.ndarray
        The normalized image
    '''
    # if ignore_zeros is True, ignore zeros in the normalization but keep them in the image
    if ignore_zeros:
        # convert image to float
        img = img.astype(float)
        # convert 0s to inf
        img[img == 0] = np.inf
        # normalize the image based on the lower and upper bounds
        img = (img - lower) / (upper - lower)
        # convert inf back to 0
        img[img == np.inf] = 0
    else:
        img = (img - lower) / (upper - lower)
    return img

    