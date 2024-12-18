# This is used to address the nesting complexity brought about by nesting various if, else, and elif statements for intricate situations
day = input("Enter the day of the week (monday-sunday)").lower()

match day:
    case "monday":
        print("Ugh, Mondays")
    case "tuesday":
        print("Just another work day...")
    case "wednesday":
        print("Hump day!")
    case "thursday":
        print("Almost there!")
    case "friday":
        print("TGIF!")
    case "saturday"| "sunday":
        print("weekend vibes.")
    case _:
        print("You have entered an invalid day")
    