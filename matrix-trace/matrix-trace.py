import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    trace = 0

    A = np.asarray(A, dtype=float)
    row, col = A.shape

    for r in range(row):
        trace +=A[r,r]

    # for r in range(row):
    #     for c in range(col):

    #         if r ==c : 
    #             trace += A[r,c]
            
    return trace
