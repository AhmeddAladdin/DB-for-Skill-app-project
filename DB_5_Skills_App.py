"""
=============================================
----> DB -> SQLite -> Create skills app <----
=============================================
"""

# Input message
Input_Message = """
What do you want to do?
's' => Show all data.
'a' => Add new skill.
'd' => Delete a skill.
'u' => update skill progress.
'q' => Quit App.
Choose a letter: """

# input option choose
user_input = input(Input_Message).strip().lower()

# User ID
uid = input("Enter your ID: ")

# space
print("=" *50)

# Import SQLite module
import sqlite3

# Connect to database
db = sqlite3.connect("DB_SA.db")

# setting up cursor
crsr = db.cursor()

# Create tables and columns
crsr.execute(
    "CREATE TABLE if not exists users (name TEXT, user_id INTEGER)"
)
crsr.execute(
    "CREATE TABLE if not exists skills (name TEXT, progress INTEGER, user_id INTEGER)"
)

# Inserting data
lst1 = [
'Ahmed', 'Ali', 'Khaled', 'Mahmoud', 'Manar', 'Mona', 'Amira', 'Omar', 'Khloud', 'Yousef'
]

# for key, user in enumerate(lst1, 100701):
    
#    crsr.execute(f"insert into users(name, user_id) values('{user}', {key})")

def Save_ans_Close():
    """Commit and close the connection with DB""" 
    db.commit()  # Save changes
    crsr.close()  #close DB
    print("Connection to Database is closed")

# Define methods
def Show_all_data():
    """Show all data for the assigned ID"""
    crsr.execute(f"select * from skills where user_id = {uid}")
    data = crsr.fetchall()

    for key, user in enumerate(data, 1):
        print(f"{key}- name => {user[0]},", end=" ")
        print(f"progress => {user[1]}%,", end=" ")
        print(f"user_id => {user[2]}")

    Save_ans_Close()

def Add_new_skill():
    """Adding a new skill for the assigned ID"""
    sk = input("Enter skill name: ").strip().capitalize()
    prog = float(input("Enter your progress: ").strip())

    crsr.execute(f"insert into skills(name, progress, user_id) values('{sk}', {prog}, {uid})")

    print("Added successfully!")

    Save_ans_Close()

def Delete_a_skill():
    """Delete the assigned skill"""
    sk = input("Enter skill name: ").strip().capitalize()

    crsr.execute(f"delete from skills where name = '{sk}' and user_id = {uid}")

    print("Deleted successfully!")

    Save_ans_Close()

def Update_skill():
    """Update progress for the assigned skill"""
    sk = input("Enter skill name: ").strip().capitalize()
    prog = float(input("Enter your progress: ").strip())

#    crsr.execute(f"update skills set name = '{sk}' where user_id = {uid}")

    crsr.execute(f"update skills set progress = {prog} where name = '{sk}'")

    print("Updated successfully!")

    Save_ans_Close()

# check if choise is exists
command_lst = ['s', 'a', 'd', 'u', 'q']
if user_input in command_lst:
    
    if user_input == 's':
        Show_all_data()
    
    elif user_input == 'a':
        Add_new_skill()

    elif user_input == 'd':
        Delete_a_skill()

    elif user_input == 'u':
        Update_skill()

    else:
        Save_ans_Close()
        print("App is Closed, Bye!") 

else: 
    print(
    f"Error, this command \"{user_input}\" is't found,"
      " please choose only one letter from ['s', 'a', 'd', 'u', 'q']")