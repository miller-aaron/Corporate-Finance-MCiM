"""
Problem 1
A.: $6,848.44
B.: $148,779.12
C.: $1,000.00

Problem 2
Answer - PV of all future company earnings: $51,981,214.36

Problem 3
Balance at 5 years:: $154,286.22
A. Monthly Payments on New Loan:: $-987.91
B. Monthly Payments on New Loan (25yr Term):: $-1,053.83
C. Time to repay at prior payment amount: 14.15746245052627
Full Loan Balance:: $205,259.23
D. Additional Amt Borrowed:: $50,973.01

Porblem 4
existing card min payment (interest): $437.50
new monthly payment amount: $350.00
detla between payments: $87.50
Answer - amount of additional debt that yields same payment: $8,750.00

Problem 5
PV of Salary: $614,665.54
PV of Bonus: $107,417.28
PV of Deferred Pymts: $505,365.12
Answer - Total Contract Value: $1,627,447.94

Problem 6
A. NPV of a, b, c: $119,369.37, $9,639.64, $-16,666.67
Proj A and B have a positive NPV so they should be pursued
B. Max Available T1: $3,029,200.00
C. NPV of a, b, c: $135,321.10, $21,376.15, $-10,550.46
Proj A and B still have a positive NPV so the answer to A would not change
The new answer for B- Max avaialable T1: $3,004,800.00

PROBLEM 7
Present Value of Flower Vow: $3,633.07

PROBLEM 8
Retirement balance needed to sustain 100K annual burn: $1,294,767.23
Contribution Required: $9,366.29

PROBLEM 9
First Payment: $7,461.18
% Required: 9.95%
"""

import numpy_financial as npf
from sympy import symbols, Eq, solve

#FINANCE HOME WORK 1 

#print answer in a readable, financial format
def print_answer(label, value):
  if isinstance(value, tuple):
    formatted_values = [f"${val:,.2f}" for val in value]
    formatted_value = ", ".join(formatted_values)
    print(f"{label}: {formatted_value}")
  else:
    formatted_value = "{:,.2f}".format(value)
    print(f"{label}: ${formatted_value}")

#------ Problem 1  ------
CURRENT_AGE = 18
ACCT_BAL = 3996
RATE = .08

def future_val(rate, beg_bal, yrs):
  return beg_bal * (1+rate)**yrs

def present_val(rate, end_bal, yrs):
  return end_bal/ (1+rate)**yrs

print("Problem 1")
#a. calculate addition interest between 18 and 25
print_answer(label="A.", value=npf.fv(rate=RATE, nper=25-CURRENT_AGE, pmt=0, pv=-ACCT_BAL))

#b. 65th
print_answer(label="B.", value=npf.fv(rate=RATE, nper=65-CURRENT_AGE, pmt=0, pv=-ACCT_BAL))

#c. discount current balance back to PV when grandfather invested 
print_answer(label="C.", value=npf.pv(rate=RATE, nper=CURRENT_AGE, pmt=0, fv=-ACCT_BAL))



#------ Problem 2 ------
print("\nProblem 2")

#Define a function to calculate the present value of a growing perpetuity
def growing_perp(int_rate, cash_flow, growth_rate):
  # The formula for the present value of a growing perpetuity is Cash Flow / (Interest Rate - Growth Rate)
  return cash_flow/(int_rate - growth_rate)

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
init_cash_flows = [future_val(rate=high_growth_rate, beg_bal=beg_bal, yrs=x)/(1+RATE)**x for x in range (1, high_growth_time+1)]
# Sum up the present values to get the total present value during the high growth period
pv_initial_growth = sum(init_cash_flows)

# Calculate the cash flow for the first year after the high growth period
# This is done by growing the last cash flow during the high growth period at the slow growth rate for one year
CF1 = future_val(rate=slow_growth_rate, beg_bal=init_cash_flows[-1], yrs=1)

# Calculate the present value of cash flows during the slow growth period
# This is done using the formula for a growing perpetuity
perpituity_cash_flows = growing_perp(RATE, CF1, slow_growth_rate)

# Print the present value of all future company earnings
# This is the sum of the present value during the high growth period and the present value during the slow growth period
print_answer(label="Answer - PV of all future company earnings", value=perpituity_cash_flows + pv_initial_growth)

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
print_answer(label="Balance at 5 years:", value=current_bal)

print_answer(label="A. Monthly Payments on New Loan:", value=npf.pmt(rate=NEW_LOAN_RATE/COMP_FREQ, nper=TOTAL_PERIODS, pv=current_bal))
print_answer(label="B. Monthly Payments on New Loan (25yr Term):", value=npf.pmt(rate=NEW_LOAN_RATE/COMP_FREQ, nper=REMAINING_PERIODS, pv=current_bal))
print(f"C. Time to repay at prior payment amount: {npf.nper(rate=NEW_LOAN_RATE/COMP_FREQ, pmt=-INIT_LOAN_PMT, pv=current_bal)/COMP_FREQ}")

