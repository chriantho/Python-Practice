#Mutable objects: Can be changed after creation.
#Ex → list, dict, set

#Immutable objects: Cannot be changed after creation.
#Ex → int, float, string
#When you modify a mutable object, Python updates the same memory address. But when you modify an immutable object, Python creates a new object in memory.

# Mutable Example (List)
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits, "Memory:", id(fruits))

fruits.append("mango")
print("After modification:", fruits, "Memory:", id(fruits))  # same memory address

# Immutable Example (String)
name = "Chrishelle"
print("\nOriginal string:", name, "Memory:", id(name))

name += " Anthoneyz"
print("After modification:", name, "Memory:", id(name))  # different memory address
