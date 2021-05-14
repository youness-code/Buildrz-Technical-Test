import json
import psycopg2 as pg


class DataBase():
    def __init__(self, dbname, host, port, user, password):
        self.conn = pg.connect(dbname=dbname, host=host, port=port, user=user, password=password)

def fetch_todo() -> dict:
    query = "select * from projet"
    records = execute_read_query(query)
    todo_list = []
    for result in records:
        item = {
            "id": result[0],
            "parcelle": result[1],
            "ca": result[2],
            "cree-le": result[3],
            "status": result[4]
        }
        todo_list.append(item)

    return json.dumps(todo_list)


def insert_new_project(text: str) -> int:

    conn = DataBase.connect()
    query = 'Insert Into project (task, status) VALUES ("{}", "{}");'.format(
        text, "Todo")
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    project_id = query_results[0][0]
    conn.close()

    return project_id

def execute_read_query(self, query):
    records = []
    cur = self.conn.cursor()
    try:
        cur.execute(query)
        records = cur.fetchall()
    except Exception as e:
        print("Error", e)
    finally:
        cur.close()
    return records

