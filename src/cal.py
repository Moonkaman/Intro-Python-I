"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

date = datetime.now()


def month_get(month):
    switcher = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12
    }
    return str(switcher.get(month, 'Please provide a LOWERCASE valid month name such as "january"'))


if len(sys.argv) <= 1:
    c = calendar.TextCalendar().formatmonth(date.year, date.month)
    print(c)
elif len(sys.argv) == 2:
    selected_month = month_get(sys.argv[1])
    if selected_month.isalpha():
        print(selected_month)
    else:
        c = calendar.TextCalendar().formatmonth(date.year, int(selected_month))
        print(c)
else:
    selected_year = str(sys.argv[2])
    selected_month = month_get(sys.argv[1])
    if selected_month.isalpha():
        print(selected_month)
    elif selected_year.isalpha():
        print('Invalid year')
    else:
        c = calendar.TextCalendar().formatmonth(int(selected_year), int(selected_month))
        print(c)
