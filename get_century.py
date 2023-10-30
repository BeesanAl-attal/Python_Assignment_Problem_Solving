# The first century spans form the year 1 up to 100 , the second century from the year 101 up to year 200 etc.
# Task: given a year, return the century it is in .
# to break this down ->
# the first century is and it spans from year one to 100 
# the maximun value of the years(number) which is 100
# contains only ONE (100) --> first century 
# if we are in year 300 it 300 contains THREE 100 --> Third century 
# so we divide the year by 100
# what if the year is 201 and the division equals = 2.01 --> round it up 
# to round up use the math ceil function 

import math

def get_century(year):
    century = math.ceil((year / 100))
    print(century)

# test 
get_century(1705) # 18
get_century(1900) # 19
get_century(1601) # 17
get_century(2000) # 20
get_century(2023) # 21
get_century(1)    # 1