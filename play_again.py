def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").strip ().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("thanks for playing!")
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            

