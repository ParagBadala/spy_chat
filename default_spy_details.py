'''

name1 = "Mr. SPY"
name2 = "Ms. SPY"
age = "19"
rating = "4.5"
spy_is_online = True



friends = [
    {
        'name': 'Rajat',
        'saultation': 'Mr.',
        'rating': 4.9,
        'age': 19,
        'chats': []
    },
    {
        'name': 'Abhijeet',
        'saultation': 'Mr.',
        'rating': 4.95,
        'age': 22,
        'chats': []
    },
    {
        'name': 'Mohit',
        'saultation': 'Mr.',
        'rating': 4.39,
        'age': 16,
        'chats': []
    }
]

'''

from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy("bond", "Mr.", 20, 3.7)
spy1=Spy("jane", "Ms.", 20, 3.7)

friend_one = Spy('Rajat', 'Mr.', 23, 4.9)
friend_two = Spy('Abhijeet', 'Mr.', 21, 4.39)
friend_three = Spy('Mohit', 'Mr.', 22, 4.95)


friends = [friend_one, friend_two, friend_three]
