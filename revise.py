message = 'Hello World'
print(len(message))

print(message[10])
print(message[6:11])
print(message[6:])
print(message[:6])

print(message.upper())
print(message.lower())
print(message.count('Hello'))
print(message.count('l'))
print(message.find('lo'))
print(message.find("uni"))
new_message = message.replace('Hello', 'Hi')
print(new_message)
message = message.replace('World', 'Universe')
print(message)

name = 'Rajat'
greeting = 'Hi'

message = greeting + ' ' + name + ', How are you?'
print(message)

message = '{} {}, Welcome!'.format(greeting, name)
print(message)

message = f'{greeting} {name}, Welcome!'
print(message)

message = f'{greeting.lower()} {name.upper()}, Welcome!'
print(message)

print(dir(name))
print(help(str))

number = 3.14
print(type(number))

print(5 // 2)
print(3 ** 4)

print(8 % 2)
print(9 % 4)

print(3 * (4 + 8))
num = 1

num += 1
print(num)

num = 1
num *= 10
print(num)

num = 1
num -= 10
print(num)

num = 1
num /= 10
print(num)

num = 10
num %= 5
print(num)

num = 2
num -= 10
print(abs(num))
print(num)

num = 1.75
print(round(num))

num = 4.8768564
print(round(num, 3))

num_1 = 4
num_2 = 7
print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_2 > num_1)

num_1 = 3
num_2 = 1 + 2
print(num_1 >= num_2)
