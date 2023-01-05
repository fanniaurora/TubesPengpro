#Tugas A
def dealer_mobil(file_text):
    '''
    Fungsi ini untuk membuat list dengan elemen dictionary yang digunakan untuk menyimpan tipe mobil, warna, bahan bakar, dan stok

    Parameter:
    file_text (.txt): berisi beberapa baris data mobil yang menyatakan tipe, warna, jenis bahan bakar, dan stok  
    '''
    list_mobil = [] #membuat list kosong
    teks = file_text.read().splitlines() #untuk membaca file text dan dijadikan list
    
    #for loop digunakan untuk membuat dictionary yang berisi tipe mobil, warna, jenis bahan bakar, dan stok
    for i in teks:
        i = i.split("#") #membuat list dengan (#) sebagai pemisah
        dict_mobil = {} #membuat dictionary kosong
        dict_mobil["tipe mobil"] = i[0] 
        dict_mobil["warna"] = i[1]
        dict_mobil["jenis bahan bakar"] = i[2]
        dict_mobil["stok"] = int(i[3])
        list_mobil.append(dict_mobil) #untuk menambahkan dictionary ke dalam list 
    return list_mobil #untuk mengembalikan list mobil


#Tugas B
def stok_mobil(list_mobil):
    '''
    Fungsi ini untuk mengembalikan total mobil yang ada di dealer

    Parameter:
    list_mobil (list): list yang elemennya dictionary yang berisi stok mobil
    '''
    total_stok = 0 #sebagai stok awal

    #for loop digunakan untuk menghitung stok
    for i in list_mobil:
        total_stok = total_stok + i["stok"]
    return total_stok 


#Tugas C
def tampil_warna(list_mobil):
    '''
    Fungsi ini dibuat untuk menampilkan warna mobil yang tersedia di dealer

    Parameter:
    list_mobil (list): list yang elemennya dictionary yang berisi warna mobil
    '''
    list_warna = [] #membuat list kosong

    #for loop digunakan untuk mengetahui warna mobil yang tersedia
    for i in list_mobil:
        warna = i["warna"]

        #untuk memastikan bahwa tidak ada warna yang sama 
        if warna not in list_warna:
            list_warna.append(warna)
    warna = ', '.join(list_warna) #untuk menggabungkan list menjadi string
    print(warna) #untuk mencetak warna yang tersedia


#Tugas D
file_text = open("tubes.txt","r") #untuk membuka file
list_mobil = dealer_mobil(file_text) #pembuatan list mobil

print("Berikut adalah data mobil pada dealer:")
#for loop digunakan untuk mencetak dictionary
for i in list_mobil:
    print(i)

print()
print("Total mobil yang tersedia di dealer :", stok_mobil(list_mobil)) #mencetak stok mobil
print("Warna mobil yang tersedia di dealer :", end=" ")
tampil_warna(list_mobil) #menampilkan warna mobil
file_text.close() #menutup file text
