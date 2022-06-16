import os
from re import M
#Mode w = write mode / mode menulis dan menghapus file lama , Jika file tidak ada maka akan akan dibuat file baru 
#Mode r = read mode only / hanya bisa membaca 
#Mode a = appending mode / menambahkan data di akhir baris 
#Mode r+ = write and read mode 
def menambah(): 
    #INPUTAN MENAMBAH DATA
    print("=============== CATATAN PENTING =========================================================")
    print(""" 
        1.Apabila ingin menambah data lebih dari 1 kata gunakan spasi 
        2.Setiap Awalan Kata Gunakan Huruf Kapital, Contoh: [Faiz Amsyari]
        3.Saat menginput divisi harus menggunakan huruf besar semua, Contoh: [PSDM] 
    """)
    print("========================================================================================")
    print("")
    nama = str(input("Masukkan Nama Pendaftar: "))
    umur = int(input("Masukkan Umur Pendaftar: "))
    jurusan = str(input("Masukkan Jurusan Pendaftar: "))
    divisi = str(input("Masukkan Divisi Yang Dipilih: "))
    nilai = float(input("Masukkan Penilaian Peserta: "))
    konversi = divisi.upper()
    konversijurusan = jurusan.title()
    konversinama = nama.title()
    ini = open("panitia.txt", "r")
    for nana in ini:
        itu = nana.split("||")
        if itu [4] == konversinama :
            print("MOHON MAAF NAMA YANG DIINPUT TELAH ADA")
            ini.close()
            pilihan = int(input("""
                Ketik 1 jika ingin mecoba menambah data lagi
                Ketik 2 untuk kembali ke menu 
                Ketik 3 untuk keluar program
            """))
            if pilihan == 1:
                file = open("panitia.txt","r")
                file.close()
                menambah()
            elif pilihan == 2:
                awalan()
            elif pilihan == 3:
                exit()
    if nilai > 90.0:
        status = "LULUS"
        file = open("panitia.txt",'a')
        file.writelines(["==="+"||" + konversi + "||" + str(umur)  + "||" + konversijurusan  + "||"+ konversinama + "||" + str(nilai) +"||" + status + "||" "==="+"\n"])
        file.close()
        print("Selamat Data Telah Ditambahkan")
    else:
        status = "TIDAK LULUS"
        file = open("panitia.txt",'a')
        file.writelines(["==="+"||" + konversi + "||" + str(umur)  + "||" + konversijurusan  + "||"+ konversinama + "||" + str(nilai) +"||" + status + "||" "==="+"\n"])
        file.close()
        print(type(nama))
        print("Selamat Data Telah Ditambahkan")
    #=======================================================================
    pindah = int(input("""Apakah Anda Ingin Melakukan Hal Lain?
            Ketik 1 Untuk Menambahkan Data Pendafar Lagi 
            Ketik 2 Untuk Kembali Ke Menu
            Ketik 3 Untuk Keluar Program 
        """))
    if pindah == 1:
        file = open("panitia.txt","r")
        file.close()
        menambah()
    elif pindah == 2:
        awalan()
    elif pindah == 3:
        print("Sampai Jumpa Kembali")
        exit()

def melihat():
    print("SELAMAT MELIHAT DATA KESELURUHAN")
    file = open("panitia.txt","a")
    file = open("panitia.txt","r")
    membaca = file.readlines()
    membaca.sort()
    patokan = 0 
    if len (membaca) == 0:
        print ("MOHON MAAF DATA MASIH KOSONG")
        awalan()
    else:
        for ninu in membaca:
            pecah = ninu.split ("||")
            #    print(membaca)
            #    print(pecah)
            print ("\n")
            print("=================DATA Ke: " + str(patokan + 1) + " Setelah Diurutkan Berdasarkan Divisi============================")
            print("Nama Pendaftar:" + pecah[4])
            print("Umur:" + pecah[2])
            print("Jurusan:" + pecah[3])
            print("Divisi Yang Dipilih:" + pecah[1])
            print("Nilai Tes:" + pecah[5])
            print("Status Pendaftar:" + pecah [6])
            print("============================================================================================================")
            patokan +=1
            file.close()
        pindah = int(input("""Apakah Anda Ingin Melakukan Hal Lain?
                    Ketik 1 Untuk Melihat Data Lagi 
                    Ketik 2 Untuk Kembali Ke Menu
                    Ketik 3 Untuk Keluar Program 
                """))
        if pindah == 1:
            file = open("panitia.txt","r")
            file.close()
            melihat()
        elif pindah == 2:
            file = open("panitia.txt","r")
            file.close()
            awalan()
        elif pindah == 3:
            print("Sampai Jumpa Kembali")
            exit()

