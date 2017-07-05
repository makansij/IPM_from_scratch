# Jordan Makansi

'''
This program takes as input a linear programming problem, and outputs the solution, after solving it using the interior point method.
The interior point method works as follows:
    - Form the Barrier function B(x,u) = c^T*x - u*sum(log(c_i(x) for c_i in constraints))
    - set u = infinity (or something really high)
    - three options for stopping conditions:
         1) when u = 0
         2) when duality gap is = 0
         3) when two consecutive objective function values are the same.
    - while u != 0:

'''

from scale import *
from project import *
from get_theta import *

# Constants
L = 5   # number of bits in linear program
mu = 10**5 # something high

# Starting point 
'''
To get a starting point, you need to solve an initial LP, Karger Kkoltech says, although I still have to figure out what that means.
'''

# Solution loop
while mu > 2**-L:
    # scale A and x s.t. all the x's = 1 
    A,x = scale(A,x)

    # use a projection to solve the linear system
    dx, dy, ds = project(A, mu)

    # get theta, which will tell us how *far* to move in the directions dx and ds
    # note that getting theta also requires knowing "n" but can know that here from 
    #...from the length of the "x" vector.
    theta = get_theta(x, s, mu)