#determine the present value of a loan that requires 25yr paymnet of $1402, the delta is the answer
full_loan_bal = -npf.pv(rate=NEW_LOAN_RATE/COMP_FREQ, nper=REMAINING_PERIODS, pmt=INIT_LOAN_PMT)
print_answer(label="Full Loan Balance:", value=full_loan_bal)
print_answer(label="D. Additional Amt Borrowed:", value=full_loan_bal - current_bal)


#------ Porblem 4 ------
print(f"\nPorblem 4")

DEBT_BAL = 35000
CURR_APR = .15
NEW_APR = .12

#determine the currently minimum monthly payment for the existing card
interest_payment = DEBT_BAL * CURR_APR/COMP_FREQ
print_answer(label="existing card min payment (interest)", value=interest_payment)

#determine new monthly payment minimum
new_interest_payment = DEBT_BAL * NEW_APR/COMP_FREQ
print_answer(label="new monthly payment amount", value=new_interest_payment)

#determine delta
delta_monthly_pmt = interest_payment - new_interest_payment
print_answer(label="detla between payments", value=delta_monthly_pmt)

#what is the debt balance increase that can lead to the same monthly payment
additional_debt = delta_monthly_pmt / (NEW_APR/COMP_FREQ)
print_answer(label="Answer - amount of additional debt that yields same payment", value=additional_debt)


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
print_answer(label="PV of Salary", value=pv_salary)

# PV of Bonuses
pv_bonus = npf.pv(rate=EAR, nper=3, pmt=-PROB_WEIGHT_AVG_BONUS)
print_answer(label="PV of Bonus", value=pv_bonus)

# PV of Def Payments
pv_def_payments = 0
total_periods = (SALARY_DURATION + DEF_DURATION)*2
for x in range(total_periods+1):
  if (x > 6):
    pv_def_payments += npf.pv(rate=RATE, nper=x, pmt=0, fv=-DEF_AMT/2)

# Method 2 - calculate PV of all cashflows in year 3 dollars then discount to PV
all_def_payments = npf.pv(rate=RATE, nper=DEF_DURATION*2, pmt=-DEF_AMT/2)
pv_alt_def_payments = npf.pv(rate=RATE, nper=SALARY_DURATION*2, pmt=0, fv=-all_def_payments)

print_answer(label="PV of Deferred Pymts", value=pv_def_payments)
# PV Contract
print_answer(label="Answer - Total Contract Value", value=pv_signing + pv_salary + pv_bonus + pv_def_payments)


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

print_answer(label="A. NPV of a, b, c", value=(npv_a, npv_b, npv_c))
print("Proj A and B have a positive NPV so they should be pursued")

#B
amt_after_consum = INVEST_AMT - T0_CONSUMPTION
amt_after_proj = amt_after_consum - A_PRINCIPAL - B_PRINCIPAL
val_with_interest = npf.fv(rate=RATE, nper=1, pmt=0, pv=-amt_after_proj)
total = val_with_interest + A_RETURN + B_RETURN
print_answer(label="B. Max Available T1", value=total)

#C
npv_a = npf.npv(rate=MOD_RATE, values=[-A_PRINCIPAL, A_RETURN])
npv_b = npf.npv(rate=MOD_RATE, values=[-B_PRINCIPAL, B_RETURN])
npv_c = npf.npv(rate=MOD_RATE, values=[-C_PRINCIPAL, C_RETURN])
print_answer(label="C. NPV of a, b, c", value=(npv_a, npv_b, npv_c))
print("Proj A and B still have a positive NPV so the answer to A would not change")

amt_after_consum = INVEST_AMT - T0_CONSUMPTION
amt_after_proj = amt_after_consum - A_PRINCIPAL - B_PRINCIPAL
val_with_interest = npf.fv(rate=MOD_RATE, nper=1, pmt=0, pv=-amt_after_proj)
total = val_with_interest + A_RETURN + B_RETURN
print_answer(label="The new answer for B- Max avaialable T1", value=total)

#------ PROBLEM 7 ------
print(f"\nPROBLEM 7")

FLOWER_COST = 4
RATE = .04
COMP_FREQ = 52
PERIODS = 30 * COMP_FREQ

pv_flower_vow = npf.pv(rate=RATE/COMP_FREQ, nper=PERIODS, pmt=-FLOWER_COST)
print_answer(label="Present Value of Flower Vow", value=pv_flower_vow)

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
print_answer(label="Retirement balance needed to sustain 100K annual burn", value=ret_balance)

# What annual contribution fulfills this account balance requirement
contribution = npf.pmt(rate=RET_ACCT_RATE, nper=RET_AGE-CURR_AGE, pv=0, fv=-ret_balance)
print_answer(label="Contribution Required", value=contribution)

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
print_answer(label="First Payment", value=first_payment[0])
print(f"Percent of Salary Required: {first_payment[0]/INIT_SALARY*100:.2f}%")