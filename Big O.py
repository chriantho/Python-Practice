import time

# O(1) - Constant time
def get_first_item(lst):
    return lst[0]

# O(n) - Linear time
def print_all_items(lst):
    for item in lst:
        print(item)

# O(n²) - Quadratic time
def print_pairs(lst):
    for i in lst:
        for j in lst:
            print(i, j)

# Measuring performance
numbers = list(range(1000))

start = time.time()
print_pairs(numbers[:100])  # smaller input for demo
end = time.time()

print("\nExecution time:", round(end - start, 5), "seconds")
