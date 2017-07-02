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


def main():

