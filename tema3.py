tabla = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

def afiseaza(tabla):
    nr_linii = len(tabla)
    nr_coloane = len(tabla[0])
    for i in range(nr_linii):
        for j in range(nr_coloane):
            print(tabla[i][j], end=" ")
        print()

def citeste_mutare(tabla, jucator):
    while True:
        print("Jucatorul", jucator, "- introduceti linia si coloana (0, 1, 2):")
        linie = int(input("Linie: "))
        coloana = int(input("Coloana: "))
        if linie < 0 or linie > 2 or coloana < 0 or coloana > 2:
            print("Coordonate invalide! Trebuie sa fie intre 0 si 2.")
            continue
        if tabla[linie][coloana] != '.':
            print("Pozitia nu este libera!")
            continue
        return linie, coloana

def stare_joc(tabla):
    for i in range(3):
        if tabla[i][0] == tabla[i][1] == tabla[i][2] != '.':
            return tabla[i][0]
    for j in range(3):
        if tabla[0][j] == tabla[1][j] == tabla[2][j] != '.':
            return tabla[0][j]
    if tabla[0][0] == tabla[1][1] == tabla[2][2] != '.':
        return tabla[0][0]
    if tabla[0][2] == tabla[1][1] == tabla[2][0] != '.':
        return tabla[0][2]
    for i in range(3):
        for j in range(3):
            if tabla[i][j] == '.':
                return "CONTINUA"
    return "EGAL"

jucator = 'X'

while True:
    afiseaza(tabla)
    linie, coloana = citeste_mutare(tabla, jucator)
    tabla[linie][coloana] = jucator
    stare = stare_joc(tabla)
    if stare != "CONTINUA":
        break
    if jucator == 'X':
        jucator = 'O'
    else:
        jucator = 'X'

afiseaza(tabla)
if stare == 'X':
    print("A castigat X!")
elif stare == 'O':
    print("A castigat O!")
else:
    print("Egalitate!")
