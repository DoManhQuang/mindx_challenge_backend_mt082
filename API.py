import sqlite3
import pandas as pd
import numpy as np
import json


def connect_database():
    db = sqlite3.connect('test.db')
    sta = "Opened database successfully"
    return db, sta


def load_data_set(csv):
    data = np.array(pd.read_csv(csv, index_col=False))
    return data


def insert(db, data_feature):
    sqlcmd = "INSERT INTO user_covid (uuid,fullname,address,location,health_status) VALUES (?, ?, ?, ?, ?);"
    db.execute(sqlcmd, data_feature)
    db.commit()
    return "DONE"


def insert_dataset(db, data_set):
    for data in data_set:
        insert(db, data)
    return "Insert DONE!"


def select_top_100(db):
    cursor = db.execute("SELECT uuid, health_status from user_covid LIMIT 100")  # obj
    top_100 = []
    for row in cursor:
        top_100.append(row)
    json_data = json.dumps(np.array(top_100).tolist())
    return json_data


def select_random_top_1000(db):
    cursor = db.execute("SELECT uuid,fullname,address,location,health_status "
                        "from user_covid ORDER BY RANDOM() LIMIT 10")
    top_1000 = []
    for row in cursor:
        top_1000.append(row)
    json_data = json.dumps(np.array(top_1000).tolist())
    return json_data


if __name__ == '__main__':
    connect, status = connect_database()
    dataset = load_data_set('dataset.csv')
    print(dataset.shape)
    status_add = insert_dataset(connect, dataset)
    print(status_add)
    top100 = select_top_100(connect)
    print(top100)
    random_top1000 = select_random_top_1000(connect)
    print(random_top1000)

    pass




