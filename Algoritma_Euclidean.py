# Teorema:
# Misalkan m dan n adalah dua bilangan bulat dengan syarat n > 0 sedemikian sehingga m = nq + r, dengan q dan r adalah bilangan bulat. Maka, PBB dari m dan n adalah sama dengan PBB dari n dan r.


# Algoritma Euclidean adalah alogritma untuk mencari PBB dari dua buah bilangan bulat
# 1. Jika n = 0, maka
#   m adalah PBB(m, n);
#    kelbalikan m;
#    Jika tidak, maka lanjut ke langkah 2
# 2. Bagilah m dengan n dan misalkan r adalah sisanya
# 3. Ganti nilai m dengan n dan nilai n dengan r, lalau ulangi kembali langkah 1


# Algoritma Euclidean dengan rekursif
def pbb(m, n):
    if n == 0:
        return m
    else:
        print(f"{m} = {n} * {m // n} + {m % n}")
        return pbb(n, m % n)
    
m = int(input("m: "))
n = int(input("n: "))

print(f"PBB dari {m} dan {n} adalah {pbb(m, n)}")