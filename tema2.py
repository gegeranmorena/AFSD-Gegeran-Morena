elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9, 7, 10, 4, 8]

elev_nou = "Felix"
nota_elev_nou = 6
elev_de_sters = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]
absente = [1, 0, 2, 3, 0]

for i in range(len(elevi)):
    print(elevi[i], "are nota", note[i])

max_nota = note[0]
min_nota = note[0]
for i in range(1, len(note)):
    if note[i] > max_nota:
        max_nota = note[i]
    if note[i] < min_nota:
        min_nota = note[i]

nume_max = []
nume_min = []
for i in range(len(elevi)):
    if note[i] == max_nota:
        nume_max.append(elevi[i])
    if note[i] == min_nota:
        nume_min.append(elevi[i])

print("Nota maxima este", max_nota, " elevi:", ", ".join(nume_max))
print("Nota minima este", min_nota, " elevi:", ", ".join(nume_min))

suma_note = 0
for i in range(len(note)):
    suma_note += note[i]
media = suma_note / len(note)
print("Media clasei este: {:.2f}".format(media))

for i in range(len(elevi)):
    if note[i] >= 5:
        print(elevi[i])

for i in range(len(note)):
    note[i] = note[i] + 1
    if note[i] > 10:
        note[i] = 10

elevi.append(elev_nou)
note.append(nota_elev_nou)
print("elevi:", elevi)
print("note:", note)

pozitie_sters = -1
for i in range(len(elevi)):
    if elevi[i] == elev_de_sters:
        pozitie_sters = i
        break
if pozitie_sters != -1:
    del elevi[pozitie_sters]
    del note[pozitie_sters]

for i in range(len(elevi)):
    print(elevi[i], "are nota", note[i])

idx = 0
while idx < len(interogari_nume):
    nume = interogari_nume[idx]
    if nume == "stop":
        break
    poz = -1
    for i in range(len(elevi)):
        if elevi[i] == nume:
            poz = i
            break
    if poz != -1:
        print(nume, "are nota", note[poz])
    else:
        print(nume, "nu exista in catalog")
    idx += 1

promovati = 0
respinsi = 0
for i in range(len(note)):
    if note[i] >= 5:
        promovati += 1
    else:
        respinsi += 1
print("Promovati:", promovati, " Respinsi:", respinsi)

suma_prom = 0
cnt_prom = 0
for i in range(len(note)):
    if note[i] >= 5:
        suma_prom += note[i]
        cnt_prom += 1
if cnt_prom > 0:
    media_prom = suma_prom / cnt_prom
    print("Media promovatilor este: {:.2f}".format(media_prom))
else:
    print("Nu exista promovati")
