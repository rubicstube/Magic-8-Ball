import use_input 
import random_response
import play_again

def magic_8_ball():
    print("welcome to the gamr")
    while True:
        user_input = use_input.get_user_guess()
        if user_input is None:
            break
        response=random_response.get_random_response()
        random_response.display_response(response)
        if not play_again.play_again():
            break

if __name__=="__main__":
    magic_8_ball()



