# This Kata is about multiplying a given number by eight if it is an even number 
# and by nine other wise 
#-----notes before writing the solution-----#

# 1. In mathematics, even and odd numbers are typically defined for integers --> so when we are dealing with even/odd numbers your numbers are integers for sure
# 2. What does the word kata mean?
# Answer : a "kata" refers to a small coding exercise or challenge. These coding katas are used for practice and improvement in coding skills.
# even number % 2 == 0 otherwise it is an odd number
def multiply_by_eight_or_nine(number):
    if number % 2 == 0:
        print(number * 8)

    else:
        print(number * 9)

# Function test 
multiply_by_eight_or_nine(22) # output 22*8 = 176
multiply_by_eight_or_nine(33) # output 33*9 = 297 