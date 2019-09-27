import math


def list_mean(V):
    """
    Calculate the mean of an input list

    Parameters:
    V: A list of numbers in integer or float format

    Return:
    mean: A integer of float type number
    """
    if V is None:
        raise ValueError('ValueError: Input is None')
    mean = None
    try:
        mean = sum(V) / len(V)
    except ZeroDivisionError as error:
        raise ZeroDivisionError('ZeroDivisionError: V has len 0')
    return mean


def list_stdev(V):
    """
    Calculate the stdev of an input list

    Parameters:
    V: A list of numbers in integer or float format

    Return:
    stdev: A integer of float type number
    """
    if V is None:
        raise ValueError('ValueError: Input is None')
    mean = list_mean(V)
    stdev = None
    try:
        stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / (len(V) - 1))
    except ZeroDivisionError as error:
        raise ZeroDivisionError('ZeroDivisionError: V has len 0')
    return stdev
