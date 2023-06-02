import mysql.connector


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Deniblanco69!",
  database="menagerie"
)
cursor = mydb.cursor()

def create_database():
    cursor.execute("DROP DATABASE IF EXISTS menagerie")
    cursor.execute("CREATE DATABASE menagerie")

def show_records():
    query = "SELECT * FROM pet"
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)


def show_table():
    query = "DESCRIBE pet"
    cursor.execute(query)
    table = cursor.fetchall()
    for column in table:
        print(column)

def show_female():
    query = "SELECT * FROM pet WHERE sex = 'f'"
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)

def show_databases():
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    for db in databases:
        print(db[0])
    cursor.close()
    mydb.close()

def show_name_birth():
    query = "SELECT name, birth FROM pet"
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        name, birth = record
        print(f"Name: {name}, Birth: {birth}")

def how_many_per_owner():
    query = "SELECT owner, COUNT(*) as num_pets FROM pet GROUP BY owner"
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        owner, num_pets = record
        print(f"Owner: {owner}, Number of Pets: {num_pets}")

def month_of_birth():
    query = "SELECT name, birth, MONTH(birth) as month_of_birth FROM pet"

    cursor.execute(query)
    records = cursor.fetchall()
    print("_______________________________________________")
    print("|   name     |     birth    |   MONTH(birth)  |")
    print("_______________________________________________")

    for record in records:
        name, birth, month_of_birth = record
        print(f"|  {name.ljust(8)}  |  {birth}  |  {str(month_of_birth).rjust(13)}  |")
    print("_______________________________________________")

if __name__ == '__main__':
    # create_database()
    # show_table()
    # show_databases()
    # show_records()
    # show_female()
    # show_name_birth()
    # how_many_per_owner()
    month_of_birth()
    cursor.close()
    mydb.close()


