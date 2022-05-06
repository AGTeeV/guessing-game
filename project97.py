import random
print('NUMBER GUESSING GAME')

print('GUESS A NUMBER BETWEEN 1 AND 9')

number=random.randint(1,9)

chances=0

while chances<5:
    guess=int(input('ENTER YOUR GUESS =>'))
    if guess==number:
        print("CONGRATULATIONS YOU WON")
        break
    elif guess<number:
        print('YOUR GUESS WAS TOO LOW')
    else :
        print('YOUR GUESS WAS TOO HIGH')
    chances+=1

if not chances<5:
    print('YOU LOSE! THE NUMBER IS ', number)