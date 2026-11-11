class Buch:
    def __init__(self, bestand = 0, ausgeleiben = 0):
        self.__bestand = bestand 
        self.__ausgeleiben = ausgeleiben

    def set_bestand(self, bestand):
        if bestand < 0:
            print("Số sách không được phép âm!")
        else:
            self.__bestand = bestand
            if bestand < self.__ausgeleiben:
                print("Số sách còn phải lớn hơn số sách mượn!")

    def set_ausgeleiben(self, ausgeleiben):
        self.__ausgeleiben = ausgeleiben            
            
    
    def get_bestand(self):
        return self.__bestand

    def get_ausgeleiben(self):
        return self.__ausgeleiben

    def buch_hinzufuegen(self):
        anzahl = int(input("Số sách muốn thêm: "))
        if anzahl <= 0 or anzahl > 100:
            print("Số sách thêm không hợp lệ!")
        else:
            self.set_bestand(self.get_bestand() + anzahl)
            print("Thêm sách thành công!")

    def buch_ausleihen(self):
        anzahl = int(input("Số sách muốn mượn: "))
        if anzahl <= 0 or anzahl > self.get_bestand():
            print("Số sách thêm không hợp lệ!")
        else:
            self.set_bestand(self.get_bestand() - anzahl)
            self.set_ausgeleiben(self.get_ausgeleiben() + anzahl)
            print("Mượn sách thành công!")

    def buch_zurueckgeben(self):
        anzahl = int(input("Số sách muốn trả: "))
        if anzahl <= 0 or anzahl > self.get_ausgeleiben():
            print("Số sách trả không hợp lệ!")
        else:
            self.set_bestand(self.get_bestand() + anzahl)
            self.set_ausgeleiben(self.get_ausgeleiben() - anzahl)
            print("Trả sách thành công!") 

    def buch_entfernen(self):
        anzahl = int(input("Số sách muốn xóa: "))
        if anzahl <= 0 or anzahl > self.get_bestand():
            print("Số sách xóa không hợp lệ!") 
        else:
            self.set_bestand(self.get_bestand() - anzahl)

    def einzeigen():
        so_sach_trong_thu_vien = int(input("Số sách đang có trong thư viện: "))
        so_sach_da_cho_muon = int(input("Số sách đã cho mượn: "))
        buch = Buch(so_sach_trong_thu_vien, so_sach_da_cho_muon)
        # nhớ trả về class Buch
        return buch
    
    def anzeigen(buch):
        print("Số sách hiện có:", buch.get_bestand())
        print("Số sách đang mượn: ", buch.get_ausgeleiben())

def main():
    buch = Buch.einzeigen()

    while True:
        print("\n===== BIBLIOTHEKSVERWALTUNG =====")
        print("1. Bücher anzeigen")
        print("2. Bücher hinzufügen")
        print("3. Bücher ausleihen")
        print("4. Bücher zurückgeben")
        print("5. Bücher entfernen")
        print("6. Bestand ändern")
        print("0. Beenden")

        wahl = int(input("Bitte wählen: "))

        match wahl:
            case 1:
                Buch.anzeigen(buch)
            case 2:
                buch.buch_hinzufuegen()
            case 3:
                buch.buch_ausleihen()
            case 4:
                buch.buch_zurueckgeben()
            case 5:
                buch.buch_entfernen()
            case 0:
                print("Programm beendet!")
                break
            case _:
                print("Ungültige Auswahl!")

main()

    
        
        