text = "    Un incendiu care a izbucnit luni dimineaţa într-un bloc de zece etaje din din Lyon, al treilea cel mai mare oraş din Franţa, a provocat moartea a patru persoane, a anunţat prefectura Rhône într-un comunicat citat de presa franceză. Cele patru persoane au murit în ciuda intervenţiei echipelor de salvare, iar zece persoane sunt în prezent examinate medical, se precizează în comunicat."

lungime = len(text)
jumatate = lungime // 2
half1 = text[:jumatate]
half2 = text[jumatate:]

half1 = half1.upper()
half1 = half1.strip()

half2 = half2[::-1]

half2 = half2.capitalize()

for punctuatie in ".,!?":
    half2 = half2.replace(punctuatie,"")

print(half1 + half2)