# get name and age from the user
name = input ('Enter your name: ')
age = int(input('Enter your age: '))

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
