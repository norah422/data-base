import sqlite3
from pathlib import Path

message = """
"a" => Add New Task
"d" => Delete A Task
"s" => Show All Task
"u" => Update A Task
"q" => Quit The App
Please choose an option:
"""

user_input = input(message).strip().lower()
# command list
commands_list = ["a", "d", "s", "u", "q"]
user_id = 1

try:
    #connect to db
    db_path = sqlite3.connect(Path.home() / Path('Desktop', 'To_do_app.db'))
    crsr = db_path.cursor()

except:
    print("connection error")

finally:
    if db_path:
        #create table
        sql_command = """CREATE TABLE if not exists Tasks(
        user_id INTEGER,
        task_name VARCHAR(20),
        description TEXT)"""
        crsr.execute(sql_command)


        def show_task():
            crsr.execute(f"SELECT * FROM Tasks WHERE user_id = {user_id}")

            results = crsr.fetchall()

            print(f" you have {len(results)} tasks")

            if len(results) > 0:
                for task in results:
                    print(f"task name: {task[1]} and", end=" ")
                    print(f"task description: {task[2]}")

            db_path.commit()


        def add_task():
            task_name = input("Enter Task Name: ").strip()
            des = input("Enter The Task Description: ").strip()

            crsr.execute(f"INSERT INTO Tasks (user_id, task_name, description) VALUES ('{user_id}', '{task_name}', '{des}')")
            db_path.commit()

        def delete_task():
            task_name = input("Enter The Task Name You Want To Delete: ").strip()
            crsr.execute(f"DELETE FROM Tasks WHERE task_name = '{task_name}' and user_id= '{user_id}'")
            db_path.commit()


        def update_task():
            task_name = input('enter the name of the task you want to modify: ').strip()
            crsr.execute(f"SELECT * FROM Tasks WHERE task_name = '{task_name}' AND user_id = '{user_id}' ")
            results = crsr.fetchall()

            if not results:
                print("there is no task with this name")

            else:
                des = input("enter the new task description: ").strip()
                crsr.execute(f"UPDATE Tasks SET description = '{des}' WHERE task_name = '{task_name}' AND user_id = '{user_id}'")

                db_path.commit()

                print("the task has been successfully modified")


        def quit_app():
            print('program closed')
            exit()

        if user_input in commands_list:

            if user_input == "s":
                show_task()

            elif user_input == "a":
                add_task()

            elif user_input == "d":
                delete_task()

            elif user_input == "u":
                update_task()


        else:
            print('Sorry This Command Is Not Found')


        if user_input == "q":
            quit_app()


    db_path.close()


