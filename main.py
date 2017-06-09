from default_spy_details import *
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored

# list of old status
STATUS_MESSAGES = ["Sleeping", "Hii I am using Spy chat", "At the gym"]

#list of special words
special_words = ["SOS", "SAVE ME", "ASAP", "LOL", "LMAO", "ROFL"]

# adding status
def add_status(current_status_message):

    updated_status_message = None


    if current_status_message != None:
        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'


    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("Enter new status message ")


        if len(new_status_message) > 0:
            # appending the new status in the old status list
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        status_no = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (status_no, message)
            status_no = status_no + 1

        status_selection = int(raw_input("\nChoose from the above messages "))


        if len(STATUS_MESSAGES) >= status_selection:
            updated_status_message = STATUS_MESSAGES[status_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if  updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message


# adding a friend
def add_friend():

    new_friend = Spy("","",0,0.0)
    #taking friends details
    new_friend.name = raw_input("Add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age? ")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    #checking the validation for adding friends
    if len(new_friend.name) > 0 and new_friend.age > 18 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    # returning the number of friends a Spy have
    return len(friends)



# selecting a friend

def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose the friends for chatting ")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

# sending a message
def send_message():
    # selection of friend
    friend_choice = select_a_friend()

    # taking the message from the spy
    text = raw_input("Enter the secret message containing less than 30 words : \n ")

    avg = text.split()

    # checking that a spy can send 10 words at a time
    if len(avg) > 30:
        print "Sorry you can send 30 words at a time . Reframe the message again !!!"

    else:

        # selected the image
        original_image = raw_input("Enter the name of the image : ")

        # name of output image after message have encoded
        #output_path = "output.jpg"
        output_path = raw_input("Enter the name of Output image")
        # encoding the message into the image
        Steganography.encode(original_image, output_path, text)

        # adding the time to the message send
        new_chat = ChatMessage(text, True)

        # saving the older chat in the specific friend name
        friends[friend_choice].chats.append(new_chat)

        print "Your secret message image is ready to be delivered!"


# secret message to be read
def read_message():

    sender = select_a_friend()

    # input the output file
    output_path = raw_input("What is the name of the file?")

    # extracting the secret message
    secret_text = Steganography.decode(output_path)

    # checking if image conatain message or not
    if len(secret_text)==0:
        print "Empty Message"

    else:
        # printing secret message
        print (secret_text)

        # handling special words
        for item in special_words:
            if item in secret_text:
                z='Message contain special word : %s' %(item)
                #print ('Message contain special word : %s' %(item))
                print colored(z,"red")
        # adding the time to message received
        new_chat = ChatMessage(secret_text, False)

        # saving the chat by the reciever by whom he received the chat
        friends[sender].chats.append(new_chat)

        print "Your secret message has been saved!"


def read_chat_history():
    # select the friend whose chat history to be read
    read_for = select_a_friend()

    for chat in friends[read_for].chats:
        # checking if the message is send by me or by my friend
        if chat.sent_by_me:

            a = '[%s]' % (chat.time.strftime("%d %B %Y"))
            b = 'You said: '
            c = '%s' % (chat.message)
            print colored(a, 'red'), colored(b,'blue'), colored(c,'green')
        else:
            a = '[%s]' %(chat.time.strftime("%d %B %Y"))
            b = '%s said : ' %(friends[read_for].name)
            c = '%s' %(chat.message)
            print colored(a,'red'), colored(b,'blue'), colored(c,'green')


#showing the menu options
def start_chat():
    current_status_message = None

    show_menu = True

    while show_menu:
        menu_choices = "Enter The choice? \n 1. Add a status update \n 2. Add a friend \n 3. See Friend's List \n 4. Send a secret message \n 5. Read a secret message \n 6. Read Chats from a user \n 7. Close Application \n"
        #enter the choice
        menu_choice = raw_input(menu_choices)

        if len(menu_choice) > 0:
            menu_choice = int(menu_choice)

            # checking which action to be performed
            if menu_choice == 1:
                current_status_message = add_status(current_status_message)
            elif menu_choice == 2:
                number_of_friends = add_friend()
                print 'You have %d friends' % (number_of_friends)
            elif menu_choice == 3:
                index = select_a_friend()
                print index
            elif menu_choice == 4:
                send_message()
            elif menu_choice == 5:
                read_message()
            elif menu_choice == 6:
                read_chat_history()
            else:
                show_menu = False



#------------------------------------------starting of spy chat-------------------------------------------------------#
#                                                                                                                     #
#                                     Welcome to the world of Hackers                                                 #
#                                                                                                                     #
#---------------------------------------------------------------------------------------------------------------------#


#Enter the spy chat room
print "Hello Spy"
print "Welcome in spy chat room"

spy = Spy('Parag','Mr. ',19,4.0)
spy1 = Spy('Jane','Ms. ',19,4.0)
spy2 = Spy('','',0,0.0)

#asking to be a default user or create his own user
user_cat = raw_input("Do yo want to be a default user or custom user : ")

if user_cat.upper() == "DEFAULT":
    # print the info of default spy
    user_sal = raw_input("Should i call you Mr or Ms : ")  #asking spy about its gender

    if user_sal.upper() == "MR":
        print  " Name : " + spy.salutation + spy.name + "\n" + "Age : "+ str(spy.age) + "\n" + "Rating : " + str(spy.rating)
    else:
        print  " Name : " + spy1.salutation + spy1.name + "\n" + "Age : "+ str(spy1.age) + "\n" + "Rating : " + str(spy1.rating)

    # calling the start_chat fun to start the chat
    start_chat()

else:
    # creating the custom user
    i = 1
    while i :
        spy2.name = raw_input("Can you tell me your spy name first: ")
        #checking if spy has entered valid name
        if len(spy2.name) > 4:
            print "Welcome " + spy2.name
            i = 0
        else:
            print "Spy_name should be greater than 4. Enter new spy name "

    spy2.salutation = raw_input("Should I call you Mr or Ms : ")

    #printing spy_name with the salutation
    spy2.name = spy2.salutation.capitalize() + " " + spy2.name.capitalize()

    print "Alright " + spy2.name + ". Update you profile before we proceed..."

    # creating variable for age, rating, is_online
#    spy_age = 0
#    spy_rating = 0.0
    spy2.is_online = False

    # asking spy age and converting to integer
    spy2.age = int(raw_input("What is your age : "))

    '''checking age validation i.e spy should be greater than 18 and less than 50 years of age if it satisfy then asking
        his rating . This is multi line comment '''

    if spy2.age > 18 and spy.age < 50:
        # asking for spy_rating and conerting to float
        spy2.rating = raw_input("What is your spy rating : ")

        spy2.rating = float(spy.rating)

        # checking in which category spy falls
        if spy2.rating > 4.5:
            print "You are top spy"
        elif spy2.rating > 3.5 and spy2.rating <= 4.5:
            print "You are one of the good spy."
        elif spy2.rating >= 2.5 and spy2.rating <= 3.5:
            print "You can do better"
        else:
            print "Need to improve Please!!!."

        # making spy come online
        spy2.is_online = True

        # Printing all the details of the spy final time
        print "Profile Updated . Welcome  %s,  age: %d and rating of: %.1f . Now you can START" %(spy.name, spy.age, spy.rating)

        # calling the start_chat fun to start the chat
        start_chat()
    else:
        print 'Sorry you are not of the correct age to be a spy'


