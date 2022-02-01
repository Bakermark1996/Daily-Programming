fruit = ["Apple", "Orange", "Pear"]
fruit.append("Banana")
fruit.append("Peach")
print(fruit)
fruit.pop()
print(fruit)

my_tuple = ("M. Jackson", 1958, True)
print(my_tuple[1])

my_dict = {"Mark": 25,
           "Rebekkah": 27}

print(my_dict)

n = input("Type a noun:")
v = input("Type a verb:")
n1 = input("Type another noun:")

print("The {} {} the {}.".format(n, v, n1))
