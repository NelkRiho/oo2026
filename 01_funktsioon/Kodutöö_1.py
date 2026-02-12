def arvuta_auto_kulu(kytuse_hind, kulu_100km, km_aastas, kindlustus_aastas):
    kytusekulu = (km_aastas / 100) * kulu_100km * kytuse_hind
    kogukulu = kytusekulu + kindlustus_aastas
    kulu_per_km = kogukulu / km_aastas
    return kytusekulu, kogukulu, kulu_per_km

kytuse_hind = float(input('Sisesta kütuse hind (€/l): '))
kulu_100km = float(input('Sisesta auto kütusekulu (l/100km): '))
km_aastas = int(input('Sisesta aastane läbisõit (km): '))
kindlustus = float(input('Sisesta kindlustuse hind (€/aastas): '))

kytusekulu, kogukulu, kulu_per_km = arvuta_auto_kulu(kytuse_hind, kulu_100km, km_aastas, kindlustus)

print("Kütusekulu aastas:", kytusekulu, "€")
print("Kogukulu aastas:", kogukulu, "€")
print("Kulu kilomeetri kohta:", kulu_per_km, "€")
