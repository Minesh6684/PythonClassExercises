# Two variables with int value
var_1 = 5
var_2 = 9

# addition to the third variable
var_3 = var_1 + var_2

# print all variables
print(f'First-variable: {var_1}')
print(f'Second-variable:{var_2}')
print(f'Third-variable:{var_3}')

# Two lists or any iterable can be concatenated using extend method
listOne = ['minesh', 674, 'smallpython']
listTwo = ['bigpython', True]
listOne.extend(listTwo)
print(listOne)

# Remove an element of a list

# POP-METHOD
# specific-element using index
listOne.pop(0)
print(listOne)
# last-element
listOne.pop()
print(listOne)

# REMOVE_METHOD
listOne.remove(674)
print(listOne)

# list element add
listOne.append('python') # adding element at the end of the list

# Accessing the elements of a list

listAccess = ['Jigar', 'Krishna', True, 45]
print(listAccess[2:5])