def hapus():
    print("Pastikan Spasi Dan Tanda Baca Benar")
    hapus_pendaftar = str(input("Masukkan Nama Pendaftar: "))
    hapus_umur = str(input("Masukkan Umur Pendaftar: "))
    hapus_pendaftar_baru = hapus_pendaftar.title()
    file = open("panitia.txt","r+")
    # file2 = open("sementara.txt","a")
    menghapus = file.readlines()
    awal = 0
    for ninu in menghapus:
       pecah = ninu.split ("||")
       if pecah [2] == hapus_umur and pecah [4] == hapus_pendaftar_baru:
           del(menghapus[awal]) 
           print("Data Pendaftar Telah Dihapus")
        #    file2.writelines(menghapus)
        #    file2.close()
           file = open("panitia.txt","w")
           file.writelines(menghapus)
           file.close()
        #    os.remove("panitia.txt")
        #    os.rename("sementara.txt","panitia.txt")
           break
       awal += 1
    else:
        print("======MOHON MAAF DATA TIDAK DITEMUKAN=====")
    pindah = int(input("""Apakah Anda Ingin Melakukan Hal Lain?
            Ketik 1 Untuk Menghapus Data Lagi 
            Ketik 2 Untuk Kembali Ke Menu
            Ketik 3 Untuk Keluar Program 
        """))
    if pindah == 1:
        file = open("panitia.txt","r")
        file.close()
        hapus()
    elif pindah == 2:
        awalan()
    elif pindah == 3:
        print("Sampai Jumpa Kembali")
        exit()

def cari():
    file = open("panitia.txt" , "r") 
    mencari = file.readlines()
    patokan = 0
    print("""
        Pilih Salah Satu :
          1.Mencari data secara detail
          2.Mencari data berdasarkan status 
    """)
    pilihan = int(input("Masukkan Pilihan Anda:"))
    if pilihan  ==  1:
        hapus_pendaftar = str(input("Masukkan Nama Pendaftar Yang Ingin Dicari: "))
        inikonversi = hapus_pendaftar.title()
        jumlah = 0
        for ninu in mencari:
            pecah = ninu.split ("||")
            untukmu = pecah[4]
            if inikonversi in untukmu:
                print("")
                print("DATA TERKAIT " + inikonversi + " DITEMUKAN PADA URUTAN KE- " + str(patokan + 1))
                print ("Nama Pendaftar: " + pecah[4])
                print ("Umur: " + pecah[2])
                print ("Jurusan: " + pecah[3])
                print ("Divisi Yang Dipilih: " + pecah[1])
                print ("Nilai tes: " + pecah[5])
                print ("Status Pendaftar: " + pecah[6])
                file.close()
                jumlah +=1
            patokan +=1
        
        patokan = 0
        for nana in mencari:
            pecah = nana.split("||")
            inikonversa=inikonversi
            inikonversa = inikonversi.lower()
            halu = pecah [4]
            if inikonversa in halu:
                print("")
                print("DATA TERKAIT " + inikonversa + " DITEMUKAN PADA URUTAN KE- " + str(patokan + 1))
                print ("Nama Pendaftar: " + pecah[4])
                print ("Umur: " + pecah[2])
                print ("Jurusan: " + pecah[3])
                print ("Divisi Yang Dipilih: " + pecah[1])
                print ("Nilai tes: " + pecah[5])
                print ("Status Pendaftar: " + pecah[6])
                file.close()
                jumlah +=1
            patokan +=1

        if jumlah == 0:
            print("MOHON MAAF DATA YANG DICARI TIDAK DITEMUKAN")
    elif pilihan == 2:
        print("""Ketikkan 
                    1.LULUS
                    2.TIDAK LULUS
        """)
        pilihan2 = int(input("Masukkan Status Yang Anda Ingin Cari: "))
        if pilihan2 == 1:
            jumlah = 0
            for lala in mencari:
                pecah = lala.split ("||")
                if pecah[6] == "LULUS":
                    print("================================================================================================")
                    print("Selamat Data Yang Dicari Telah Ditemukan")
                    print("==================== DATA PESERTA LULUS URUTAN KE- " + str(patokan + 1) +  " DIDALAM FILE TEXT===")
                    print("Nama Pendaftar: " + pecah[4])
                    print("Umur: " + pecah[2])
                    print("Jurusan: " + pecah[3])
                    print("Divisi Yang Dipilih:" + pecah[1])
                    print("Nilai Tes: " + pecah[5])
                    print("Status Pendaftar: " + pecah[6])
                    print("======================================================================================================")
                    # print("DATA INI BERADA PADA URUTAN KE - " + patokan + "PADA FILE PENYIMPANAN")
                    jumlah +=1
                patokan+=1
            file.close()
            print("")
            print("Jumlah Data Peserta Lulus Saat Ini: " , jumlah )
            print("")
            print("========================================================================================================")
            print("Jumlah Data Peserta Lulus Saat Ini: " , jumlah )
        elif pilihan2 == 2:
            jumlah = 0
            for lulu in mencari:
                pecah = lulu.split ("||")
                if pecah[6] == "TIDAK LULUS":
                    print("================================================================================================")
                    print("Selamat Data Yang Dicari Telah Ditemukan")
                    print("============== DATA PESERTA TIDAK LULUS URUTAN KE- " + str(patokan + 1) + " DIDALAM FILE TEXT===")
                    print("Nama Pendaftar: " + pecah[4])
                    print("Umur: " + pecah[2])
                    print("Jurusan: " + pecah[3])
                    print("Divisi Yang Dipilih:" + pecah[1])
                    print("Nilai Tes: " + pecah[5])
                    print("Status Pendaftar: " + pecah[6])
                    print("=========================================================================================================")
                    # print("DATA INI BERADA PADA URUTAN KE - " + patokan + "PADA FILE PENYIMPANAN")
                    jumlah+=1
                patokan +=1
            file.close()
            print("")
            print("Jumlah Data Peserta Tidak Lulus Saat Ini: " , jumlah )
            print("")
            print("========================================================================================================")
    # print("================MOHON MAAF DATA TIDAK DITEMUKAN=========================")
    pindah = int(input("""Apakah Anda Ingin Melakukan Hal Lain?
            Ketik 1 Untuk Mencari Data Lagi 
            Ketik 2 Untuk Kembali Ke Menu
            Ketik 3 Untuk Keluar Program 
        """))
    if pindah == 1:
        file = open("panitia.txt","r")
        file.close()
        cari()
    elif pindah == 2:
        file = open("panitia.txt","r")
        file.close()
        awalan()
    elif pindah == 3:
        print("Sampai Jumpa Kembali")
        exit()

