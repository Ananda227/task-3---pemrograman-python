#OUTPUT

print(1, 3, 5, 7)
#output : 1  3 5 7

print(1, 3, 5, 7, sep='*')
#output : 1*3*5*7

print(1, 3, 5, 7, sep='*', end='&')
#output : 1*3*5*7&

#INPUT 
# contoh 1 :
a = input("Masukkan Nilai A : ")
b = input("Masukkan Nilai B : ")

c = print(a,b)

#Bila kita menginput bilangan, misalnya integer lewat fungsi input(), maka hasil inputan
# tersebut adalah string dan bukan integer. Kita harus mengubahnya terlebih dahulu
# menjadi tipe integer menggunakan fungsi int().
#contoh 1:
a = int(input("masukkan nilai A : "))
b = int(input("masukkan nilai B : "))

c = a + b
print(c)

#contoh 2:
a = input("Masukkan angka A : ")
b = input("Masukkan angka B : ")

c = int(a) + int(b)
print(c)

#Kemudian ada juga float() untuk menginput bilangan pecahan.
#contoh : 
a = input("Masukkan angka A : ")
b = input("Masukkan angka B : ")

c = float(a) + float(b)
print(c)


#abs(). Dengan menggunakan fungsi abs() kita bisa hilangkan tipe data yang ada minusnya .
a = -5
c = abs(a)

print(c)

#pow(). Adalah fungsi untuk menghitung pangkat.
#contoh pow() statis :
c = pow(3,3)
print(c)

#contoh pow() dinamis
a = int(input("Masukkan Nilai : "))
b = int(input("Masukkan Nilai pangkat : "))

c = pow(a,b)
print(c)