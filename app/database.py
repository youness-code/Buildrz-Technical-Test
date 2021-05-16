from app import db
import json
import psycopg2 as pg


class DataBase():
    def __init__(self, dbname, host, port, user, password):
        self.conn = pg.connect(dbname=dbname, host=host, port=port, user=user, password=password)

    def fetch_todo() -> dict:
        conn = db.connect()
        query = "SELECT adresse, surface, cree_le, ca FROM parcelle pa INNER JOIN projet pr ON pa.id=pr.parcelle WHERE ville='Montreuil' AND status='en cours'"
        records = conn.execute(query).fetchall()
        conn.close()
        todo_list = []
        for result in records:
            item = {
                "Adresse = ", result[0],
                "Surface = ", float(result[1]),
                "Cree_le = ", result[2],
                "CA  = ", float(result[3])
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

    '''
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
        '''

