print("lets play guessing game,enter any number " )
print("enter any number between 1 upto 10")
import random

y=random.randint(1,10)
print(y)

x=int(input())


if x==y:
    print("yay!you guessed right")
else:
    print("sorry try again,the right answer was "+str(y))
#