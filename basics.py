name = "Roly"
print(name)

x = 11
print(x)
print(type(x))
print("x = " + str(x))

if name == "Roly":
    print("True")
else:
    print("False")

for i in range(0, x):
    if i % 2 == 0:
        print(i, end=" ")

print("")


def is_palindrome(word):
    temp = word[::-1]
    if word.lower() == temp.lower():
        return "This is a Palindrome"
    else:
        return "This is not a Palindrome"


print(is_palindrome("RaceCar"))
