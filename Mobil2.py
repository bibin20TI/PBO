class Mobil2():

    def __init__(self, jumlah_roda, transmisi, merk):  
        self.jumlah_roda = jumlah_roda                        
        self.transmisi = transmisi                            
                                                                                     #nama: Bibin aripin
    def __init__(self, jumlah_roda, transmisi, merk):                                #kelas : TI20C
        self.jumlah_roda = jumlah_roda                                               #NIM : 20200040002
        self.transmisi = transmisi                                                   #TUGAS OOP : inheritance(pewarisan)
        self.merk = merk  

    def jalankan(self):
        print("ayo jalan "+self.merk)

        sedan = Mobil2(4, "auto", "mazda")
        sedan.jalankan()
        print(sedan.__dict__)	