import pathlib
import sqlite3
import pandas as pd
from pathlib import Path


path = Path().cwd()
path

def create_db( db_name , filename, table_name):
    file_path = path / filename

    con = sqlite3.connect(db_name) 
    cursor = con.cursor()

    students = pd.read_csv(file_path)    
    students.to_sql(table_name, con, index = False, if_exists= 'replace')
            
    results = cursor.execute(f"SELECT * FROM {table_name}").fetchall()
    print(results)
                             
    con.commit()
    con.close()  
    
if __name__=="__main__":
    db_name = "School3.db"
    filename = "students_1.csv"
    table_name = "students"
    create_db(db_name, filename, table_name)
    

