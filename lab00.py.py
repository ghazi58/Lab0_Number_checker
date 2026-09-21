# CYB434 - Lab 0 - Number Checker
# Name: Ghazi
# University ID: 4502702


def classify_number(number):
    # A function is a named task. 'number' receives the value passed to it.
    # Replace the return below with if / elif / else.
    # Return "Positive" for values above 0, "Negative" for values below 0,
    # and "Zero" for 0. Use return to send the answer back to the caller.
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


# This loop is provided. Read it and keep it in your program.
choice = "y"
while choice == "y":
    # input gives text; int converts valid whole-number text to an integer.
    number = int(input("Enter a whole number: "))
    result = classify_number(number)

    # There is one deliberate variable-name error on the next line.
    print(result)

    # Type lowercase y to repeat, or lowercase n to stop.
    choice = input("Check another number? (y/n): ")

print("Goodbye!")


# Complete these comments after testing. Do not remove the # characters.
# Error fixed: The variable name was written as resultt instead of result, so I corrected it to result.
# Loop explanation: When choice is y, the while condition is true and the loop repeats. When choice is n, the condition is false and the loop stops.
# My test results: 8 -> Positive, -3 -> Negative, and 0 -> Zero. Each test also printed Goodbye! after entering n to stop.
