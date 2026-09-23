import requests
import pprint from pprint
import random
import html
vpr = int(input("Koliko vprašanj želiš? "))
url = f"https://opentdb.com/api.php?amount={vpr}"
klic = requests.get(url).json()
vprasanje = klic["result"]
score  = 0
for v in vprasanje():
    prav = v["correct_answer"]
    odgovori = v["incorrect_answer"] + [prav]