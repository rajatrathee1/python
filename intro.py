message = 'Hello World'
# print the total length of a string
print(len(message))

# slicing
#[02] is wrong method to define
print(message[10])
print(message[6:11])
# when we write [6:11] 11th index will not be included, but the 10th index will be included
print(message[6:])

# functions to convert to lower and upper
print(message.upper())
print(message.lower())

# print the number of times an argument occurs in a string
print(message.count('Hello'))
print(message.count('l'))

# print the index number of particular sub-string
print(message.find('World'))
print(message.find('l'))
print(message.find('Universe'))

# to replace a sub-string in a string

# to set the value in a new string
new_message = message.replace('World', 'Universe')
print(new_message)

# to set the value in the same string
message = message.replace('World', 'Universe')
print(message)

# to concatinate two strings
greeting = 'Hello'
name = 'Rajat'

message = greeting + ', ' + name
print(message)

message = greeting + ', ' + name + '. How are you? '
print(message)

# better method using placeholder -- {} is called placeholder

message = '{}, {}.Welcome!'.format(greeting, name)
print(message)

# new method for python 3.6 and above

message = f'{greeting}, {name}, Welcome!'
print(message)

# advantage of last method is to be able to do coding(use functions) within the placeholder
message = f'{greeting.lower()}, {name.upper()}, let us find the best software for your profession!'
print(message)

# to generate a directory of all the functions available for a string

print(dir(name))

# to find out detailed info about every function related to a string or any data type
print(help(str))

# ____ """WORKING with numeric data- integers and floats"""_____
number = 3.14
print(type(number))

print(1 + 3)
print(3 - 1)
print(1 * 4)

print(3 / 2)
# for command above python 2, answer will be 1. for python 3, answer will be 1.5

# floor division- print 2 if answer is 2.5
print(5 // 2)

# exponent - 1st number base, 2nd number power
print(3 ** 4)

# mode - prints the remainder
print(8 % 2)
print(9 % 2)

# changing the order of operations
# 1 original output
print(3 * 2 + 4)

# 2 change order
print(3 * (2 + 4))


# incrementing a number (increasing value by 1)
# normal non-efficient way
num = 1
num = num + 1
print(num)

# python more efficient way

num = 1
num += 1
print(num)

# can also combine other operators with =
num = 1
num *= 10
print(num)

num = 1
num -= 10
print(num)

num = 9
num %= 2
print(num)

# abs function to print absolute value/ remove negative sign

num = 2
num -= 10
print(num)
print(abs(num))

# to round a value

num = 1.75
print(round(num))

# to round to specified number of digits after decimal, write the number of digits you want to round it off to after comma

num = 4.57245
print(round(num, 3))

# ____comparisons (output is in boolean ( T or F))

# equal to, compares the two numbers to check if they are equal or not

num_1 = 4
num_2 = 7

print(num_1 == num_2)

# not equal to, checks if the numbers are not equal, if not equal then output is true otherwise false
print(num_1 != num_2)

# greater than, checks if the left number is greater than number on the right
print(num_1 > num_2)

# less than, checks if the left number is less than the one on the right
print(num_1 < num_2)

# greater than/less than equal to - they print true if the left number is not greater/less but still equal to the right one
num_1 = 3
num_2 = 1 + 2
print(num_1 >= num_2)

# _______to caste numeric data in string form to integer form and carry out operations
num_1 = '100'
num_2 = '200'

# the undesired result
print(num_1 + num_2)

# the desired result
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)


# ___"""Lists, Tuples, and Sets"""___

# list
courses = ['History', 'Math', 'Physics', 'CompSci']
# length of list/number of members
print(len(courses))

# to access each member of a list, if total number of elements are 4 then we use index[0] for first value and index[3] for last member.
print(courses[0])
print(courses[3])

# using negative index, it is easier to access items at the end of long lists, last item index is always [-1], the one above [-2] so on.
print(courses[-1])
print(courses[-2])
print(courses[-3])

# to access a range, first number is inclusive, second isnt
# to access first two values, the command is going to be
print(courses[0:2])

# if we dont provide the first number, it assumes it to be 1st idex i.e [0]
print(courses[0:2])

# similarly for the second number, leave it blank and it will assume it to be last
print(courses[2:])

# to add another entry into the end of the list.
courses.append('art')
print(courses)

# to add another entry at a specific location
courses.insert(0, 'PhysicalEdu')
print(courses)

# to add another list at any position
courses_2 = ['python', 'database']
courses.insert(0, courses_2)
print(courses)
print(courses[0])

