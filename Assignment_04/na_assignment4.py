#Constants for Sales Manager Position
MIN_YEAR_SALES = 2
MIN_YEARS_TOP_AWARD = 1

# User's provided data:
years_sales = int(input('Enter your years of sales experience:'))
years_top_award = int(input('Enter how many years you have been salesperson of the year:')) # any error would be user error in this case.

if years_sales >= MIN_YEAR_SALES and years_top_award >= MIN_YEARS_TOP_AWARD:
    print('Congratulations! You are eligible for the Sales Manager Position.')
else:
# Multi-ine with f-string
    print(f'''
Sorry, you do not meet the requirements for the Sales Manager Position.

You need at least:
- {MIN_YEAR_SALES} years of sales experience
- {MIN_YEARS_TOP_AWARD} years as salesperson of the years_sales
''')