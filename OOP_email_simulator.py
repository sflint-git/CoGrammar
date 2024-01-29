### --- OOP Email Simulator --- ###

# --- Email Class --- #
class Email:

    has_been_read = False
    is_spam = False

    # Initialises the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    
    # Method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True
    
    # Method to mark email as spam:
    def mark_as_spam(self):
        self.is_spam = True
        print(f"\nEmail '{self.subject_line}' has been marked as spam.")


# --- Inbox List & Email Objects --- #
# Empty list to store the email objects.
inbox = []

# 3 sample emails to add to the Inbox list at launch. 
email_1 = Email("matt@yahoo.com", "Learn Python", "Guide on how to learn python")
email_2 = Email("claire@yahoo.com", "Learn Java", "Guide on how to learn java")
email_3 = Email("james@yahoo.com", "Learn C++", "Guide on how to learn C++")

# --- Functions --- #

# Function to populate inbox list 
def populate_inbox(email):
    inbox.append(email)

# Function that prints the email’s subject_line, along with a corresponding number.
def list_emails():
    email_subject_list = []
    for email in inbox:
        email_subject_list.append(email.subject_line)

    for count, ele in enumerate(email_subject_list):
        print(count, ele)

# Function which displays a selected email and sets the 'has_been_read' variable to True
def read_email(email_selected):
    inbox[email_selected].mark_as_read() 
    print(f'''---------------------------------------------------------
Email subject: {inbox[email_selected].subject_line}
Email contents:\n{inbox[email_selected].email_content}\n
Email from {inbox[email_selected].email_address} has been marked as read.
---------------------------------------------------------''')

# Function which deletes email from inbox:
def delete_email(email):
    print(f"Email '{inbox[email].subject_line}' deleted.")
    del inbox[email]

# --- Email Program --- #

# Populate the Inbox with three sample emails.
populate_inbox(email_1)
populate_inbox(email_2)
populate_inbox(email_3)

# Email Menu
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
1. Read an email
2. View unread emails
3. Quit application

Enter selection: '''))
      
    if user_choice == 1:
        # list emails and display email selected by user
        print()
        list_emails()
        
        email_selected = int(input('\nPlease select an email to read: '))
        while email_selected >= len(inbox):
            email_selected = int(input("Invalid selection. Please try again: "))
        
        read_email(email_selected)

        # Allow user to mark email as spam or delete email
        email_options = int(input('''\nWould you like to: 
1. Mark email as spam
2. Delete email
3. Return to main menu
                                  
Enter selection: '''))
                
        if email_options == 1:
            inbox[email_selected].mark_as_spam()
        
        elif email_options == 2:
            delete_email(email_selected)

        else:
            print()        

    elif user_choice == 2:
        # view unread emails
        print()
        counter = 0
        for email in inbox:
            if email.has_been_read == False:
                print(f'''{counter} {email.subject_line}''')
                counter += 1 
                  
    
    elif user_choice == 3:
        # quit appplication
        print("Goodbye!")
        exit()

    else:
        print("Incorrect input. Please try again.")        