from mhsTIF import *


def cariTerkecil(daftar):
    terkecil = daftar[0].uangSaku
    for i in daftar:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku
    return terkecil

print(cariTerkecil(Daftar))
