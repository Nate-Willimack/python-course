import random

def num():
    print("can you guess what number I am thinking of?")

    num = random.randint(1,100)

    guesses = 0
    while True:
            guess = int(input("guess the number!:"))
            guesses +=1
            
            if guess < num:
                    print("too low!")
            elif guess > num:
                    print("too high!")
            else:
                    print(f"congratulations! you have guess the number in {guesses}!")
                    break
num()
    


