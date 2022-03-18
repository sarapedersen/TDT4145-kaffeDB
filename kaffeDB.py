import sqlite3
con = sqlite3.connect("kaffe.db")

cursor = con.cursor()

## Må kommenteres ut etter de har blitt kjørt en gang.  ##

#cursor.execute("INSERT INTO bruker VALUES ('saraped@stud.ntnu.no', 'Passord123', 'Sara', 'Pedersen')")
#cursor.execute("INSERT INTO kaffegård VALUES (1, 'Klæbugården', 500, 'Norge', 'Trondheim')")
#cursor.execute("INSERT INTO kaffebønner VALUES ('Arabica', 'Coffea Arabica')")
#cursor.execute("INSERT INTO kaffebønner VALUES ('Robusta', 'Coffea Robusta')")
#cursor.execute("INSERT INTO kaffebønner VALUES ('Liberica', 'Coffea Liberica')")

cursor.execute("SELECT * FROM bruker")
cursor.execute("SELECT navn FROM kaffebønner")

print(cursor.fetchall())

con.commit()


con.close()

## Kjøres med "python kaffeDB.py" i terminalen


