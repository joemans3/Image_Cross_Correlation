import numpy as np


def sim_circle_img(dims: tuple, radii: int | list, loc: tuple | list) -> np.ndarray:
    ''' Create a 2D image of circle(s) with specified radius(radii) and location(s)

    Parameters:
    -----------
    dims: tuple
        The dimensions of the image
    radii: int or list
        The radii of the circle(s) 
    loc: tuple or list
        The location of the circle(s)

    Returns:
    --------
    np.ndarray
        The image of the circle(s)    
    '''
    # make sure the radii and loc of same size if list
    if isinstance(radii, list):
        assert len(radii) == len(loc)
    else:
        radii = [radii]
        loc = [loc]
    img = np.zeros(dims)
    for r, l in zip(radii, loc):
        for i in range(dims[0]):
            for j in range(dims[1]):
                if (i - l[0])**2 + (j - l[1])**2 < r**2:
                    img[i, j] = 1
    return img


def sim_rectangle_img(dims: tuple, width: int | list, height: int | list, loc: tuple | list) -> np.ndarray:
    ''' Create a 2D image of rectangle(s) with specified width, height and location(s)

    Parameters:
    -----------
    dims: tuple
        The dimensions of the image
    width: int or list
        The width of the rectangle(s) 
    height: int or list
        The height of the rectangle(s)
    loc: tuple or list
        The location of the rectangle(s)

    Returns:
    --------
    np.ndarray
        The image of the rectangle(s)    
    '''
    # make sure the width, height and loc of same size if list
    if isinstance(width, list):
        assert len(width) == len(height) == len(loc)
    else:
        width = [width]
        height = [height]
        loc = [loc]
    img = np.zeros(dims)
    for w, h, l in zip(width, height, loc):
        for i in range(dims[0]):
            for j in range(dims[1]):
                if l[0] <= i < l[0] + w and l[1] <= j < l[1] + h:
                    img[i, j] = 1
    return img
