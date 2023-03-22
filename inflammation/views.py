"""Module containing code for plotting inflammation data."""

from matplotlib import pyplot as plt
import numpy as np


def visualize(data_dict):
    """Display plots of basic statistical properties of the inflammation data.

    :param data_dict: Dictionary of name -> data to plot
    """
    # TODO(lesson-design) Extend to allow saving figure to file

    num_plots = len(data_dict)
    fig = plt.figure(figsize=((3 * num_plots) + 1, 3.0))

    for i, (name, data) in enumerate(data_dict.items()):
        axes = fig.add_subplot(1, num_plots, i + 1)

        axes.set_ylabel(name)
        axes.plot(data)

    fig.tight_layout()

    plt.show()
    return True

def textoutput(data_dict):
    """Display text of basic statistical properties of the inflammation data.

    :param data_dict: Dictionary of name -> data to output
    """
    outputstrings = []
    for i, (name, data) in enumerate(data_dict.items()):
        # check if these numbers are actually int
        if all([(j == 0) or (i / j == 1) for i, j in zip(data, np.floor(data))]):
            data = np.int32(data)
        else:
            data = np.round(data, 2)
        currstring = '{0}. {1}: {2}'.format(i, name, data)
        outputstrings.append(currstring)
    finaloutputstring="\n".join(outputstrings)
    print(finaloutputstring)
    return finaloutputstring
