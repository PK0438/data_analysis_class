import sys

filename = input("Enter the file: ")

try:
    with open(filename) as f:
        contents = f.read()
    value1 = int(input("Enter the first integer value: "))
    value2 = int(input("Enter the second integer value: "))

    result = value1 + value2
    print("Outcome: ", result)

except ValueError:
    print("Please enter valid integer values.")
except FileNotFoundError as e:                              #Inspecting the error by assigning it to a variable
    print(f'The file {filename} was not found')
    print(type(e), e)                                       # Print the type of the error and the error. 
    # raise FileNotFoundError('You must enter integers only')        # Raising a custom error message using raise
    sys.exit()
except OSError:
    print('THere was an error accessing the file')
except Exception:
    print('Something went wrong')


