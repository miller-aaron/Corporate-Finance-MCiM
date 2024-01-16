"""
Problem 1
a. 6848.441778042966
b. 148779.12062667691
c. 999.9951203479017 -- Problem 1

Problem 2
51981214.36183257

Problem 3
current_bal: 154286.21654390302
A. Monthly Payments on New Loan: -987.9115559587024
B. Monthly Payments on New Loan (25yr Term): -1053.8346050735254
C. Time to repay at prior payment amount: 14.15746245052627
full_loan_bal: 205259.22621364315
D. Additional Amt Borrowed: $50973.00966974013

Porblem 4
interest_payment: 437.5
new_interest_payment: 350.0
detla: 87.5
additional_debt: 8750.0

Problem 5
pv_salary: 614665.5407506742
pv_bonus: 107417.27896613715
pv_all_def_payments: 505365.11631501745
pv_def_payments: 505365.11631501705
Total Contract Value: 1627447.9360318284

Problem 6

A. NPV of a, b, c: (119369.36936936935, 9639.639639639528, -16666.666666666686)
Proj A and B have a positive NPV so they should be pursued

B. Max Avaialable T1 : 3029200.0

C. NPV of a, b, c: (135321.10091743118, 21376.146788990824, -10550.458715596353)
Proj A and B still have a positive NPV so the answer to A would not change

 The new answer for B: Max avaialable T1 : 3004800.0

PROBLEM 7
Present Value of Flower Vow: 3633.0674357650714

PROBLEM 8
ret_balance needed to sustain 100K annual burn: 1294767.2300430937
contribution needed: 9366.29389698343

PROBLEM 9
First Payment: 7461.18013753000
% Required: 0.0994824018337333
"""

import numpy_financial as npf
from sympy import symbols, Eq, solve

#FINANCE HOME WORK 1 

#------ Problem 1  ------
print(f"Problem 1 ")

CURRENT_AGE = 18
ACCT_BAL = 3996
RATE = .08

def future_val(rate, beg_bal, yrs):
  return beg_bal * (1+rate)**yrs

def present_val(rate, end_bal, yrs):
  return end_bal/ (1+rate)**yrs

print("Problem 1")
#a. calculate addition interest between 18 and 25
print(f"a. {npf.fv(rate=RATE, nper=25-CURRENT_AGE, pmt=0, pv=-ACCT_BAL)}")

#b. 65th
print(f"b. {npf.fv(rate=RATE, nper=65-CURRENT_AGE, pmt=0, pv=-ACCT_BAL)}")

#c. discount current balance back to PV when grandfather invested 
print(f"c. {npf.pv(rate=RATE, nper=CURRENT_AGE, pmt=0, fv=-ACCT_BAL)}")



#------ Problem 2 ------
print("\nProblem 2")

#Define a function to calculate the present value of a growing perpetuity
def growing_perp(intRate, cashFlow, growthRate):
  # The formula for the present value of a growing perpetuity is Cash Flow / (Interest Rate - Growth Rate)
  return cashFlow/(intRate - growthRate)

# Set the beginning balance
beg_bal = 1000000
# Set the high growth rate
high_growth_rate = .3
# Set the duration of high growth
high_growth_time = 5

# Set the slow growth rate
slow_growth_rate = .02

# Calculate the present value of cash flows during the high growth period
# This is done by discounting the future value of the beginning balance at the high growth rate for each year
initCashFlows = [future_val(rate=high_growth_rate, beg_bal=beg_bal, yrs=x)/(1+RATE)**x for x in range (1, high_growth_time+1)]
# Sum up the present values to get the total present value during the high growth period
pv_initial_growth = sum(initCashFlows)

# Calculate the cash flow for the first year after the high growth period
# This is done by growing the last cash flow during the high growth period at the slow growth rate for one year
CF1 = future_val(slow_growth_rate, initCashFlows[-1], 1)

# Calculate the present value of cash flows during the slow growth period
# This is done using the formula for a growing perpetuity
perpituity_cash_flows = growing_perp(RATE, CF1, slow_growth_rate)

# Print the present value of all future company earnings
# This is the sum of the present value during the high growth period and the present value during the slow growth period
print(f"PV of all future company earnings: {perpituity_cash_flows + pv_initial_growth}")
#------ Problem 3 ------ 
print("\nProblem 3")

def pv_annuity(payment, rate, comp_freq, total_periods):
  return (payment/(rate/comp_freq))*(1-(1/(1+(rate/comp_freq))**total_periods))

