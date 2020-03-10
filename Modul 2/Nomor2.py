from mahasiswa import Mahasiswa

mhs = Mahasiswa('Paiji', 07899, 'Jakarta', 300000)
# a
print(mhs.ambilKotaTinggal())
# b
mhs.perbaruiKotaTinggal('papua')
print(mhs.ambilKotaTinggal())
#c
print(mhs.ambilUangSaku())
mhs.tambahUangSaku(50000)
print(mhs.ambilUangSaku())
