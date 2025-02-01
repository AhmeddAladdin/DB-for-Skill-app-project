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

# User ID
uid = input("Enter your ID: ")

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
#for key, user in enumerate(lst1, 100701): 
    #crsr.execute(f"insert into users(name, user_id) values('{user}', {key})")

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
    if len(data) == 0:
        print("you have 0 skill")
    for key, user in enumerate(data, 1):
        print(f"{key}- name => {user[0]},", end=" ")
        print(f"progress => {user[1]}%,", end=" ")
        print(f"user_id => {user[2]}")
    Save_ans_Close()
    
def Add_new_skill():
    """Adding a new skill for the assigned ID"""
    sk = input("Enter skill name: ").strip().capitalize()
    crsr.execute(f"select name from skills where name = '{sk}' and user_id = {uid}")
    data = crsr.fetchone()
    if data == None:
        prog = float(input("Enter your progress: ").strip())
        crsr.execute(f"insert into skills(name, progress, user_id) values('{sk}', {prog}, {uid})")
        print("Added successfully!")
    else:
        print("This skill is already exists, Do you want to update it?")
        while True:
            ask = input("choose Y for (yes) or N fo (no): ").upper()
            if ask == "Y":
                prog = float(input("Enter your progress: ").strip())
                crsr.execute(f"update skills set progress = {prog} where name = '{sk}' and user_id = {uid}")
                print("Updated successfully!")
                break
            elif ask == "N":
                break
            else:
                print("Undefined choise, please choose Y or N")
            continue
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
    crsr.execute(f"update skills set progress = {prog} where name = '{sk}' and user_id = {uid}")
    print("Updated successfully!")
    Save_ans_Close()

while True:
    # input option choose
    user_input = input(Input_Message).strip().lower()
    # check if choise is exists
    command_lst = ['s', 'a', 'd', 'u', 'q']
    if user_input in command_lst:
        if user_input == 's':
            Show_all_data()
            break
        elif user_input == 'a':
            Add_new_skill()
            break
        elif user_input == 'd':
            Delete_a_skill()
            break
        elif user_input == 'u':
            Update_skill()
            break
        else:
            Save_ans_Close()
            print("App is Closed, Bye!") 
            break
    else: 
        print(
        f"Error, this command \"{user_input}\" is't found,"
          " please choose only one letter from ['s', 'a', 'd', 'u', 'q']")
    continue
