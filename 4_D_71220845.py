ttl2 = 0
a = 0

def yagt(tgs,uts,uas):
    ttl = (((tgs*3)/10)+((uts*3)/10)+((uas*4)/10))
    return ttl


print("Alat Hitung Nilai")
while a < 2:
    print (f"---= Nilai Ke-{a+1} =---")
    tgs = int(input("Masukan Nilai Tugas >> "))
    uts = int(input("Masukan Nilai UTS >> "))
    uas = int(input("Masukan Nilai UAS >> "))
    a += 1
    ttl2 += (yagt(tgs,uts,uas))
    ttl3 = ttl2/2
print ("---= Total Nilai =---")
print ("Nilai yang didapat >> ",ttl3)
if ttl3 > 79:
    print ("Nilai Huruf >> A")
elif ttl3 > 59:
    print ("Nilai Huruf >> B")
elif ttl3 > 39:
    print ("Nilai Huruf >> C")
elif ttl3 > 19:
    print ("Nilai Huruf >> D")
else:
    print ("Nilai Huruf >> E")