# Create a function the takes an integer as an argument and returns "Even" for even numbers ans "Odd" for odd numbers 
# beginner friendly problem

def is_even_or_odd(number):
   return (number % 2 == 0)
# the function above returns False or True
# 0 -> odd
# 1 -> even 

def is_even_or_odd1(number):
   if number % 2 == 0:
      print("Even")
   else:
      print("Odd")

# test 
print(is_even_or_odd(1)) # Fasle
print(is_even_or_odd(2)) # True

# test 
is_even_or_odd1(23) # Odd
is_even_or_odd1(22) # even 



