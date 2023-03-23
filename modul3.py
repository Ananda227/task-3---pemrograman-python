#====================================================
#                      Tuple
#====================================================

#-------------------Membuat Tuple--------------------

#tuple kosong 
tuple1 = ()
print(tuple1)
#output : ()

#tuple 1 element
tuple1 = (1, )
print(tuple1)
#output : (1,)

#tuple 1 element
tuple1 = (1, )
print(tuple1)
#output : (1,)

#tuple berisi integer
tuple1 = (1,2,3)
print(tuple1)
#output : (1, 2, 3)

#tuple bersarang
tuple1 = ("hello", [1,2,3], (4,5,6))
print(tuple1)
#output : ('hello', [1, 2, 3], (4, 5, 6))

#tuple bisa juga tidak menggunakan tanda () berisi integer
tuple1 = 1,2,3
print(tuple1)
#output : (1, 2, 3)

#memasukkan anggota tuple ke variabel
a,b,c = tuple1
print(a,b,c)
#output : 1 2 3
#----------------------------------------------------
#---------------Mengakses Anggota Tuple--------------

tuple2 = ('p','y','t','h','o','n')
print(tuple2[0])
#output : p

print(tuple2[1])
#output : y

print(tuple2[-1])
#output : n

print(tuple2[-2])
#output : o

#index eror
# print(tuple2[6])

#___mengakses tuple dengan range___
print(tuple2[:3])
#output : ('p', 'y', 't')

print(tuple2[2:5])
#output :('t', 'h', 'o')

print(tuple2[2:])
#output : ('t', 'h', 'o', 'n')
#----------------------------------------------------
#---------------Mengubah Anggota Tuple---------------

# Setelah tuple dibuat, maka anggota tuple tidak bisa lagi diubah atau dihapus. Akan
# tetapi, bila anggota tuple-nya adalah tuple bersarang dengan anggota seperti list, maka
# item pada list tersebut dapat diubah.

tuple3 = (2,3,4,[5,6]) #hanya list "[]" didalam tuple yang dapat diubah

tuple3[3][0] = 7
print(tuple3)
#output : (2, 3, 4, [7, 6])

#tuple bisa diganti dengan penugasan kembali
tuple3 = ('p','y','t','h','o','n')
print(tuple3)
#output : ('p', 'y', 't', 'h', 'o', 'n')

#anggota tuple tidak bisa dihapus satu satu menggunakan del(),
# hanya bisa dihapus secara keseluruhan
del tuple3
# print(tuple3) => akan eror karena tuple3 sudah dihapus
#----------------------------------------------------
#---------------Menguji Anggota Tuple----------------

# Seperti halnya string dan list, kita bisa menguji apakah sebuah objek adalah anggota
# dari tuple atau tidak, yaitu dengan menggunakan operator in atau not in untuk
# kebalikannya.

tuple1 = (1, 2, 3, 'a', 'b', 'c')

#menggunakan in
print(3 in tuple1)
#output : True

print('3' in tuple1)
#output : False

print('c' in tuple1)
#output : True

#menggunakan not in
print('l' not in tuple1)
#output : True
#----------------------------------------------------
#------------------Iterasi pada Tuple----------------

#Kita bisa menggunakan for untuk melakukan iterasi pada tiap anggota dalam tuple.