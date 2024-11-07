try:
    # number = int(input("Enter a number: "))
    number = 5
    result = 10 / number
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a numeric value.")
else:
    print("The result is:", result)
# If no exception occurs, the result will be printed
c = 2**4
print(c)

describe ='my na'