name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you be inviting?')
numGuests = int(input())
if numGuests:
    print('Be sure to have enough room for all your guests.')
print('Done!')