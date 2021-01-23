try:
    age = int(input("Enter your age: "))  # Enter 3
    months = age * 12
except Exception as e:
    print(f"The problem was: {e}")
    print("Hey user, you have not provided a valid number?")
    age = int(input("Enter your age: "))  # Enter 3
    months = age * 12

print(f"You have lived for {months} months.")  # Prints You have lived for 36 months.

"""
A small exercise: calculate number of seconds lived instead of months!
"""
