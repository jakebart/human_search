import random
def main():
    cpu_num_choice = random.randint(1,100)
    print("Guess a number 1-100:")
    correct = True
    while(correct):
        user_input = int(input(""))
        if user_input > cpu_num_choice:
            print("Incorrect number, guess a smaller number:")
            user_input
        elif user_input < cpu_num_choice:
            print("Incorrect number, guess a larger number:")
            user_input
        else:
            print("Cangrats you guessed ", user_input, "and cpu guessed ", cpu_num_choice)
            correct = False
main()
