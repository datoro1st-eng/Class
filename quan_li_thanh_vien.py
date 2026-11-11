class Mitglied:
    def __init__(self, guthaben):
        self.__guthaben = guthaben
        self.__aktiv = guthaben >= 20

    def set_guthaben(self, guthaben):
        if guthaben < 0:
            print("Số dư không hợp lệ!")
        else:
            self.__guthaben = guthaben
            if guthaben < 20:
                self.__aktiv = False  
         
    def get_guthaben(self):
        return self.__guthaben 
    def get_aktiv(self):
        return self.__aktiv

    def einzeigen():
        n = int(input("Số thành viên hiện tại:"))
        thanh_viens = []
        for i in range(n):
            guthaben = int(input(f"Tài khoản thành viên {i+1} là:"))
            thanh_vien = Mitglied(guthaben)
            thanh_viens.append(thanh_vien)
        return thanh_viens 

    def anzeigen(thanh_viens):
        for i in range(len(thanh_viens)):
            print(f"Tài khoản thành viên {i+1} là:", thanh_viens[i].get_guthaben())
            if thanh_viens[i].get_aktiv() == True:
                print(f"Người tham gia {i+1} là thành viên!")
            else:
                print(f"Người tham gia {i+1} không còn là thành viên!")

           
    def aufladen(self):
        betrag = int(input("Nhập số tiền cần nạp: "))
        if betrag <= 0 or betrag > 500:
            print("Số tiền không hợp lệ!")
            print("Nạp tiền không thành công!")
        else:
            self.set_guthaben(self.get_guthaben() + betrag)
            print("Nạp tiền thành công!")

    def training(self):
        betrag = int(input("Chi phí tập luyen: "))
        if betrag < 0 or betrag > self.get_guthaben():
            print(" Số tiền thanh toán không hợp lệ!")
        else:
            self.set_guthaben(self.get_guthaben() - betrag)
            print("Thanh toán thành công!")


def main():
    thanh_viens = Mitglied.einzeigen()
    wahl = 0
    while True:
        print("1. Guthaben anzeigen")
        print("2. Geld aufladen")
        print("3. Training bezahlen")
       # print("4. Mitglied aktivieren")
       # print("5. Mitglied deaktivieren")
        print("0. Beenden")
        print("====================================")
        print("Bitte wählen:") 
        wahl = int(input("Option: "))
        match wahl:
         case 1:
            Mitglied.anzeigen(thanh_viens)
         case 2:
            index = int(input("Lựa chọn thành viên muốn nạp tiền:")) - 1
            if 0 <= index < len(thanh_viens):
                thanh_viens[index].aufladen()
            else:
                print("Không tìm thấy thành viên!")          
         case 3:
            index = int(input("Lựa chọn thành viên muốn thanh toán:")) - 1
            if 0 <= index < len(thanh_viens):
             thanh_viens[index].training()
            else:
             print("Không tìm thấy thành viên!")           
                        
         case 0:
            print("Hủy bỏ.")
            break
         case _:
            print("Không có lựa chọn phù hợp!")

main()       

            
    

