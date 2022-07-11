# Python Script Example: fibonacci script
# Record of Revisions
#
# Date            Programmer              Descriptions of Change
# ====         ================           ======================
# 10-July-22      Kianté Fernandez               Original code

import numpy as np
import pandas as pd

def fibonacci(n):
    """
    Generates the Fibonacci sequence. This is where each number is the sum 
    of the two preceding ones
    Parameters
    ----------
    n: the length of the sequence to generate
    Returns
    _________
    an np.array of the corresponding n fibonacci elements
    """
    result = np.array([0, 1])
    temp_n = 2
    while temp_n < n:
      result = np.append(result, result[temp_n - 1] + result[temp_n - 2])
      temp_n += 1
    return (result)


if __name__ == '__main__':
    assert fibonacci(1)[0] == 0
    assert fibonacci(10)[-1]
    print("Tests passed")