# to add another list at last position
courses_2 = ['python', 'database']
courses.append(courses_2)
print(courses)

# the setback of the above method is that the first value(insert)/last value(append) of the courses list is now all the values of courses_2. to check
print(courses[0])

# therefore we use the 'extend' method to remove this problem
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['python', 'database']
courses.extend(courses_2)
print(courses[5])

# dont mix extend with append as append is going to only add the second string at the end in a single value like insert does at the begginning

# REMOVING ITEMS FROM A LIST

# using remove method
courses.remove('Math')
print(courses)

# using pop method will automatically remove the last value
courses.pop()
print(courses)

# you can print the popped value
popped = courses.pop()
print(popped)
print(courses)

# SORTING YOUR LISTS
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.reverse()
print(courses)

# to sort the list in alphabetical order
courses.sort()
print(courses)

# to sort numbers in ascending order
nums = [5, 4, 6, 3, 2, 7, 9, 1]
nums.sort()
print(nums)

# to sort in descending order use reverse=True
courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [5, 4, 6, 3, 2, 7, 9, 1]
courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)

# to create a different sorted version of an existeing list without altering the original one we use sorted function which does not alter the original list but creates a sorted version
courses = ['History', 'Math', 'Physics', 'CompSci']
sorted(courses)
print(courses)

# we got the original list in above statement as above statement does not sort the original list. We have to create a seperate version to get the sorted version
sorted_courses = sorted(courses)
print(sorted_courses)

# to get minimum, maximum values and sum
nums = [5, 4, 6, 3, 2, 7, 9, 1]
print(min(nums))
print(max(nums))
print(sum(nums))

# to find the index of value
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses.index('Math'))

# when we find the index of a value that does not exist
# print(courses.index('Art'))

# to find wether a value is in the list or not
courses_1 = ['History', 'Math', 'Physics', 'CompSci']
print('Art' in courses_1)
print('History' in courses_1)

# looping in python
courses = ['History', 'Math', 'Physics', 'CompSci']
for course in courses:
    print(course)

# to print the index value along with the looping, we use enumerate function, uncomment the below code, run, then comment again to run the next code successfully
# for index, course in enumerate(courses):
    # print(index, course)

# to start with value = 1
courses = ['History', 'Math', 'Physics', 'CompSci']
for index, course in enumerate(courses, start=1):
    print(index, course)

# __To turn a list into string__
courses_str = '- '.join(courses)
print(courses_str)
print(type(courses_str))
print(len(courses_str))
print(courses_str.upper())

# SPLIT GIVES VALUE ON BOTH SIDES OF THE SPLITTING FACTOR AS A LIST

new_list = courses_str.split(' - ')
print(new_list)
print(courses_str)

# __TUPLES are immutable(non-modifiable) lists

# Issue with mutable(modifiable) objects, when two immutable objects are equal, then the change we make in one object is changed in other object as well
list_1 = ['actor', 'animator', 'architect', 'athlete', 'biologist', 'biotechnologist', 'chemist']
list_2 = list_1
print(list_1)
print(list_2)
# making changes in the first index with the below command leads to changes in the first index of the second list as well
list_1[0] = 'Civil Engineer'
print(list_1[0])
print(list_2[0])

# Using tuple to get rid of the above problem
# tuple looks exactly like the list but we use () instead of []
tuple_1 = ('actor', 'animator', 'athlete', 'biologist', 'biotechnologist', 'chemist')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
# below code wont be executed as tuple are immutable
# tuple_1[0] = 'Cricketer'

# a possible use of tuple
list_1 = ['actor', 'animator', 'architect', 'athlete', 'biologist', 'biotechnologist', 'chemist']
tuple_2 = tuple(list_1)
print(list_1)
print(tuple_2)

list_1[0] = 'footballer'

print(list_1[0])
print(tuple_2[0])
# only the first item of list_1 was changed and not of tuple_2

# __SETS- Sets are values that are unordered and also, have no duplicates. They look like lists, but use {} instead of []

set_1 = {'actor', 'animator', 'psychologist', 'biologist'}
# the print command below will produce the set values in random order
print(set_1)

# sets are basically the most efficient way to check wether a value is a part of a set and second is to remove duplicates. It removes duplicates automatically. In example below we will add actor twice and print the set.
set_1 = {'actor', 'animator', 'psychologist', 'biologist', 'actor'}

# to check wether it is a member. IT IS THE MOST EFFICIENT WAY!
print('actor' in set_1)

# sets are also used to find wether one object is in both the sets, we use intersection
cs_courses = {'maths', 'java', 'dbms', 'english'}
arts_courses = {'maths', 'politics', 'history', 'english'}
print(cs_courses.intersection(arts_courses))

