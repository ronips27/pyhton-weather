def ganjilGenap(angka):
    if (angka % 2 == 0):
        return 'Genap'
    else :
        return 'Ganjil'

def ubahJadiGG(listAngka):
    return list(map(ganjilGenap, listAngka))

list1 = [1,2,3,5,6,7,7,8,]

list1 = ubahJadiGG(list1)

print(list1)

def filterGaji(listGaji) :
    return list(filter(lambda gaji : gaji * 95/100 > 9000000, listGaji))

list2 = [9100000, 9800000, 9500000, 10300000, 9300000]

list2 = filterGaji(list2)

print(list2)