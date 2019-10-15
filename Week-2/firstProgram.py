print('Please type your password')
Password = input()
while Password != 'chicken':
    if Password == 'chicken':
        print('Correct')
    else:
        print('incorrect')
        print('Please retype your password')
        Password = input()
print('Correct')
print('welcome user')