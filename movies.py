import sqlite3
mov = sqlite3.connect('movielists.db')
c = mov.cursor()
c.execute("""CREATE TABLE movies (
        movie_name text,
        lead_actor text,
        actress text,
        release_year text,
        director text    
    )""")
movie_list = [
              ('The Curious Case Of Benjamin Button','Brad Pitt','Cate Blanchett','2008','David Fincher'),
              ('The Revenant', 'Leonardo DiCaprio','Tom Hardy','2015','Alejandro González Iñárritu'),
              ('Dangal','Aamir Khan','Fatima Sana Shaikh','2016','Nitesh Tiwari'),
              ('Shutter Island','Leonardo DiCaprio','Mark Ruffalo','2010','Martin Scorsese'),
              ('Neelakasham Pachakadal Chuvanna Bhoomi','Dulquer Salmaan','Sunny Wayne','2013','Sameer Thahir'),
              ('Aruvi','Aditi Balan','Lakshmi Gopalaswami','2016','Arun Prabhu'),
              ('Avatar','Zoe Saldana','Sam Worthington','2009','James Cameron'),
              ('Memories','Prithviraj Sukumaran','Meghana Raj','2013','Jeethu Joseph'),
              ]
c.executemany("INSERT INTO movies VALUES (?,?,?,?,?)", movie_list )
c.execute("SELECT * FROM movies")
c.execute("SELECT * FROM movies WHERE lead_actor = 'Leonardo DiCaprio' ")
items = c.fetchall()
for item in items:
    print(item) 
mov.commit()
mov.close()