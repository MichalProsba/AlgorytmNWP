class NWP(object):
    def __init__(self, strA, strB):
        #Ciag tekstu A
        self.strA = strA
        #Ciag tekstu B
        self.strB = strB
        #Dlugosc ciag tekstu A odpowiada ilosci wierszy w macierzy
        self.LengthstrA = len(strA) + 1
        #Dlugosc ciag tekstu B odpowiada ilosci kolumn w macierzy
        self.LengthstrB = len(strB) + 1
        #Macierz C potrzebna do programowania dynamicznego
        self.C = []
        #Najdluzszy wspolny podciag
        self.nwp = ''

        #Inicjalizacja tablicy C wartościami Null
        for i in range(0, self.LengthstrA):
            #w = [9] * self.LengthstrB
            w = [None] * self.LengthstrB
            self.C.append(w)

        #Inicjalizacja C (Pierwsza wiersz oraz pierwsza kolumne inicjujemy 0)

        #Pierwszy wiersz
        for i in range(0,self.LengthstrA):
            self.C[i][0] = 0

        #Pierwsza kolumna
        for j in range(0,self.LengthstrB):
            self.C[0][j] = 0

        #C po inicjalizacji
        self.printMatrix("Po inicjalizacji")

        for i in range(1,self.LengthstrA):
            for j in range(1,self.LengthstrB):
                if(self.strA[i-1] == self.strB[j-1]):
                    self.C[i][j] = self.C[i-1][j-1] + 1
                else:
                    self.C[i][j] = max(self.C[i-1][j], self.C[i][j-1])

        #Po algorytmie
        self.printMatrix("Po algorytmie")

        #Przejście do tyłu
        i = self.LengthstrA - 1
        j = self.LengthstrB - 1
        while (i != 0 and j != 0):
            if(self.C[i][j] == self.C[i-1][j]):
                self.C[i][j] = 'x'
                i = i-1
            elif(self.C[i][j] == self.C[i][j-1]):
                self.C[i][j] = 'x'
                j = j-1
            else:
                self.nwp = strB[j-1] + self.nwp
                self.C[i][j] = 'x'
                i = i - 1
                j = j - 1

        self.C[i][j] = 'x'
        self.C[0][0] = 'x'
        print("Wynik NWP:")
        print(self.nwp)
        self.printMatrix("Po przejsciu do tylu")

    def printMatrix(self, message):
        print("======================================")
        print("Matrix C[][] - " + message)
        print("======================================")
        for i in range(0,self.LengthstrB):
            for j in range(0, self.LengthstrA):
                print(str(self.C[j][i]) + " ", end='')
            print()
        print("======================================")
