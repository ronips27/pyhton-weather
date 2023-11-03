x = 485

sisaHari = ""

tahun = round(x / 360)
sisaHari = x % 360
print(tahun)
bulan = round(sisaHari / 30)
sisaHari = sisaHari % 30
print(bulan)
minggu = round(sisaHari / 7)
sisaHari = sisaHari % 7
print(minggu)
hari = sisaHari
print(hari)