# to find courses in cs_courses which are not there in arts_courses, we use difference
print(cs_courses.difference(arts_courses))

# to print all the members present in both the sets, we use union
print(cs_courses.union(arts_courses))

# to create empty list we have two ways
empty_list = []
empty_list = list()

# to create empty tuple we have two ways
empty_tuple = ()
empty_tuple = tuple()

#_but to create empty set we have only one way, we cant use empty_tuple = {} as it will create an empty dictionary not set.
# therefore the only way to create an empty set is create built in set class with no values ie:
empty_set = set()


# Dictionaries are used to create key value pairs- in dictionaries, the word is the key and its defination is the value.
Professional = {'Name': 'rajat', 'Profession': 'Business Analyst', 'Age': 25, 'Tools': ['Microsoft Power Bi', 'Apache Hive', 'SAP Hana', 'Talend', 'Qlik View', 'Podium Data'], 'gender': 'Male'}
print(Professional['Profession'])
print(Professional['Age'])
print(Professional['Tools'])

# using get method which reduces number of errors(more efficient) since it does not give error if value is not found
print(Professional.get('Name'))
print(Professional.get('Phone'))
print(Professional.get('Age'))

# to add a default specific message when a key is not found
print(Professional.get('Phone', 'Specified detail could not be found'))

# to add a missing value
Professional['Phone'] = 99999999
print(Professional.get('Phone', 'Specified detail could not be found'))

# To update a single value
Professional.update({'Name': 'Rathee'})
print(Professional.get('Name'))

# To delete a single value
del Professional['Age']
print(Professional)

# using pop method. We can also see the value we have popped off
gender = Professional.pop('gender')
print(Professional)
print(gender)

# length of a dictionary
print(len(Professional))

# to print all the keys in a dictionary
print(Professional.values())

# to print all the pairs in a dictionary
print(Professional.items())

# looping through dictionaries, 1 printing all the keys
for key in Professional:
    print(key)

# to print all the pairs in a dictionary
for key, value in Professional.items():
    print(key, value)


#____***Conditionals and Booleans - If, Else, and Else if Statements***___
if True:
    print('Let me find the best softwares for you')

if False:
    print('Conditionals was true')

# For comparisons we will use
# Equals ==
# Not Equals !=
# Greater than >
# Less than <
# Greater than Equal to    >=
# Less than Equal to       <=
# Object Identity          is

# using conditionals for variables
free_demo = 'available'
link_message_text = 'you can download the free demo from'
link = 'www.firezilla.com/freedemo'
link_message = f'{link_message_text} {link}'

if free_demo == 'available':
    print(link_message)

# not equal !=
free_tutorial = 'not available'
if free_tutorial != 'available':
    print('Sorry the free tutorial is not available')

# Using else and Greater than
i = 3
if i > 3:
    print('i is greater than  3')
else:
    print('not greater')

# similarly for <,>=, <=

# difference between equals (==) and Object Identity (is)
# equals just stands for equal value wether the two objects are different in memory while Object Identity checks if it has
# the same location in the memory or basically have the same id
# exam
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
# printing the memory locations of both using id function to prove that both are different objects
print(id(a))
print(id(b))

# to make the id of both the objects same
a = [1, 2, 3]
a = b
# now both will have same id
print(id(a))
print(id(b))
# now both equals and object identity will be true
print(a == b)
print(a is b)
print
# so basically identity is can be defined as
print(id(a) == id(b))


# elif (similar to else-if in Java)

language = 'Java'

if language == 'Python':
    print('Congratulations! You are eligible for the Project')
elif language == 'Java':
    print('Congratulations! You are elgible for the Project')
else:
    print('Sorry! You are inelegible')

# There are no Switch case in Python as elif statement has the same purpose


# Boolean Operations
# and
# or
# not

user = 'Admin'
logged_in = False
username = 'Rathee'

# and : both condtions should be true
if user == 'Admin' and logged_in:
    print('Welcome Leo')
else:
    print('Bad Credentials')

# or : either one of the conditions can be true
if user == 'Admin' or logged_in:
    print('Welcome Leo')
else:
    print('Bad Credentials')

# not is just used to switch a boolean. It will turn True to False and vice-versa
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')


# the values that are false by-default. All values except these are True by default
# False
# None
# Zero Of any numeric type
# Any empty sequence, for example '', (),[],
# Any empty mapping, for example, {}.

# It can be combined with if condition to test wether any string is empty

condition = False

if condition:
    print('condition evaluated to be true')
