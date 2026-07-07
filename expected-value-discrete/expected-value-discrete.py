import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    p = np.asarray(p, dtype=float)

    if p.sum() != 1:
        raise ValueError

    expected_value = np.dot(x,p)

    return expected_value
