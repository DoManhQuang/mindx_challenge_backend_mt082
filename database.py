import sqlite3


def created_table(connect):
    connect.execute('''CREATE TABLE user_covid(
                    uuid VARCHAR(50) PRIMARY KEY NOT NULL,
                    fullname VARCHAR(500) NOT NULL,
                    address VARCHAR(500),
                    location TEXT,
                    health_status VARCHAR(50));''')

    print("Table created successfully")


def insert_data_same(connect, data):
    connect.execute("INSERT INTO user_covid (uuid,fullname,address,location,health_status) "
                    "VALUES (?, ?, ?, ?, ?);", data)

    connect.commit()
    print("Records created successfully")


def select_db(connect):
    cursor = connect.execute("SELECT uuid,fullname,address,location,health_status from user_covid LIMIT 4")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("Operation done successfully")


if __name__ == '__main__':
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    # created_table(conn)
    # data = ['4', 'Paul', 'California', '21.022978, 105.795811', 'F1']
    # insert_data_same(conn, data)
    select_db(conn)
    conn.close()




