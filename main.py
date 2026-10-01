with open ("morcata.txt", encoding="utf-8") as soubor:
    for radek in soubor:
        radek = radek.strip()
        if not radek:
            continue

        casti = radek.split(";")
        if len(casti) != 5:
            continue

        jmeno = casti[0]
        hmotnost = casti[1]
        datum_narozeni = casti[2]
        cena = float(casti[3])
        pohlavi = casti[4]

        if pohlavi.lower() == "m":
            druh_pohlavi = "Sameček"
        else:
            druh_pohlavi = "Samička"

        cena_se_slevou = cena * 0.9

        print(f"{druh_pohlavi} morčete jménem: {jmeno}")
        print(f"- váží: {hmotnost} g")
        print(f"- datum narození: {datum_narozeni}")
        print(f"- cena : {cena} Kč, cena se slevou 10%: {cena_se_slevou:.1f} Kč")
        print("-" * 40)