'''
A leap year (in the Gregorian calendar) occurs:

In every year that is evenly divisible by 4.
Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly divisible by 400.
Some examples:

1997 was not a leap year as it's not divisible by 4.
1900 was not a leap year as it's not divisible by 400.
2000 was a leap year!

Instructions
Your task is to determine whether a given year is a leap year.
'''

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
