# Answer the questions or complete the tasks outlined in bold below, 
# use the specific method described if applicable.

# Q1 : ** What is 7 to the power of 4?**
x = 7 ** 4
print(x)
#------------------#

# Q2 : ** Split this string:** *into a list. * 
# ['Hi', 'there', 'Sam!']
# the split method returns a list 
text = "Hi there Sam!"
text_list = text.split(" ")
print(text_list)

#-------------------#

# Q3 : ** Given the variables:** 
# planet = "Earth" , diameter = 12742
# ** Use .format() to print the following string: **
# The diameter of Earth is 12742 kilometers.
# note that when formating a string the curly brackets acts as place holders for the variables 
# define the variables 
planet = "Earth"
diameter = 12742
formated_string  = "The diameter of {} is {} kilometers.".format(planet, diameter)
print(formated_string)

#---------------------#

# Q4 : Given this nested list, use indexing to grab the word "hello"

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
third_element = lst[3]
first_element_in_third_element = third_element[1]
second_element_in_first_element_in_third_element = first_element_in_third_element[2]
zero_element_in_econd_element_in_first_element_in_third_element = second_element_in_first_element_in_third_element[0]
print(zero_element_in_econd_element_in_first_element_in_third_element)

# Q5 : d1 = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
# here the nesting consistes of dict -> list -> dict -> list -> dict -> list in this exact arrange 
# so we need to dig through this dict using the above map 
# note that when you use the fuction .values the returned value type is dict_valued and you can not use indexing with that 
# so to get the value with its exact data type use the key to navigate through the dictionary 
d1 = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
lst1 = d1['k1']
d2 = lst1[3]
lst2 = d2["tricky"]
d3 = lst2[3]
lst3 = d3['target']
# Now you know that 'hello' is in the third list which was in the third dictionary 
print(lst3[3])

#------------#

# Q6 : ** Create a function that grabs the email website domain from a string in the form: **
# So for example, passing "user@domain.com" would return: domain.com
def domain_Get(email):
    email_pieces = email.split("@")
    return email_pieces[1]

# function test
print(domain_Get("beesan_alattal@wow.com"))

#-----------------------#

# Q7 : Create a basic function that returns True if the word 'dog' is contained in the input string.
#  Don't worry about edge cases like a punctuation being attached to the word dog, 
# but do account for capitalization. **

def find_dog(text):
    lower_text = text.lower()
    return "dog" in lower_text

# function test 
text = "Yesterday, I took my DOG, for a long walk in the park."
print(find_dog(text))

#----------------------#
# Q8 : ** Create a function that counts the number of times the word "dog" occurs in a string.
# Again ignore edge cases. **

def count_dog(text):
    text_lower = text.lower()
    return text_lower.count('dog')

# function test 
text1 = 'This dog runs faster than the other dog dude!'
count_dog(text1)

# Q9 : Use lambda expressions and
#  the filter() function to filter out words from 
# a list that don't start with the letter 's'.
#  For example:**
#  seq = ['soup','dog','salad','cat','great']
# output : ['soup','salad']
# filter function - filter(function, iterable)
# returns  filter object , the fuction you pass should return a boolean value and 
# the other argument should be an iterable value such as a list dictionary 

seq = ['soup','dog','salad','cat','great']
filterd_list = list(filter(lambda word : word.startswith('s') or word.startswith('S'), seq))

# test lambda 
print(filterd_list)

# Q10 : the final problem 
#*You are driving a little too fast, and a police officer stops you.
#  Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
# If your speed is 60 or less, the result is "No Ticket". 
# If speed is between 61 and 80 inclusive, the result is "Small Ticket". 
# If speed is 81 or more, the result is "Big Ticket".
#  Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, 
# your speed can be 5 higher in all cases. *
# in this case you need to import the datetime 
from datetime import datetime  
def is_birthday(birth_date):
    today = datetime.now().date()
    return today.month == birth_date.month and today.day == birth_date.day
def caught_speeding(speed, is_birthday) :
    if is_birthday or speed <= 60:
        print("No ticket :)")
    elif 61 <= speed <= 80 :
        print("Small Ticket")
    elif speed >= 81:
        print("Big Ticket!")
# test 
# tip : to insert your birth date use a variable datetime type 
# tip : remember when passing a function as an argument write it as you are calling it normally 
# datetime(year, month, day)
birthday1 = datetime(2000, 10, 25) # True 
birthday2 = datetime(2004, 1, 10) # false 
caught_speeding(81, is_birthday(birthday1)) 
caught_speeding(81, is_birthday(birthday2)) 









 


