import random

def GussingNumber():
    number = random.randint(1,10)
    print(number)
    return number

random_number = GussingNumber()


count = 1
while(count<=5):
    exp_number = int(input())
    if random_number == exp_number:
        print('congratulations')
        break
    else:
        print('incorrect expected number \nplease try again')

        count+=1

