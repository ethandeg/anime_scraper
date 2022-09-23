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
            close_db(cur)
    except Exception as e:
        print(e)


def get_studio(id):
    try:
        conn=connect_db()
        cur=conn.cursor()
        query="SELECT * FROM studios WHERE mal_id=%s" 
        cur.execute(query,[id])
        studio=cur.fetchone()
        return studio
    except Exception as e:
        print(e)
    finally:
        close_db(cur)

def insert_studio(id,name):
    try:
        #first check if id already exists
        studio=get_studio(id)
        if(studio):
            print(f"that studio already exists: {id}")
        else:
            conn=connect_db()
            cur=conn.cursor()
            query="INSERT INTO studios (mal_id,name) VALUES (%s,%s) RETURNING mal_id"
            cur.execute(query,[id,name])
            conn.commit()
            row=cur.fetchone()
            if(row):
                print(f"Found row, so sucessfully inserted! {row}")
            close_db(cur)
    except Exception as e:
        print(e)
def get_rank(name):
    try:
        conn=connect_db()
        cur=conn.cursor()
        query="SELECT * FROM ranks WHERE name=%s" 
        cur.execute(query,[name])
        rank=cur.fetchone()
        return rank
    except Exception as e:
        print(e)
    finally:
        close_db(cur)

def insert_rank(name):
    try:
        #first check if id already exists
        rank=get_rank(name)
        if(rank):
            print(f"that rank already exists: {id}")
        else:
            conn=connect_db()
            cur=conn.cursor()
            query="INSERT INTO ranks (name) VALUES (%s) RETURNING mal_id"
            cur.execute(query,[name])
            conn.commit()
            row=cur.fetchone()
            if(row):
                print(f"Found row, so sucessfully inserted! {row}")
            close_db(cur)
    except Exception as e:
        print(e)
def get_link(url,mal_id):
    try:
        conn=connect_db()
        cur=conn.cursor()
        print(f'*****************Url: {url}')
        query="SELECT * FROM anime_links WHERE link=%s AND mal_id=%s" 
        cur.execute(query,[url,mal_id])
        url=cur.fetchone()
        return url
    except Exception as e:
        print(e)
    finally:
        close_db(cur)

def insert_link(url,mal_id):
    try:
        #first check if id already exists
        link=get_link(url,mal_id)
        if(link):
            print(f"that url already exists: {link}")
        else:
            conn=connect_db()
            cur=conn.cursor()
            query="INSERT INTO anime_links (link,mal_id) VALUES (%s,%s) RETURNING link"
            print(f"inserting url**************: {url}")
            cur.execute(query,[url,mal_id])
            conn.commit()
            row=cur.fetchone()
            if(row):
                print(f"Found row, so sucessfully inserted! {mal_id}: {url}")
            close_db(cur)
    except Exception as e:
        print(e)



