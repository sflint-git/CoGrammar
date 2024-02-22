# Notes: 
# Task manager program allowing users to add, update and assign tasks



#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:                      
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

#===Functions Section===

# Fuction 1: Register a new user and add them to user.txt
def reg_user(new_username):
    while new_username in username_password.keys():
        new_username = input("Error. Username already taken. Please try again: ")
    
    new_password = input("New Password: ")
    confirm_password = input("Confirm Password: ") 
    while new_password != confirm_password:
        confirm_password = input("Error. Passwords do not match. Re-confirm password: ")
    print("New user added")
    
    username_password[new_username] = new_password
    with open("user.txt", "w") as out_file:
        user_data = []
        for k in username_password:
            user_data.append(f"{k};{username_password[k]}")
        out_file.write("\n".join(user_data))
    
    username_list.append(new_username)

# Function 2: Add a new task
def add_task(task_username):
    while task_username not in username_password.keys():
        task_username = input("User does not exist. Please enter a valid username: ")
        break
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")
 

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False,
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No",
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

# Function 3: View all tasks
def view_all(task_list):
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Task Number: \t {task_list.index(t)}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)
            
# Function 4: Vew tasks assigned to user
def view_mine(task_list):
    for t in task_list:
        if t['username'] == curr_user:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Task Number: \t {task_list.index(t)}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)

# Function 5: Calculating number of complete, incomplete & overdue tasks
num_tasks = len(task_list)

def completed_tasks(task_list):
    num_completed_tasks = sum(1 if (t['completed'] == True) else 0 for t in task_list)
    return num_completed_tasks

def incompleted_tasks(task_list):
    num_incomplete_tasks = sum(1 if (t['completed'] == False) else 0 for t in task_list)
    return num_incomplete_tasks

def overdue_tasks(task_list):
    current_date = date.today().strftime('%Y-%m-%d')
    num_overdue_tasks = sum(1 if ((t['due_date'].strftime('%Y-%m-%d') < current_date) and (t['completed'] == False)) else 0 for t in task_list)
    return num_overdue_tasks

def ppt_incomplete_tasks(incompleted_tasks):
    return float(incompleted_tasks(task_list)) / num_tasks * 100

def ppt_overdue_tasks(overdue_tasks):
    return float(overdue_tasks(task_list)) / num_tasks * 100

# Function 6: Generate and print a task overview report
def generate_task_report(task_list):
    with open("task_overview.txt", "w") as task_overview_file:
        task_overview_file.write(f'''------------------------------------------
Total number of tasks:            {num_tasks}
Number of completed tasks:        {completed_tasks(task_list)}
Number of incompleted tasks:      {incompleted_tasks(task_list)}
Number of overdue tasks:          {overdue_tasks(task_list)}
Percentage of incomplete tasks:   {ppt_incomplete_tasks(incompleted_tasks)}%
Percentage of overdue tasks:      {ppt_overdue_tasks(overdue_tasks)}%
------------------------------------------''')

# Function 7: Generates and prints a report on the users
    # Calculates the no. comp, incomp and overdue tasks by user
