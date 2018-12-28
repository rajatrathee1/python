Input_Data_Profile_112 = {'Name': 'Rajat', 'Email': 'xyz@gmail.com', 'Age': 28, 'Linked_Profile': 'Yes', 'Married': 'Yes', 'From': 'India', 'To': 'Ireland'}

Email = Input_Data_Profile_112.get('Email')
Login_Status = 'Success'
Name_1 = Input_Data_Profile_112.get('Name')
Welcome_Message = f'Hi {Name_1} Lets plan your Journey'

if Email == None:
    print('Please enter your e-mail to continue')
elif Login_Status == 'Success':
    print(Welcome_Message)

Age = Input_Data_Profile_112.get('Age')

if Login_Status == 'Success' and Age > 18:
    print('First select your interests')


Luggage_Suggestions_Interest = {'Common_Hand': ['Passport', 'Tickets', 'Medicines', 'Chargers', 'Books'], 'Common_Checkin': ['Clothes', 'Shoes', 'Sanitary'], 'Partying': ['Cigarettes', 'Alcohol'], 'Adventure': ['hiking gear', 'tent']}

print('based on your interest, we would like to suggest you some luggage items')

Interest = 'Adventure'
if Interest == 'Adventure':
    print(Luggage_Suggestions_Interest.get('Common_Hand'))
    print(Luggage_Suggestions_Interest.get('Common_Checkin'))
    print(Luggage_Suggestions_Interest.get('Adventure'))
elif Interest == 'Partying':
    print(Luggage_Suggestions_Interest.get('Common_Hand'))
    print(Luggage_Suggestions_Interest.get('Common_Checkin'))
    print(Luggage_Suggestions_Interest.get('Partying'))
