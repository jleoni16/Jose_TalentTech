import pymysql

db_host = 'dbjose1.cvg8emksavzi.us-east-2.rds.amazonaws.com'
db_user = 'Jose'
db_passw = 'Aixa93414L'

try:
    connection = pymysql.connect(
        host = db_host,
        user = db_user,
        password = db_passw
    )
    print("Succefull connection to DB")
except Exception as err:
    print("Error:", err)
    connection = None

def add_user(id, name, lastname, birthday):
    instruction_sql = "INSERT INTO Registro.Register(id, nombre, lastname, Birthday) VALUES ("+id+", '"+name+"', '"+lastname+"', '"+birthday+"')"
    try:
        cursor = connection.cursor()
        cursor.execute(instruction_sql)
        connection.commit()
        print("User added")
    except Exception as err:
        print("Error:", err)

def consult_user(id):
    instruction_sql = "SELECT * FROM db_users.users WHERE id="+id 
    try:
        cursor = connection.cursor()
        cursor.execute(instruction_sql)
        result = cursor.fetchall()
        print("User consulted")
        return result
    except Exception as err:
        print("Error:", err)
