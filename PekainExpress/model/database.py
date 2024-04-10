import sqlite3

def creer_table() :

    conn = sqlite3.connect('train.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Train")
    cur.execute("""CREATE TABLE Train (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                destination TEXT,
                heures text)
                """)
    conn.close()

creer_table()

conn = sqlite3.connect('train.db')
cur = conn.cursor()

#cur.execute("""INSERT INTO Train (id, nom, destination, heures)
    # VALUES (1, 'JIJI', 'Strasbourg', '15h10')""")
#conn.commit()

#train_2 = ('LOPA', 'Tokyo', '08h30')
#cur.execute("""INSERT INTO Train (nom, destination, heures)
#     VALUES (?, ?, ?)""", train_2)
#conn.commit()

#train_3 = {'nom' : 'JIFY', 'destination': 'New York', 'heures': '11h20'}
#cur.execute("""INSERT INTO Train (nom, destination, heures)
     #VALUES (:nom, :destination , :heures)""", train_3)
#conn.commit()

def trains() :
    mes_trains = [
    ('JIJI', 'Strasbourg', '15h10'),
    ('LOPA', 'Tokyo', '08h30'),
    ('JIFY', 'New York', '11h20'),
    ('GIUY', 'Venise', '21h45'),
    ('VOGA', 'Bruxelle', '07h28'),
    ('XWBL', 'Miami', '18h12'),
    ('AZEC', 'Luxembourg', '13h57'),
    ('DYNG', 'Pekain', '12h23'),
    ('IFET', 'Lisbonne', '08h36'),
    ('TYFX', 'Séoul', '09h22'),
    ('KJHR', 'Alsace', '16h06'),
    ('UHCG', 'Paris', '23h00'),
    ('LJHI', 'Thaïlande', '14h49'),
    ('HEDV', 'Laos', '10h26'),
    ('DXGF', 'Bali', '13h31'),
    ('KHJM', 'Chili', '06h50'),
    ('HDYY', 'Argentine', '14h19'),
    ('ATKM', 'Russie', '19h28'),
    ('FGDF', 'Los-Angeles', '16h15'),
    ('PXNE', 'Pérou', '17h26')
]



#for train in autres_train:
#    cur.execute("""INSERT INTO Train (nom, destination, heures)
#        VALUES (?, ?, ?)""", train)
#conn.commit()

cur.executemany("""INSERT INTO Train (nom, destination, heures)
     VALUES (?, ?, ?)""", trains) 
conn.commit()

#res = cur.execute("SELECT * FROM Train")
#print(res.fetchall())
#print(list(res))
#print(res.fetchone())
#print(res.fetchmany(3))

#res = cur.execute("SELECT id, nom, destination, heures FROM Train WHERE destination LIKE 'A%'")
#print(res.fetchall())

def recup_train_par_destination(destination):
    conn = sqlite3.connect('train.db')
    cur = conn.cursor()
    res = cur.execute("SELECT id, nom, destination, heures FROM Train WHERE destination = ?", (destination, ))
    trains = res.fetchall()
    conn.close()
    return trains

print(recup_train_par_destination('Paris'))


conn.close()

