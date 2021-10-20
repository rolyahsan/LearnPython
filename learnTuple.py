# Built-in Tuple methods:
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

fav_food = ("Pizza", "Bear Claws", "Cake", "Ice Cream", "Candy")

# Prints the second item from the tuple
print(fav_food[1])

# Prints the last item from the tuple
print(fav_food[-1])

# The search will start at index 1 (included) and end at index 4 (not included)
# Value from the 1st index will be included, and value from the 4th index will be excluded
print(fav_food[1:4])

# Returns the items from the beginning to, but NOT included, "Ice Cream"
print(fav_food[:3])

# Returns the items from "Cake" and to the end
print(fav_food[2:])

# Returns the items from index -4 (included) to index -1 (excluded)
print(fav_food[-4:-1])

# Check if the item is in the tuple
if "cake" in fav_food:
    print("Cake is in fav_food tuple list")
else:
    print("Item does not exist")

# Since tuple is immutable, you cannot add item to it. But there are different ways you can add item to a tuple.
# First, convert the tuple into a list, add item(s), and convert it back into a tuple
food_list = list(fav_food)
print(type(food_list))  # Check the list type
food_list.append("Cookie")
food_list.append("Milk Shake")
print(food_list)
new_fav_food = tuple(food_list)
print(type(new_fav_food))  # Check the list type
print(new_fav_food)

# Using FOR loop to iterate through a tuple
for x in new_fav_food:
    print(x, end="   ")

print("")

# Using WHILE loop to iterate through a tuple
i = 0
while i < len(new_fav_food):
    print(new_fav_food[i], end="   ")
    i = i + 1

print("")

# Join Tuples
tuple1 = ("a", "b", "c", "a", "c", "a")
tuple2 = (1, 2, 3, 6, 4, 4, 2, 2)
alphanumeric_char = tuple1 + tuple2
print(alphanumeric_char)

# Count number of times the occurs in the Tuple
print(alphanumeric_char.count(2))
print(alphanumeric_char.count("a"))
print(alphanumeric_char.count("c"))
