from abc import ABC, abstractmethod

# Abstraktne baasklass
class Mängija(ABC):
    def __init__(self, nimi: str, number: int):
        self.nimi = nimi
        self.number = number

    def liigub(self):
        print(f"{self.nimi} liigub väljakul.")

    @abstractmethod
    def lööb(self):
        pass


# Abstraktne vaheklass
class Kaitsja(Mängija):
    def blokeerib(self):
        print(f"{self.nimi} blokeerib palli!")


# Konkreetsed klassid
class Väravavaht(Mängija):
    def lööb(self):
        print(f"{self.nimi} lööb palli kaugele välja.")

    def tõrjub(self):
        print(f"{self.nimi} teeb hiilgava tõrje! ")


class Keskaitsja(Kaitsja):
    def lööb(self):
        print(f"{self.nimi} lööb pea või jalaga.")


class Keskaründaja(Mängija):
    def lööb(self):
        print(f"{self.nimi} lööb värava suunas! ")

    def sööb(self):
        print(f"{self.nimi} teeb täpse söödu.")


# Näiteprogramm
meeskond: list[Mängija] = [
    Väravavaht("Mart Poom", 1),
    Keskaitsja("Ragnar Klavan", 5),
    Keskaründaja("Henri Anier", 9),
]

for mängija in meeskond:
    mängija.liigub()
    mängija.lööb()

    if isinstance(mängija, Väravavaht):
        mängija.tõrjub()
    if isinstance(mängija, Kaitsja):
        mängija.blokeerib()
    if isinstance(mängija, Keskaründaja):
        mängija.sööb()

    print("---")