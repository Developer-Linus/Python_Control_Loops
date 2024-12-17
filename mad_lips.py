adjective1 = input("Give your first adjective describing the day.")
action1 = input("Give your first action verb of how you accomplish your day")
name1 = input("Give a name of a creature of supreme being.")
action2 = input("Give your second action verb")
adjective2 = input("Give your second adjective describing a story.")

if len(adjective1)>0 and len(adjective2)>0 and len(action1)>0 and len(action2)>0 and len(name1)>0:
    print("You are a great story teller.")

print(f'''Every day I woke up to a {adjective1} day.
      The first thing that comes to my mind is how I {action1} the new day.
      Then I remember only {name1} said you don't have to {action2} as I am with you. 
      Did this sound {adjective2} to you?''')