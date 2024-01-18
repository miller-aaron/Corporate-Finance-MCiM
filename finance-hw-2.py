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
import numpy_financial as npf

def print_answer(label, value):
  if isinstance(value, tuple):
    formatted_values = [f"${val:,.2f}" for val in value]
    formatted_value = ", ".join(formatted_values)
    print(f"{label}: {formatted_value}")
  else:
    formatted_value = "{:,.2f}".format(value)
    print(f"{label}: ${formatted_value}")

#FINANCE HOME WORK 2
print(f"\nFINANCE HOME WORK 2")

#------ Problem 1  ------
print(f"\nProblem 1 ")
fv_7 = npf.fv(rate=.1, nper=7, pmt=0, pv=-1000)
fv_20 = npf.fv(rate=.1, nper=20, pmt=0, pv=-1000)
fv_75 = npf.fv(rate=.1, nper=75, pmt=0, pv=-1000)

print_answer("Future Value (7)", fv_7)
print_answer("Future Value (20)", fv_20)
print_answer("Future Value (75)", fv_75)


#------ Problem 2  ------
print(f"\nProblem 2 ")
amt = 10000
pv_8, pv_20, pv_6 = npf.pv(rate=.05, nper=8, pmt=0, fv=-amt), npf.pv(rate=.1, nper=20, pmt=0, fv=-amt), npf.pv(rate=.015, nper=6, pmt=0, fv=-amt)
print_answer("Present Value (8)", pv_8)
print_answer("Present Value (20)", pv_20)
print_answer("Present Value (6)", pv_6)

#------ Problem 3  ------
print(f"\nProblem 3 ")
cash_flows = [-1000, 4000, -1000, 4000]
print_answer("Positive NPV", npf.npv(rate=.02, values=cash_flows))

#------ Problem 4  ------
print(f"\nProblem 4 ")
# PV of Perpituity 
pv_perp = 100 / .095
# if PV_perp > iniital investment it's wortwhile
print("pv of perpitutity is above initial investment so you should proceed.")
print_answer("PV of Perpituity", pv_perp)

#------ Problem 5  ------
print(f"\nProblem 5 ")
RATE = .08
YRS = 40
SAVINGS_AMT = 5000

#how much saved for retirement
fv_annuity = npf.fv(rate=RATE, nper=YRS, pmt=-SAVINGS_AMT, pv=0)
print_answer("Future Value of Annuity (from 25)", fv_annuity)

#how much saved if you wait until 35 to start saving
fv_annuity_35 = npf.fv(rate=RATE, nper=YRS-10, pmt=-SAVINGS_AMT, pv=0)
print_answer("Future Value of Annuity (from 35)", fv_annuity_35)
