import sqlite3


class notlar:
    isim =""
    not1=""
    not2=""
    not3=""

con = sqlite3.connect("work.db")
cursor = con.cursor()

def dbConnect():
    cursor.execute("CREATE TABLE IF NOT EXISTS NOTLAR ( ISIM TEXT,NOT1 INT , NOT2 INT , NOT3 INT)")
    con.commit()

def kayitEkle(isim , not1,not2,not3):
    cursor.execute("INSERT INTO NOTLAR(ISIM , NOT1,NOT2,NOT3) VALUES ( ? , ? , ? , ? )",(isim , not1,not2,not3))
    con.commit()

def dbListe():
    data = cursor.execute("SELECT * FROM NOTLAR")
    for x in data:
        print(x)

def deleteRecords():
    cursor.execute("DELETE FROM NOTLAR")
    con.commit()

def notHesapla(psatir):
    nots = notlar()
    list = psatir.split(",")
    nots.isim = list[0]
    nots.not1= int(list[1])
    nots.not2=int(list[2])
    nots.not3=int(list[3])

    return  nots

dbConnect()
deleteRecords()
with open("C:/Users/hphp/Desktop/bilgiler.txt", "r") as file:

    for i in file:
        #print(i)
        #notlar = notHesapla(i)
        nots = notHesapla(i)
       # list = i.split(",")
        #nots.isim = list[0]
        #nots.not1 = int(list[1])
        #nots.not2 = int(list[2])
        #nots.not3 = int(list[3])

        #print(nots.isim)
        kayitEkle(nots.isim,nots.not1,nots.not2,nots.not3)

#notlar = notHesapla("Fatih Akman,100,10,60")
#print(notlar.isim)
dbListe()