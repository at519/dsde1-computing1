print('Guess a number between 1 and 10')
Guess = input()
if Guess == '7':
        print('Correct')
else:
    print('Incorrect please try again')
    Guess = input()
    if Guess == '7':
        print('Correct')
    else:
        print('Incorrect please try again')
        Guess = input()
        if Guess == '7':
            print('Correct')
        else:
            print('Incorrect you lose')
print('end')