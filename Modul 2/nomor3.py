from mahasiswa import Mahasiswa

print('Program untuk memasukan mahasiswa baru')
nama = input('Masukan Nama: ')
NIM = int(input('Masukan NIM: '))
kota = input('Masukan Kota: ')
uangSaku = int(input('Masukan uang saku: '))

mhs = Mahasiswa(nama, NIM, kota, uangSaku)
print('\n Terima Kasih Anda telah menginputkan data Mahasiswa, sebagai berikut: \n')
print(mhs)
