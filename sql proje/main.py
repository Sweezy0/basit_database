import sqlite3

db = sqlite3.connect("vt.sqlite")

im = db.cursor()

im.execute("""CREATE TABLE IF NOT EXISTS kullanicilar
    (kullanici_adi, parola)""")

veriler = [
            ("ahmet123", "12345678"),
            ("mehmet321", "87654321"),
            ("selin456", "123123123")
          ]

for i in veriler:
    im.execute("""INSERT INTO kullanicilar VALUES (?, ?)""", i)

db.commit()

kull = input("Kullanıcı adınız: ")
paro = input("Parolanız: ")

im.execute("""SELECT * FROM kullanicilar WHERE
kullanici_adi = ? AND parola = ?""", (kull, paro))

data = im.fetchone()

if data:
    print("Programa hoşgeldin {}!".format(data[0]))
else:
    print("Parola veya kullanıcı adı yanlış!")