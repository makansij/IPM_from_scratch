# Jordan Makansi


def scale(A,x):
    # re-scale x and A 
    # for each x 
    '''
    Args:
        A (numpy matrix): matrix of values for constraints Ax=b
        x (numpy array): numpy array of current values of variables in x
    Output:
        A and x, rescaled.
    Raises:
        ValueError if the dimensions for A and x do not match up.
    '''
    if A.shape[1] != x.shape[0]:
        raise ValueError('dimensions of A and x do not match in order to do multiplication A*x')
    
    x_copy = np.copy(x)
    for i, x_i in enumerate(np.nditer(x)):
        print 'scaling x_i =', x_i, ' to 1.0'
        # for numerical roundoff reasons, since we know that we are scaling 
        #...the x's to be 1, might as well make it as such
        x[i] = 1.0
        print 'scaling the ith column of A by x_i = ', x_i
        # for each element in the column i scale by x_i 
        for j in range(A.shape[1]):
            A[j,i] = A[j,i]*x_copy[i]
