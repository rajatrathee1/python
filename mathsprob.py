greeting = 'Hello '
name = 'Rajat'

greeting = f'{greeting} {name}, let us find the best softwares, applications and websites for your profession'
print(greeting)

professions = ['actor', 'animator', 'architect', 'athlete', 'biologist', 'biotechnologist', 'chemist', ]


for profession in professions:
    print(profession.upper())
professions = ['actor', 'animator', 'architect', 'athlete', 'biologist', 'biotechnologist', 'chemist', ]
professions_2 = ['graphic designer', 'Software Engineer', 'Data Analyst', 'Doctor', 'Real Estate Dealer', 'Business Analyst', 'Network Security Manager']
professions_2.sort()
print(professions_2)
professions.extend(professions_2)
print(professions)

Professional = {'Name': 'rajat', 'Profession': 'Business Analyst', 'Age': 25, 'Tools': ['Microsoft Power Bi', 'Apache Hive', 'SAP Hana', 'Talend', 'Qlik View', 'Podium Data'], 'gender': 'Male'}
print(Professional['Profession'])
print(Professional['Age'])
print(Professional['Tools'])

if True:
    print('Here is the list of best suited softwares for your profession')


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


####

Prof_limit = 3
x = len(professions)

if x > Prof_limit:
    print('You have too many professions. Are you even human?')
else:
    print('The best Softwares for your profession are :')


###