else:
    print('condition evaluated to be false')


condition = None

if condition:
    print('condition evaluated to be true')
else:
    print('condition evaluated to be false')


condition = 0

if condition:
    print('condition evaluated to be true')
else:
    print('condition evaluated to be false')

condition = 10

if condition:
    print('condition evaluated to be true')
else:
    print('condition evaluated to be false')


condition = []

if condition:
    print('condition evaluated to be true')
else:
    print('condition evaluated to be false')

condition = {}

if condition:
    print('condition evaluated to be true')
else:
    print('condition evaluated to be false')


# **** LOOPS AND INTERATIONS - FOR/WHILE LOOP

nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

# break keyword will break completely out of a loop and the continue keyword moves onto the next iteration of the keyword

# using break to find a particular value
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

# if we use continue, the loop will execute the condition provided for that iteration and continue from the next iteration
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('found!')
        continue
    print(num)


# loop inside loop
# in the below code it will loop through every letter of abc with first number then it will loop through every letter with the net number and go on

# for loop iterates through a certain number of values
nums = [1, 2, 3, 4, 5]

for num in nums:
    for letter in 'abc':
        print(num, letter)

# to loop for a fixed number of times we have range not including the last value
for i in range(10):
    print(i)

# if we want to start from a particular values, i.e. 1 and go on including 10
for i in range(1, 11):
    print(i)

# while loop continues until a condition is true
print ('while loop')
x = 0
while x < 10:
    print(x)
    x += 1

# break
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# creating an infinite loop using while loop to executr comment out line 663 (if x == 5) and line 664(break) and run,
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1
# use control c to stop this infinite loop[mac]


# _____FUNCTIONS_____

def hello_function():
    pass


hello_function()

# using print without parenthesis() command for execution wont work as it will print the details like memory location of the function
print(hello_function)
print(hello_function())


# benefit of using function- It allows us to put a code with specific purpose at a single place. So any changes wont have to be done manually at different places. It helps us to keep the code 'DRY(Dont Repeat Yourself)'
def hello_func():
    print('Hello User')


# return command does not print the value but it stores the value in a string by the name of the function

def Greeting():
    return('Hi')


Greeting()

# the above command wont print anything but the value has been assigned using return. Therefore, when we print the function as shown below we will get the desired result.
print(Greeting())

print(len(Greeting()))

print(Greeting().upper())

# Adding parameters to function 1. We define the parameter in between () in the function name defination 2. We use {} to define the position and .format(parameter name) in the function body. 3. We define the value of the parameter in between ()when we run the function


def Travel_Greeting(username):
    return 'Hello {}, Ready for your journey?'.format(username)


print(Travel_Greeting('Rajat'))

# the scope of the parameter is only local to the function
# the username in above argument is called as required argument. It does not have a default value when we pass it. The default argument value can be defined when we declare the function name and argument names

# in the below function we will be passing multiple arguments in the function with one argument having default value. Since we will not provide any value while running the function it took the default value


def profession_greeting(greeting, name='there'):
    return '{} {}! Lets find the best Softwares for you'.format(greeting, name)


print(profession_greeting('Hi'))

# when we provide a value for a default parameter when running it. It will override the original value and run the function with the provided value as can be seen below.


def goodbye(name='dear'):
    return 'Goodbye {}'.format(name)


print(goodbye('Rajat'))


# * allowing us to accept an aribitrary number of positional or keyword arguments. It is useful when data is extraceted and we dont know the exact number of values the arguments will have. By convention, *args will be used for positional arguments(tuples). **kwargs for keyword arguments(dictionaries)

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='Rajat', age=24)
# args has been printed as a tuple where all the kwargs will be printed as a dictionary

# We may sometimes see arguments in a function being called with * or **. Why so? When it is used in that context. It will actually unpack a sequence or a dictionary and pass those values individually. For example first lets try without using * and **.


def profession_info(*args, **kwargs):
    print(args)
    print(kwargs)


skills = ('Graphic Designing', 'Website creation')
info = {'name': 'Himanshu', 'email': 'xyz@gmail.com'}

profession_info(skills, info)  # not using * and **

# now when we called the function without using * and ** in front of arguments then the output is not the desired output as it has both of the argument as a single positional argument(tuple) instead of one positional argument and one keyword argument. To solve this problem we will use * and ** in front of the arguments when calling the above function as shown below

profession_info(*skills, **info)  # using * and ** and getting the desired output

# finding if an year is a leap year
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(2017))

print(days_in_month(2017, 2))

#### for import module check files my_module.py and test-module.py in this directory

