class Fahrzeug:
    def __init__(self, kennzeichen = "", tyb = "", status = True, parkzeit = 0):
        self.__kennzeichen = kennzeichen
        self.__tyb = tyb
        self.__status = status
        self.__parkzeit = parkzeit

    def eingeben():
        n = int(input("nhap so luong phuong tien : "))
        phuong_tien = []
        for i in range(n):
            kennzeichen = input("nhap bien so xe :")
            tyb = input("nhap loai phuong tien (oto/xemay) : ").strip()
            status = input("tinh trang (ja/nein) :").strip()
            if status == "ja":
                parkzeit = int(input("nhap thoi gian do :"))
                phuong_tien.append(Fahrzeug(kennzeichen,tyb, status, parkzeit))
            elif status == "nein":
                parkzeit = "Khong do xe = khong mat phi"
                phuong_tien.append(Fahrzeug(kennzeichen,tyb, status, parkzeit))    

        
            
        
        return phuong_tien

    def kosten(self):
        if self.__tyb == "oto":
            if self.__status =="ja":
             print("chi phi do moi gio cua oto la 3 euro!")
             return self.__parkzeit * 3
        elif self.__tyb == "xemay":
            if self.__status == "ja":
             print("chi phi do moi gio cua xemay la 2 euro!")
             return self.__parkzeit * 2

    
    def anzeigen(phuong_tien):
        for i in range(len(phuong_tien)):
            print(f"=======Phuong tien {i+1}==========")
            print("bien so xe :", phuong_tien[i].__kennzeichen)
            if phuong_tien[i].__tyb == "oto":
                print("Auto")
            elif phuong_tien[i].__tyb == "xemay":
                print("Xemay")
            if phuong_tien[i].__status == "ja":
                print("Thoi gian do :",phuong_tien[i].__parkzeit)
                print("chi phi do xe :",phuong_tien[i].kosten())
            elif phuong_tien[i].__status == "nein":
                print("Khong con do!")

    def einfahren(phuong_tien):
        kennzeichen = input("nhap bien so xe :")
        tyb = input("nhap loai phuong tien (oto/xemay) :")
        status = "ja"
        if tyb == "oto":
            print("chi phi do moi gio cua oto la 3 euro!")
            parkzeit = int(input("nhap thoi gian do xe :"))
        elif tyb =="xemay":
            print("chi phi do moi gio cua oto la 2 euro!")
            parkzeit = int(input("nhap thoi gian do xe :"))

        phuong_tien.append(Fahrzeug(kennzeichen, tyb, status, parkzeit))    

    def ausfahren(phuong_tien):
        kennzeichen = input("nhap bien so xe ban can tim :")
        gefunden = False
     
        for xe in range(len(phuong_tien)):
            if kennzeichen == phuong_tien[xe].__kennzeichen:
                gefunden = True
                print("===Thong tin xe muon thanh toan phi do ===")
                print("bien so :", phuong_tien[xe].__kennzeichen)
                print("loai phuong tien :", phuong_tien[xe].__tyb)
                print("Vui long thanh toan khoan phi do xe :",phuong_tien[xe].kosten())
                thanh_toan = input("ja/nein :")
                if thanh_toan == "ja":
                    print("thanh toan thanh cong!")
                    phuong_tien[xe].__status = "nein"
                elif thanh_toan == "nein":
                    print("thanh toan khong thanh cong!")
                    break
        if not gefunden:
            print("Khong tim thay xe!")  

    def loesen(phuong_tien):
        kennzeichen = input("nhap bien so xe can xoa :")
        gefunden = False
        for xe in range(len(phuong_tien)):
         if kennzeichen == phuong_tien[xe].__kennzeichen:   
             gefunden = True
             if phuong_tien[xe].__status == "nein":
              xoa = input("Ban chac chan muon xoa xe chu (ja/nein) : ")
              if xoa == "ja":
                    phuong_tien.pop(xe)
                    print("Xoa xe thanh cong")
                    return
              elif xoa == "nein":
                 print("Xoa xe khong thanh cong!")
                 return
             if phuong_tien[xe].__status == "ja":
                 print("Xe nay dang do!")
                 return    
        if not gefunden:
             print("Khong tim thay phuong tien!")        

                              

        

    
def main():
    phuong_tien = Fahrzeug.eingeben()

    while True:
        print("\n========== PARKHAUSVERWALTUNG ==========")
        print("1. Hiển thị danh sách phương tiện (Anzeigen)")
        print("2. Xe vào bãi (Einfahren)")
        print("3. Xe rời bãi (Ausfahren)")
        print("4. Xoa phuong tien")
        print("0. Thoát (Beenden)")

        auswahl = int(input("Nhập lựa chọn: "))

        if auswahl == 1:
            Fahrzeug.anzeigen(phuong_tien)

        elif auswahl == 2:
            Fahrzeug.einfahren(phuong_tien)
            

        elif auswahl == 3:
            Fahrzeug.ausfahren(phuong_tien)
            

        elif auswahl == 4:
            Fahrzeug.loesen(phuong_tien)
            pass


        elif auswahl == 0:
            print("Chương trình kết thúc!")
            break

        else:
            print("Lựa chọn không hợp lệ!")

main()



        
