#Set = {1,3,5}. Use loop to print even numbers (none)
set= {1,3,5}
print('---Access complete set---')
print(set)

#access data using loop
print('---loop to access even numbers---')
for i in set:
    if i%2 == 0: #if statement to check even numbers
        print(i, end= ' ')
    else:
        print("(none)")