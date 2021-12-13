nilai_list = [1, 2, 3, 4, 5]
hasil_list = list(map(lambda i: i*12, nilai_list))
print(hasil_list)

#fungsi tambah

def tambah(x, y):
    return x+y
    
fungsi_2 = tambah(5,3)
print(fungsi_2)

#tambah

fungsi_2 = lambda x, y : x + y

print(fungsi_2(5,3))

#jumlah

def tambah(x):
    return x+1
    
fungsi_1 = tambah(5)
print(fungsi_1)

#jumlah

fungsi_1 = lambda x : x + 1

print(fungsi_1(5))

#Tambahkan 10 ke argumen a, dan kembalikan hasilnya.

x = lambda a: a + 10
print(x(5))

#Fungsi lambda dapat mengambil sejumlah argumen:

x = lambda a, b: a * b
print(x(5, 6))

#Fungsi lambda 

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))