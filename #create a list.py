# Creating a list
my_list = [1, 2, 3, 4, 5]

# Adding an element to the list
my_list.append(6)
print("My list after adding an element to the list:", my_list)

# Removing an element from the list
my_list.remove(3)
print("My list after removing an element from the list:", my_list)

# Modifying an element in the list
my_list[0] = 10
print("Updated List:", my_list)

# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'Delhi'}

# Adding an element to the dictionary
my_dict['gender'] = 'Male'

# Removing an element from the dictionary
del my_dict['age']

# Modifying an element in the dictionary
my_dict['city'] = 'Mumbai'

# Display the updated dictionary
print("Updated dictionary:", my_dict)

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding an element to the set
my_set.add(6)

# Removing an element from the set
my_set.remove(3)

# Modifying the set (removing one element and adding another)
my_set.discard(1)
my_set.add(10)

print("Updated Set:", my_set)
