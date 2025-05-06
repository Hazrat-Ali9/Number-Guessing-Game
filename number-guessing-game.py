# A number guessing Game

import random
print("Let us play a guessing game")
print("Instruction:")
print('Guess a number between 0 and 100')

try:
   user_number = int(input("Guess a number: "))
   rand_num = random.randint(0, 100)
   while rand_num != user_number:
        print(rand_num, user_number)
        if rand_num > user_number:
            print('The number is greater than your guess')
            user_number = int(input("Guess a number: "))
        elif rand_num == user_number:
            print('CONGRA')
            break
        elif rand_num < user_number:
            print('The number is less than your guess')
            user_number = int(input("Guess a number: "))
        else:
            print('Not a number')
   print('\n')
   print('***********************************')
   print('* Bingo! Congratulation, You WON! *')
   print('***********************************')
   print('\n')
except:
    print('Please, enter an integer')




    
