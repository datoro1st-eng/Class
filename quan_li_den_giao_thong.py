import time
class Ampel:
    def __init__(self, rot = True, geld = True, grune = True):
        self.__rot = rot
        self.__geld = geld
        self.__grune = grune

    def anzeigen(self): # truyển dữ liệu vào class
        print("Đèn đỏ :", self.__rot)

        print("Đèn vàng :", self.__geld)

        print("Đèn xanh :", self.__grune)

    def eingeben(self): # nhập dữ liệu 
        rot = input("Đèn đỏ đang bật hay tắt :").strip()
        if rot == "bật":
            rot = True
        elif rot == "tắt":
            rot = False
        geld = input("Đèn vàng đang bật hay tắt :").strip()
        if geld == "bật":
            geld = True
        elif geld == "tắt":
            geld = False

        if rot == True and geld == False:
            grune = False
            ampel = Ampel(rot, geld, grune) # đưa dữ liệu nhập vào class
            return ampel # return về class

        elif geld == True and rot == False:
            grune = False
            ampel = Ampel(rot, geld, grune)
            return ampel
        elif geld == False and rot == False:
            grune = True
            ampel = Ampel(rot, geld, grune)
            return ampel

    def dem_nguoc(self, giay):
        while giay > 0:
            print("Đếm ngược:", giay)
            time.sleep(1)
            giay -= 1 # hàm đếm ngước

    
    def zahlen(self):
        zeit_rot = int(input("nhật số giây đếm ngược đèn đỏ : "))
        zeit_geld = int(input("nhật số giây đếm ngược đèn vàng : "))
        zeit_grune = int(input("nhật số giây đếm ngược đèn xanh : "))
        if zeit_rot <= 0 or zeit_geld <= 0 or zeit_grune <= 0:
            print("Thời gian phải lớn hơn 0!")
            return

        while True:
            if self.__rot:
                self.anzeigen()
                self.dem_nguoc(zeit_rot)

                self.__rot = False
                self.__geld = False
                self.__grune = True

            elif self.__grune:
                self.anzeigen()
                self.dem_nguoc(zeit_grune)

                self.__grune = False
                self.__geld = True
                self.__rot = False

            elif self.__geld:
                self.anzeigen()
                self.dem_nguoc(zeit_geld)

                self.__geld = False
                self.__rot = True
                self.__grune = False

            stop = input("Nhập 0 để dừng, Enter để tiếp tục: ")
            if stop == "0":
                break
        
        

        
            



ampel = Ampel() # gán oject vào class
ampel =ampel.eingeben() # vì return về ampel nên phải gán ampel = ampel.eingeben() để nhận dữ liệu

ampel.zahlen()





