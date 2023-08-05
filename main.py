from typing import Union

from fastapi import FastAPI

import cx_Oracle

app = FastAPI()



@app.get("/")
async def index():
    return {"Hello" : "World"}
    
@app.get("/find/{id}")
async def find_id(id : int, q : Union[str,None] = None):
    qry = '''SELECT * FROM employees WHERE EMPLOYEE_ID = ''' + str(id)
    try:
        conn = cx_Oracle.connect('HR/hr@localhost:1521/XEPDB1')
        print("Connected!")
        cur = conn.cursor()
        cur.execute(qry)
        data = cur.fetchall()
        
        return {"EMPLOYEE_ID" : data[len(data)-1][0] ,
            "FIRST_NAME" : data[len(data)-1][1] ,
            "LAST_NAME" : data[len(data)-1][2] ,
            "EMAIL" : data[len(data)-1][3].lower() + "@vit.ac.in" ,
            "PHONE_NUMBER" : data[len(data)-1][4] ,
            "HIRE_DATE" : data[len(data)-1][5] ,
            "JOB_ID" : data[len(data)-1][6] ,
            "SALARY" : data[len(data)-1][7] ,
            "COMMISSION_PCT" : data[len(data)-1][8] ,
            "MANAGER_ID" : data[len(data)-1][9] ,
            "DEPARTMENT_ID" : data[len(data)-1][10]}
    
    except Exception as e:
        print(str(e))
        return {"Error" : str(e)}
    