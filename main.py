import random

def pogodi_broj_od_korisnika():
    gornja_granica = 0
    donja_granica = 0
    rezultat = ''

    while True:
        donja_granica = int(input("Unesi donju granicu: "))
        gornja_granica = int(input("Unesi gornju granicu: "))
        if donja_granica >= gornja_granica:
            print("Gornja granica mora biti veca i razlicita od donje granice!")
            continue
        else:
            break

    print(f"Ok, sada zamisli broj od {donja_granica} do {gornja_granica}, a ja cu pokusati da pogodim taj broj.")

    while rezultat != 't':
        if donja_granica != gornja_granica:
            pokusaj = random.randint(donja_granica, gornja_granica)
        else:
            pokusaj = donja_granica
        rezultat = input(f"Da li je {pokusaj} previsoko (V), prenisko (N), ili je tacan (T)? ").lower()

        if rezultat == 'v':
            gornja_granica = pokusaj - 1
        elif rezultat == 'n':
            donja_granica = pokusaj + 1

    print(f"Uspeo sam! Pogodio sam tvoj broj. Zamislio si broj {pokusaj}.")

pogodi_broj_od_korisnika()