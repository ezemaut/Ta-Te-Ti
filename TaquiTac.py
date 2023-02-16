import PySimpleGUI as sg
import random
from pathlib import Path
import os




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

        self.cpu_center:int = 0
        self.visi:bool = 1
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

        self.tat:bool = 0
        self.winner:str = ''

        self.EXIT:bool = 0
        self.cantidad:int = 0

        self.keytit:str = 'TITLE'
        
        self.ok_cancel= sg.Button("OK",bind_return_key=True ,size=(10), font=("Helvetica",25)),sg.Button("Cancel",size=(10), font=("Helvetica",25))
        self.player1 = [sg.Text("Nombre jugador 1:", visible=False, font=("Helvetica",25), key = 'j1'),sg.In(key="name1",focus=True,size=(20), visible=False)]
        self.player2 = [sg.Text("Nombre jugador 2:", visible=False, font=("Helvetica",25), key = 'j2'),sg.In(key="name2",size=(20), visible=False)]
        self.cpu0_text = [sg.Text("CPU:\t",font=("Helvetica",25), visible=False, key = 'C0')]
        self.cpu1_text = [sg.Text("CPU 1:\t",font=("Helvetica",25), visible=False, key = 'C1')]
        self.cpu2_text = [sg.Text("CPU 2:\t",font=("Helvetica",25), visible=False, key = 'C2')]
        self.cpu1_butt = [sg.Button("Easy",key="CPU1 Easy",font=("Helvetica",20), visible=False),sg.Button("Hard",key="CPU1 Hard",font=("Helvetica",20), visible=False)]
        self.cpu2_butt = [sg.Button("Easy",key="CPU2 Easy",font=("Helvetica",20), visible=False),sg.Button("Hard",key="CPU2 Hard",font=("Helvetica",20), visible=False)]
        self.cPU1 = self.cpu1_text + self.cpu1_butt
        self.space0 = [sg.T('\n', key = "00000")]
        self.space1 = [sg.T('\n\n', key = "00001")]
        self.XvX_list = ['j1', "name1", 'j2', "name2", 'C0', 'C1', 'C2', "CPU1 Easy", "CPU1 Hard", "CPU2 Easy", "CPU2 Hard"]
        
        self.ls = [1, 3, 5, 1, 11 , 111]
        self.inText = [sg.Text("Manual input:", font=("Helvetica",20), key ='MI', expand_x=True),sg.In(key="-IN-",focus=True,  size=(28)),sg.Button("GO",bind_return_key=True,focus=True)]
        self.Best_Text = sg.Push(),sg.Text("Best of", font=("Helvetica",35), key = "head", justification='center'),sg.Push()
        self.Best_Text1 = sg.Push(),sg.Text("Best of", font=("Helvetica",35), key = "head1", justification='center'),sg.Push()
        self.button_small_num = [[sg.Button(f'{num}', key=str(num)+'small', size=(15,1), font=("Helvetica",35))]for num in self.ls[0:3]]
        self.button_big_num = [[sg.Button(f'{num}', key=str(num)+'big', size=(15,1), font=("Helvetica",35))]for num in self.ls[3:6]]
        self.button_back = sg.Push(),sg.Button("Back",size=(10), font=("Helvetica",20),expand_x=True, key = "bc"),sg.Push()
        button_back1 = sg.Button("Back",size=(10), font=("Helvetica",20), key = "bk")
        Visi_button_CPU = sg.Button("Visulisation on/off", key = "off", font=("Helvetica",20), tooltip = "On by default")
        last_row_buttons_cpu = [sg.Push(),button_back1, Visi_button_CPU,sg.Push()]

        self.layout_START = [self.button_mode(f'{mode}') for mode in self.modes]
        self.layout_XvX =    [self.player1+self.cPU1, 
                              self.space0,
                              self.player2+self.cpu0_text+self.cpu2_text+self.cpu2_butt, 
                              self.space1, 
                              self.ok_cancel,]
                    
        self.layout_BOF_small = [self.Best_Text]
        self.layout_BOF_small += self.button_small_num
        self.layout_BOF_small.append(self.button_back)
        
        self.layout_BOF_big = [self.Best_Text1]
        self.layout_BOF_big += self.button_big_num
        self.layout_BOF_big.append(self.inText)
        self.layout_BOF_big.append(last_row_buttons_cpu)

        letters_display = ['a', 'b', 'c']
        l5 = ['1', '2', '3']

        text0_game = [sg.T("Turno de: " + self.turno1v1 + '('+ self.turno +')', font=("Helvetica",20), key = 'TITLE')]
        text1_game = '\n' + self.jugador1Name + ": " + str(self.jugador1Points)
        text2_game = self.jugador2Name + ": " + str(self.jugador2Points)
        self.layout_game = [text0_game]
        self.layout_game += [[self.button_game(f'{letter}{num}') for num in l5] for letter in letters_display]
        self.layout_game.append([sg.T(text1_game, font=("Helvetica",20), key = "game1")])
        self.layout_game.append([sg.T(text2_game, font=("Helvetica",20), key = "game2")])
    
        Next_button_CPU = sg.Button("Next", key = "Next",size=(7), font=("Helvetica",25))
        Visi_off_CPU = sg.Button("Visualisation off", key = "offf",size=(13), font=("Helvetica",25))
        line_cpu = sg.Push(),Next_button_CPU,Visi_off_CPU,sg.Push()
        names_CPU_1 = [sg.T('', font=("Helvetica",10), key = "NC1")]
        names_CPU_2 = [sg.T('', font=("Helvetica",10), key = "NC2")]
        
        self.layout_game_CPU = [[sg.Button('',size =(5,1), font=("Helvetica", 40), disabled_button_color = ("white"), key = x+y, disabled=True)for x in l5] for y in letters_display]
        self.layout_game_CPU.append(names_CPU_1)
        self.layout_game_CPU.append(names_CPU_2)
        self.layout_game_CPU.append(line_cpu)

        self.text1_continue = self.jugador1Name + ": " + str(self.jugador1Points)
        self.text2_continue = self.jugador2Name + ": " + str(self.jugador2Points)
        BoX_button = sg.Button(f"Best of {self.cantidad+2}" , key= "Bof", expand_x=True, font=("Helvetica",20))
        self.layout_continue = [
                        [sg.T("Puntaje", font=("Helvetica",35))],
                        [sg.T("", key = '0000')],
                        [sg.T(self.text1_continue, font=("Helvetica",20), key = 'txt_cont1')],
                        [sg.T(self.text2_continue, font=("Helvetica",20), key = 'txt_cont2')],
                        [sg.T("", key = '100')],
                        [sg.T("", key = '200')],
                        [BoX_button],
                        [sg.Button("Finish", bind_return_key=True, expand_x=True, font=("Helvetica",20))]
                      ]
        
        if self.textoganador == 'Empate':
            text_end = 'Empate'
        else: text_end = 'Ganador:'
        exit_button = sg.Button("Exit", expand_x=True, font=("Helvetica",20), key= 'Exit')
        again_button = sg.Button("Volver a jugar?", expand_x=True, font=("Helvetica",20), key= 'Again')
        self.layout_end = [
                        [sg.T(text_end,justification='center', font=("Helvetica",35), key = 'txt_end')],
                        [sg.T('', font=("Helvetica",35), key= "320")],
                        [sg.Push(),sg.T(self.winner, font=("Helvetica",20), key = 'winner', justification= 'center'),sg.Push()],
                        [exit_button],
                        [again_button]
                      ]

        layout1 = sg.Column(self.layout_START, key='-COL1-')
        layout2 = sg.Column(self.layout_XvX, visible=False, key='-COL2-')
        layout3 = sg.Column(self.layout_BOF_small, visible=False, key='-COL3-')
        layout3_5 = sg.Column(self.layout_BOF_big, visible=False, key='-COL3.5-')
        layout4 = sg.Column(self.layout_game, visible=False, key='-COL4-')
        layout4_5 = sg.Column(self.layout_game_CPU, visible=False, key='-COL4.5-')
        layout5 = sg.Column(self.layout_continue, visible=False, key='-COL5-')
        layout6 = sg.Column(self.layout_end, visible=False, key='-COL6-')


        self.layout = [[layout1, layout2, layout3, layout3_5,layout4, layout4_5, layout5, layout6]]
        self.window = sg.Window('Tic-Tac-Toe', self.layout,margins=(100, 240), element_justification='center', finalize=True)
        self.window.maximize()

        self.memwinner =[]
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

        self.cpu_center = 0

        self.textoganador = 'ERROR'

        self.mem1 = []
        self.mem2 = []
        self.mem3 = []
        self.mem4 = []
        self.mem5 = []  

        self.tat = 0
        if self.EXIT == 0:
            self.window['off'].set_tooltip('On by default') 
    def clear_board(self) -> None:     
        lista = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
        lsi = ['1a', '2a', '3a', '1b', '2b', '3b', '1c', '2c', '3c']
        if self.EXIT == 0:
            if self.mode == 'CPUvCPU':
                for x in lsi:
                    self.window[x].update("")
            else:
                for x in lista:
                    self.window[x].update("")
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
                            f.write(x[0:3][0]+x[0:3][1]+x[0:3][2]+'\t\t\t')
                        f.write('\n')
                        for x in ls:
                            f.write(x[3:6][0]+x[3:6][1]+x[3:6][2]+'\t\t\t')
                        f.write('\n')
                        for x in ls:
                            f.write(x[6:9][0]+x[6:9][1]+x[6:9][2]+'\t\t\t')
                        f.write('\n')
                        for x in self.memwinner:
                            f.write(f'{x}\t')
                        f.write('\n')
            else:
                with open (dir_path.joinpath(file_name),'w') as f:  
                    f.write('\n' + self.jugador1Name + ": " + str(self.jugador1Points) + '\t|\t' + self.jugador2Name + ": " + str(self.jugador2Points)+ "\t|" + self.textoganador)
                    if len(ls) != 0:
                        f.write("\n")
                        for x in ls:
                            f.write(x[0:3][0]+x[0:3][1]+x[0:3][2]+'\t\t\t')
                        f.write('\n')
                        for x in ls:
                            f.write(x[3:6][0]+x[3:6][1]+x[3:6][2]+'\t\t\t')
                        f.write('\n')
                        for x in ls:
                            f.write(x[6:9][0]+x[6:9][1]+x[6:9][2]+'\t\t\t')
                        f.write('\n')
                        for x in self.memwinner:
                            f.write(f'{x}\t')
                        f.write('\n')
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
        if self.EXIT == 0:

            event = 'temp'
            if self.visi == 1:
                event, values = self.window.read()
            
            if event == sg.WIN_CLOSED:
                self.EXIT = 1
            
            if choice == 'ERROR': #DEBUGGING
                print(self.counter,"ROTO")
                print(self)
                self.clear()
                return

            if self.mode == 'PvCPU':
                self.window[choice].update(self.turno)
            if self.mode == 'CPUvCPU' and self.visi == 1 and self.EXIT == 0:
                swap = choice[1] + choice[0]
                self.window[swap].update(self.turno)

            if choice in self.disponibles:
                self.disponibles.remove(choice)
            else:
                print(type(choice))
                print("Rompiste algo")
                pass
            self.counter += 1

            if choice == 'a1':
                self.a1 = self.turno
                self.fila[0] = self.turno
                self.col1[0] = self.turno
                self.diag1[0] = self.turno

            elif choice == 'a2':
                self.a2 = self.turno
                self.fila[1] = self.turno
                self.col2[0] = self.turno

            elif choice == 'a3':
                self.a3 = self.turno
                self.fila[2] = self.turno
                self.col3[0] = self.turno
                self.diag2[0] = self.turno

            elif choice == 'b1':
                self.b1 = self.turno
                self.filb[0] = self.turno
                self.col1[1] = self.turno

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

            elif choice == 'c1':
                self.c1 = self.turno
                self.filc[0] = self.turno
                self.col1[2] = self.turno
                self.diag2[2] = self.turno

            elif choice == 'c2':
                self.c2 = self.turno
                self.filc[1] = self.turno
                self.col2[2] = self.turno

            elif choice == 'c3':
                self.c3 = self.turno
                self.filc[2] = self.turno
                self.col3[2] = self.turno
                self.diag1[2] = self.turno

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
                if len(self.memwinner) <5:
                    self.memwinner.append(self.jugador1Name)
                # if self.jugador1Name == "CPU 1 Easy": #debugging
                #     print("llora")
                #     print(self)
            else:
                self.jugador2Points += 1.0
                if len(self.memwinner) <5:                    
                    self.memwinner.append(self.jugador2Name)

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
        self.window['-COL5-'].update(visible=False)

        if self.textoganador == 'Empate':
            text_end = 'Empate'
        else: text_end = 'Ganador:'
        self.window['txt_end'].update(text_end)
        self.window['winner'].update(self.winner)
        self.window['-COL6-'].update(visible=True)

        
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                self.EXIT = 1
                break
            if event == "Exit":
                self.text()
                self.window.close()
            if event == 'Again':
                self.text()
                self.clear()
                self.clear_board()
                self.window['-COL6-'].update(visible=False)
                self.window['-COL1-'].update(visible=True)
                self.jugador1Name= '---'
                self.jugador2Name= '---'
                self.jugador1Points= 0
                self.jugador2Points= 0
                self.mode = '' 
                self.visi =1

                self.Empezar()
            break
    def seguir(self, cantidad:int) -> None:
        if self.EXIT == 0:
            self.cantidad = cantidad
            self.text1_continue = self.jugador1Name + ": " + str(self.jugador1Points)
            self.text2_continue = self.jugador2Name + ": " + str(self.jugador2Points)

            self.window['-COL4-'].update(visible=False)
            self.window['-COL4.5-'].update(visible=False)
            self.window['Bof'].update(f"Best of {self.cantidad+2}")
            self.window['txt_cont1'].update(self.text1_continue)
            self.window['txt_cont2'].update(self.text2_continue)
            self.window['-COL5-'].update(visible=True)

            while True:
                event, values = self.window.read()
                if event == sg.WIN_CLOSED:
                    break
                if event == "Bof":
                    self.window['-COL5-'].update(visible=False)
                    if self.mode == 'CPUvCPU':
                        self.window['-COL4.5-'].update(visible=True)
                    else:
                        self.window['-COL4-'].update(visible=True)
                    self.juego(cantidad+2)                
                elif event == 'Finish':
                    self.last_screen()
                break          
    def easySelect(self) -> None:
        choice:str = random.choice(self.disponibles)
        if choice in self.corners:
            self.corners.remove(choice)
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
        return True
    def double_trouble(self) -> bool:
    # Busca si hay un moviemto que genere dos mov distintos que ganen en el proximo turno y lo juega
    # Esto esta limitado a los posibles que pueden generar el AI, hay otros que no va a ver pero nunca estaria en 
    # una posicion para que pasen
    # Esto es para defender y atacar

        if self.counter == 3:
            if len(set(self.diag1)) == 2 and '-' not in self.diag1 or len(set(self.diag2)) == 2 and '-' not in self.diag2:
                if self.b2 == 'o':
                    self.assign(random.choice(list(set(self.disponibles)-set(self.corners))))
                else:  
                    self.assign(random.choice(list(set(self.disponibles)&set(self.corners))))
                return False
            
        turn =  'x'
        if self.turno == 'x':
            turn = 'o'

        for posible in self.disponibles:
            #Crea sistema paralelo
            TEMPfila:list[self.str] = [self.a1, self.a2, self.a3]
            TEMPfilb:list[self.str] = [self.b1, self.b2, self.b3]
            TEMPfilc:list[self.str] = [self.c1, self.c2, self.c3]
            TEMPcol1:list[self.str] = [self.a1, self.b1, self.c1]
            TEMPcol2:list[self.str] = [self.a2, self.b2, self.c2]
            TEMPcol3:list[self.str] = [self.a3, self.b3, self.c3]
            TEMPdiag1:list[self.str] = [self.a1, self.b2, self.c3]
            TEMPdiag2:list[self.str] = [self.a3, self.b2, self.c1]
            TEMPtodas:list[list[str]] = [TEMPfila, TEMPfilb, TEMPfilc, TEMPcol1, TEMPcol2, TEMPcol3, TEMPdiag1, TEMPdiag2]         
            #asigna en el sistema paralelo
            if posible == 'a1':
                TEMPfila[0] = turn
                TEMPcol1[0] = turn
                TEMPdiag1[0] = turn
            elif posible == 'a2':
                TEMPfila[1] = turn
                TEMPcol2[0] = turn
            elif posible == 'a3':
                TEMPfila[2] = turn
                TEMPcol3[0] = turn
                TEMPdiag2[0] = turn
            elif posible == 'b1':
                TEMPfilb[0] = turn
                TEMPcol1[1] = turn
            elif posible == 'b2':
                TEMPfilb[1] = turn
                TEMPcol2[1] = turn
                TEMPdiag1[1] = turn
                TEMPdiag2[1] = turn
            elif posible == 'b3':
                TEMPfilb[2] = turn
                TEMPcol3[1] = turn
            elif posible == 'c1':
                TEMPfilc[0] = turn
                TEMPcol1[2] = turn
                TEMPdiag2[2] = turn
            elif posible == 'c2':
                TEMPfilc[1] = turn
                TEMPcol2[2] = turn
            elif posible == 'c3':
                TEMPfilc[2] = turn
                TEMPcol3[2] = turn
                TEMPdiag1[2] = turn

            counter_linea:int = 0
            necesita2:int = 0
            for linea in TEMPtodas:  # si hay double lo juega, para defender y atacar
                cantidad_de_space:int = 0
                if len(set(linea)) == 2: #busca las lineas con dos iguales y un vacio
                    for coord in linea:               
                        if coord == '-':
                            cantidad_de_space += 1
                    if  cantidad_de_space == 1:
                        necesita2 +=1
                    if necesita2 == 2:
                        self.assign(posible)
                        return False
                counter_linea += 1

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
            if eleccion not in self.disponibles:
                print("HardDefend", eleccion)
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
                        ele = list(set(self.squaredic[count])&set(self.disponibles)& set(self.corners))
                        eleccion = ele[0]
                        self.assign(eleccion)
                        return
                    count += 1

            else: #BEST PLAY = Draw/ B2 played in move 1
                if self.a1 == 'x' and 'c3' in self.disponibles:
                    eleccion = 'c3'
                elif self.c1 == 'x' and 'a3' in self.disponibles:
                    eleccion = 'a3'
                elif self.c3 == 'x' and 'a1' in self.disponibles:
                    eleccion = 'a1'
                elif self.a3 == 'x' and 'c1' in self.disponibles:
                    eleccion = 'c1'
                else:
                    eleccion = random.choice(self.corners)
                
            self.assign(eleccion)
                        
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
            if self.ezwin() and self.double_trouble():
            #solo entra si no tiene un movimiento que asegura victoria
                if self.counter % 2 == 0:
                    self.HardAttack()
                else: self.HardDefend()  
    def Bof(self, cantidad:int) ->None:
        self.window['-COL3-'].update(visible=False)
        self.window['-COL3.5-'].update(visible=False)
        if self.mode == 'PvP' or self.mode == 'PvCPU':
            self.window['-COL4-'].update(visible=True)
        else:
            if self.visi == 1:
                self.window['-COL4.5-'].update(visible=True)
            else:
                self.window['-COL4.5-'].update(visible=False)
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
        self.window['TITLE'].update("Turno de: " + self.turno1v1 + '('+ self.turno +')')
        self.window['game1'].update('\n' + self.jugador1Name + ": " + str(self.jugador1Points))
        self.window['game2'].update(self.jugador2Name + ": " + str(self.jugador2Points))
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

                if self.mode == "CPUvCPU" and self.visi == 1 and self.EXIT == 0:
                    self.window['NC1'].update('\n' + self.jugador1Name + ": " + str(self.jugador1Points))
                    self.window['NC2'].update(self.jugador2Name + ": " + str(self.jugador2Points))
                    self.wait()

            self.cambiar_turno()#para ganador
            self.ganador1v1()
            self.clear()
            self.clear_board()

        self.finish()
        self.seguir(cantidad)
    def select_BestOf(self) -> None:
        help = ['1small', '3small', '5small', '1big', '11big' , '111big']
        if self.EXIT == 0:
            if self.mode == 'CPUvCPU':
                self.window['-COL3.5-'].update(visible=True)
            else:
                self.window['-COL3-'].update(visible=True)

            while True:
                event, values = self.window.read()
                if event in help:
                    i=0
                    num =''
                    while event[i] in '135':                   
                        num += event[i]
                        i += 1
                    self.Bof(int(num))
                    break    
                if event == "bc" or event == "bk":
                    self.window['-COL3.5-'].update(visible=False)
                    self.window['-COL3-'].update(visible=False)
                    self.window['-COL2-'].update(visible=True)
                    self.Name_select_layout()
                    break
                if event == "GO" and self.mode == 'CPUvCPU':
                    if len(values['-IN-']) == 0:
                        self.Bof(1)
                    else: 
                        self.Bof(int(values['-IN-']))         
                if event == 'off':
                    if self.visi == 0:
                       self.visi = 1
                       self.window['off'].set_tooltip('ON')  
                    else:
                        self.visi = 0    
                        self.window['off'].set_tooltip('OFF')   
                if event == sg.WIN_CLOSED:
                    self.EXIT = 1
                    break        
    def button_mode(self,mode:str):
     return [sg.Button(mode, key = str(mode), size=(15,1), font=("Helvetica",35))]
    def Name_select_layout(self): 
        
        if self.mode == 'PvP':
            self.window['j1'].update(visible = True)
            self.window['name1'].update(visible = True)
            self.window['j2'].update(visible = True)
            self.window['name2'].update(visible = True)        
        elif self.mode == 'PvCPU':
            self.window['j1'].update(visible = True)
            self.window['name1'].update(visible = True)
            self.window['C0'].update(visible = True)
            self.window["CPU2 Easy"].update(visible = True)
            self.window["CPU2 Hard"].update(visible = True)
        elif self.mode == 'CPUvCPU':
            self.window['C1'].update(visible = True)
            self.window["CPU1 Easy"].update(visible = True)
            self.window["CPU1 Hard"].update(visible = True)
            self.window['C2'].update(visible = True)
            self.window["CPU2 Easy"].update(visible = True)
            self.window["CPU2 Hard"].update(visible = True)


        while True:
            event, values = self.window.read()

            if event == "Cancel":
                self.mode = ""
                self.window[f'-COL2-'].update(visible=False)
                for x in self.XvX_list:
                    self.window[x].update(visible=False)
                self.jugador1Name = '---'
                self.jugador2Name = '---'
                layout = 1
                self.window[f'-COL{layout}-'].update(visible=True)
                self.Menu()

            elif event == "OK":
                if len(values['name1']) > 0:
                    self.jugador1Name = values['name1']
                if len(values['name2']) > 0:
                    self.jugador2Name = values['name2']
                if len(values['name1']) > 0:
                    self.jugador1Name = values['name1']
                break
                  
            elif event == 'CPU1 Easy':
                self.jugador1Name = 'CPU 1 Easy'
            elif event == 'CPU1 Hard':
                self.jugador1Name = 'CPU 1 Hard'    
            elif event == 'CPU2 Easy':
                self.jugador2Name = 'CPU 2 Easy'
            elif event == 'CPU2 Hard':
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

        for x in self.XvX_list:
            self.window[x].update(visible=False)
        self.window['-COL2-'].update(visible=False)
        self.select_BestOf()
    def Menu(self) -> None:
        
        while True:
            event, values = self.window.read()

            if event in (None, 'Exit'):
                break
            if event in self.modes:
                if event == 'PvP':
                    self.window['j1'].update(visible = True)
                    self.window['name1'].update(visible = True)
                    self.window['j2'].update(visible = True)
                    self.window['name2'].update(visible = True)
                    self.mode = 'PvP'
                elif event == 'PvCPU':
                    self.window['j1'].update(visible = True)
                    self.window['name1'].update(visible = True)
                    self.window['C0'].update(visible = True)
                    self.window["CPU2 Easy"].update(visible = True)
                    self.window["CPU2 Hard"].update(visible = True)
                    self.mode = 'PvCPU'
                elif event == 'CPUvCPU':
                    self.window['C1'].update(visible = True)
                    self.window["CPU1 Easy"].update(visible = True)
                    self.window["CPU1 Hard"].update(visible = True)
                    self.window['C2'].update(visible = True)
                    self.window["CPU2 Easy"].update(visible = True)
                    self.window["CPU2 Hard"].update(visible = True)
                    self.mode = 'CPUvCPU'

                self.window['-COL1-'].update(visible=False)
                self.window['-COL2-'].update(visible=True)
                pass
            if event == sg.WIN_CLOSED:
                self.EXIT = 1
                break

            self.Name_select_layout()
    def ass(self, choice, turno):
        #FOR DEBUGGING
        self.turno = turno
        self.assign(choice)
    def wait(self) -> None:
        while True:
            event, values = self.window.read()
            if event in (None, 'Exit'):
                break
            if event == sg.WIN_CLOSED:
                self.EXIT = 1
            if event == "Next":
                break
            if event == 'offf':
                if self.visi == 0:
                   self.visi = 1
                   self.window['offf'].set_tooltip('ON')  
                else:
                    self.visi = 0    
                    self.window['offf'].set_tooltip('OFF')   
    def __repr__(self) -> str:
        
        print(' ', '1','2','3')
        print('a', self.a1, self.a2, self.a3)
        print('b', self.b1, self.b2, self.b3)
        print('c', self.c1, self.c2, self.c3)
        return "-----------------------------------"





tic = Tic()
tic.Empezar()