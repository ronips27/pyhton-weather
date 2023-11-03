listBuah = [
    {
        'nama': 'Apel',
        'stock': 20,
        'harga': 10000 
    },
    {
        'nama': 'Jeruk',
        'stock': 15,
        'harga': 15000
    },
    {
        'nama': 'Angur',
        'stock': 25,
        'harga': 20000
    }
]

cart = []

def menampilkanDaftarBuah() :
    print('Daftar Buah \n')
    print('Index\t| nama \t| Stok \t| Harga ')
    for i in range(len(listBuah)) :
        print('{}\t| {}\t| {}\t| {}'.format(i,listBuah[i]['nama'], listBuah[i]['stock'],listBuah[i]['harga']))


def menambahBuah() :
    namaBuah = input('Masukkan Nama Buah : ')
    stockBuah = int(input('Masukkan Stock Buah : '))
    hargaBuah = int(input('Masukkan Harga Buah : '))
    listBuah.append({
        'nama' : namaBuah, 
        'stock' : stockBuah, 
        'harga' : hargaBuah
    })
    menampilkanDaftarBuah()

def menghapusBuah():
    menampilkanDaftarBuah()
    indexBuah = int(input('Masukkan index buah yang ingin dihapus : '))
    del listBuah[indexBuah]
    menampilkanDaftarBuah()

def membeliBuah():
    menampilkanDaftarBuah()
    while True :
            indexBuah =  int(input('Masukkan index Buah yang dibeli : '))
            qtyBuah = int(input('Masukkan jumlah yang ingin dibeli : '))
            if(qtyBuah > listBuah[indexBuah]['stock']) :
                print('Stock tidak cukup, stock {} tinggal {}'. format(listBuah[indexBuah]['nama'], listBuah[indexBuah]['stock']))
            else :
                cart.append({
                    'nama': listBuah[indexBuah]['nama'], 
                    'qty': qtyBuah, 
                    'harga': listBuah[indexBuah]['harga'], 
                    'index': indexBuah
                })
            print('Isi Cart :')
            print('Nama\t| Qty\t| Harga')
            for item in cart :
                print(' {}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga']))
            checker = input('Mau beli yang lain? (ya / tidak) = ')
            if( checker == 'tidak') :
                break

            print('Daftar Belanja :')
            print('Nama\t| Qty\t| Harga\t| Total Harga')
            totalHarga = 0
            for item in cart :
                print(' {}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga']))
                totalHarga += item['qty'] * item['harga']
            while True:
                print('Total Yang Harus dibayar = {}'.format(totalHarga))
                jmlUang = int(input('Masukkan jumlah uang : '))
                if(jmlUang > totalHarga) :
                    kembali = jmlUang - totalHarga
                    print('Terima kasih \n\nUang Kembali anda : {}'.format(kembali))
                    for item in cart :
                        listBuah[item['index']]['stock'] -= item['qty']
                    cart.clear()
                    break
                elif(jmlUang == totalHarga) :
                    print('Terima Kasih')
                    for item in cart :
                        listBuah[item['index']]['stock'] -= item['qty']
                    cart.clear()
                    break
                else :
                    kekurangan =  totalHarga - jmlUang
                    print('Uang anda kurang sebesar {}'.format(kekurangan))

while True:
    pilihanMenu = input(''' 
        Selamat Datang di Pasar Buah
        
        List Menu :
        1. Menampilkan Daftar Buah
        2. Menambah Buah
        3. Menghapus Buah
        4. Membeli Buah
        5. Exit Program
        
        Masukkan angka yang ingin dijalankan : ''')
    
    if(pilihanMenu == '1'):
        menampilkanDaftarBuah()
    elif(pilihanMenu == '2'):
        menambahBuah()
    elif(pilihanMenu == '3') :
        menghapusBuah()
    elif(pilihanMenu == '4') :
        membeliBuah()
    elif(pilihanMenu == '5') :
        break