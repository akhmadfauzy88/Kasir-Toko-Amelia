import MySQLdb
import sys
import os

def tambah():
    #Clear screen
    os.system("cls")
    #Koneksi ke database
    db = MySQLdb.connect("127.0.0.1","root","","kasir")
    cursor = db.cursor()
    #Input data barang
    print("Tambah Barang")
    id = int(input("Masukan ID barang : "))
    nama = input("Masukan Nama barang : ")
    harga = int(input("Masukan Harga barang : "))
    #Query SQL
    sql = "insert into barang values ('%d', '%s', '%d')" % \
    (id, nama, harga)
    #Eksekusi Query
    try:
        cursor.execute(sql)
        db.commit()
        print("Data berhasil disimpan ...")
    except:
        db.rollback()
        print("Error ...")
    #Menutup koneksi
    db.close()

def tranksasi():
    print("Tranksasi")
    while True:
        pass

def main():
    while True:
        os.system("cls")
        print("Amelia Store")
        print("============")
        print("Menu")
        print("1. Tambah Barang")
        print("2. Tranksasi")
        print("3. Exit")

        try:
            pilihan = int(input("Masukan Pilihan : "))
            print("")
            if(pilihan==1) : tambah()
            elif(pilihan==2) : tranksasi()
            elif(pilihan==3) : break
            else : print("Pilihan tidak tersedia")
        except:
            print("Pilihan tidak tersedia")

        print("")
        pause = input("Tekan sembarang..")
        print("")

if(__name__=="__main__"): main()
