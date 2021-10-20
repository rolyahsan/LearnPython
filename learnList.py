# List of built-in methods:
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()     Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# Adding items to a list
fav_cars = ["M3", "Shelby", "ZR1", "Demon", "Plaid"]
print(fav_cars)

# Iterating through the list
for car in range(len(fav_cars)):
    print(fav_cars[car], end=" ")

print("")
# Adding a item to the end of the list
fav_cars.append("M5")
print(fav_cars)

# Deleting a specified item
fav_cars.remove("Demon")
print(fav_cars)

# Deleting a item at the specified index position
fav_cars.pop(2)
print(fav_cars)

# Adding a new item at the specified index position
fav_cars.insert(2, "ZR1")
print(fav_cars)

fav_cars[2:] = ["R7", "S1000RR"]
print(fav_cars)

fav_cars[:3] = ["R6", "ZX6R"]
print(fav_cars)

fruits = ["Apple", "Grapes", "Orange"]

# Adding a entire separate list to an existing list using extend() method
fav_cars.extend(fruits)
print(fav_cars)

# Grab the elements that contains "a", then add those to a new list
new_list = []
for x in fav_cars:
    if "a" in x.lower():
        new_list.append(x)
print(new_list)

# Used List Comprehension to grab the elements that contains "a", then add those to a new list
new_list2 = [x for x in new_list if "p" in x.lower()]
print(new_list2)

# Copied all the elements from a existing list to a new list using list() method
copied_list = list(fav_cars)
print(copied_list)

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# Value from the 2nd index will be included, and value from the 5th index will be excluded
print(fruits[2:5])
