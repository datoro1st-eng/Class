class Student:
    def __init__(self, name = "", alter = 0, matrikelnummer = 0):
        self.__name = name
        self.__alter = alter
        self.__matrikelnummer = matrikelnummer

    def anzeigen(self):
        print("Name:", self.__name)
        print("Alter:", self.__alter)
        print("Matrikelnummer:", self.__matrikelnummer)

s1 = Student("Dat", 23, 12345)
s2 = Student("Vu", 23, 23456)
s3 = Student("Hoang", 23, 34567)
s1.anzeigen()
s2.anzeigen()
s3.anzeigen()            
        
