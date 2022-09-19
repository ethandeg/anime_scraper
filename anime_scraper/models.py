from anime_scraper.db import connect_db,close_db

def get_genre(id):
    try:
        conn=connect_db()
        cur=conn.cursor()
        query="SELECT * FROM genres WHERE mal_id=%s" 
        cur.execute(query,[id])
        genre=cur.fetchone()
        return genre
    except Exception as e:
        print(e)
    finally:
        close_db(cur)

def insert_genre(id,name):
    try:
        #first check if id already exists
        genre=get_genre(id)
        if(genre):
            print(f"that genre already exists: {id}")
        else:
            conn=connect_db()
            cur=conn.cursor()
            query="INSERT INTO genres (mal_id,name) VALUES (%s,%s) RETURNING mal_id"
            cur.execute(query,[id,name])
            conn.commit()
            row=cur.fetchone()
            if(row):
                print(f"Found row, so sucessfully inserted! {row}")
            close_db()
    except Exception as e:
        print(e)

