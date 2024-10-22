'''
Day 19
Loan Calculator
'''

loan = input("Enter the loan amount: ")
interestRate = input("Enter the interest rate: ")
years = input("Enter the number of years: ")

print(f"""
    == Loan Calculator ==
    
    ${loan} loan over {years} years at {interestRate}% APR
    
    Year \t\t Loan Balance
""")

for i in range(1, int(years) + 1):
    loan = float(loan) * (1 + float(interestRate) / 100)
    print(f"\t {i} \t\t\t ${loan:.2f}")
