name = "Haroun"

print('My name is {}'.format(name))

print('1 {} 3 {} 5'.format('2', '4'))

print('1 {} 3 {} 5'.format('4', '2'))
print('1 {1} 3 {0} 5'.format('4', '2'))

print('1 {b} 3 {a} 5'.format(a='4', b='2'))

num = 1.2345678
print("The num is {n:1.4f}".format(n=num))
