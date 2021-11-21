import Mobil   #import file dengan nama Mobil.py  extensi "py" nya nggk usah 
               #di tulis
import no3      # import file dengan nama no3.py 

       

sedan = no3.Mobil_overidding(4, "auto", "mazda") #inisiasikan objek dengan 
#class Mobil_overidding yang ada di file dengan nama no3.py 

sedan.jalankan()   #panggil method jalankan yang ada di class #Mobil_overidding
truck = no3.Mobiltruck(8, "manual", "hino", 1000) #inisiasi class Mobiltruck
#yang berada file no3.py "py"nggk usah di tulis
truck.jalankan()  #jalankan method jalankan yang menimpa class Mobil ###(Mobil_overidding)

print(sedan.__dict__)
print(truck.__dict__)

mobilSedan = Mobil.Mobil(4, "auto", "mazda")
mobilTruck = Mobil.Mobiltruck(8, "manual", "hino", 1000)
mobilSedan.jalankan()



print("truck mampu menampung beban ",mobilTruck.maxMuatan(1000));  #mencoba akses method dengan visibility public dengan visibility property
#private

print(mobilSedan.__dict__)
print(mobilTruck.__dict__)
print("truck mampu menampung beban ",mobilTruck.maxMuatan(1000));  #mencoba akses method visibility public dengan property
#private