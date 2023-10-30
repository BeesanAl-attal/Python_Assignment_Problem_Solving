# create a function that checks if a number (n) is divisible by two number x and y 
# the funcion returns a boolean value 
# to break this down 
# i need to pass the function three integer non zero positive numbers 
# then if n % y == 0 and n % x == 0 then return true 

def is_dividible_by_x_and_y(n, x, y):
    if n % y == 0 and n % x == 0 :
     print(True)
    else:
       print(False)
# Function test
is_dividible_by_x_and_y(3, 1, 3) # True 
is_dividible_by_x_and_y(12, 2, 6) # True 
is_dividible_by_x_and_y(100, 5, 3) # False
is_dividible_by_x_and_y(12, 7, 5) # False 

 