import serial
import cv2

class esp32cam:
    
    def __init__(self, **kwargs):
        
        if kwargs.get("baud") == None:
            kwargs["baud"] = 115200
        if kwargs.get("start") == None:
            kwargs["start"] = b"+"
        if kwargs.get("timeout") == None:
            kwargs["timeout"] = 2
        if kwargs.get("eq_file_first") == None:
            kwargs["eq_file_first"] = "esitler_bas.txt"
        if kwargs.get("eq_file_last") == None:
            kwargs["eq_file_last"] = "esitler_son.txt"
        
        self.ser = serial.Serial(kwargs["port"], kwargs["baud"], timeout = kwargs["timeout"])
        self.start = kwargs["start"]
        self.eq_file_first_name = kwargs["eq_file_first"]
        self.eq_file_last_name = kwargs["eq_file_last"]
        
        esit_dosya = open(self.eq_file_first_name, "r")

        self.esitler_bas = []

        esitler_yazi = esit_dosya.readlines()

        for i in esitler_yazi:
            self.esitler_bas.append(int(i))

        esit_dosya_son = open(self.eq_file_last_name, "r")

        self.esitler_son = []

        esitler_yazi_son = esit_dosya_son.readlines()

        for i in esitler_yazi_son:
            self.esitler_son.append(int(i))
        
    def read(self):

        self.ser.write(self.start)

        deger_sayisi = self.ser.read(2)
        deger_sayisi = int.from_bytes(deger_sayisi, "little")

        degerler = []

        for i in self.esitler_bas:
            degerler.append(i.to_bytes(1, "little"))

        for i in range(deger_sayisi):
            deger = self.ser.read(1)
            degerler.append(deger)
        
        for i in self.esitler_son:
            degerler.append(i.to_bytes(1, "little"))

        veri = b""

        for i in degerler:
            veri += i

        resim_adi = "deneme.jpg"
        resim_dosya = open(resim_adi, "wb")

        resim_dosya.write(veri)

        resim_dosya.close()

        resim = cv2.imread("deneme.jpg")

        return resim
