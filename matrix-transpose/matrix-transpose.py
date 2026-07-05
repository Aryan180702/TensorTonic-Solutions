import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here

    A = np.asarray(A, dtype=float)
    row, col = A.shape

    B = np.zeros((col,row))

    for r in range(row):
        for c in range(col):
            B[c,r] = A[r,c]


    return B
    
    
    

