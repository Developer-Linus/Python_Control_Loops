# This one is used to check the data type entered by the user.
value = input("Enter a value (number or string): ")

match value:
    case int():
        print(f"You have entered a number, {value}")
    case str():
        print(f"You have entered a string, {value}")

    case _:
        print("You have entered an invalid data type")