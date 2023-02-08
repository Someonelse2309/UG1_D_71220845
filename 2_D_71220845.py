kal = str(input("Masukan Kalimat Anda\n>> "))
kat = str(input("Kata Yang Ingin Dicari\n>> "))
kal1 = kal.lower()
kat1 = kal1.count(kat)
if kat1 == 0:
    print("Maaf Tidak Ada Kata Yang Dicari")
else:
    print (kat1)
