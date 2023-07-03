#=====importing libraries===========
file = open("user.txt","r+") 
login = False


#====Login Section====
while login == False:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for line in file:
        valid_user, valid_password = line.strip("\n").split(", ") # need to add strip first and then split (strip used to remove "\n" new line) As we saw that when admin register then a new line is printed which will result in incorrect details
        if username == valid_user and password == valid_password:
            login = True

# If above is not true below will be false and message will be printed out then string will be looped by the while loop to enter correct username and password again.
# user_file.seek(0) is used to seek for the correct username and password as cursor moves along from left to right looking for a match
    if login == False:
        print("Incorect details! Please enter a valid username and password")
    file.seek(0)

#********* Menu for admin only *********
    if username == "admin":
        menu = input("""
        Please select one of the following options:
        r - register user
        s - display statistics of total number of task and users in txt
        e - exit
        """)
    
#********* menu "r" for admin *********
    
        if menu == "r":

            user_file = open("user.txt","a+")#I will need to append add this to user text 
        
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            confirm = input("Please confirm password: ")

            if password == confirm:
                user_file.write(f"\n{username}, {password}")
                print("Password match confirmed password")
                
            if login == False:
                print("Incorect details! confirmed password does not match password")
            user_file.close()

#********* menu "s" for admin *********
        if menu == "s":
            task_file = open("tasks.txt", "r")
            user_file = open("user.txt", "r")
            print("\nAll tasks below:")
            for line in task_file:
                task_name, title, description, start_date, end_date, is_completed = line.split(", ")

                print(f"""
                Username: {task_name}
                Title: {title}
                description = {description}
                Start date: {start_date}
                End date: {end_date}
                is_completed {is_completed}""")
            print("\nAll users below:")
            for line in user_file:
                user_name, password = line.split(", ")

                print(f"""
                Username: {user_name}
                Password: {password}
                """)
            task_file.close()
            user_file.close()

        if menu == "e":
            print("Goodbye")
            break

#********* Menu for normal user (not admin) *********

# if user is not admin then the else statment will show menu for non admin as below
else:
    menu = input("""
    Please select one of the following options:
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    """)

#********* menu "a" not admin *********
if menu == "a":
    task_file = open("tasks.txt","a+")

    task_name = input("Enter the username of the assigned task: ")
    title = input("Enter the title of the task: ")
    description = input("Enter the desription of the task: ")
    start_date = input("Enter the start date the task was assigned to user: ")
    end_date = input("Enter the end date the task was assigned to user: ")
    is_completed = input("Is the task completed: ")

    task_file.write(f"\n{task_name}, {title}, {description}, {start_date}, {end_date}, {is_completed}")
    task_file.close()

#********* menu "va" not admin *********
elif menu == "va":
    task_file = open("tasks.txt", "r")

    for line in task_file:
        task_name, title, description, start_date, end_date, is_completed = line.split(", ")

        print(f"""
        Username: {user_name}
        Title: {title}
        description = {description}
        Start date: {start_date}
        End date: {end_date}
        is_completed {is_completed}""")
    task_file.close()

#********* menu "vm" not admin *********
elif menu == "vm":
    task_file = open("tasks.txt", "r")

    for line in task_file:
        task_name, title, description, start_date, end_date, is_completed = line.split(", ")

        if username == task_name:
            
            print(f"""
            Username: {username}
            Title: {title}
            description = {description}
            Start date: {start_date}
            End date: {end_date}
            is_completed {is_completed}""")
    task_file.close()

if menu == "e":
    print("Goodbye")
