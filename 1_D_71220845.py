ulg = 0
total = 0
while ulg == 0: 
    harga = int(input("Berapa Harga Barang?\n >> "))
    total += harga
    ulang1 = str(input("Apakah Anda Mau Memasukan Item? [Y/N]\n>> "))
    ulang = ulang1.lower()
    if ulang == 'y':
        ulg = 0
    elif ulang == 'n':
        print ("Total Harga Barang \n>> ",total)
        ulg = 1
    else:
        print ("Invalid Input")
        ulg = 1
        