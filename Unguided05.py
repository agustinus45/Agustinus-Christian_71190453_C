class Mobil:
    _merk=""
    _tipe=""
    _kapasitasBBM=0
    _jenisBahanBakar=""

    def __init__(self,merk,tipe):
        self._merk = merk
        self._tipe = tipe
#        
    def setKapasitasBBM(self,kapasitasBBM):
        self._kapasitasBBM = kapasitasBBM

    def setJenisBahanBakar(self,jenisBahanBakar):
        self._jenisBahanBakar = jenisBahanBakar

    def getKapasitasBBM(self):
        return self._kapasitasBBM

    def getJenisBahanBakar(self):
        return self._jenisBahanBakar
#

    def setMerk(self,merk):
        self._merk = merk

    def setTipe(self,tipe):
        self._tipe = tipe

    def getMerk(self):
        return self._merk

    def getTipe(self):
        return self._tipe

    def printInfo(self):
        print("============ INFO ============")
        if self._merk !=" ":
            print("Merk            :", self.getMerk())
        elif self._merk == ' ':
            print("Merk            : None")
        print("Tipe            :", self.getTipe())
        if self._jenisBahanBakar !=" ":
            print("Bahan Bakar     :", self.getJenisBahanBakar())
        elif self._jenisBahanBakar == '':
            print("Bahan Bakar     : None")
        print("Kapasitas BBM   :",self.getKapasitasBBM())

    def isiBBM(self,h):
        if self._kapasitasBBM == 0:
            print("ERROR! Kapasitas BBM atau Jenis Bahan Bakar belum di inputkan")
        else:
            print("Mengisi",self.getKapasitasBBM(),"Liter")
            print("Total Harga :","RP"+str(h*self.getKapasitasBBM()))

    
        


if __name__ == "__main__":
    mobil1 = Mobil("Toyota","Avanza")
    mobil1.printInfo()

    mobil2 = Mobil("Nissan","Grand Livina")
    mobil2.setJenisBahanBakar("Bensin")
    mobil2.setKapasitasBBM(20)
    mobil2.printInfo()

    mobil1.isiBBM(14500)
    mobil2.isiBBM(14500)


