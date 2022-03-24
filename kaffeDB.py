import sqlite3
import random
con = sqlite3.connect("kaffe.db")

cursor = con.cursor()

## Må kommenteres ut etter de har blitt kjørt en gang.  ##

# cursor.execute("INSERT INTO bruker VALUES ('saraped@stud.ntnu.no', 'Passord123', 'Sara', 'Pedersen')")
# cursor.execute("INSERT INTO bruker VALUES ('theakvi@stud.ntnu.no', 'Passord123', 'Thea', 'Kvinnegard')")
# cursor.execute("INSERT INTO kaffesmaking VALUES (3, 'Firkantete', 2, '23.03.2022', 'theakvi@stud.ntnu.no', 'Frokostkaffe', 'Kaffehuset Friele')")
# cursor.execute("INSERT INTO kaffesmaking VALUES (4, 'trekantet', 12, '23.03.2022', 'saraped@stud.ntnu.no', 'Brasil, Diamond Santos', 'Jacobsen og Svart')")
# cursor.execute("INSERT INTO kaffesmaking VALUES (5, 'rund og skarp', 12, '22.03.2022', 'saraped@stud.ntnu.no', 'Espressokaffe', 'Kaffehuset Friele')")
# cursor.execute("INSERT INTO ferdigbrentKaffe VALUES ('Frokostkaffe', 'Kaffehuset Friele', '20.03.2022', 'rund og fyldig kaffe med lang ettersmak', 144, 'lys', 100)")
# cursor.execute("INSERT INTO ferdigbrentKaffe VALUES ('Kaffehuset Friele', 'Café Noir', '10.11.2021', 'mørk og god', 212, 'mørk', 100)")
# cursor.execute("INSERT INTO ferdigbrentKaffe VALUES ('Espressokaffe', 'Kaffehuset Friele', '22.12.2021', 'flott espressokaffe med god fylde', 201, 'mørk', 100)")
# cursor.execute("INSERT INTO ferdigbrentKaffe VALUES ('Honduras El Campo', 'Jacobsen og Svart ', '02.01.2022', 'søt, fruktig kaffe med smak av moden fersken, røde druer og fiken', 716, 'lys', 100)")
# cursor.execute("INSERT INTO ferdigbrentKaffe VALUES ('Brasil, Diamond Santos', 'Jacobsen og Svart ', '22.02.2022', 'søt, fruktig kaffe med smak av moden fersken, røde druer og fiken', 398, 'mørk', 100)")
# cursor.execute("INSERT INTO ferdigbrentKaffe VALUES ('Svart kaffe', 'Jacobsen og Svart ', '02.01.2022', 'søt, fruktig kaffe med smak av moden fersken, røde druer og fiken', 716, 'lys', 102)")
# cursor.execute("INSERT INTO ferdigbrentKaffe VALUES ('Ettermiddagskaffe', 'Jacobsen og Svart ', '02.01.2022', 'søt, fruktig kaffe med smak av moden fersken, røde druer og fiken', 716, 'lys', 103)")
# cursor.execute("INSERT INTO kaffegård VALUES (1, 'Klæbugården', 500, 'Norge', 'Trondheim')")
# cursor.execute("INSERT INTO kaffegård VALUES (2, 'Colombisk kaffegård', 500, 'Colombia', 'sted')")
# cursor.execute("INSERT INTO kaffegård VALUES (3, 'Fra Rwanda', 500, 'Rwaanda', 'STed')")
# cursor.execute("INSERT INTO kaffeparti VALUES (100, 550, 2021, 1, 'vasket')")
# cursor.execute("INSERT INTO kaffeparti VALUES (102, 550, 2021, 2, 'tørket')")
# cursor.execute("INSERT INTO kaffeparti VALUES (103, 550, 2021, 3, 'tørket')")
# cursor.execute("INSERT INTO foredlingsmetode VALUES ('vasket', 'vasker bærene og sånt')")
# cursor.execute("INSERT INTO kaffebønner VALUES ('Arabica', 'Coffea Arabica')")
# cursor.execute("INSERT INTO kaffebønner VALUES ('Robusta', 'Coffea Robusta')")
# cursor.execute("INSERT INTO kaffebønner VALUES ('Liberica', 'Coffea Liberica')")
# cursor.execute("DELETE FROM ferdigbrentKaffe")
# cursor.execute("SELECT * FROM ferdigbrentKaffe")
# print(cursor.fetchall())

bruker = "saraped@stud.ntnu.no"
dagensDato = "23.03.2022"

def brukerhistorie1(): 
    #  Input fra brukerens side er brenneri, kaffenavn, poeng og smaksnotat
    cursor.execute("SELECT kaffebrenneri, navn FROM ferdigbrentKaffe")
    kaffeliste = cursor.fetchall()
    for x in range(0, len(kaffeliste)): 
        print(x, ": ",  kaffeliste[x])
    kaffeid = int(input("Velg kaffe: "))   
    poeng = input("Poeng: ")
    smaksnotat = input("Smaksnotat: ")
    #bruker = input("Bruker: ")  
    poeng = int(poeng)
    cursor.execute("INSERT INTO  kaffesmaking VALUES ({}, '{}', {}, '{}', '{}', '{}', '{}')".format(counter(), smaksnotat, poeng, dagensDato, bruker, kaffeliste[kaffeid][1], kaffeliste[kaffeid][0]))
    cursor.execute("SELECT * FROM kaffesmaking")
    print(cursor.fetchall())

