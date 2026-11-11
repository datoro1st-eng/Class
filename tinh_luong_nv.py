class Nhan_vien:
    def __init__(self, ma_nv =" ", ho_ten = " ", luong_co_ban = 0, loai_nvien = " "):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_co_ban = luong_co_ban
        self.loai_nvien = loai_nvien

    def tinh_luong(self):
        return self.luong_co_ban

    def set_loai_nvien(self):
        if self.loai_nvien == "IT":
            print("Nhân viên IT")
        elif self.loai_nvien =="Sale":
            print("Nhân viên sale")    
    
    def xuat_thong_tin(self):
        print("Mã nhân viên :", self.ma_nv)
        print("Họ tên :", self.ho_ten)
        print("lương cơ bản :", self.luong_co_ban)
    
        

class Laptrinhvien(Nhan_vien):
    def __init__(self, ma_nv=" ", ho_ten=" ", luong_co_ban=0, loai_nvien = " ", so_gio_ot = 0, tien_ot_1_gio = 0):
        super().__init__(ma_nv, ho_ten, luong_co_ban, loai_nvien)
        self.so_gio_ot = so_gio_ot
        self.tien_ot_1_gio = tien_ot_1_gio 

    def set_gio_ot(self, so_gio_ot):
        if so_gio_ot >= 0:
            self.so_gio_ot = so_gio_ot
        else:
         print("Số giờ OT không hợp lệ!")

    
    def tinh_luong(self):
        return super().tinh_luong() + (self.tien_ot_1_gio * self.so_gio_ot)

class NhanViennale(Nhan_vien):
    def __init__(self, ma_nv=" ", ho_ten=" ", luong_co_ban=0, loai_nvien = " ", doanh_so = 0.0, ty_le_hoa_hong = 0.0):
        super().__init__(ma_nv, ho_ten, luong_co_ban, loai_nvien )      
        self.doanh_so = doanh_so
        self.ty_le_hoa_hong = ty_le_hoa_hong

    def tinh_luong(self):
        return super().tinh_luong() + (self.doanh_so * self.ty_le_hoa_hong)

def nhap_nhan_vien():
    ma_nv = input("Mã nhân viên: ")
    ho_ten = input("Họ tên: ")
    luong_co_ban = float(input("Lương cơ bản: "))
    loai_nvien = input("Loại nhân viên (IT/Sale): ")

    if loai_nvien == "IT":
        so_gio_ot = float(input("Số giờ OT: "))
        tien_ot_1_gio = float(input("Tiền OT mỗi giờ: "))

        return Laptrinhvien(
            ma_nv, ho_ten, luong_co_ban,
            loai_nvien, so_gio_ot, tien_ot_1_gio
        )

    elif loai_nvien == "Sale":
        doanh_so = float(input("Doanh số: "))
        ty_le_hoa_hong = float(input("Tỷ lệ hoa hồng: "))

        return NhanViennale(
            ma_nv, ho_ten, luong_co_ban,
            loai_nvien, doanh_so, ty_le_hoa_hong
        )

    else:
        print("Loại nhân viên không hợp lệ!")
        return None    

def xuat_danh_sach(danh_sach_nv):
    for nv in danh_sach_nv.values():
        print("\n========== NHÂN VIÊN ==========")
        nv.xuat_thong_tin()
        nv.set_loai_nvien()
        print("Lương thực nhận:", nv.tinh_luong())

def cap_nhat_ot(danh_sach_nv):
    ma = input("Nhập mã nhân viên: ")

    if ma in danh_sach_nv:
        nv = danh_sach_nv[ma]

        if isinstance(nv, Laptrinhvien):
            so_gio = float(input("Nhập số giờ OT mới: "))
            nv.set_gio_ot(so_gio)
            print("Cập nhật OT thành công!")
            print("Lương mới:", nv.tinh_luong())
        else:
            print("Nhân viên này không phải IT!")
    else:
        print("Không tìm thấy nhân viên!")


def main():
    
    danh_sach_nv = {}

    while True:
        print("\n===== MITARBEITERVERWALTUNG =====")
        print("1. Nhập nhân viên (Mitarbeiter hinzufügen)")
        print("2. Xuất danh sách (Mitarbeiter anzeigen)")
        print("3. Tìm nhân viên (Mitarbeiter suchen)")
        print("4. Xóa nhân viên (Mitarbeiter löschen)")
        print("5. Cập nhật giờ OT (Überstunden ändern)")
        print("0. Thoát (Beenden)")

        wahl = int(input("Bitte wählen: "))

        match wahl:
            case 1:
                n = int(input("Số nhân viên muốn nhập: "))
                for i in range(n):
                    print(f"\nNhân viên thứ {i+1}:")
                    nv = nhap_nhan_vien()
                    if nv is not None:
                        danh_sach_nv[nv.ma_nv] = nv

            case 2:
                xuat_danh_sach(danh_sach_nv)

            case 3:
                ma = input("Nhập mã nhân viên cần tìm: ")
                if ma in danh_sach_nv:
                    danh_sach_nv[ma].xuat_thong_tin()
                    print("Lương thực nhận:", danh_sach_nv[ma].tinh_luong())
                else:
                    print("Không tìm thấy nhân viên!")

            case 4:
                ma = input("Nhập mã nhân viên cần xóa: ")
                if ma in danh_sach_nv:
                    del danh_sach_nv[ma]
                    print("Đã xóa nhân viên!")
                else:
                    print("Không tìm thấy nhân viên!")

            case 5:
                cap_nhat_ot(danh_sach_nv)
            case 0:
                print("Chương trình kết thúc!")
                break

            case _:
                print("Lựa chọn không hợp lệ!")


main()

