import numpy as np


# Really basic way of separating foreground and background.
def filter_background(roi):
    # Anything further than 8000mm, we consider it as background
    # Anything less than 100mm is consider noise
    ret_val = np.ma.masked_greater(roi, 8000)
    ret_val = np.ma.masked_less(ret_val, 100)
    unique, counts = np.unique(ret_val.mask, return_counts=True)
    _dict = dict(zip(unique, counts))
    if False in _dict:
        return ret_val, _dict[False]
    else:
        return ret_val, 0


def get_x_in_meters(xmin, xmax, z_i):
    # Tune z_c to get better value lol.
    # 500 is literally randomly chosen lol
    z_c = 500
    ret_val = (z_i * (xmax + xmin - 600.0)) / (2 * z_c)
    return ret_val