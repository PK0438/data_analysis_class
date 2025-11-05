
try:
    value1 = int(input("Enter the first integer value: "))
    value2 = int(input("Enter the second integer value: "))

    result = value1 + value2
    print("Outcome: ", result)

except ValueError:
    print("Please enter valid integer values.")
    exit()

