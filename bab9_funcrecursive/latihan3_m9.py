# Latihan Rekursif faktorisasi

def jum(n):
    if (n == 0): # dimulai dari 0
        return 0 # dimulai dari 0
    elif (n == 1): # dimulai dari 1
        return 1 # dimulai dari 1
    else :
        return jum(n-1) + n

def fibo(n):
    if (n==1) or (n==2):
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

def fak(n):
    if (n==0) or (n==1):
        return 1
    else :
        return n*fak(n-1)

if __name__=="__main__":
    a = int(input("Masukan Nilai N = "))
    b = fibo(a)
    c = jum(a)
    d = fak(a)
    print()
    print("outputnya penjumlahan", c)
    print("fibonacinya adalah", b)
    print("ouput Faktorial dari",a, "adalah", d)
