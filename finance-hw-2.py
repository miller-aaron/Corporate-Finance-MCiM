"""
FINANCE HOME WORK 2 - OUTPUT

Problem 1 
Future Value (7): $1,948.72
Future Value (20): $6,727.50
Future Value (75): $1,271,895.37

Problem 2 
Present Value (8): $6,768.39
Present Value (20): $1,486.44
Present Value (6): $9,145.42

Problem 3 
Positive NPV: $5,729.69

Problem 4 
pv of perpitutity is above initial investment so you should proceed.
PV of Perpituity: $1,052.63

Problem 5 
Future Value of Annuity (from 25): $1,295,282.59
Future Value of Annuity (from 35): $566,416.06
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
