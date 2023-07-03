# Readme File

This repository contains a Python script that simulates a user login and task management system. The script allows users to register, login, and perform various tasks based on their user type (admin or normal user). Here's a breakdown of the functionalities provided by the script:

## Login Section
The script prompts the user to enter their username and password to log in. It reads the credentials from a file called "user.txt". If the entered username and password match an existing user in the file, the user is logged in successfully. Otherwise, an error message is displayed, and the user is prompted to enter valid credentials.

## Menu for Admin
If the user logging in is an admin, they are presented with the following menu options:
- **r**: Register a new user. The admin can enter a new username and password, and the details are appended to the "user.txt" file.
- **s**: Display statistics of the total number of tasks and users. The script reads the "tasks.txt" and "user.txt" files and prints all the tasks and users along with their details.
- **e**: Exit the program.

## Menu for Normal User
If the user logging in is not an admin, they are presented with the following menu options:
- **a**: Add a new task. The user can enter details such as the task's assigned username, title, description, start date, end date, and completion status. The details are appended to the "tasks.txt" file.
- **va**: View all tasks. The script reads the "tasks.txt" file and displays all the tasks along with their details.
- **vm**: View my tasks. The script reads the "tasks.txt" file and displays only the tasks assigned to the currently logged-in user.
- **e**: Exit the program.

## Files
- **user.txt**: This file stores the registered usernames and passwords. Each line represents a user in the format: "username, password".
- **tasks.txt**: This file stores the tasks added by users. Each line represents a task in the format: "username, title, description, start_date, end_date, is_completed".

Please note that this script is a simplified demonstration and should not be used for production purposes. It lacks error handling, security measures, and data validation. It serves as a starting point for building more robust user login and task management systems.
