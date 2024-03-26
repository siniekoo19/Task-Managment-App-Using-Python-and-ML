import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pandas as pd
import random

try:
    tasks = pd.read_csv('tasks.csv')
    pass
except FileNotFoundError:
    pass

# Train the task priority classifier
vectorizer = CountVectorizer()
clf = MultinomialNB()
model = make_pipeline(vectorizer, clf)
model.fit(tasks['description'], tasks['priority'])

# Function to save tasks to a CSV file
def save_tasks():
    tasks.to_csv('tasks.csv', index=False)

# Function to add a task to the list
def add_task(description, priority):
    global tasks  # Declare tasks as a global variable

    new_task = pd.DataFrame({'description': [description], 'priority': [priority]})
    tasks = pd.concat([tasks, new_task], ignore_index=True)
    save_tasks()

# Function to remove a task by description
def remove_task(description):
    tasks = tasks[tasks['description'] != description]
    save_tasks()

# Function to list all tasks
def list_tasks():
    if tasks.empty:
        print("No tasks available.")
    else:
        print(tasks)

# Function to prioritizing task base for given description
def prioritizing_task():
    if len(tasks) > 6:
        description = input("Enter task description: ")
        p = model.predict([description])

        print("The priority of the given task describtion can be :: ", p[0])
        i = int(input("If you think the prediction is according Correctly prioritized your task then press 1 Otherwise press 0 : "))

        if i == 1:
            add_task(description, p[0])

        elif i == 0:
            priority = input("Enter task priority (Low/Medium/High): ").capitalize()
            add_task(description, priority)

        else:
            print("Wrong Input")
    else:
        print("\nNot enough tasks are present in your tasks-list to compare with...")

# Function to recommend a task based on machine learning
def recommend_task():
    if not tasks.empty:
        # Get high-priority tasks
        high_priority_tasks = tasks[tasks['priority'] == 'High']
        
        if not high_priority_tasks.empty:
            # Choose a random high-priority task
            random_task = random.choice(high_priority_tasks['description'])
            print(f"Recommended task: {random_task} - Priority: High")
        else:
            print("No high-priority tasks available for recommendation.")
    else:
        print("No tasks available for recommendations.")

def Task_manager():
    while True:
        print("\nTask Management App")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Recommend Task")
        print("5. Prioriting Task")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (Low/Medium/High): ").capitalize()
            add_task(description, priority)
            print("Task added successfully...")

        elif choice == "2":
            description = input("Enter task description to remove: ")
            remove_task(description)
            print("Task removed successfully.")

        elif choice == "3":
            list_tasks()

        elif choice == "4":
            recommend_task()

        elif choice == "5":
            prioritizing_task()

        elif choice == "6":
            print("THANK YOU!!")
            break

        else:
            print("Invalid option. Please select a valid option.")
 
# Storing the infomation of a user
def user_information(ussnm, pssd):  
    name = ussnm
    print("\nPlease Enter the below Infromation...")
    address = input("1. your address: ")
    age = input("2. Your age please: ")
    ussnm_ = ussnm+" task.txt"
    f = open(ussnm_, 'a')
    f.write(pssd)
    f.write("\nName: ")
    f.write(name)
    f.write('\n')
    f.write("Address :")
    f.write(address)
    f.write('\n')
    f.write("Age :")
    f.write(age)
    f.write('\n')
    f.close()
 
# Signup for a user 
def signup():
    print("SIGNUP -- Please enter the username by which you wanna access your account...")
    username = input("please enter here:  ")
    password = input("Enter a password:  ")
    user_information(username, password)
    print("Please proceed towards log in...")
    login()

# Login for a user
def login():
    print("\nLOGIN -- Please enter your Information... ")
    user_nm = input("Enter your username: ")
    pssd_wr = (input("Enter your password: "))+'\n'

    try:
        usernm = user_nm+" task.txt"
        f_ = open(usernm, 'r')
         
        # variable 'k' contains the password as saved in the file
        k = f_.readlines(0)[0]
        f_.close()
         
        # Checking if the Password entered is same as the password saved while signing in
        if pssd_wr == k:   
            Task_manager()
        else:
            print("YOUR PASSWORD OR USERNAME IS WRONG")
            login()
 
    except Exception as e:
        print(e)
        login()
        


