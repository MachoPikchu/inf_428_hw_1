import math

def time_difference_in_hours(time1, time2):
    
    if not (0 <= time1 < 24) or not (0 <= time2 < 24):
        raise ValueError("Both times must be in the range [0, 24)")

    delta = time2 - time1
    if delta < 0:
        delta += 24 

    return delta
