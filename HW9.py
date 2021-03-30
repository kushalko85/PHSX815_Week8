import numpy as np
from scipy import optimize


#define function

def f(x):
    return 4*(x-3)**2 + 5*x - 2


#Brent's Minimization method

BM = optimize.minimize_scalar(f)
#print(BM)
minima = BM.x
print("The minimum of the function 4(x-3)^2 +5x -2 is at (%.3f, %.3f)" %(minima,f(minima)))

