import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """


    a = np.asarray(a, dtype = float)
    b = np.asarray(b, dtype = float)

    if np.sum(a**2)==0:
        return 0
    if np.sum(b**2)==0:
        return 0

    dot = np.dot(a,b) / np.sqrt((np.sum(a**2) * np.sum(b**2)))

    return dot
