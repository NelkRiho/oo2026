class Mangija:
    def __init__(self, nimi, number, positsioon, varavad=0, mangud=0):
        self.nimi = nimi
        self.number = number
        self.positsioon = positsioon
        self.varavad = varavad
        self.mangud = mangud

    # Värava löömine
    def loe_varav(self):
        self.varavad += 1
        print(f"{self.nimi} lõi värava! Kokku: {self.varavad}")

    # Mängu lisamine
    def loe_mang(self):
        self.mangud += 1
        print(f"{self.nimi} mängis mängu. Kokku mänge: {self.mangud}")

    # Väravate keskmine
    def keskmine_varav(self):
        if self.mangud == 0:
            return 0
        return round(self.varavad / self.mangud, 2)

    # Tutvustus
    def tutvustus(self):
        print(f"#{self.number} {self.nimi} - {self.positsioon}")

    # Kogu statistika
    def statistika(self):
        print(f"--- {self.nimi} ---")
        print(f"Positsioon: {self.positsioon}")
        print(f"Väravad: {self.varavad}")
        print(f"Mängud: {self.mangud}")
        print(f"Keskmine: {self.keskmine_varav()} väravat/mäng")

# FUNKTSIOONID
def lisa_mangija(nimi, number, positsioon):
    uus = Mangija(nimi, number, positsioon)
    meeskond.append(uus)
    print(f"{nimi} lisati meeskonda!")
    return uus

def eemalda_mangija(nimi):
    for m in meeskond:
        if m.nimi == nimi:
            meeskond.remove(m)
            print(f"{nimi} eemaldati meeskonnast!")
            return
    print(f"{nimi} ei leitud!")

def parim_varavalooaja():
    return max(meeskond, key=lambda m: m.varavad)


# EKSEMPLARIDE LOOMINE
bruno = Mangija("Bruno Fernandes", 8, "Poolkaitsja", 77, 200)
rasmus = Mangija("Rasmus Højlund", 11, "Ründaja", 26, 68)
marcus = Mangija("Marcus Rashford", 10, "Ründaja")

meeskond = [bruno, rasmus, marcus]

# TUTVUSTUS
bruno.tutvustus()
rasmus.tutvustus()
marcus.tutvustus()


# VÄRAVATE LÖÖMINE
marcus.loe_varav()
marcus.loe_varav()
marcus.loe_mang()
marcus.loe_mang()
marcus.loe_mang()

# STATISTIKA
bruno.statistika()
rasmus.statistika()
marcus.statistika()


# MEESKONNA KOONDSTATISTIKA
kokku_varavad = sum(m.varavad for m in meeskond)
print(f"Meeskonna väravad kokku: {kokku_varavad}")

parim = parim_varavalooaja()
print(f"Parim väravalööja: {parim.nimi} ({parim.varavad} väravat)")

# MÄNGIJA LISAMINE JA EEMALDAMINE
lisa_mangija("Harry Maguire", 5, "Kaitsja")
eemalda_mangija("Marcus Rashford")