# Exercițiu Python – Catalog de elevi
# Date inițiale
elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]
# Fiecare elev are o notă pe aceeași poziție.

# A1. Listează elevii cu notele lor
#   Folosește for și indici: afișează „Ana are nota 9” etc.
for i in range(len(elevi)):
    print(elevi[i], "are nota", note[i])
print()

# A2. Nota maximă și minimă
#   Determină și afișează valorile maxime/minime din note și numele elevilor corespunzători.
nota_max = max(note)
nota_min = min(note)
print("Nota maxima este", nota_max)
print("Nota minima este", nota_min)

for i in range(len(note)):
    if note[i] == nota_max:
        print("A luat nota maxima:", elevi[i])
    if note[i] == nota_min:
        print("A luat nota minima:", elevi[i])
print()

# A3. Media clasei
#   Calculează media aritmetică a notelor. Afișează cu două zecimale.
media = sum(note) / len(note)
print("Media clasei este", round(media, 2))
print()

# A4. Promovați
#   Afișează numele elevilor cu notă ≥ 5 (folosește if în interiorul unui for).
print("Elevii promovati:")
for i in range(len(note)):
    if note[i] >= 5:
        print(elevi[i])
print()

# B5. +1 punct fiecărei note (max 10)
#   Parcurge note cu for pe indici și crește fiecare notă cu 1.
for i in range(len(note)):
    if note[i] < 10:
        note[i] = note[i] + 1
print(note)
print()

# B6. Adaugă elevul predefinit
#   Adaugă elev_nou și nota_elev_nou la finalul listelor (append) și afișează listele actualizate.
elevi.append(elev_nou)
note.append(nota_elev_nou)
print(elevi)
print(note)
print()

# B7. Șterge elevul predefinit
#   Găsește poziția lui elev_de_sters în elevi (dacă există) și elimină-l pe el și nota corespunzătoare.
if elev_de_sters in elevi:
    poz = elevi.index(elev_de_sters)
    elevi.pop(poz)
    note.pop(poz)
print(elevi)
print(note)
print()

# B8. Afișează din nou lista
#   Listează perechile elev–notă după actualizări.
for i in range(len(elevi)):
    print(elevi[i], "are nota", note[i])
print()

# C9. Căutări de nume cu while
#   Folosește while pentru a procesa elementele din interogari_nume în ordine. Oprește-te când elementul curent este "stop". Pentru fiecare nume (altul decât "stop"), dacă se găsește în elevi, afișează nota; altfel, afișează un mesaj că nu există.
print("Căutări de nume:")
i = 0
while i < len(interogari_nume):
    nume = interogari_nume[i]
    if nume == "stop":
        break
    if nume in elevi:
        poz = elevi.index(nume)
        print(nume, "are nota", note[poz])
    else:
        print(nume, "nu exista in catalog")
    i = i + 1
print()

# C10. Număr promovați / respinși
#   Numără câți au notă ≥ 5 și câți au < 5 și afișează rezultatul.
promovati = 0
respinsi = 0
for n in note:
    if n >= 5:
        promovati = promovati + 1
    else:
        respinsi = respinsi + 1
print("Promovati:", promovati)
print("Respinsi:", respinsi)
print()

# C11. Media promovaților
#   Construiește o listă cu notele ≥ 5 și calculează media acesteia (tratare corectă a cazului listei goale).
note_promovati = []
for n in note:
    if n >= 5:
        note_promovati.append(n)
if len(note_promovati) > 0:
    media_promovati = sum(note_promovati) / len(note_promovati)
    print("Media promovati:", round(media_promovati, 2))
else:
    print("Nu exista promovati.")

#   Rezultate cerute
#   - Lista elevilor cu notele (inițiale și după B8).
#   - Nota maximă/minimă și media clasei.
#   - Elevii promovați.
#   - După actualizare: adăugarea lui Felix, ștergerea lui Darius (dacă există), liste corecte.
#   - Răspunsuri la căutări (Ana, Mara, Elena) până la „stop”.
#   - Număr promovați/respinși și media promovaților.
