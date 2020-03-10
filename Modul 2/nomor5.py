from mahasiswa import Mahasiswa

mhs9 = Mahasiswa('Fikri', 166, 'Bekasi', 10000000)
mhs9.ambilKuliah('Hacking')
mhs9.ambilKuliah('DEFACE WEBSITE')
mhs9.ambilKuliah('Networking')
print(mhs9.listKuliah)
mhs9.hapusKuliah('Hacking')
print(mhs9.listKuliah)
