from model import Matrika

def pozdrav():
    print("\nAhoj, tu sem, da te rešim dolgočasnih delov linearne algebre!")
    print("POZOR! Matrike piši tako, da elemente iste vrstice ločiš s presledkom, vrstice pa z vejicami.")
    print("Identiteta recimo izgleda takole: 1 0 0, 0 1 0, 0 0 1 \n")

def izberi(mozni_odgovori):
    for indeks, odgovor in enumerate(mozni_odgovori):
        print('{}) {}'.format(indeks + 1, odgovor))
    izbira = input('-> ')
    return int(izbira) - 1

def meni():
    print("Kako ti lahko danes pomagam?")
    izbira = izberi([
        "seštej",
        "odštej",
        "pomnoži (s skalarjem ali drugo matriko)",
        "sledi (izračunaj sled)",
        "transponiraj",
        "determiniraj (izračunaj determinanto)",
        "obrni (poišči inverz, če obstaja)",
    ])

    if izbira == 0:
        sestej()
    elif izbira == 1:
        odstej()
    elif izbira == 2:
        pomnozi()
    elif izbira == 3:
        sled()
    elif izbira == 4:
        transponiraj()
    elif izbira == 5:
        determinanta()
    elif izbira == 6:
        inverz()
    else:
        assert False

def sestej():
    # mogoče je še mal tko eh
    matrika1 = input("Navedi prvo matriko, ki jo želiš sešteti: ")
    matrika1 = matrika1.split(",")
    prva_matrika = []
    for vrstica in matrika1:
        vrstica = vrstica.split()
        vrstica = [int(x) for x in vrstica]
        prva_matrika.append(vrstica)
    prva_matrika = Matrika(prva_matrika)

    matrika2 = input("Navedi drugo matriko, ki jo želiš sešteti: ")
    matrika2 = matrika2.split(",")
    druga_matrika = []
    for vrstica in matrika2:
        vrstica = vrstica.split()
        vrstica = [int(x) for x in vrstica]
        druga_matrika.append(vrstica)
    druga_matrika = Matrika(druga_matrika)
    print(prva_matrika + druga_matrika)
    

def odstej():
    matrika1 = input("Navedi matriko, od katere želiš odštevati: ")
    matrika1 = matrika1.split(",")
    prva_matrika = []
    for vrstica in matrika1:
        vrstica = vrstica.split()
        vrstica = [int(x) for x in vrstica]
        prva_matrika.append(vrstica)
    prva_matrika = Matrika(prva_matrika)

    matrika2 = input("Navedi matriko, ki jo želiš odšteti: ")
    matrika2 = matrika2.split(",")
    druga_matrika = []
    for vrstica in matrika2:
        vrstica = vrstica.split()
        vrstica = [int(x) for x in vrstica]
        druga_matrika.append(vrstica)
    druga_matrika = Matrika(druga_matrika) * -1
    print(prva_matrika + druga_matrika)

def pomnozi():
    matrika1 = input("Navedi prvo matriko, ki jo želiš množiti: ")
    matrika1 = matrika1.split(",")
    prva_matrika = []
    for vrstica in matrika1:
        vrstica = vrstica.split()
        vrstica = [int(x) for x in vrstica]
        prva_matrika.append(vrstica)
    prva_matrika = Matrika(prva_matrika)

    matrika2 = input("Navedi drugo matriko, ki jo želiš množiti: ")
    matrika2 = matrika2.split(",")
    druga_matrika = []
    for vrstica in matrika2:
        vrstica = vrstica.split()
        vrstica = [int(x) for x in vrstica]
        druga_matrika.append(vrstica)
    druga_matrika = Matrika(druga_matrika)
    print(prva_matrika * druga_matrika)

def sled():
    matrika = input("Navedi matriko, katere sled želiš izračunati: ")
    matrika = matrika.split(",")
    matrika1 = []
    for vrstica in matrika:
        vrstica = vrstica.split()
        vrstica = [int(x) for x in vrstica]
        matrika1.append(vrstica)
    matrika1 = Matrika(matrika1)
    print(matrika1.sled())

def transponiraj():
    matrika = input("Navedi matriko, ki jo želiš transponirarti: ")
    matrika = matrika.split(",")
    matrika1 = []
    for vrstica in matrika:
        vrstica = vrstica.split()
        vrstica = [int(x) for x in vrstica]
        matrika1.append(vrstica)
    matrika1 = Matrika(matrika1)
    print(matrika1.transponiraj())

def determinanta():
    matrika = input("Navedi matriko, katere determinanto želiš izračunati: ")
    matrika = matrika.split(",")
    matrika1 = []
    for vrstica in matrika:
        vrstica = vrstica.split()
        vrstica = [int(x) for x in vrstica]
        matrika1.append(vrstica)
    matrika1 = Matrika(matrika1)
    print(matrika1.determinanta())

def inverz():
    matrika = input("Navedi matriko, ki jo želiš obrniti: ")
    matrika = matrika.split(",")
    matrika1 = []
    for vrstica in matrika:
        vrstica = vrstica.split()
        vrstica = [int(x) for x in vrstica]
        matrika1.append(vrstica)
    matrika1 = Matrika(matrika1)
    print(matrika1.inverz())

def main():
    pozdrav()
    while True:
        meni()

main()
