import sys


def read_stdin_col(col_num):
    """
    Store an array of numbers selected at col_num position
    
    Parameters:
    col_num: The 0-based index of number you want to add
    
    Return:
    An array of numbers in integer or float format
    """
    if col_num < 0:
        raise ValueError('Col number should be a non-negative number')
    if sys.stdin is None:
        raise ValueError('No data in stdin')

    data_list = []
    for line in sys.stdin:
        temp_list = line.strip().split()
        if col_num >= len(temp_list):
            raise ValueError('Invalid col num. Index out of boundary')
        data_list.append(int(temp_list[col_num]))
    return data_list
