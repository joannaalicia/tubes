from functions import mylen, myappend

def ubahjin(users, status):
    if(status == True):
        stat = True
        nama = str(input("Masukan username jin : "))
        for i in range(2, mylen(users)):
            if(nama == users[i][0]):                #looping lagi nyari nama jin yang sama kek inputan
                stat = False                        #mastiin buat line 32 ga kecetak semisal inputan ada di dalam list jin
                if(users[i][2] == "pembangun"):
                    pilihan = input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)?")
                    if(pilihan == "Y"):
                        users[i][2] = "pengumpul"
                        print("Jin telah berhasil diubah")
                    elif(pilihan == "N"):
                        break
                    else:
                        print("Jawaban Tidak Valid!!!")
                        break
                else:                                                                                                      #IF ELSE biasa kalo pembangun jadi pengumpul dan sebaliknya
                    pilihan = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?")
                    if(pilihan == "Y"):
                        users[i][2] = "pembangun"
                        print("Jin telah berhasil diubah")
                    elif(pilihan == "N"):
                        break
                    else:
                        print("Jawaban Tidak Valid!!!")
                        break
            else:
                continue
        if(stat == True):
            print("Tidak ada jin dengan username tersebut.")
    else:
        print("log in terlebih dahulu")
    return users