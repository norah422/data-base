import sqlite3
from pathlib import Path
import csv

connection2 = sqlite3.connect(Path.home()/ Path('Desktop', 'Data_Base.db'))
crsr = connection2.cursor()
print('connected to the database')

# create table
command = """CREATE TABLE if not exists employees (
id INTEGER,
Name VARCHAR(20),
Salary INTEGER,
Date_of_employment TEXT)"""

crsr.execute(command)

# read file
file = open(Path.home()/ Path('Desktop', 'employees_1 (1).csv'))
rows = csv.reader(file)

crsr.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", rows)

connection2.commit()
connection2.close()
