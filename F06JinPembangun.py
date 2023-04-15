import random as rd
from functions import mylen, myappend

def bangun(users, candi, bahan_bangunan, status):
    if(status == True):
        candidibuat = [] 
        jinbuat = []
        cukup = True
        kpasir = rd.randint(1,5)
        kbatu = rd.randint(1,5)             #generate random buat nentuin keperluan bangun
        kair = rd.randint(1,5)

        for i in range (2, mylen(users)):
            if(users[i][2] == "pembangun"):
                jinbuat = myappend(jinbuat, users[i][0])           #ngeloop buat masukin nama nama jin pembangun ke dalam list jinbuat
        if(jinbuat == []):
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")     #kalo listnya kosong artinya jin lom ada langsung return udahan
            return candi



        if(int(bahan_bangunan[0][2]) < kpasir or int(bahan_bangunan[1][2]) < kbatu or int(bahan_bangunan[2][2]) < kair ): #misal bahan kurang
            cukup = False
        
        if(cukup == False):
            print("Bahan bangunan tidak mencukupi")         
        else:                                                                       #misal bahan cukup
            bahan_bangunan[0][2] = int(bahan_bangunan[0][2]) - kpasir           
            bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) - kbatu
            bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) - kair                 #bahan baku dikurangin

            jinkerja = rd.choice(jinbuat)                                           #memilih acak jin pekerja mana yang kerja
            candidibuat = [int(mylen(candi)+1), jinkerja , kpasir, kbatu, kair ]    #masukin list candi dibuat dari no urut, siapa yg kerja, sama material apa aja
            candi = myappend(candi, candidibuat)                                    #ditambahin listnya ke list utama

            print("Membangun candi dengan total bahan ",kpasir, " pasir, ", kbatu, " batu, dan ",kair, " air", sep = "" )
            print("Candi berhasil dibangun")
            print("Sisa candi yang perlu dibangun:", 100 - int(mylen(candi)))

            #print(candi)
            #print(bahan_bangunan)  hapus aja, w make pas buat cek
    else:
        print("log in terlebih dahulu")
        
    return candi
        
            