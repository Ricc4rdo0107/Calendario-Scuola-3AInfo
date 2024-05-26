import keyboard
from time import sleep

giorni = ["lun", "mar", "mer", "gio", "ven", "sab", "dom"]
mesi   = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
mesiTable = {
    "gen":31, "feb":None, "mar":31, "apr":30, "mag":31, "giu":30, "lug":31, "ago":31, "set":30, "ott":31, "nov":30, "dic":31
}

def isBisestile(anno):
    return (anno % 400 == 0) or (anno % 4 == 0 and not (anno % 100 == 0))

def printMese(giorno, mese, anno):
    mesiTable["feb"] = 28 if not isBisestile(anno) else 29
    meseString = ""
    meseString += f"{mese+' '+str(anno):^20}\n"    #centra la parola "mese" tra 20 caratteri
    meseString += " L  M  M  G  V  S  D\n"
    for i in range(spaces := giorni.index(giorno)):
        meseString += "// "

    for i in range(mesiTable[mese]):
        g = str(i + 1)
        if len(g) == 1:
            g = "/" + g
        meseString += f"{g} "
        if (i + 1 + spaces) % 7 == 0:
            meseString += "\n"
    return meseString


def nextMonth(giorno, mese, anno):
    tmpmese = mese
    if mese[:3] == "dic":
        anno += 1
        mese = "gen"
    else:
        mese = mesi[mesi.index(mese) + 1]
        giornoIndex = giorni.index(giorno)
        giorno = giorni[(giornoIndex + mesiTable[tmpmese]) % len(giorni)]

    return printMese(giorno, mese, anno), giorno, mese, anno

def previousMonth(giorno, mese, anno):
    tmpmese = mese
    if mese[:3] == "gen":
        anno -= 1
        mese = "dic"
    else:
        mese = mesi[mesi.index(mese) - 1]
    giorni_nel_mese_precedente = mesiTable[mese]
    index_giorno_corrente = giorni.index(giorno)
    index_giorno_precedente = (index_giorno_corrente - giorni_nel_mese_precedente % 7) % 7
    giorno = giorni[index_giorno_precedente]

    return printMese(giorno, mese, anno), giorno, mese, anno

# MAIN
if __name__ == "__main__":
    giorno = input("Giorno: ").lower()[:3]
    while not (giorno in giorni):
        print("Inserisci un giorno valido (lun, mar, mer, gio, ven, sab, dom)")
        giorno = input("Giorno: ").lower()[:3]

    mese = input("Mese:   ")[:3]
    while not (mese in mesi):
        print("Inserisci un mese valido (gen, feb, mar, apr, mag, giu, lug, ago, set, ott, nov, dic)")
        mese = input("Mese:  ")[:3]

    anno = int(input("Anno:   "))

    meseString = printMese(giorno=giorno, mese=mese, anno=anno)
    print(meseString)

    print("Premere + per andare avanti, - per andare indietro o Q per uscire")

    
    while True:
        key = keyboard.read_key()
        if key == "+":
            ms, giorno, mese, anno = nextMonth(giorno, mese, anno)
            print(ms)
            sleep(0.5)
        elif key == "-":
            ms, giorno, mese, anno = previousMonth(giorno, mese, anno)
            print(ms)
            sleep(0.5)
        elif key == "q":
            print("Programma terminato.")
            break
        print("Premere + per andare avanti, - per andare indietro o Q per uscire")