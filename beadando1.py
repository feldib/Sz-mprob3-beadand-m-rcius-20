def Befilenyit():
    hiba=True
    while hiba:
        try:
            print("Add meg a bemeneti fájl nevét!")
            filenev=input()
            befile=open(filenev, "rt", encoding="utf-8")
            hiba=False
        except:
            print("A ", filenev, " bemeneti fájl nem nyílt meg.")
    print("A ", filenev, " bemeneti fájl sikeresen megnyílt.")
    return (befile)

def Kifilenyit():
    hiba=True
    while hiba:
        try:
            print("Add meg a kimeneti fájl nevét!")
            filenev=input()
            kifile=open(filenev, "wt", encoding="utf-8")
            hiba=False
        except:
            print("A ", filenev, " kimeneti fájl nem jött létre.")
    print("A ", filenev, " kimeneti fájl sikeresen létrejött.")
    return (kifile)

def Feldolgozas(befile):
    sor=befile.readline()
    try:
        for i in range(0, len(sor.split())):
            int(sor.split()[i])
        while sor!="":
            if '0' not in sor.split():
                befile.close()
                return True
            else:
                for j in range(0, len(sor.split())):
                    int(sor.split()[j])
                sor=befile.readline()
        befile.close()
        return False
    except:
        befile.close()
        print("A bemeneti fájl nem megfelelő. Kérlek olyan fájlt adj meg, amelynek legalább egy nem üres sora van, és csak számok szerepelnek benne!")
        befile = Befilenyit()
        Feldolgozas(befile)

def Kiiras(kifile, ertek):
    if ertek:
        kifile.write("Igen")
        kifile.close()
    else:
        kifile.write("Nem")
        kifile.close()
    print("Az eredmény a kimeneti fájlban található.")

befile=Befilenyit()
kifile=Kifilenyit()
Kiiras(kifile, Feldolgozas(befile))
        
    