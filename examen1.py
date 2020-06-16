class Clima:
    def __init__(self):
        self.codigo = []
        self.ciudad = []
        self.temp_minima = []
        self.temp_maxima = []
        self.zona = []
        self.estado = []

    def menu(self):
        opciones = """
        ********* Clima de los Departamentos **********
        1. Mostrar
        2. Promedio
        3. Temperatura mas baja del llano
        4. Temperatura mas alta altiplano
        """
        print(opciones)
        elegir = int(input("Seleccione una opcion: \n"))
        if(elegir == 1):
            print(self.mostrar())
            print(self.menu())
        elif(elegir == 2):
            print(self.promedio())
        elif(elegir == 3):
            pass
        else:
            print("Elija Una Opcion valida.")
            self.menu()

    def registrar(self):
        codigo = int(input("codigo: \n"))
        ciudad = (input("ciudad: \n"))
        min = (input("Tempertaura minima: \n"))
        max = (input("Temperatura maxima: \n"))
        zona = (input("zona: \n"))
        print(self.guardar(codigo, ciudad, min, max, zona))

    def guardar(self, codigo, ciudad, temp_minima, temp_maxima, zona):
        self.codigo.append(codigo)
        self.ciudad.append(ciudad)
        self.temp_minima.append(temp_minima)
        self.temp_maxima.append(temp_maxima)
        self.zona.append(zona)
        self.estado.append(1)
        return "todos los departamentos de bolivia"


    def mostrar(self, posicion):
        print("*********** Departamentos *********")
        print("codigo: {}".format(self.codigo[posicion]))
        print("ciudad: {}".format(self.ciudad[posicion]))
        print("Temperatura Minima: {}".format(self.temp_minima[posicion]))
        print("Temperatura Maxima: {}".format(self.temp_maxima[posicion]))
        print("zona: {}".format(self.zona[posicion]))
        print("*****************************************")
        pass

    def mostrar(self):
        for i in range(len(self.ciudad)):
            self.detalle(i)
        pass

    def detalle(self, posicion):
        print("Codigo: {}".format(self.codigo[posicion]))
        print("Ciudad: {}".format(self.ciudad[posicion]))
        print("Temperatura minima: {}".format(self.temp_minima[posicion]))
        print("Temperatura maxima: {}".format(self.temp_maxima[posicion]))
        print("Zona: {}".format(self.zona[posicion]))
        print("*****************************************")
        pass


    def promedio(self):
        print(" ")
        print(" ********************")
        print(" ")
        print(f"Minimas  - Ciudades")
        for i in range(len(self.temp_minima)):
            print(self.temp_minima[i], (" "), self.zona[i])
        suma = 0
        for i in range(len(self.zona)):
            suma += self.temp_minima[i] 


clima = Clima()
clima.guardar(1, "Santa Cruz", 15, 29, "llano")
clima.guardar(2, "Beni", 17, 31, "llano")
clima.guardar(3, "Pando", 18, 30, "llano")
clima.guardar(4, "La Paz", 1, 13, "altiplano")
clima.guardar(5, "Oruro", 2, 15, "altiplano")
clima.guardar(6, "Potosi", 2, 14, "altiplano")
clima.guardar(7, "Cbba", 5, 18, "valle")
clima.guardar(8, "Sucre", 9, 23, "valle")
clima.guardar(9, "Tarija", 10, 25, "llano")
clima.menu()