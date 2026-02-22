#Write function that takes list and returns its length
cities = ['Amravati','Nagpur', 'Delhi', 'Hyderabad', 'Mumbai'] #list
def take(cities): #passing list as parameter
    return len(cities) #return length of list

#call function
take(cities)
print("Length of the list:", take(cities))