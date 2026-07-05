import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here

    size  = len(v)
    A = np.zeros((size, size))

    row, col  = A.shape

    for r in range(row):

        A[r,r] = v[r]
    
    return A
