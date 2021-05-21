from flask import Flask
import psycopg2

def init_connection_engine():
    #initialize database setup
    
    conn = None
    try:
        conn = psycopg2.connect(user="youness",
                                password="",
                                host="127.0.0.1",
                                port="5000",
                                database="postgres_db"
        )
    
    except (Exception, psycopg2.Error) as error :
        print ("Erreur lors de la connexion à PostgreSQL", error)

    return conn


app = Flask(__name__)
db = init_connection_engine
from app import routes

