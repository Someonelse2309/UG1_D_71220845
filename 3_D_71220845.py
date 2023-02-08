angka = int(input("Masukan Angka Anda\n>> "))
b = 0 
c = 0
d = -1
while b < angka :
        print (' '*(angka - d),'* '*(c))
        b = b + 1
        c = c + 1
        d = d + 1
b = 0 
c = 0
d = angka - 1
while b < angka:
    print (' '*(angka - d),'* '*(angka - c))
    b = b + 1
    c = c + 1
    d = d - 1