import random

secretnum=random.randint(1,10)
count = 1

while(True):
    guess=int(input("guess the number (1-10) >> "))
    if guess == secretnum:
        print("you guessed right number congralution")
        break
    else:
        print("you typed wrong number, please try again!")
        count += 1

print(f"you tryed these time {count} ")