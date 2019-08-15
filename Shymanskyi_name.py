z = input('enter 1 name: ')
b = input('enter 2 name: ')
print(z,b)
print('l name lang: ', len(z))
print('2 name lang: ', len(b))

if len(z)==len(b):
    print(' name have the same lang ', z, '=', b)
elif len(z)>len(b):
    print('1 name larger ', z, '>', b)
else:
    print('2 name is lager ', b, '>', z)