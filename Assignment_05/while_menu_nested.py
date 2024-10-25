### Assignment 05
# Primes menu option variable
menu_option = ''

# Loop that runs until menu_option is equal to 'q
while menu_option != 'q':
    print(f'''
    Pawsome Pet Care and Salon:
    a: Schedule Vet Visit
    b: Schedule Pet Grooming
    q: exit
    ''')

if menu_option =='a':
    print('Please call us so we can provide you with our best service!')
elif menu_option == 'b': 
    van_driver = input('Have you taken your pet to our establishment before? enter (y or n): ')
    if van_driver == 'y':
        print("Pawsome! It's great to see you again!")
    else:
        print("Please call us to set up a new pet profile for your pawsome friend!")
    