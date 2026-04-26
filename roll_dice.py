import random
print("Welcome to the game of rolling a dice")

while True:
    choice = input("Press enter to roll the dice Or 'Q' to quit")
    if choice == 'Q':
        print("Thanks for playing the game , bye!!")
        break
    elif choice == '':
        num = random.randint(1,6)
        print(f"Your number is {num}")
    else:
        print("The input is INVALID!!!")

print("GAME OVER")

