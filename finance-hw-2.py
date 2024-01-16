"""
FINANCE HOME WORK 2 - OUTPUT

Problem 1 
fv_7: 1948.7171000000012, fv_20: 6727.499949325611, fv_75: 1271895.3713950724

Problem 2 
pv_8: 6768.39362028687, pv_20: 1486.4362802414346, pv_6: 9145.421925178718

Problem 3 
Yes, b/c NPV is positive: 5729.6891844011725

Problem 4 
pv of perpitutity is above initial investment so you should proceed. PV = 1052.6315789473683

Problem 5 
fv of annuity from 25: 1295282.5935499938
fv of annuity from 35: 566416.0555670906
"""

#SOLUTION:
import math
import numpy_financial as npf
from sympy import symbols, Eq, solve

#FINANCE HOME WORK 2
print(f"\nFINANCE HOME WORK 2")

#------ Problem 1  ------
print(f"\nProblem 1 ")
fv_7 = npf.fv(.1, 7, 0, -1000)
fv_20 = npf.fv(.1, 20, 0, -1000)
fv_75 = npf.fv(.1, 75, 0, -1000)

print(f"fv_7: {fv_7}, fv_20: {fv_20}, fv_75: {fv_75}")


#------ Problem 2  ------
print(f"\nProblem 2 ")
amt = 10000
pv_8, pv_20, pv_6 = npf.pv(.05, 8, 0, -amt), npf.pv(.1, 20, 0, -amt), npf.pv(.015, 6, 0, -amt)
print(f"pv_8: {pv_8}, pv_20: {pv_20}, pv_6: {pv_6}")

#------ Problem 3  ------
print(f"\nProblem 3 ")
cash_flows = [-1000, 4000, -1000, 4000]
print(f"Yes, b/c NPV is positive: {npf.npv(.02,cash_flows)}")

#------ Problem 4  ------
print(f"\nProblem 4 ")
# PV of Perpituity 
pv_perp = 100 / .095
# if PV_perp > iniital investment it's wortwhile
print(f'pv of perpitutity is above initial investment so you should proceed. PV = {pv_perp}')

#------ Problem 5  ------
print(f"\nProblem 5 ")
RATE = .08
YRS = 40
SAVINGS_AMT = 5000

#how much saved for retirement
fv_annuity = npf.fv(rate=RATE, nper=YRS, pmt=-SAVINGS_AMT, pv=0)
print(f"fv of annuity from 25: {fv_annuity}")

#how much saved if you wait unitl 35 to start saving
fv_annuity_35 = npf.fv(rate=RATE, nper=YRS-10, pmt=-SAVINGS_AMT, pv=0)
print(f"fv of annuity from 35: {fv_annuity_35}")



