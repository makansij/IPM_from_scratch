# Jordan Makansi
import numpy as np

'''
Project mu multiplied by the ones vector onto A, and get the perpendicular part, too (which is the projection onto A^T).
'''
def project(A, mu):
    '''
    Args:
        A (numpy matrix): rescaled matrix of values for constraints Ax=b
           (remember that we are assuming that the rows of A are linearly independent, 
            which in linear programming means that the equality constraints are not redundant)
        mu (numpy array): numpy array of mu times the ones vector 
    Output:
        dx (numpy array): projection of mu onto col(A)
        ds (numpy array): projection of mu onto null(A)
    Raises:
        ValueError if the dimensions for A and mu do not match up.
    '''
    e = np.asmatrix(np.ones(A.shape[1])).T
    # remember that a projection is just a linear transformation:
    proj_A = A*np.linalg.inv(A.T*A)*A.T
    # proj_A is a projection matrix, so we can just hit mu with it to get the projection
    mu_vector = mu*e
    dx = proj_A*mu_vector
    
    # but we also need the *orthogonal* projection to get ds
    # orthogonal projection is the original vector minus the projection
    ds = mu_vector - dx

    return dx, ds
