######################################################
# Python Basics
######################################################

import datetime

def find_vowels_consonants(string):
    """
    Write a function that takes a string in English as input 
    and returns the number of vowels and consonants.
    For example:
    If the string is 'The cat is sleeping', 
    then the function should return : (6, 10)
    """
    
    number_vowels = 0
    number_consonants = 0
    
    # write your code here

    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'

    string = string.lower()  # preprocessing

    for char in string:

        if char in vowels:

            number_vowels += 1

        elif char in consonants:

            number_consonants += 1

    return number_vowels, number_consonants



def make_team():
    """
    Write a function that takes a dictionary called people as input (see below) 
    and returns 3 lists named cook, gardener and clerk containing the name of 
    each individual with this job.
    """
    
    people = {
        'Pete': {
            'Age': 51,
            'Job': 'Cook'
        },
        'John': {
            'Age': 32,
            'Job': 'Gardener'
        },
        'Jim': {
            'Age': 45,
            'Job': 'Cook'
        },
        'Sheila': {
            'Age': 19,
            'Job': 'Clerk'
        },
        'Carol': {
            'Age': 67,
            'Job': 'Gardener'
        },
        'Richard': {
            'Age': 17,
            'Job': 'Clerk'
        }
    }
        
    cook = []
    gardener = []
    clerk = []
    
    # write your code here

    for name in people:

        if people[name]['Job'] == 'Cook':

            cook.append(name)

        elif people[name]['Job'] == 'Gardener':

            gardener.append(name)

        elif people[name]['Job'] == 'Clerk':

            clerk.append(name)

    return cook, gardener, clerk



def find_fridays(start_date, end_date):
    """
    Write a function that given a start date and end date returns how many 
    Fridays there are between the two dates.
    start_date and end_date should be 'YYYY-MM-DD' strings, e.g. '2014-01-31'
    """
    
    number_of_fridays = 0
    
    # write you code here

    # assumed between was non inclusive
    # using the module datetime

    # concerting to datetime.date objects
    start_date = datetime.date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10]))
    end_date = datetime.date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10]))

    days_between = (end_date - start_date).days - 1

    number_of_fridays += int(days_between / 7)  # 1 friday every full week

    if start_date.weekday() != 4:  # if start_date is not friday, friday is defined as 4 in datetime.date.weekday()

        extra_days = days_between % 7
        friday_gap = (4 - start_date.weekday()) % 7  # number of days between start_date and the next friday

        if extra_days >= friday_gap:  # check if enough 'extra' days to reach the next friday

            number_of_fridays += 1

    return number_of_fridays



def check_number_anagram(integer):
    """
    Write a function that gets an integer number as input and returns a boolean 
    type True or False based on whether the number when read backwards gives 
    the same number. This would be the equivalent of an anagram with strings.
    E.g. input of number 1234321 would return True.
    """
    
    flag = True

    # write you code here

    # this is just checking for palindromes not anagrams
    # '112' and '121' are anagrams of each other but only '121' is a palindrome

    integer = str(integer)
    flipped = ''

    for i in range(len(integer)):

        flipped += integer[-i - 1]

    flag = flipped == integer

    # also works with strings

    return flag
