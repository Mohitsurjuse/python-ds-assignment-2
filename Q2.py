#Create an empty list, add 3 fruits to it, then print the list

fruits = [] #empty list
print('---Empty list---')
print(fruits)
fruits.append('Strawberry') #append () adds data at end of list
fruits.insert(1, 'Grapes') #insert () adds data at specified index
fruits.extend(['Banana']) #extend () adds data at end of list, but it can add multiple items at once
print('---After adding 3 fruits to list---')
print(fruits)