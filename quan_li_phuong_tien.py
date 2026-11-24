class Fahrzeug:
    def __init__(self, ma_xe = 0, ten_xe = " ", gia_co_ban = 0, loai_xe = " "):
        self.ma_xe = ma_xe
        self.ten_xe = ten_xe
        self.gia_co_ban = gia_co_ban
        self.loai_xe = loai_xe

    def tinh_gia(self):
        return self.gia_co_ban

    def set_loai_xe(self):
        if self.loai_xe == "Oto":
            print("Ô tô")
        elif self.loai_xe =="XeMay":
            print("Xe máy")    

    def xuat_thong_tin(self):
        print("Mã xe :", self.ma_xe)
        print("Tên xe :", self.ten_xe)
        print("Giá cơ bản :", self.gia_co_ban)
        print("Loại xe :", self.loai_xe)

class Oto(Fahrzeug):
    def __init__(self, ma_xe=0, ten_xe=" ", gia_co_ban=0, loai_xe=" ", so_ghe = 0, phi_bao_hiem = 0):
        super().__init__(ma_xe, ten_xe, gia_co_ban, loai_xe)
        self.so_ghe = so_ghe
        self.phi_bao_hiem = phi_bao_hiem

    def set_phi_bh(self, phi_bao_hiem):
            if phi_bao_hiem >= 0:
                self.phi_bao_hiem = phi_bao_hiem
                return True
            else:
             print("Phí bảo hiểm không hợp lệ!")
             return False
    
    
    def tinh_gia(self):
        return super().tinh_gia() + self.phi_bao_hiem

class XeMay(Fahrzeug):
    def __init__(self, ma_xe=0, ten_xe=" ", gia_co_ban=0, loai_xe=" ", dung_tich = 0, phi_dang_ky = 0):
        super().__init__(ma_xe, ten_xe, gia_co_ban, loai_xe)     
        self.dung_tich = dung_tich
        self.phi_dang_ky = phi_dang_ky

    def set_phi_dangki(self, phi_dang_ky):
        if phi_dang_ky >= 0:
            self.phi_dang_ky = phi_dang_ky
            return True
        else:
            print("Phí đăng kí không hợp lệ!") 
            return False   
    
    def tinh_gia(self):
        return super().tinh_gia() + self.phi_dang_ky

def nhap_phuong_tien():
    ma_xe = int(input("Mã xe :"))
    ten_xe = input("Tên xe :")
    gia_co_ban = int(input("Giá cơ bản :"))
    loai_xe = input("Loại xe ( Ô tô / Xe Máy) :")
    if loai_xe == "Oto":
        so_ghe = int(input(" Số ghế ngồi :"))
        phi_bao_hiem = int(input("Phí bảo hiểm :"))
        return Oto(ma_xe, ten_xe, gia_co_ban, loai_xe, so_ghe, phi_bao_hiem)
    
    elif loai_xe == "XeMay":
        dung_tich = int(input("Dung tích của xe :"))
        phi_dang_ky = int(input("Phí đăng kí :"))
        return XeMay(ma_xe, ten_xe, gia_co_ban, loai_xe, dung_tich, phi_dang_ky)

    else:
        print("Không có xe nào hợp lệ !!!")

def xuat_danh_sach(danh_sach_xe):
    for xe in danh_sach_xe.values():
        print("\n========== Phương tiện ==========")
        xe.xuat_thong_tin()
        xe.set_loai_xe()
        print("Giá xe thực tế :", xe.tinh_gia())

def tim_phuong_tien(danh_sach_xe):
    ma_xe = int(input(" Nhập mã xe bạn cần tìm :"))
    if ma_xe in danh_sach_xe:
        danh_sach_xe[ma_xe].xuat_thong_tin()
        print("Giá trị thực tế của xe :", danh_sach_xe[ma_xe].tinh_gia())
    else:
        print("Không tìm thấy xe bạn cần tìm! ")

def cap_nha_gia(danh_sach_xe):
     ma_xe = int(input("Nhập mã xe: "))
    
     if ma_xe in danh_sach_xe:
        xe = danh_sach_xe[ma_xe]
    
        if isinstance(xe, Oto):
         phi_bao_hiem = int(input("Nhập số phí bảo hiểm mới: "))
         xe.set_phi_bh(phi_bao_hiem)
         print("Cập nhật giá thành công!")
         print("Giá trị thực thế :", xe.tinh_gia())
        elif isinstance(xe, XeMay):
         phi_dang_ky = int(input("Nhập phí đăng kí mới :"))
         xe.set_phi_dangki(phi_dang_ky)
         print("Cập nhật giá thành công!")
         print("Giá trị thực thế :", xe.tinh_gia())
        else:
         print("Không tìm thấy xe cần cập nhật!")


def main():
    danh_sach_xe = {}

    while True:
        print("\n===== FAHRZEUGVERWALTUNG =====")
        print("1. Phương tiện mới hinzufügen")
        print("2. Danh sách anzeigen")
        print("3. Phương tiện suchen")
        print("4. Giá cập nhật (Preis ändern)")
        print("5. Phương tiện löschen")
        print("0. Beenden")

        wahl = int(input("Bitte wählen: "))

        match wahl:
            case 1:
               n = int(input("Số xe muốn nhập: "))
               for i in range(n):
                print(f"\nXe thứ {i+1}:")
                xe= nhap_phuong_tien()

                if xe is not None:
                    if xe.ma_xe not in danh_sach_xe:
                     danh_sach_xe[xe.ma_xe] = xe
                    else:
                     print(" Mã xe đã tồn tại!")    

            case 2:
               xuat_danh_sach(danh_sach_xe)

            case 3:
                tim_phuong_tien(danh_sach_xe)

            case 4:
                cap_nha_gia(danh_sach_xe)

            case 5:
                ma_xe = int(input(" Nhập mã xe bạn muốn xóa :"))
                if ma_xe in danh_sach_xe:
                    del danh_sach_xe[ma_xe]
                    print(" Đã xóa xe thành công!")
                else:
                    print(" Không tìm thấy xe bạn muốn xóa!")   

            case 0:
                print("Programm beendet!")
                break

            case _:
                print("Ungültige Auswahl!")       

main()
   


    


          

