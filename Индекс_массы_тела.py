
print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Kirjuta sinu numi: ")
print(nimi, ", oi kui ilus nimi!")
a = float(input (nimi + " Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
if a == 1:
    pikkus=float(input("Kirjuta sinu pikkus: "))
    mass=float(input("Kirjuta sinu mass: "))
    indeks=round(mass / (0.01*pikkus)**2,1)
    print(nimi + (f"! Sinu keha indeks on: {indeks}"))
    if indeks<16:
        print("Tervisele ohtlik alakaal")
    elif indeks>16 and indeks<19:
        print("Alakaal")
    elif indeks>19 and indeks<25:
        print("Normaalkaal")
    elif indeks>25 and indeks<30:
        print("Ülekaal")
    elif indeks>30 and indeks<35:
        print("Rasvumine")
    elif indeks>35 and indeks<40:
        print("Tugev rasvumine")
    elif indeks>40:
        print("Tervisele ohtlik rasvumine")
    else:
        print("Kahju! See on väga kasulik info!")
        print()
        print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

else:
    print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
