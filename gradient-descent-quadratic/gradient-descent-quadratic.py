def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """





    def diff_x(a,b,x0):

        return (2*a*x0)+b


    for i in range(0,steps):

        x0 = x0-(lr*diff_x(a,b,x0))


    return x0
    
    