def rubah():
    print("************************************************************************")
    print("SELAMAT MELAKUKAN PERUBAHAN DATA PASTIKAN DATA YANG INGIN DIRUBAH BENAR")
    print("**********************************************************************")
    nama = str(input("Masukkan Nama Pendaftar: "))
    jurusan = str(input("Masukkan Jurusan Pendaftar: "))
    file = open("panitia.txt","r") 
    # file2 = open("sementara.txt","a")
    namakonversi = nama.title()
    jurusankonversi = jurusan.title()
    merubah = file.readlines()
    patokan = 0
    for ninu in merubah:
        pecah = ninu.split ("||")
    #Index 2 adalah tanggal, Index 4 adalah bulan dan Index 6 adalah tahun
        if pecah [4] == namakonversi and pecah [3] == jurusankonversi:
            nama_baru = str(input("Masukkan Nama Baru:"))
            umur_baru = int(input("Masukkan Umur Baru:"))
            jurusan_baru = str(input("Masukkan Jurusan Baru:"))
            divisi_baru = str(input("Masukkan Divisi Baru:"))
            nilai_baru = float(input("Masukkan Nilai Baru:"))
            nama_baru_konversi = nama_baru.title()
            jurusan_baru_konversi = jurusan_baru.title()
            divisi_baru_konversi = divisi_baru.upper()
            for nana in merubah:
                kunci = 0
                itu = nana.split("||")
                if itu [4] == nama_baru_konversi :
                    print("MOHON MAAF NAMA YANG DIINPUT TELAH ADA")
                    file.close()
                    ini = int(input("Masukkan:"))
                    if ini == 1:
                        file = open("panitia.txt","r")
                        file.close()
                        rubah()
                    else:
                        file = open("panitia.txt","r")
                        file.close()
                        awalan()
                kunci+=1
            if nilai_baru > 90.0:
                status_baru = "LULUS"
                merubah[patokan] = "==="+"||" + divisi_baru_konversi + "||" + str(umur_baru)  + "||" + jurusan_baru_konversi  + "||"+ nama_baru_konversi + "||" + str(nilai_baru) +"||" + status_baru + "||" "==="+"\n"
                # file2.writelines(merubah)
                # file2.close()
                print("*SELAMAT DATA TELAH BERHASIL DIRUBAH*")
                print("")
                print("=====================DATA SEBELUM DIRUBAH===================================")
                print("Nama Pendaftar Sebelum Dirubah: " + pecah[4])
                print("Nama Pendaftar:" + pecah[4])
                print("Umur:" + pecah[2])
                print("Jurusan:" + pecah[3])
                print("Divisi Yang Dipilih:" + pecah[1])
                print("Nilai Tes:" + pecah[5])
                print("Status Pendaftar:" + pecah [6])   
                print("")
                print("============================================================================")
                file = open("panitia.txt","w")
                file.writelines(merubah)
                # os.remove("panitia.txt")
                # os.rename("sementara.txt","panitia.txt")
                print("")
                print("==========================DETAIL DATA SETELAH DIRUBAH=======================")
                print("Nama:" + nama_baru_konversi)
                print("Umur:" + str(umur_baru))
                print("Jurusan:" + jurusan_baru_konversi)
                print("Divisi:" + divisi_baru_konversi)
                print("Nilai Tes:" + nilai_baru)
                print("Status:" + status_baru)
                print("")
                print("============================================================================")
                file.close()
                break
            elif nilai_baru <= 90.0:
                status_baru = "TIDAK LULUS"
                merubah[patokan] = "==="+"||" + divisi_baru_konversi + "||" + str(umur_baru)  + "||" + jurusan_baru_konversi  + "||"+ nama_baru_konversi+ "||" + str(nilai_baru) +"||" + status_baru + "||" "==="+"\n"
                # cob = file.writelines(merubah)
                # file2.writelines(merubah)
                # file2.close()
                print("*SELAMAT DATA TELAH BERHASIL DIRUBAH*")
                print("")
                print("=====================DATA SEBELUM DIRUBAH===================================")
                print("Nama Pendaftar Sebelum Dirubah: " + pecah[4])
                print("Nama Pendaftar:" + pecah[4])
                print("Umur:" + pecah[2])
                print("Jurusan:" + pecah[3])
                print("Divisi Yang Dipilih:" + pecah[1])
                print("Nilai Tes:" + pecah[5])
                print("Status Pendaftar:" + pecah [6])   
                print("")
                print("============================================================================")
                file = open("panitia.txt","w")
                file.writelines(merubah)
                # file.close()
                # os.remove("panitia.txt")
                # os.rename("sementara.txt","panitia.txt")
                print("")
                print("==========================DETAIL DATA SETELAH DIRUBAH=======================")
                print("Nama:" + nama_baru_konversi)
                print("Umur:" + str(umur_baru))
                print("Jurusan:" + jurusan_baru_konversi)
                print("Divisi:" + divisi_baru_konversi)
                print("Status:" + status_baru)
                print("")
                print("============================================================================")
                file.close()
                break
        patokan += 1
    else:
        print("MOHON MAAF DATA YANG INGIN DIRUBAH TIDAK ADA")         
    pindah = int(input("""Apakah Anda Ingin Melakukan Hal Lain?
                        Ketik 1 Untuk Merubah Data Lagi 
                        Ketik 2 Untuk Kembali Ke Menu
                        Ketik 3 Untuk Keluar Program 
                    """))
    if pindah == 1:
        file = open("panitia.txt","r")
        file.close()
        rubah()
    elif pindah == 2:
        file = open("panitia.txt","r")
        file.close()
        awalan()
    elif pindah == 3:
        print("Sampai Jumpa Kembali")
        exit()
            
