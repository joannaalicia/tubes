from functions import mylen, myappend


def hapusjin(users, status):
    if(status):
        stat = True
        nama = str(input("Masukan username jin : "))
        for i in range(2, mylen(users)):    #ngeloop jin dari 2 sampe akhir, alasan 2 karena 0 dan 1 adalah user
            if(nama == users[i][0]):        #ngecek kalo inputan ada yang sama di dalem list 
                stat = False                #mastiin kalo nama jin beneran ada biar ga nyetak line 30   
                pilihan = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
                if(pilihan == "Y"):
                    hasil = []
                    tambahan = []
                    for j in range(0, mylen(users)):
                        if users[j][0] != users[i][0]:
                            tambahan = [users[j][0], users[j][1], users[j][2]]      #ini nge loop masukin ulang semua list user awal ke user yang baru tanpa jin yang akan dihapus
                            hasil = myappend(hasil, tambahan)                       #singkatnya loop ini untuk ngapus jin yang di inginkan
                    users = hasil
                    #print(users) ini apus aja w pake buat test
                    break
                elif pilihan == "N":
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

    