def annuity_factor(rate, periods):
    return (1/(rate/12))*(1 - (1/(1+rate/12)**periods))

#CONSTANTS
INIT_LOAN_PMT = 1402
INIT_LOAN_RATE = .1
LOAN_TERM = 30
COMP_FREQ = 12
TOTAL_PERIODS = LOAN_TERM*COMP_FREQ
REMAINING_PERIODS = 25*COMP_FREQ
NEW_LOAN_RATE = .06625

# determine what the initial balance for the loan actually was so you can see what principle was paid down
initial_bal = pv_annuity(INIT_LOAN_PMT, INIT_LOAN_RATE, COMP_FREQ, TOTAL_PERIODS)
# determine the balance of the loan at year 5
current_bal = INIT_LOAN_PMT * annuity_factor(INIT_LOAN_RATE, REMAINING_PERIODS)
print(f"current_bal: {current_bal}")

print(f"A. Monthly Payments on New Loan: {npf.pmt(NEW_LOAN_RATE/COMP_FREQ, TOTAL_PERIODS, current_bal)}")
print(f"B. Monthly Payments on New Loan (25yr Term): {npf.pmt(NEW_LOAN_RATE/COMP_FREQ, REMAINING_PERIODS, current_bal)}")
print(f"C. Time to repay at prior payment amount: {npf.nper(NEW_LOAN_RATE/COMP_FREQ, -INIT_LOAN_PMT, current_bal)/COMP_FREQ}")

#determine the present value of a loan that requires 25yr paymnet of $1402, the delta is the answer
full_loan_bal = -npf.pv(NEW_LOAN_RATE/COMP_FREQ, REMAINING_PERIODS, INIT_LOAN_PMT)
print(f"full_loan_bal: {full_loan_bal}")
print(f"D. Additional Amt Borrowed: ${full_loan_bal - current_bal}")


#------ Porblem 4 ------
print(f"\nPorblem 4")

DEBT_BAL = 35000
CURR_APR = .15
NEW_APR = .12

#determine the currently minimum monthly payment for the existing card
interest_payment = DEBT_BAL * CURR_APR/COMP_FREQ
print(f"interest_payment: {interest_payment}")

#determine new monthly payment minimum
new_interest_payment = DEBT_BAL * NEW_APR/COMP_FREQ
print(f"new_interest_payment: {new_interest_payment}")

#determine delta
delta_monthly_pmt = interest_payment - new_interest_payment
print(f"detla: {delta_monthly_pmt}")

#what is the debt balance increase that can lead to the same monthly payment
additional_debt = delta_monthly_pmt / (NEW_APR/COMP_FREQ)
print(f"additional_debt: {additional_debt}")


#------ Problem 5 ------
print(f"\nProblem 5")

def calc_EAR(apr, per):
  return (1+apr/per)**per - 1

def discount_factor(rate, per):
  return 1 / (1+rate)**per

SIGN_BONUS = 400000
SALARY = 250000
SALARY_DURATION = 3
DEF_DURATION = 10
DEF_AMT = 125000
PERF_BONUS_AMT = 75000
PERF_BONUS_PROB = .6
PROB_WEIGHT_AVG_BONUS = PERF_BONUS_AMT*PERF_BONUS_PROB #+0*(1-PERF_BONUS_PROB)
RATE = .06 #every 6 months
EAR = calc_EAR(RATE*2, 2)

#PV of initial 3 years
# PV of Signing Bonus is unimpacted: $400K
pv_signing = 400000

# PV of Salary ()
pv_salary = npf.pv(rate=RATE, nper=6, pmt=-SALARY/2)
print(f"pv_salary: {pv_salary}")

# PV of Bonuses
pv_bonus = npf.pv(rate=EAR, nper=3, pmt=-PROB_WEIGHT_AVG_BONUS)
print(f"pv_bonus: {pv_bonus}")

# PV of Def Payments
pv_def_payments = 0
total_periods = (SALARY_DURATION + DEF_DURATION)*2
for x in range(total_periods+1):
  if (x > 6):
    pv_def_payments += npf.pv(rate=RATE, nper=x, pmt=0, fv=-DEF_AMT/2)

# Method 2 - calculate PV of all cashflows then discount to PV
all_def_payments = npf.pv(rate=RATE, nper=DEF_DURATION*2, pmt=-DEF_AMT/2)
pv_alt_def_payments = npf.pv(rate=RATE, nper=SALARY_DURATION*2, pmt=0, fv=-all_def_payments)

