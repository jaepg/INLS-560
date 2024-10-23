#Constants for Pet Insurance Assistance
MIN_YEAR_OWNER = 3
MIN_YEARS_PET_INSURANCE = 1

# User's provided data:
years_sales = int(input('Enter your amount of pets:'))
years_top_award = int(input('Enter how many years you have had at least 3 pets:')) # any error would be user error in this case.

if years_sales >= MIN_YEAR_OWNER and years_top_award >= MIN_YEARS_PET_INSURANCE:
    print('Congratulations! You are eligible for pet insurance assistance.')
else:
# Multi-ine with f-string
    print(f'''
Sorry, you do not meet the requirements for pet insurance assistance.

You need at least:
- {MIN_YEAR_OWNER} pets under your ownership.
- {MIN_YEARS_PET_INSURANCE} year taking care of at least 3 pets.
''')