def generate_user_report(task_list):
    task_user_freq = {}
    task_user_completed = {}
    task_user_incomplete = {}
    task_user_overdue = {}
    proportion_of_tot_tasks = {}
    user_proportion_completed = {}
    user_proportion_incomplete = {}
    user_proportion_overdue = {}
    
    for i in username_list:
        current_date = date.today().strftime('%Y-%m-%d')
        count_user_tasks = 0
        count_user_comp = 0
        count_user_incomp = 0
        count_user_overdue = 0
        for t in task_list:
            if t['username'] == i:
                count_user_tasks += 1
                task_user_freq[i] = count_user_tasks
            else:
                count_user_tasks += 0
                task_user_freq[i] = count_user_tasks
            if (t['username'] == i) and (t['completed'] == True):
                count_user_comp += 1
                task_user_completed[i] = count_user_comp
            else:
                count_user_comp += 0
                task_user_completed[i] = count_user_comp
            if  (t['completed'] == False) and (t['username'] == i):
                count_user_incomp += 1
                task_user_incomplete[i] = count_user_incomp
            else:
                count_user_incomp += 0
                task_user_incomplete[i] = count_user_incomp
            if (t['due_date'].strftime('%Y-%m-%d') < current_date) and (t['completed'] == False) and (t['username'] == i):
                count_user_overdue += 1
                task_user_overdue[i] = count_user_overdue
            else:
                count_user_overdue += 0
                task_user_overdue[i] = count_user_overdue
    
    for i in task_user_freq:
        proportion_of_tot_tasks[i] = str(task_user_freq[i] / num_tasks * 100) + "%"
        for i in task_user_completed:
            if task_user_freq[i] == 0:
                user_proportion_completed[i] = "0.0%"
            else:
                user_proportion_completed[i] = str(task_user_completed[i] / task_user_freq[i] * 100) + "%"
        for i in task_user_incomplete:
            if task_user_freq[i] == 0:
                user_proportion_incomplete[i] = "0.0%"
            else:
                user_proportion_incomplete[i] = str(task_user_incomplete[i] / task_user_freq[i] * 100) + "%"
        for i in task_user_overdue:
            if task_user_freq[i] == 0:
                user_proportion_overdue[i] = "0.0%"
            else:    
                user_proportion_overdue[i] = str(task_user_overdue[i] / task_user_freq[i] * 100) + "%"

    # Generate User Overview report with key statistics
    with open("user_overview.txt", "w") as user_overview_file:
        user_overview_file.write(f'''---------------------------------------------
Total number of users:            {num_users}
Total number of tasks:            {num_tasks}
''')
        for i in username_list:
            user_overview_file.write(f'''---------------------------------------------
User:                             {i}
Number of tasks:                  {task_user_freq[i]}
Proportion of total tasks:        {proportion_of_tot_tasks[i]}
Proportion of tasks completed:    {user_proportion_completed[i]}
Proportion of tasks incomplete:   {user_proportion_incomplete[i]}
Proportion of tasks overdue:      {user_proportion_overdue[i]}
''')
        user_overview_file.write('''---------------------------------------------''')
            

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

# Turn the username password dictionary into a list of usernames:
username_list = []
for username in username_password.keys():
    username_list.append(username)

num_users = len(username_password.keys())

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks
gr - Generate Reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        '''Add a new user to the user.txt file'''
        new_username = input("New Username: ")
        reg_user(new_username)


    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        task_username = input("Name of person assigned to task: ")
        add_task(task_username)


    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''
        view_all(task_list)
            

    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) '''
        view_mine(task_list)
    
    # Allow user to select and edit a specific task
        task_selected = input("Select a task to edit or enter -1 to return to main menu: ")
        print(task_selected)
        if task_selected == "-1":
            print("")
        else:
            error_check = 1
            for t in task_list:
                if (task_list.index(t) == int(task_selected)) and (t['username'] == curr_user):
                    selection = input('''Please select one of the following options:
1 - Mark task as complete
2 - Update the person whom the task is assigned to
3 - Update the due date of task    
:''')
                    if selection == "1":
                        t['completed'] = True
                        print("Task updated.")
                        error_check = 0
                    elif selection == "2":
                        update_username = input("Please update the name that the task is assigned to: ")
                        if update_username not in username_password.keys():
                            update_username = input("Error. Please enter a valid username: ")
                        t['username'] = update_username
                        print("Username updated.")
                        error_check = 0
                    elif selection == "3":
                        update_due_date = input("Due date of task (YYYY-MM-DD): ")
                        new_due_date_time = datetime.strptime(update_due_date, DATETIME_STRING_FORMAT)
                        t['due_date'] = new_due_date_time
                        print("Due date updated.")
                        error_check = 0
            else:
                if error_check != 0:
                    print("Error. Invalid selection.")
        
            
            # Open and update the tasks file with the updated information
            with open("tasks.txt", "w") as task_file:
                task_list_to_write = []
                for t in task_list:
                    str_attrs = [
                        t['username'],
                        t['title'],
                        t['description'],
                        t['due_date'].strftime(DATETIME_STRING_FORMAT),
                        t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if t['completed'] else "No",
                    ]
                    task_list_to_write.append(";".join(str_attrs))
                task_file.write("\n".join(task_list_to_write))

    elif menu == 'ds':
        if curr_user == 'admin': 
            '''If the user is an admin they can display statistics about number of users
            and tasks. Statistics from the User and Tasks files.
            User and task files generated if not already available.'''
        
            generate_task_report(task_list)
            with open("task_overview.txt","r") as task_overview:
                print(task_overview.read())
                            
            generate_user_report(task_list)
            with open("user_overview.txt","r") as user_overview:
                print(user_overview.read())

        else:
            print("Error. Only Admin can display statistics.")       
    
    elif menu == 'gr':
        generate_task_report(task_list)
        generate_user_report(task_list)
        print("Reports generated.")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")