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
    cursor.execute("select count(id) from barang")
    results = cursor.fetchall()
    for row in results:
        data = row[0]
    print("ID barang terakhir :",data)
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
    #Clear screen
    os.system("cls")
    #Koneksi ke database
    db = MySQLdb.connect("127.0.0.1","root","","kasir")
    cursor = db.cursor()
    #Input data barang
    print("Tranksasi")
    while True:
        inisial = input("Masukan nama barang : ")
        sql = "select id, nama from barang where nama like '%s'" % \
                ("%"+inisial+"%")
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            nama = row[1]
            print("")
            print("ID :",id)
            print("Nama :",nama)
            print("")

        id = int(input("Masukan id barang : "))
        jumlah = int(input("Masukan jumlah barang : "))
        sql = "insert into chart values (curdate(), '%d', (select nama from barang where id='%d'), (select harga from barang where id='%d'), '%d')" % \
        (id, id, id, jumlah)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        os.system("cls")
        print("Keranjang Belanja")
        sql = "select * from chart"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                tanggal = row[0]
                id = row[1]
                nama = row[2]
                harga = row[3]
                jumlah = row[4]
                print("")
                print("ID Barang :", id)
                print("Nama Barang :", nama)
                print("Harga :", harga)
                print("jumlah :", jumlah)
                print("")
        except:
                print("error ...")

        sql = "select sum(harga*jumlah) from chart"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                total = row[0]
                print("Total biaya : ",total)
        except:
            print("Error")

        pilihan = int(input("1. Tambah barang / 2. Bayar : "))
        if(pilihan==1): print("")
        else: break

    os.system("cls")
    print("Detail Transaksi")
    sql = "select * from chart"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print("=============================================================")
        for row in results:
            tanggal = row[0]
            id = row[1]
            nama = row[2]
            harga = row[3]
            jumlah = row[4]
            print("ID Barang :", id)
            print("Nama Barang :", nama)
            print("Harga :", harga)
            print("jumlah :", jumlah)
            print("")
        print("=============================================================")
    except:
            print("error ...")

    sql = "select sum(harga*jumlah) from chart"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            total = row[0]
            print("Total biaya : ",total)
        print("=============================================================")
    except:
        print("Error")
    bayar = int(input("Masukan besaran mata uang : "))
    kembalian = bayar - total
    print("kembalian anda :",kembalian)
    cursor.execute("truncate table chart")

def main():
    os.system("Title Amelia Store")
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
