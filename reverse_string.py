# complete the solution so that it reverses the string passed into it 

# to break this problem down 
# strings are just a list of characters which means that 
# they have indecies and are iterable
# we can use slicing -> the slice notation [start:stop:step]
# to explain the slicing in this case
'''
The start index, which is empty (:), means that the slice starts at the beginning of the sequence.
The stop index is also empty (:), which means that the slice goes to the end of the sequence.
The step value is -1, which specifies that you should traverse the sequence backward, moving from the end to the beginning.
'''
def reverse_string(word):
    reversed_string = word[::-1]
    print(reversed_string)

# Function test 
reverse_string("world") # dlrow
reverse_string("word")  # drow