def brukerhistorie2(): 
    # En bruker skal kunne få skrevet ut en liste over hvilke brukere som har smakt flest unike kaffer så langt i år, sortert synkende
    cursor.execute("SELECT fornavn, etternavn, COUNT(*) AS kaffecount FROM bruker INNER JOIN kaffesmaking USING(epost) GROUP BY bruker.epost ORDER BY kaffecount DESC")
    liste = cursor.fetchall()
    for x in liste: 
        print(x[0], x[1] + ":", x[2])
    

def brukerhistorie3():
    #   En skal kunne se hvilke kaffer som gir forbrukeren mest for pengene
    #   ifølge KaffeDBs brukere (høyeste gjennomsnittsscore kontra pris), sortert synkende. 
    #   Listen skal inneholde brennerinavn, kaffenavn, pris og gjennomsnittsscore for hver kaffe
    
    # gjennomsnittScore = 0
    #cursor.execute("SELECT * FROM ferdigbrentKaffe INNER JOIN kaffesmaking USING(kaffebrenneri, ferdigbrentkaffe.navn) ")
    # prisliste = cursor.fetchall()
    # for x in prisliste:
    print("hei")

def brukerhistorie4():
    ord = input("Søk etter ord: ") 
    kaffeliste = cursor.execute("SELECT DISTINCT ks.kaffenavn, fbk.kaffebrenneri FROM ferdigbrentkaffe AS fbk INNER JOIN kaffesmaking AS ks ON ks.kaffenavn = fbk.navn AND ks.kaffebrenneri = fbk.kaffebrenneri WHERE ks.notater LIKE '%{}%' OR fbk.beskrivelse LIKE '%{}%'".format(ord, ord))
    for x in kaffeliste: 
        print(x[0], x[1])

#AND kaffeparti.foredlingsmetode NOT LIKE 'Vasket'
def brukerhistorie5(): 
    kaffeliste = cursor.execute("SELECT fbk.navn, fbk.kaffebrenneri, kaffegård.land, kaffeparti.foredlingsmetode FROM (ferdigbrentkaffe AS fbk INNER JOIN kaffeparti ON fbk.partiId = kaffeparti.id) INNER JOIN kaffegård ON kaffeparti.gårdId = kaffegård.id WHERE kaffegård.land LIKE 'Colombia' OR kaffegård.land LIKE 'Rwaanda' AND kaffeparti.foredlingsmetode NOT LIKE 'vasket'")
    for x in kaffeliste: 
        print(x[0], x[1])



def loggIn(): 
    riktigInfo = False
    
    while riktigInfo == False: 
        brukerliste = cursor.execute("SELECT epost, passord FROM bruker")
        epost = input("Epost: ")
        passord = input("Passord: ")
        for y in brukerliste: 
            if epost == y[0]:
                if passord == y[1]: 
                    riktigInfo == True
                    return epost
        print("Feil epost eller passord er oppgitt, prøv igjen") 


def lagBruker(): 
    print("Du må lage bruker :D")
    epost = input("Epost: ")
    unik = False
    while unik == False:
        brukerliste = cursor.execute("SELECT epost, passord FROM bruker")
        unik = True
        for x in brukerliste: 
            if epost == x[0]: 
                unik = False
                print("Denne eposten finnes fra før, vennligst bruk en annen epost.") 
                epost = input("Epost: ")
    fornavn = input("Fornavn: ")   
    etternavn = input("Etternavn: ")
    passord1 = input("Passord: ") 
    passord2 = input("Bekreft passord: ") 
    while passord1 != passord2:
        print("Passordene matchet ikke, vennligst prøv igjen")
        passord1 = input("Passord: ") 
        passord2 = input("Bekreft passord: ")
    cursor.execute("INSERT INTO bruker VALUES ('{}', '{}', '{}', '{}')".format(epost, passord1, fornavn, etternavn))
    print("Gratulerer du har laget bruker!")
    return epost

def counter(): 
    return random.randrange(0, 10000, 1)

def main(): 
    print("Velkommen til kaffeDB!") 
    # harBruker = input("Har du bruker? (j/n) ")
    # if harBruker == "j": 
    #     bruker = loggIn()
    # else: 
    #     bruker = lagBruker()
    print("Du er nå logget inn")   
    userInput = "null"
    while userInput != "exit" :
        userInput = input()
        if userInput == "1": 
            brukerhistorie1()
            print(userInput)
        if userInput == "2": 
            brukerhistorie2()
        if userInput == "4": 
            brukerhistorie4()
        if userInput == "5": 
            brukerhistorie5()

main()


con.commit()



con.close()

# test = input()
# print(test)

## Kjøres med "python kaffeDB.py" i terminalen

# De fem brukerhistoriene må være tilfredsstilt. Enkleste løsning er å lage et
# tekstbasert grensesnitt som kjører i et terminalvindu (eksempelvis cmd, bash, o.l.). Husk at
# poenget med oppgaven er å lage modeller, skrive SQL og gjøre databaseaksess fra Python.