def awalan():
    print("========================================================================")
    print("Selamat Datang Di Sistem Informasi Pendataan Calon Anggota Organisasi / UKM")
    print("========================================================================")
    print("")
    print("""Apa Yang Anda Ingin Lakukan:
        1.Menambah Data Pendaftar
        2.Melihat Data Pendaftar
        3.Merubah Data Pendaftar
        4.Menghapus Data Pendaftar
        5.Mencari Data Pendaftar 
        6.Keluar Program
        """)
    print("=========================================")

    pilihan = int(input("Masukkan Tujuan Anda: "))

    if pilihan == 1:
        print("ANDA BERADA DALAM MODE MENAMBAH DATA")
        buka = open("panitia.txt" , "a")
        buka.close()
        menambah()
    elif pilihan == 2:
        print("ANDA BERADA DALAM MODE MELIHAT DATA ")
        melihat()
    elif pilihan == 3:
        print("ANDA BERADA DALAM MODE MERUBAH DATA")
        rubah()
    elif pilihan == 4:
        print("ANDA BERADA DALAM MODE MENGHAPUS DATA")
        hapus()
    elif pilihan == 5:
        print("ANDA BERADA DALAM MODE MENCARI DATA ")
        cari()
    elif pilihan == 6:
        exit()

awalan()



