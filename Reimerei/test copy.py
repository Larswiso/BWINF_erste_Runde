vokale = ["a","e","i","o","u","ä","ö","ü"]
grundword = "Bieneeala"
vokale_wort = []

for index, buchstabe in enumerate(grundword):
    voks = ""
    if buchstabe in vokale:
        for ind, buc in enumerate(grundword[index:]):
            if buc in vokale:
                voks += buc
            else:
                break
        len_voks = len(voks)
        if len_voks >= 2:
            vokale_wort.append(voks)

print(vokale_wort)