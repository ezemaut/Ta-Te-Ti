import random
from pathlib import Path
import os

class Tic:

    def __init__(self) -> None:
        self.a1 = '-'
        self.a2 = '-'
        self.a3 = '-'

        self.b1 = '-'
        self.b2 = '-'
        self.b3 = '-'

        self.c1 = '-'
        self.c2 = '-'
        self.c3 = '-'
        self.counter = 0

        self.fila = [self.a1, self.a2, self.a3]
        self.filb = [self.b1, self.b2, self.b3]
        self.filc = [self.c1, self.c2, self.c3]

        self.col1 = [self.a1, self.b1, self.c1]
        self.col2 = [self.a2, self.b2, self.c2]
        self.col3 = [self.a3, self.b3, self.c3]

        self.diag1 = [self.a1, self.b2, self.c3]
        self.diag2 = [self.a3, self.b2, self.c1]

        self.todas = [self.fila, self.filb, self.filc, self.col1, self.col2, self.col3, self.diag1, self.diag2]

        self.disponibles = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

        self.turno = 'x'

        self.jujador1Name = 'CPU 1'
        self.jujador2Name = 'CPU 2'

        self.jujador1Points = 0
        self.jujador2Points = 0
        
        self.partidoNUM = 0

        self.turno1v1 = ''

        self.corners =  ['a1','a3','c1','c3']

        self.FILa = ['a1', 'a2', 'a3']
        self.FILb = ['b1', 'b2', 'b3']
        self.FILc = ['c1', 'c2', 'c3']

        self.COL1 = ['a1', 'b1', 'c1']
        self.COL2 = ['a2', 'b2', 'c2']
        self.COL3 = ['a3', 'b3', 'c3']

        self.DIAG1 = ['a1', 'b2', 'c3']
        self.DIAG2 = ['a3', 'b2', 'c1']

        self.square = [self.fila, self.col1, self.filc, self.col3]
        self.squaredic = {0:self.FILa, 1:self.COL1, 2:self.FILc, 3:self.COL3}

        self.dicNumToLinea:dict[list] = {0:self.FILa, 1:self.FILb, 2:self.FILc, 3:self.COL1, 4:self.COL2, 5:self.COL3, 6:self.DIAG1, 7:self.DIAG2}

        self.double1 = ['a1', 'a2', 'a3', 'b3', 'c3']
        self.double2 = ['a1', 'b1', 'c1', 'c2', 'c3']
        self.double3 = ['c1', 'b1', 'a1', 'a2', 'a3']
        self.double4 = ['c1', 'c2', 'c3', 'b3', 'a3']
        self.DOUBLE1 = [self.a1, self.a2, self.a3, self.b3, self.c3]
        self.DOUBLE2 = [self.a1, self.b1, self.c1, self.c2, self.c3]
        self.DOUBLE3 = [self.c1, self.b1, self.a1, self.a2, self.a3]
        self.DOUBLE4 = [self.c1, self.c2, self.c3, self.b3, self.a3]

        self.cpu_center = 0

        self.textoganador = 'ERROR'

        self.mode = '' #PvP, PvCPU, CPUvCPU
        self.diffculty = '' #PvP, PvCPU = EASY, HARD, CPUvCPU = easyX2 easyHARD hardX2

        self.empezo = ''

        self.mem1 = []
        self.mem2 = []
        self.mem3 = []
        self.mem4 = []
        self.mem5 = []
        self.mems = [self.mem1, self.mem2, self.mem3, self.mem4, self.mem5]

    def clear(self) -> None:
        
        self.a1 = '-'
        self.a2 = '-'
        self.a3 = '-'

        self.b1 = '-'
        self.b2 = '-'
        self.b3 = '-'

        self.c1 = '-'
        self.c2 = '-'
        self.c3 = '-'
        self.counter = 0

        self.fila = [self.a1, self.a2, self.a3]
        self.filb = [self.b1, self.b2, self.b3]
        self.filc = [self.c1, self.c2, self.c3]

        self.col1 = [self.a1, self.b1, self.c1]
        self.col2 = [self.a2, self.b2, self.c2]
        self.col3 = [self.a3, self.b3, self.c3]

        self.diag1 = [self.a1, self.b2, self.c3]
        self.diag2 = [self.a3, self.b2, self.c1]

        self.todas = [self.fila, self.filb, self.filc, self.col1, self.col2, self.col3, self.diag1, self.diag2]

        self.disponibles = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

        self.turno = 'x'

        self.square = [self.fila, self.col1, self.filc, self.col3]
        self.squaredic = {0:self.FILa, 1:self.COL1, 2:self.FILc, 3:self.COL3}

        self.corners =  ['a1','a3','c1','c3']

        self.double1 = ['a1', 'a2', 'a3', 'b3', 'c3']
        self.double2 = ['a1', 'b1', 'c1', 'c2', 'c3']
        self.DOUBLE1 = [self.a1, self.a2, self.a3, self.b3, self.c3]
        self.DOUBLE2 = [self.a1, self.b1, self.c1, self.c2, self.c3]

        self.cpu_center = 0

        self.textoganador = 'ERROR'

        self.mem1 = []
        self.mem2 = []
        self.mem3 = []
        self.mem4 = []
        self.mem5 = []
    
    def saltear(self) -> list[list[str]]:
        i:int = 4
  
        while len(self.mems[i]) == 0:
            if len(self.mems[i]) == 0:
                i = i-1

        return self.mems[0:i+1]
    
    def text(self) -> None:

        dir_path = Path.cwd().joinpath(r"Tateti scores")
        file_name = self.jujador1Name + " vs " + self.jujador2Name + '.txt'
        file_path = dir_path.joinpath(file_name)
        ls = self.saltear()
        # check if directory exists, if not creates it
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        # check if directory exists (fail safe)
        if dir_path.is_dir():

            # check if file already exists
            if file_path.is_file():

                with open(dir_path.joinpath(file_name), "a") as f:
                    f.write('\n' + self.jujador1Name + ": " + str(self.jujador1Points) + '\t|\t' + self.jujador2Name + ": " + str(self.jujador2Points)+ "\t|" + self.textoganador+'\n')
                    for x in ls:
                        f.write(x[0:3][0]+x[0:3][1]+x[0:3][2]+'\t\t')
                    f.write('\n')
                    for x in ls:
                        f.write(x[3:6][0]+x[3:6][1]+x[3:6][2]+'\t\t')
                    f.write('\n')
                    for x in ls:
                        f.write(x[6:9][0]+x[6:9][1]+x[6:9][2]+'\t\t')
            else:
                with open (dir_path.joinpath(file_name),'w') as f:  
                    f.write('\n' + self.jujador1Name + ": " + str(self.jujador1Points) + '\t|\t' + self.jujador2Name + ": " + str(self.jujador2Points)+ "\t|" + self.textoganador+'\n')
                    for x in ls:
                        f.write(x[0:3][0]+x[0:3][1]+x[0:3][2]+'\t\t')
                    f.write('\n')
                    for x in ls:
                        f.write(x[3:6][0]+x[3:6][1]+x[3:6][2]+'\t\t')
                    f.write('\n')
                    for x in ls:
                        f.write(x[6:9][0]+x[6:9][1]+x[6:9][2]+'\t\t')
                    print('File was created.')

    def analisis(self) -> bool:
        #Mira todas linea de 3 en la escuadra y busca si hay 3 iguales
        #Si hay 3 iguales -> Devuelve False, sino True
        if self.counter >= 5:   # minima cantidad para poder ganar

            for ls in self.todas:
                if (len(set(ls)) == 1 and ls[0] != '-'):
                    return False    #False == hay ganador
        return True
    
    def cambiar_turno(self) -> None:
        #Pasa de x a o y de o a x
        if self.turno == 'x':
            self.turno = 'o'
        else: self.turno = 'x'

        #Cambia de turno usando el string del jugador
        if self.turno1v1 == self.jujador1Name:
            self.turno1v1 = self.jujador2Name
        else: 
            self.turno1v1 = self.jujador1Name

    def assign(self, choice:str) -> None:
        #asigna en las listas que usa el AI
        #Aumenta el counter de cantidad de moviminetos
        #llama a cambiar_turno()

        if choice in self.disponibles:
            self.disponibles.remove(choice)
        else:
            print("Rompiste algo")
            pass
        self.counter += 1

        if choice == 'a1':
            self.a1 = self.turno
            self.fila[0] = self.turno
            self.col1[0] = self.turno
            self.diag1[0] = self.turno
            self.DOUBLE1[0] = self.turno
            self.DOUBLE2[0] = self.turno
            self.DOUBLE3[2] = self.turno

        elif choice == 'a2':
            self.a2 = self.turno
            self.fila[1] = self.turno
            self.col2[0] = self.turno
            self.DOUBLE1[1] = self.turno
            self.DOUBLE3[3] = self.turno

        elif choice == 'a3':
            self.a3 = self.turno
            self.fila[2] = self.turno
            self.col3[0] = self.turno
            self.diag2[0] = self.turno
            self.DOUBLE1[2] = self.turno
            self.DOUBLE3[4] = self.turno
            self.DOUBLE4[4] = self.turno

        elif choice == 'b1':
            self.b1 = self.turno
            self.filb[0] = self.turno
            self.col1[1] = self.turno
            self.DOUBLE2[1] = self.turno
            self.DOUBLE3[1] = self.turno

        elif choice == 'b2':
            self.b2 = self.turno
            self.filb[1] = self.turno
            self.col2[1] = self.turno
            self.diag1[1] = self.turno
            self.diag2[1] = self.turno
            
        elif choice == 'b3':
            self.b3 = self.turno
            self.filb[2] = self.turno
            self.col3[1] = self.turno
            self.DOUBLE1[3] = self.turno
            self.DOUBLE4[3] = self.turno

        elif choice == 'c1':
            self.c1 = self.turno
            self.filc[0] = self.turno
            self.col1[2] = self.turno
            self.diag2[2] = self.turno
            self.DOUBLE2[2] = self.turno
            self.DOUBLE3[0] = self.turno
            self.DOUBLE4[0] = self.turno

        elif choice == 'c2':
            self.c2 = self.turno
            self.filc[1] = self.turno
            self.col2[2] = self.turno
            self.DOUBLE2[2] = self.turno
            self.DOUBLE4[1] = self.turno

        elif choice == 'c3':
            self.c3 = self.turno
            self.filc[2] = self.turno
            self.col3[2] = self.turno
            self.diag1[2] = self.turno
            self.DOUBLE1[4] = self.turno
            self.DOUBLE2[4] = self.turno
            self.DOUBLE4[3] = self.turno

        self.cambiar_turno()

    def seleccionar(self) -> None:
    #Consigue el movimiento que quiere hacer el usuario
    #Llama a assaign()
            choice:str = input("INPUT:")

            if choice in self.disponibles:
                self.assign(choice)
            else:
                print("Volve a intentar")
                self.seleccionar()

    def Empezar(self) -> None:
        self.Menu()

    def ganador1v1(self) -> None:
        # Imprime el partido
        # Suma los puntos acorde el reustado, W +1 E +0.5 L +0
        # Imprime si hubo empate o hubo ganador en el match
        # Decide quien gana depende del dato turno1v1
        # Imprime cuanto puntos lleva cada uno en el game
        # Si hay ganador gaurda en memoria el partido, limited to 5

        print(self)
        if self.analisis():
            print("Empate")
            self.jujador1Points += 0.5
            self.jujador2Points += 0.5
        else:   
            print("Gano", self.turno1v1)
            if self.turno1v1 == self.jujador1Name:
                self.jujador1Points += 1.0
            else: self.jujador2Points += 1.0

            out = 0
            for MEM in self.mems:
                if out == 0 and len(MEM) == 0:
                    MEM.append(self.a1)
                    MEM.append(self.a2)
                    MEM.append(self.a3)
                    MEM.append(self.b1)
                    MEM.append(self.b2)
                    MEM.append(self.b3)
                    MEM.append(self.c1)
                    MEM.append(self.c2)
                    MEM.append(self.c3)
                    out = 1

        print(self.jujador1Name, self.jujador1Points, "puntos")
        print(self.jujador2Name, self.jujador2Points, "puntos")
        return
    
    def finish(self) -> None:
        #Imprime quien gano el game
        # quien gano depende de quien tenga mas puntos caundo se la llama

        if self.jujador1Points > self.jujador2Points:
            self.textoganador = 'Ganador: ' + self.jujador1Name
            
        elif self.jujador1Points < self.jujador2Points:
            self.textoganador = 'Ganador: ' + self.jujador2Name

        else: 
            self.textoganador = 'Empate'
        
        print(self.textoganador)

    def seguir(self, cantidad:int) -> None:
        # Permite continuar el Best of manteniendo los datos

        print("Best of", cantidad+2, "y/n")
        elejir = input()

        if elejir == "y":
            self.juego(cantidad+2)

        elif elejir == "n":
            self.text()
            return
        else:
            print("Volve a intentar")
            self.seguir(cantidad)

    def easySelect(self) -> None:

        choice:str = random.choice(self.disponibles)
        self.assign(choice)
    
    def ezwin(self) -> bool:
        #busca si hay un movimiento que gana y lo juega
        # Si una fila tiene dos iguales y un vacio, elije la posicion vacia
        # Si hay dos lineas que cumplen esto, prefiere la linea que gane el match
        # Llama a double_trouble()

        counter_linea:int = 0
        defend:list[str] = []

        for linea in self.todas:

            cantidad_de_x:int = 0
            cantidad_de_o:int = 0

            for coord in linea:               
                if coord == 'x':
                    cantidad_de_x += 1
                if coord == 'o':
                    cantidad_de_o += 1

            if (self.turno == 'x' and cantidad_de_x == 2 and cantidad_de_o == 0) or (self.turno == 'o' and cantidad_de_o == 2 and cantidad_de_x == 0): #busca las lineas con dos iguales y un vacio
                win = list(set(self.dicNumToLinea[counter_linea]) & set(self.disponibles))      #elije el vacio       
                self.assign(win[0])
                return False
            
            if (self.turno == 'x' and cantidad_de_o == 2 and cantidad_de_x == 0) or (self.turno == 'o' and cantidad_de_x == 2 and cantidad_de_o == 0): #busca las lineas con dos iguales y un vacio
                defend = list(set(self.dicNumToLinea[counter_linea]) & set(self.disponibles))    #elije el vacio
                
            counter_linea += 1

        if len(defend) != 0: #para generar preferencia
                self.assign(defend[0])
                return False
        return self.double_trouble()
    
    def double_trouble(self) -> bool:

    # Busca si hay un moviemto que genere dos mov distintos que ganen en el proximo turno y lo juega
    # Esto esta limitado a los posibles que pueden generar el AI, hay otros que no va a ver pero nunca estaria en 
    # una posicion para que pasen
    # Esto es para defender y atacar
        
        count_x_double_1:int = 0
        count_x_double_2:int = 0
        count_x_double_3:int = 0
        count_x_double_4:int = 0

        for coord in self.DOUBLE1:
            if coord == 'x':
                count_x_double_1 += 1
        for coord in self.DOUBLE2:
            if coord == 'x':
                count_x_double_2 += 1
        for coord in self.DOUBLE3:
            if coord == 'x':
                count_x_double_1 += 1
        for coord in self.DOUBLE4:
            if coord == 'x':
                count_x_double_2 += 1

        if count_x_double_1 == 2 and len(set(self.DOUBLE1)) == 2 and '-' in self.DOUBLE1:
            choice:str = list(set(self.disponibles) & set(self.double1))
            self.assign(random.choice(choice))
            return False

        if count_x_double_2 == 2 and len(set(self.DOUBLE2)) == 2 and '-' in self.DOUBLE2:
            choice:str = list(set(self.disponibles) & set(self.double2))
            self.assign(random.choice(choice))
            return False
        
        if count_x_double_3 == 2 and len(set(self.DOUBLE3)) == 2 and '-' in self.DOUBLE3:
            choice:str = list(set(self.disponibles) & set(self.double3))
            self.assign(random.choice(choice))
            return False

        if count_x_double_4 == 2 and len(set(self.DOUBLE4)) == 2 and '-' in self.DOUBLE4:
            choice:str = list(set(self.disponibles) & set(self.double4))
            self.assign(random.choice(choice))
            return False

        return True

    def HardDefend(self) -> None:

        if self.counter == 1:
            if 'b2' in self.disponibles: # Guarantees atleast draw for CPU
                self.assign('b2')
                self.cpu_center:bool = 1
            else: 
                eleccion = random.choice(self.corners)
                self.assign(eleccion)
                self.corners.remove(eleccion)

        elif self.counter == 3:
            if self.cpu_center:
                eleccion = random.choice(list(set(self.disponibles) - set(self.corners))) #cross
            else:
                eleccion = random.choice(list(set(self.disponibles) & set(self.corners))) #cornes
            self.assign(eleccion)

        else:
            print("RANDOM RANDOM")
            self.easySelect()

    def HardAttack(self) -> None:

        eleccion:str = 'ERROR'

        if self.counter == 0:
                eleccion = random.choice(self.corners)
                random.choice(eleccion)
                self.assign(eleccion)
                self.corners.remove(eleccion)

        elif self.counter == 2:
            if 'b2' in self.disponibles:
                count:int = 0
                for linea in self.square:
                        
                        if len(set(linea)) == 2 and 'o' not in linea:
                            eleccion = list(set(self.squaredic[count])&set(self.disponibles)& set(self.corners))
                            self.assign(eleccion[0])
                            return

                        count += 1
            else:
                if self.a1 == 'x':
                    self.assign('c3')
                elif self.c1 == 'x':
                    self.assign('a3')
                elif self.c3 == 'x':
                    self.assign('a1')
                elif self.a3 == 'x':
                        self.assign('c1')
                        
        elif self.counter == 4:
            if 'b2' in self.disponibles:
                
                for coord in self.corners:
                    if coord in self.disponibles:
                        if coord == 'a1' and 'a2' in self.disponibles and 'b1' in self.disponibles:
                            eleccion = 'a1'
                        elif coord == 'c1' and 'c2' in self.disponibles and 'b1' in self.disponibles:
                            eleccion = 'c1'
                        elif coord == 'a3' and 'a2' in self.disponibles and 'b3' in self.disponibles:
                            eleccion = 'a3'
                        elif coord == 'c3' and 'c2' in self.disponibles and 'b3' in self.disponibles:
                            eleccion = 'c3'
                self.assign(eleccion)
        else:
            print("RANDOM RANDOM")
            self.easySelect()

    def hardSelect(self) -> None:
        #Llama a ezwin(), hard_attack() y hard_defend()
        # en movimientos pares ataca e impares defiende
        if self.counter == 0:
            self.HardAttack()
        elif self.counter == 1:
            self.HardDefend()
        else:
            if self.ezwin():
            #solo entra si no tiene un movimiento que asegura victoria
                # print("NO ezwin, No double", self.counter)
                if self.counter % 2 == 0:
                    self.HardAttack()
                else: self.HardDefend()  

    def Bof(self, cantidad:int) ->None:
        self.juego(cantidad)

    def match_change(self) -> None:
        # asegura que siemrpre cambie quien empieza el match
            if self.empezo  == '':
                self.turno1v1 = self.jujador1Name
                self.empezo = self.jujador1Name

            elif self.empezo == self.jujador1Name:
                self.turno1v1 = self.jujador2Name
                self.empezo = self.jujador2Name

            else:
                self.turno1v1 = self.jujador1Name
                self.empezo = self.jujador1Name

    def jugador(self) -> None:
    # Turno jugador, llama a seleccionar()
        print("")
        print("Turno de", self.turno1v1,"(" + self.turno +")")
        print("Elija entre: ", self.disponibles)
        print(self)          
        self.seleccionar()

    def juego(self, cantidad:int) -> None:

        while(self.jujador1Points < (cantidad + 1)/2 and self.jujador2Points < (cantidad + 1)/2):

            self.match_change()

            while(self.analisis() and self.counter < 9): 


                if self.mode == "PvP" or (self.mode == "PvCPU" and self.turno1v1 == self.jujador1Name):
                    self.jugador()

                elif self.mode == "PvCPU" or self.mode == "CPUvCPU":

                    if self.turno1v1 == "CPU 1 Easy" or self.turno1v1 == "CPU 2 Easy":
                        self.easySelect()

                    elif self.turno1v1 == "CPU Hard" or self.turno1v1 == "CPU 2 Hard":
                        self.hardSelect()

                # self.cambiar_turno1v1() #elejir y cambiar

            self.cambiar_turno()#para ganador
            self.ganador1v1()
            self.clear()

        self.finish()
        self.seguir(cantidad)

    def select_CPU1(self) -> None:

        dif:str = input( "1. Easy\n2. Hard\n")
        if dif == '1':
            self.jujador1Name = "CPU 1 Easy"
        elif dif == '2':
            self.jujador1Name = "CPU 1 Hard"

    def select_CPU2(self) -> None: 

        dif:str = input( "1. Easy\n2. Hard\n")
        if dif == '1':
            self.jujador2Name = "CPU 2 Easy"
        elif dif == '2':
            self.jujador2Name = "CPU 2 Hard"

    def select_BestOf(self) -> None:
    # User imputs Bof and calls Bof()

        Bo:str = input("\n1. Best of 1\n2. Best of 3\n3. Best of 5\n")
            
        if Bo == '2':
            var = 3
        elif Bo == '3':
            var = 5
        else: var = 1
        
        self.Bof(var)

    def select_BestOf_CPUvCPU(self) -> None:
        # User imputs Bof and calls Bof()

            Bo:str = input("\n1. Best of 1\n2. Best of 11\n3. Best of 101\n")
                
            if Bo == '2':
                var = 11
            elif Bo == '3':
                var = 101
            else: var = 1
            
            self.Bof(var)

    def Menu(self) -> None:
        
        choice:str = input("1. PvP \n2. PvCPU \n3. CPUvCPU\n")

        if choice == '1': #1v1
            self.mode = "PvP"
            jug1:str = input("Nombre jugagdor 1:")
            self.jujador1Name = jug1
            self.turno1v1 = jug1
            jug2:str = input("Nombre jugagdor 2:")
            self.jujador2Name = jug2
            self.select_BestOf()
        
        elif choice == '2': #1vcpu
            self.mode = "PvCPU"
            jug1:str = input("Nombre jugagdor 1:")
            self.jujador1Name = jug1
            self.turno1v1 = jug1
            print("\nDifficulty:")
            self.select_CPU2()
            self.select_BestOf()

        elif choice == '3': #cpuvcpu
            self.mode = "CPUvCPU"
            print("\nCPU 1:")
            self.select_CPU1()
            print("CPU 2:")
            self.select_CPU2()
            self.select_BestOf_CPUvCPU()
    
    def ass(self, choice, turno):
        #FOR DEBUGGING
        self.turno = turno
        self.assign(choice)
        
    def __repr__(self) -> str:
        
        print(' ', '1','2','3')
        print('a', self.a1, self.a2, self.a3)
        print('b', self.b1, self.b2, self.b3)
        print('c', self.c1, self.c2, self.c3)
        return "-----------------------------------"


a = Tic()
a.Empezar()


#TODO 

# text imprima en el .txt el tablero final (si hay ganador?)
