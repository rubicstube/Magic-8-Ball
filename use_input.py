guess=int(input("enter a number : 1-100:  "))
def get_user_guess():
    while True:
        try:
            guess=int(input("enter a number : 1-100"))
            if guess >=1 and guess <= 100:
                return guess 
            else:
                print("number should be between 1-100")
        except ValueError:
            print("invalid input , please enter a number")

