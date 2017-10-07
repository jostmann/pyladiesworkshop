print()
print("Welcome to the dungeon!")
print("Do you go through door 1 or door 2?")

door = input("> ")

if door == "1":
    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("1. Smile and nod")
    print("2. Scream and run")

    vampire = input("> ")

    if vampire == "1":
        print("Congratulations, you found a new friend!")
    elif vampire == "2":
        print("Sorry, the vampire is faster. You become a dinner.")
    else:
        print("You are not so good with numbers, are you?")

elif door == "2":
    print ("a trap door opens and you fall deep down into a hole of everlasting madness")
    print ("a T-Rex is emerging in front of your eyes and asks for a cigarette")
    print ("1. You are giving the T-Rex a cigarette!")
    print ("2. Do you deny him and tell him to get lost")
    
    T_Rex = input (">") 
    if T_Rex == "1":
        print ("You pass the T-Rex a cig and he throws it on the ground and stomps on it, telling you that this shit is unhealthy")
    elif T_Rex == "2":
        print ("T-Rex eats you up for breakfast")

else:
    print("You are not so good with numbers, are you?")