print(f"pv_all_def_payments: {pv_alt_def_payments}")
print(f"pv_def_payments: {pv_def_payments}")
# PV Contract
print(f"Total Contract Value: {pv_signing + pv_salary + pv_bonus + pv_def_payments}")


#------ Problem 6 ------
print(f"\nProblem 6")

INVEST_AMT = 5000000
T0_CONSUMPTION = 2400000
A_PRINCIPAL = 750000
A_RETURN = 965000
B_PRINCIPAL = 630000
B_RETURN = 710000
C_PRINCIPAL = 350000
C_RETURN = 370000
RATE = .11
MOD_RATE = .09

# A
npv_a = npf.npv(rate=RATE, values=[-A_PRINCIPAL, A_RETURN])
npv_b = npf.npv(rate=RATE, values=[-B_PRINCIPAL, B_RETURN])
npv_c = npf.npv(rate=RATE, values=[-C_PRINCIPAL, C_RETURN])

print(f"\nA. NPV of a, b, c: {npv_a, npv_b, npv_c}")
print("Proj A and B have a positive NPV so they should be pursued")

#B
amt_after_consum = INVEST_AMT - T0_CONSUMPTION
amt_after_proj = amt_after_consum - A_PRINCIPAL - B_PRINCIPAL
val_with_interest = npf.fv(rate=RATE, nper=1, pmt=0, pv=-amt_after_proj)
total = val_with_interest + A_RETURN + B_RETURN
print(f"\nB. Max Avaialable T1 : {total}")

#C
npv_a = npf.npv(rate=MOD_RATE, values=[-A_PRINCIPAL, A_RETURN])
npv_b = npf.npv(rate=MOD_RATE, values=[-B_PRINCIPAL, B_RETURN])
npv_c = npf.npv(rate=MOD_RATE, values=[-C_PRINCIPAL, C_RETURN])
print(f"\nC. NPV of a, b, c: {npv_a, npv_b, npv_c}")
print("Proj A and B still have a positive NPV so the answer to A would not change")

amt_after_consum = INVEST_AMT - T0_CONSUMPTION
amt_after_proj = amt_after_consum - A_PRINCIPAL - B_PRINCIPAL
val_with_interest = npf.fv(rate=MOD_RATE, nper=1, pmt=0, pv=-amt_after_proj)
total = val_with_interest + A_RETURN + B_RETURN
print(f"\n The new answer for B: Max avaialable T1 : {total}")

#------ PROBLEM 7 ------
print(f"\nPROBLEM 7")

FLOWER_COST = 4
RATE = .04
COMP_FREQ = 52
PERIODS = 30 * COMP_FREQ

print(f"Present Value of Flower Vow: {npf.pv(rate=RATE/COMP_FREQ, nper=PERIODS, pmt=-FLOWER_COST)}")

#------ PROBLEM 8 ------
print(f"\nPROBLEM 8") 

RET_ACCT_RATE = .07
RET_AGE = 65
CURR_AGE = 30
DEATH_AGE = 100
RET_LENGTH = DEATH_AGE - RET_AGE
RET_BURN = 100000

#Caclculate how much you need in retirement to sustain $100k/yr
ret_balance = npf.pv(rate=RET_ACCT_RATE, nper=RET_LENGTH, pmt=-RET_BURN)
print(f"ret_balance needed to sustain 100K annual burn: {ret_balance}")

#What annual contribution fulfills this account balance requirement
contribution = npf.pmt(rate=RET_ACCT_RATE, nper=RET_AGE-CURR_AGE, pv=0, fv=-ret_balance)
print(f"contribution needed: {contribution}")

#------ PROBLEM 9 ------
print(f"\nPROBLEM 9") 
INIT_SALARY = 75000
SALARY_GROWTH_RATE = .02

# Define symbols
C, r, g, t, PV, FV = symbols('C r g t PV FV')

# The formula for the present value of a growing annuity
fv_annuity = Eq(FV, C * (((1+r)**t - (1+g)**t)/(r-g)))

# Example values for PV, r, g, t
fv_value = ret_balance  # Present Value
r_value = RET_ACCT_RATE    # Interest rate per period 
g_value = 0.02    # Growth rate of the annuity payments (2%)
t_value = 35      # Number of periods

# Solve for C (first payment)
first_payment = solve(fv_annuity.subs({FV: fv_value, r: r_value, g: g_value, t: t_value}), C)
print(f"First Payment: {first_payment[0]}")
print(f"% Required: {first_payment[0]/INIT_SALARY}")





