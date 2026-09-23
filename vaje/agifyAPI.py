import requests
# agify API
# najdi najstarejše imen iz seznama
imena = ["Bine", "Luka"]
najstarejši = 0
for i in imena:
    url = f"https://api.agify.io/?name={i}"
    call=requests.get(url).json()
    st=call["age"]
    if st > najstarejši:
        najstarejši=st
        ime=i
print(ime, najstarejši)