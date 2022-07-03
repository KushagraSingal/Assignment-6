line = str(input('Enter string here: '))
reverse = line[::-1]

if line.lower().replace(' ', '') == reverse.lower().replace(' ', ''):
    print('Palindrome!')
else:
    print('Not a palindrome')
