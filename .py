from art import logo2
print(logo2)
print("welcome to treasure land :")
print("your mission is to find the treasure.")

#first decision: left or right
choice1 = input('do you want to go "left" or "right" ').lower()

if choice1 == "left":
    # second decision : swim or wait
    choice2 = input('Do you want to "swim" or "wait" ? ').lower()
    if choice2 == "wait":
        choice3 = input('which door? "red","blue",or "yellow"?').lower()

        if choice3 == "yellow":
            print("you win!")
        elif choice3 == "red":
            print("burned by fire. game over")
        elif choice3 == "blue":
            print("eaten by beasts. game over")
        else:
            print("game over.")
    else:
        print("attacked by trout. game over.")
else:
    print("fall into hole. game over.")
