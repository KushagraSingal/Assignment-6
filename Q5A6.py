list = str(input('Enter words separated by hyphen: ')).split('-')
list.sort()
output = ''

for i in list:
    output = output + '-' + i

print(output[1::])
