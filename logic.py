import sqlite3

from config import DATABASE

conn = sqlite3.connect(".\[IND] M4L3_world_information.db")

with conn:
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM continents;
""")
    result = cur.fetchall()

    print(result)



    with conn:
        cur = conn.cursor()
        cur.execute("""
        SELECT * FROM country
        where continent_id < 2;
    """)
        result = cur.fetchall()

        print(result)

with conn:
        cur = conn.cursor()
        cur.execute("""
        SELECT * FROM country
        where continent;
    """)
        result = cur.fetchall()

        #print(result)
