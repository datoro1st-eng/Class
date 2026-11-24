class Waschmaschine:
    def __init__(self, marke = "", kapazitaet = 0, status = ""):
        self.__marke = marke
        self.__kapazitaet = kapazitaet
        self.__status = status

    def get_marke(self):
        return self.__marke

    def get_status(self):
        return self.__status

    def get_kapazitaet(self):
        return self.__kapazitaet

    def eingeben():
        maschinen = []
        n = int(input("Nhap so luong may giat dang quan li : "))
        for i in range(n):
            marke = str(input(f"Thuong hieu may giat {i+1} la : "))
            kapazitaet = int(input(f"Dung tich may giat {i+1} la :"))
            status = input(f"Trang thai may giat {i+1} la (ja/nein) : ")
            if status == "ja":
                status = "Đang được sử dụng"
            elif status == "nein":
                status = "Có thể sử dụng"
            maschinen.append(Waschmaschine(marke, kapazitaet, status))
        return maschinen    
            
     
    def anzeigen(maschinen):
        for i in range(len(maschinen)):
         print("======= May Giat {i+1} ======= ")
         print(f"Thuong hieu may giat {i+1} : ", maschinen[i].get_marke())
         print(f"Dung tich may giat : ", maschinen[i].get_kapazitaet())
         print(f"Trang thai may giat : ", maschinen[i].get_status())



    def Miete_kosten(self):
        zeit = int(input("Nhap thoi gian thue (theo phut): "))
        kosten = 0
        thanh_toan = ""
        if zeit <= 0:
            print("Thoi gian thue khong hop le!")
        else:
            kosten = zeit * 2 
            print("Thanh tien :", kosten,"euro!")
            thanh_toan = input("Vui long thanh toan (ja/nein) :").strip()
            if thanh_toan == "ja":
                print("Thanh toan thanh cong")
                self.__status = "Đang được sử dụng"
            elif thanh_toan == "nein":    
                print("Thanh toan chua thanh cong!")

            
                 
        
        
def main():
    maschinen = Waschmaschine.eingeben()

    while True:
        print("\n========== WASCHMASCHINENVERMIETUNG ==========")
        print("1. Hiển thị danh sách máy giặt (Anzeigen)")
        print("2. Thuê máy giặt (Mieten)")
        print("3. Thoát (Beenden)")

        auswahl = int(input("Lựa chọn của bạn: "))

        if auswahl == 1:
            Waschmaschine.anzeigen(maschinen)

        elif auswahl == 2:
            marke = input("Nhập thương hiệu máy giặt bạn muốn thuê: ")
            
            for xe in maschinen:
                if xe.get_marke() == marke:
                    gefunden = True
                
                    if xe.get_status() == "Đang được sử dụng":
                        print("Máy giặt này đang được cho thuê!")
                        break
            
                    elif xe.get_status() == "Có thể sử dụng":
                        xe.Miete_kosten()
                        break
                if not gefunden:
                 print("Không tìm thấy máy giặt!") 
          

        elif auswahl == 3:
            print("Chương trình kết thúc!")
            break

        else:
            print("Lựa chọn không hợp lệ!")

main()

