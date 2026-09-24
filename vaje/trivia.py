import requests
import random
import html
vpr = int(input("Koliko vprašanj želiš? "))
url = f"https://opentdb.com/api.php?amount={vpr}"
klic = requests.get(url).json()
vprasanja = klic["results"]

for vprasanje in  vprasanja:
    odgovori = vprasanje["incorrect_answers"]
    odgovori.append(vprasanje["correct_answer"])
    random.shuffle(odgovori)
    print(vprasanje["question"])
    for i, odgovor in enumerate(odgovori):
        print(i+1, odgovor)
    odgovor=int(input("odgovor: "))
    if odgovori[odgovor-1] == vprasanje["correct_answer"]:
        print("correct")