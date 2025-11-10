# Debugging a division function

def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError as e:
        print("Error:", e)
    finally:
        print("Execution complete.")

divide_numbers(10, 2)
divide_numbers(5, 0)  # triggers ZeroDivisionError


# Using print debugging
numbers = [1, 2, 3, 0, 4]

for num in numbers:
    print("Current number:", num)
    if num == 0:
        print("Skipping division by zero")
        continue
    print("10 / num =", 10 / num)
