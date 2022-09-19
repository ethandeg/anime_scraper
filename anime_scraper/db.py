import psycopg2
import os
from anime_scraper.config import PG_CONFIG
def connect_db():


    try:
        host=os.environ.get('PG_HOST',PG_CONFIG['host']) 
        user=os.environ.get('PG_USER',PG_CONFIG['user']) 
        database=os.environ.get('PG_DB',PG_CONFIG['database']) 
        password=os.environ.get('PG_PASS',PG_CONFIG['password']) 
        port=os.environ.get('PG_PORT',PG_CONFIG.get('port'))
        conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port)
        # execute a statement
    #     print('PostgreSQL database version:')
    #     cur.execute('SELECT version()')

    #     # display the PostgreSQL database server version
    #     db_version = cur.fetchone()
    #     print(db_version)
        
    # # close the communication with the PostgreSQL
    #     cur.close()
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    #         print('Database connection closed.')

def close_db(con):
    if con is not None:
        con.close()


