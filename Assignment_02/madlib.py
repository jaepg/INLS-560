# Mad lib example for functions.

def madlib(noun_1, noun_2, verb_1, verb_2, adverb_1, noun_3, verb_3, adverb_2, 
    adj_1):
    '''Mad lib function'''

    story =f'''
Once upon a time, a charming dog decided to take a young lady on a date. They 
met at the local {noun_1} , where the dog handed her a beautiful {noun_2} . 
Together, they {verb_1} down the street, enjoying the fresh air. Suddenly, the 
dog stopped and began to {verb_2} {adverb_1} in front of her, causing everyone 
to stare. Embarrassed but flattered, the young lady smiled and petted the dog. 
They continued their date at a nearby {noun_3} , where they {verb_3} {adverb_2} 
until the sun set. It was a {adj_1} day, and the young lady couldn’t help 
but think this was the best date she'd ever been on.
'''
    return story

def get_user_input():
    """Prompt the user for input for the madlib"""
    noun_1 = input("Enter ")
    noun_2 = input("Enter ")
    verb_1 = input("Enter ") 
    verb_2 = input("Enter ") 
    adverb_1 = input("Enter ") 
    noun_3 = input("Enter ") 
    verb_3 = input("Enter ") 
    adverb_2 = input("Enter ")
    adj_1 = input("Enter ")

    return noun_1, noun_2, verb_1, verb_2, adverb_1, noun_3, verb_3, adverb_2, adj_1

# Get user input.
user_inputs = get_user_input()

# Print the madlib story.
print(madlib(*user_inputs))