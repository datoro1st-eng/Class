class Bankkonto :
    def __init__(self, kontoinhaber = " ", kontostand = 0):
          self.__kontoinhaber = kontoinhaber
          self.__kontostand = kontostand
          #self.set_kontostand() = 0

    def einzeigen(self):
          self.__kontoinhaber =str(input("Kontoinhber einzeigen: "))
          self.__kontostand = int(input("Kontostand einzeigen: "))

    def anzeigen(self):
          print("Kontoinhaber: ", self.__kontoinhaber)
          print("Kontostand: ", self.__kontostand, "euro")
    
    def einzahlen(self):
          betrag = int(input("Geld einzahlen: "))
          if betrag <= 0:
                print("Geld muss positive!!!")
          else:
            self.__kontostand += betrag
            print("Neue Kontostand: ", self.__kontostand)

    def abheben(self):
          betrag = int(input("Geld abheben: "))
          if betrag < 0:
              print("Geld muss positive!!!")
          elif betrag > self.__kontostand:
              print("Du hatte nicht genug Geld zur Abhebung!!!")
          else:
              self.__kontostand -= betrag
              print("Neue Kontostand: ", self.__kontostand)

def main():
      konto = Bankkonto()
      konto.einzeigen()
      while True:
        print("\n========== BANKVERWALTUNG ==========")
        print("1. Konten anzeigen")
        print("2. Geld einzahlen")
        print("3. Geld abheben")
        print("0. Beenden")
        print("====================================")

        wahl = int(input("Bitte wählen: "))

        if wahl == 1:
          konto.anzeigen()


        elif wahl == 2:
          konto.einzahlen()
          

        elif wahl == 3:
          konto.abheben()
          

        elif wahl == 0:
            print("Programm beendet!")
            break

        else:
            print("Ungültige Auswahl!")

            
main()                    

                

                      
          
             
