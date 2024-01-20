# Scratch pad to test and play with formulas
import math
import numpy_financial as npf
from sympy import symbols, Eq, solve
from scipy.optimize import linprog

# Define bond prices
bond_A = [100, 100, 1100]
bond_B = [120, 1120, 0]
bond_C = [100, 100, 100]

# Define objective function coefficients
c = [0, 0, 0]

# Define equality constraints matrix
A_eq = [[bond_A[x], bond_B[x], bond_C[x]] for x in range(len(bond_A))]
print(f"eq: {A_eq}")

# Define equality constraints vector
B_eq = [0, 1000, 0]

# Solve linear programming problem
result = linprog(c=c, A_eq=A_eq, b_eq=B_eq, method='highs', bounds=(None, None))
print(f"result: {result}")

# Calculate bond values based on optimal solution
calcs = [0, 0, 0]
for x in range(len(calcs)):
    calcs[x] = bond_A[x] * result.x[0] + bond_B[x] * result.x[1] + bond_C[x] * result.x[2]
print(f"calcs: {calcs}")


