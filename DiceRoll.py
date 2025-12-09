import random



def main():
    print("\nWelcome to DiceRoll!\n")
    while True:
        choice = input("Roll Dice? (y/n): ").lower()

        if choice == "y":
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f"\nyou rolled a {die1} and a {die2}\n")

        elif choice == 'n':
            print('Thanks for Playing!')
            break

        else:
            print('wrong input...')

main()