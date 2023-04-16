import math


def find_opt_angle(d1, d2, h, n):
    """
    function for searching optimized start angle based on initial set geometry between point-1
    and point-2. Shortest distance is a sum of two lines.
    :param d1: horizontal distance for media separated line from left
    :param d2: horizontal distance for media separated line from right
    :param h: vertical distance from points
    :param n: a mean to estimate difference in velocity values for medium one and two.
    There velocity on medium one is base
    :return: optimized start angle from point 1 to separation line
    """
    alpha_start = 0
    alpha_opt = 0
    alpha_max = math.atan(h / d1)
    length_min = math.inf
    while alpha_start <= alpha_max:
        length = math.sqrt(d1 ** 2 + (d1 * math.tan(alpha_start)) ** 2) + \
                 n * math.sqrt(d2 ** 2 + (h - d1 * math.tan(alpha_start)) ** 2)
        if length < length_min:
            length_min = length
            alpha_opt = alpha_start
        alpha_start += 0.001
    return alpha_opt



