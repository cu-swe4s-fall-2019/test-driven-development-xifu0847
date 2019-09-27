import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math_lib


def boxplot(L, out_file_name):
    """
    Draw a boxplot diagram and save it as a figure.

    Parameters:
    L: A list of numbers in either integer or float type
    out_file_name: The file name for the output figure

    """
    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)
    fig = plt.figure(dpi=300)

    ax = fig.add_subplot(1, 1, 1)
    plt.boxplot(L)
    plt.title("mean: {} stdev: {}".format(mean, stdev))
    plt.ylabel('Value')
    plt.show()
    plt.savefig(out_file_name)


def histogram(L, out_file_name):
    """
    Draw a histogram diagram and save it as a figure.

    Parameters:
    L: A list of numbers in either integer or float type
    out_file_name: The file name for the output figure

    """
    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)
    fig = plt.figure(dpi=300)

    ax = fig.add_subplot(1, 1, 1)
    plt.hist(L)
    plt.title("mean: {} stdev: {}".format(mean, stdev))
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig(out_file_name)


def combo(L, out_file_name):
    """
    Draw one boxplot diagram and one histogram diagram in one figure
    and save it as out_file_name.

    Parameters:
    L: A list of numbers in either integer or float type
    out_file_name: The file name for the output figure

    """
    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)
    fig = plt.figure(dpi=300)

    ax = fig.add_subplot(2, 1, 1)
    plt.boxplot(L)
    plt.title("mean: {} stdev: {}".format(mean, stdev))
    plt.ylabel('Value')
    plt.savefig(out_file_name)

    ax = fig.add_subplot(2, 1, 2)
    plt.hist(L)
    plt.title("mean: {} stdev: {}".format(mean, stdev))
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig(out_file_name)
