# pip install --upgrade PySimpleGUI
import PySimpleGUI as sg
import random
from pathlib import Path
import os
import time


class Tic:

    def __init__(self) -> None:
        self.a1:str = '-'
        self.a2:str = '-'
        self.a3:str = '-'

        self.b1:str = '-'
        self.b2:str = '-'
        self.b3:str = '-'

        self.c1:str = '-'
        self.c2:str = '-'
        self.c3:str = '-'
        self.counter:int = 0

        self.fila:list[self.str] = [self.a1, self.a2, self.a3]
        self.filb:list[self.str] = [self.b1, self.b2, self.b3]
        self.filc:list[self.str] = [self.c1, self.c2, self.c3]

        self.col1:list[self.str] = [self.a1, self.b1, self.c1]
        self.col2:list[self.str] = [self.a2, self.b2, self.c2]
        self.col3:list[self.str] = [self.a3, self.b3, self.c3]

        self.diag1:list[self.str] = [self.a1, self.b2, self.c3]
        self.diag2:list[self.str] = [self.a3, self.b2, self.c1]

        self.todas:list[list[self.str]] = [self.fila, self.filb, self.filc, self.col1, self.col2, self.col3, self.diag1, self.diag2]

        self.disponibles:list[str] = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

        self.turno:str = 'x'

        self.jugador1Name:str = '---'
        self.jugador2Name:str = '---'

        self.jugador1Points:int = 0
        self.jugador2Points:int = 0
        
        self.partidoNUM:int = 0

        self.turno1v1:str = ''

        self.corners:list[str] =  ['a1','a3','c1','c3']

        self.FILa:list[str] = ['a1', 'a2', 'a3']
        self.FILb:list[str] = ['b1', 'b2', 'b3']
        self.FILc:list[str] = ['c1', 'c2', 'c3']

        self.COL1:list[str] = ['a1', 'b1', 'c1']
        self.COL2:list[str] = ['a2', 'b2', 'c2']
        self.COL3:list[str] = ['a3', 'b3', 'c3']

        self.DIAG1:list[str] = ['a1', 'b2', 'c3']
        self.DIAG2:list[str] = ['a3', 'b2', 'c1']

        self.square:list[list[str]] = [self.fila, self.col1, self.filc, self.col3]
        self.squaredic:dict[int:list[str]] = {0:self.FILa, 1:self.COL1, 2:self.FILc, 3:self.COL3}

        self.dicNumToLinea:dict[list] = {0:self.FILa, 1:self.FILb, 2:self.FILc, 3:self.COL1, 4:self.COL2, 5:self.COL3, 6:self.DIAG1, 7:self.DIAG2}

        self.double1:list[str] = ['a1', 'a2', 'a3', 'b3', 'c3']
        self.double2:list[str] = ['a1', 'b1', 'c1', 'c2', 'c3']
        self.double3:list[str] = ['c1', 'b1', 'a1', 'a2', 'a3']
        self.double4:list[str] = ['c1', 'c2', 'c3', 'b3', 'a3']
        self.DOUBLE1:list[self.str] = [self.a1, self.a2, self.a3, self.b3, self.c3]
        self.DOUBLE2:list[self.str] = [self.a1, self.b1, self.c1, self.c2, self.c3]
        self.DOUBLE3:list[self.str] = [self.c1, self.b1, self.a1, self.a2, self.a3]
        self.DOUBLE4:list[self.str] = [self.c1, self.c2, self.c3, self.b3, self.a3]

        self.cpu_center:int = 0

        self.textoganador:str = 'ERROR'

        self.mode:str = '' #PvP, PvCPU, CPUvCPU
        self.diffculty:str = '' #PvP, PvCPU = EASY, HARD, CPUvCPU = easyX2 easyHARD hardX2

        self.empezo:str = ''

        self.mem1:list[str] = []
        self.mem2:list[str] = []
        self.mem3:list[str] = []
        self.mem4:list[str] = []
        self.mem5:list[str] = []
        self.mems:list[self.list[str]] = [self.mem1, self.mem2, self.mem3, self.mem4, self.mem5]

        self.modes:list[str]= ['PvP' , 'PvCPU', 'CPUvCPU']
        self.layout = []
        self.window = sg.Window("")

        self.tat:bool = 0
        self.winner:str = ''

        self.EXIT:bool = 0

        self.keytit:str = 'TITLE'
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

        self.tat = 0
    def saltear(self) -> list[list[str]]:
        i:int = 4
        while i>=0 and len(self.mems[i]) == 0:
            if len(self.mems[i]) == 0:
                i = i-1

        return self.mems[0:i+1]  
    def text(self) -> None:

        dir_path = Path.cwd().joinpath(r"Tateti scores")
        file_name = self.jugador1Name + " vs " + self.jugador2Name + '.txt'
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
                    f.write('\n' + self.jugador1Name + ": " + str(self.jugador1Points) + '\t|\t' + self.jugador2Name + ": " + str(self.jugador2Points)+ "\t|" + self.textoganador)
                    if len(ls) != 0:
                        f.write("\n")
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
                    f.write('\n' + self.jugador1Name + ": " + str(self.jugador1Points) + '\t|\t' + self.jugador2Name + ": " + str(self.jugador2Points)+ "\t|" + self.textoganador)
                    if len(ls) != 0:
                        f.write("\n")
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
        if self.turno1v1 == self.jugador1Name:
            self.turno1v1 = self.jugador2Name
        else: 
            self.turno1v1 = self.jugador1Name
    def assign(self, choice:str) -> None:
        #asigna en las listas que usa el AI
        #Aumenta el counter de cantidad de moviminetos
        #llama a cambiar_turno()

        if self.mode == 'PvCPU':
            self.window[choice].update(self.turno)

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

        if self.mode == 'PvCPU' or self.mode == "PvP":
            self.window[self.keytit].update("Turno de: " + self.turno1v1 + '('+ self.turno +')')
    def seleccionar(self) -> None:
        while True:
            event, values = self.window.read()
            if event in self.disponibles:
                self.window[event].update(self.turno)
                self.assign(event)        
            if event == sg.WIN_CLOSED:
                self.EXIT = 1
                break
            break
    def Empezar(self) -> None:
        self.Menu()
    def ganador1v1(self) -> None:
        # Suma los puntos acorde el reustado, W +1 E +0.5 L +0
        # Decide quien gana depende del dato turno1v1
        # Imprime cuanto puntos lleva cada uno en el game
        # Si hay ganador guarda en memoria el partido, limited to 5

        if self.analisis():
            self.jugador1Points += 0.5
            self.jugador2Points += 0.5
        else:   
            if self.turno1v1 == self.jugador1Name:
                self.jugador1Points += 1.0
            else: self.jugador2Points += 1.0

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
        return
    def finish(self) -> None:
        # quien gano depende de quien tenga mas puntos caundo se la llama
        if self.jugador1Points > self.jugador2Points:
            self.textoganador = 'Ganador: ' + self.jugador1Name
            self.winner = self.jugador1Name
            
        elif self.jugador1Points < self.jugador2Points:
            self.textoganador = 'Ganador: ' + self.jugador2Name
            self.winner = self.jugador2Name

        else: 
            self.textoganador = 'Empate'
    def last_screen(self) -> None:
        self.layout =[]
        if self.textoganador == 'Empate':
            text = 'Empate'
        else: text = 'Ganador:'
        exit_button = sg.Button("Exit", expand_x=True, font=("Helvetica",20))
        self.layout = [
                        [sg.T(text,justification='center', font=("Helvetica",35))],
                        [sg.T('', font=("Helvetica",35))],
                        [sg.T(self.winner, font=("Helvetica",20))],
                        [exit_button]
                      ]
        if self.EXIT == 0:
            self.window = sg.Window('Exit', self.layout,margins=(200, 200), element_justification='center')
            while True:
                event, values = self.window.read()
                if event == sg.WIN_CLOSED:
                    break
                if event == "Exit":
                    self.text()
                    self.window.close()
                self.window.close()
                break
    def seguir(self, cantidad:int) -> None:
        
        self.layout = []
        text1 = self.jugador1Name + ": " + str(self.jugador1Points)
        text2 = self.jugador2Name + ": " + str(self.jugador2Points)
        BoX_button = sg.Button(f"Best of {cantidad+2}" , key= "Bof", expand_x=True, font=("Helvetica",20))
        self.layout = [
                        [sg.T("Puntaje", font=("Helvetica",35))],
                        [sg.T("", key = '000')],
                        [sg.T(text1, font=("Helvetica",20))],
                        [sg.T(text2, font=("Helvetica",20))],
                        [sg.T("", key = '001')],
                        [sg.T("", key = '002')],
                        [BoX_button],
                        [sg.Button("Finish", bind_return_key=True, expand_x=True, font=("Helvetica",20))]
                      ]
        self.window = sg.Window('Continue?', self.layout,margins=(200, 200), element_justification='center')

        if self.EXIT == 0:
            while True:
                event, values = self.window.read()
                if event == sg.WIN_CLOSED:
                    break
                if event == "Bof":
                    self.window.close()
                    self.juego(cantidad+2)                
                elif event == 'Finish':
                    self.window.close()
                    self.last_screen()

                self.window.close()
                break
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
                if self.counter % 2 == 0:
                    self.HardAttack()
                else: self.HardDefend()  
    def Bof(self, cantidad:int) ->None:
        self.juego(cantidad)
    def match_change(self) -> None:
        # asegura que siemrpre cambie quien empieza el match
            if self.empezo  == '':
                self.turno1v1 = self.jugador1Name
                self.empezo = self.jugador1Name

            elif self.empezo == self.jugador1Name:
                self.turno1v1 = self.jugador2Name
                self.empezo = self.jugador2Name

            else:
                self.turno1v1 = self.jugador1Name
                self.empezo = self.jugador1Name
    def button_game(self,coord:str):
        return sg.Button('', key = str(coord), size=(3,1), font=("Helvetica",50))
    def jugador(self) -> None:
    # Turno jugador, llama a seleccionar()    
        self.seleccionar()
    def display_game(self) -> None:
        ls = ['a', 'b', 'c']
        l5 = ['1', '2', '3']

        if self.tat == 0 and self.EXIT == 0:
            self.window.close()
            self.layout = []
            text0 = [sg.T("Turno de: " + self.turno1v1 + '('+ self.turno +')', font=("Helvetica",20), key = 'TITLE')]
            text1 = '\n' + self.jugador1Name + ": " + str(self.jugador1Points)
            text2 = self.jugador2Name + ": " + str(self.jugador2Points)
            self.layout= [text0,[[self.button_game(f'{letter}{num}') for num in l5] for letter in ls],[sg.T(text1, font=("Helvetica",20))],[sg.T(text2, font=("Helvetica",20))]]

            self.window = sg.Window('Ta-Te-Ti', self.layout,margins=(200, 100), finalize=True)
            self.tat =1
    def juego(self, cantidad:int) -> None:

        while(self.jugador1Points < (cantidad + 1)/2 and self.jugador2Points < (cantidad + 1)/2 and self.EXIT == 0):

            self.match_change()

            if self.mode == "PvP" or self.mode == "PvCPU":
                self.display_game()

            while(self.analisis() and self.counter < 9 and self.EXIT == 0): 


                if self.mode == "PvP" or (self.mode == "PvCPU" and self.turno1v1 == self.jugador1Name):
                    self.jugador()

                elif self.mode == "PvCPU" or self.mode == "CPUvCPU":

                    if self.turno1v1 == "CPU 1 Easy" or self.turno1v1 == "CPU 2 Easy":
                        self.easySelect()

                    elif self.turno1v1 == "CPU 1 Hard" or self.turno1v1 == "CPU 2 Hard":
                        self.hardSelect()
            self.window.close()
            self.cambiar_turno()#para ganador
            self.ganador1v1()
            self.clear()

        self.finish()
        self.seguir(cantidad)
    def select_CPU1(self) -> None:

        dif:str = input( "1. Easy\n2. Hard\n")
        if dif == '1':
            self.jugador1Name = "CPU 1 Easy"
        elif dif == '2':
            self.jugador1Name = "CPU 1 Hard"
    def select_CPU2(self) -> None: 

        dif:str = input( "1. Easy\n2. Hard\n")
        if dif == '1':
            self.jugador2Name = "CPU 2 Easy"
        elif dif == '2':
            self.jugador2Name = "CPU 2 Hard"
    def select_BestOf(self) -> None:
    # User imputs Bof and calls Bof()

        ls = [1, 3, 5, 1, 11 , 111]

        self.layout = []
        inText = [sg.Text("Manual input:", font=("Helvetica",20), expand_x=True),sg.In(key="-IN-",focus=True,  size=(28)),sg.Button("OK",bind_return_key=True)]
        Best_Text = [sg.Text("Best of", font=("Helvetica",35), justification= 'center')]
        button_small_num = [[sg.Button(f'{num}', key=num, size=(15,1), font=("Helvetica",35))]for num in ls[0:3]]
        button_big_num = [[sg.Button(f'{num}', key=num, size=(15,1), font=("Helvetica",35))]for num in ls[3:6]]
        
        if self.mode == 'PvP' or self.mode == 'PvCPU':
            self.layout = [Best_Text,button_small_num]
        elif self.mode == 'CPUvCPU':
            self.layout = [button_big_num, inText]


        if self.EXIT == 0:
            self.window = sg.Window('Best of', self.layout,margins=(200, 200),finalize=True, element_justification='center')
            while True:
                event, values = self.window.read()
                if event in ls:         
                    self.window.close()
                    self.Bof(event)
                    break
                if event == "OK" and self.mode == 'CPUvCPU':
                    if len(values['-IN-']) == 0:
                        self.Bof(1)
                    else: 
                        self.window.close()
                        self.Bof(int(values['-IN-']))
                    self.window.close()
                if event == sg.WIN_CLOSED:
                    self.EXIT = 1
                    break        
    def button_mode(self,mode:str):
     return [sg.Button(mode, key = str(mode), size=(15,1), font=("Helvetica",35))]
    def Name_select_layout(self): 

        self.layout = []
        ok_cancel= [sg.Button("OK",bind_return_key=True ,size=(10), font=("Helvetica",25)),sg.Button("Cancel",size=(10), font=("Helvetica",25))]
        player1 = [sg.Text("Nombre jugador 1:", font=("Helvetica",25)),sg.In(key="name1",focus=True,size=(20))]
        player2 = [sg.Text("Nombre jugador 2:", font=("Helvetica",25)),sg.In(key="name2",size=(20))]
        cPU0 = [sg.Text("CPU:",font=("Helvetica",25)),sg.Button("Easy",key="CPU2 Easy",font=("Helvetica",15)),sg.Button("Hard",key="CPU2 Hard",font=("Helvetica",15))]
        cPU1 = [sg.Text("CPU 1:",font=("Helvetica",25)),sg.Button("Easy",key="CPU1 Easy",font=("Helvetica",15)),sg.Button("Hard",key="CPU1 Hard",font=("Helvetica",15))]
        cPU2 = [sg.Text("CPU 2:",font=("Helvetica",25)),sg.Button("Easy",key="CPU2 Easy",font=("Helvetica",15)),sg.Button("Hard",key="CPU2 Hard",font=("Helvetica",15))]
        space = [sg.T('')]

        if self.mode == "PvP":       
            self.layout = [player1, player2, space, ok_cancel]
        elif self.mode == 'PvCPU':
            self.layout = [player1, cPU0, space, ok_cancel]
        elif self.mode == 'CPUvCPU':
            self.layout = [cPU1, cPU2, space, ok_cancel]
  
        self.window = sg.Window('Player names', self.layout,margins=(200, 200),finalize=True,element_justification='center')
        if self.EXIT == 0:
            while True:
                event, values = self.window.read()
                if event == "OK":
                    if self.mode == "PvP":
                        if len(values['name1']) > 0:
                            self.jugador1Name = values['name1']
                        if len(values['name2']) > 0:
                            self.jugador2Name = values['name2']
                    elif self.mode == 'PvCPU':
                        if len(values['name1']) > 0:
                            self.jugador1Name = values['name1']
                    elif self.mode == 'CPUvCPU':
                        break
                    self.window.close()
                    break
                if event == "Cancel":
                    self.window.close()
                    self.mode = ""
                    self.Menu()
                    break

                if event == 'CPU1 Easy':
                    self.jugador1Name = 'CPU 1 Easy'
                if event == 'CPU1 Hard':
                    self.jugador1Name = 'CPU 1 Hard'    
                if event == 'CPU2 Easy':
                    self.jugador2Name = 'CPU 2 Easy'
                if event == 'CPU2 Hard':
                    self.jugador2Name = 'CPU 2 Hard'
                    
                if event == sg.WIN_CLOSED:
                    self.EXIT = 1
                    break
                    
            if self.mode == 'PvCPU':
                if self.jugador2Name == '---':
                    self.jugador2Name = random.choice(['CPU 2 Easy','CPU 2 Hard'])

            if self.mode == 'CPUvCPU':
                if self.jugador1Name == '---':
                    self.jugador1Name = random.choice(['CPU 1 Easy','CPU 1 Hard'])
                if self.jugador2Name == '---':
                    self.jugador2Name = random.choice(['CPU 2 Easy','CPU 2 Hard'])
            self.window.close()
            self.select_BestOf()
    def Menu(self) -> None:
        
        self.layout = [self.button_mode(f'{mode}') for mode in self.modes]
        self.window = sg.Window('Menu', self.layout,margins=(200, 200),finalize=True)

        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                self.EXIT = 1
                break
            if event == "PvP":
                self.mode = "PvP"                
            elif event == 'PvCPU':
                self.mode = "PvCPU"
            elif event == 'CPUvCPU':
                self.mode = "CPUvCPU"
            self.window.close()
            break
        if self.EXIT == 0:
            self.Name_select_layout()
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

tic = Tic()
tic.Empezar()


#TODO
#fix when nadie gana e imprime lineas vacias en el archivo
