import sqlite3
import pandas as pd
from pathlib import Path

db_path = sqlite3.connect(Path.home()/ Path('Desktop', 'Data_Base.db'))
cursor2 = db_path.cursor()
print('connected to the database')

cursor2.execute('SELECT first_name,last_name,age FROM students')
data = cursor2.fetchall()

columns = [desc[0] for desc in cursor2.description]

df = pd.DataFrame(data, columns = columns)
file_path = (Path.home() / Path("Desktop","students.xlsx"))
df.to_excel(file_path, index= False, engine='openpyxl')

cursor2.close()
db_path.close()
