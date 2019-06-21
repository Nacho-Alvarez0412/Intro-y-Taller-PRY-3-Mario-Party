####################################################################################################  
#                                                                                                  #
#                                                GAME                                              #
#                                                                                                  #
#                                           WARRIORS CLASH                                         #
#                                                                                                  #
#                                                                                                  #
#                                                                                                  #
####################################################################################################

# Ignacio Ávarez Barrantes 2019039643

# Marco Reveiz Rojas 2019053583

####################################################################################################
#                                                                                                  #
#                                              Librerias                                           #
#                                                                                                  #
####################################################################################################

import numpy
import pygame
import sys
import os
import random
import numpy as np
import time
import string

#------ ICON ---------
ICON = pygame.image.load('ICON.png')
pygame.display.set_icon(ICON)

#==================================   INICIALIZACIONES   =============================================


#PROYECTA LA VENTANA EN EL CENTRO DEL MONITOR DE LA COMPUTADORA-----------------
x = 20                                                                         #
y = 40                                                                         #
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)                           #
#-------------------------------------------------------------------------------
pygame.init()  

#=================================   VARIABLES GLOBALES   ============================================

#ESTADO DE VICTORIA

VICTORIA = False

#LISTAS

LISTA = [1,2,3,4,5,6,7,8,9]*2+[10,11,12,13.1,13.2,13.3,14,15]

#FUENTE

MAINFONT = pygame.font.Font("EnglishTowne.ttf", 60)

#COLORES

BLANCO = (255, 255, 255)

NEGRO = (0, 0, 0)

TURQUESA = (0,255,255)

#NOMBRE DE JUGADORES

JUGADOR1 = "NAME"

JUGADOR2 = "NAME"

JUGADOR3 = "NAME"

JUGADOR4 = "NAME"

#INDICES DE JUGADORES

INDICEP1 = 0

INDICEP2 = 0

INDICEP3 = 0

INDICEP4 = 0

#ESTADO DE SELECCION

SELECTION1 = False

SELECTION2 = False

SELECTION3 = False

SELECTION4 = False

#TABLERO DE JUEGO

GAMEBOARD = numpy.zeros((5,8))

#ORDEN DE JUGADORES

ORDER = []

ALEATORIO = 0

TURNO = 0

#MOVIMIENTO JUGADORES

DADO = 0 

DADO_STATE = True

RIVAL = ''

#===============================================   TEXTO  ==============================================     

# Configuracion texto
#E:  Un string, un color, un numero
#S:  No tiene
#D:  Verifica la superficie en la que se escribira el texto

def texto_aux(texto,fuente,color):
    superficie = fuente.render(texto,True,color)
    return superficie, superficie.get_rect()

#E: Tres numeros, un color, un string
#S: Un texto
#D: Crea el texto
                 
def texto(x,y,texto,tamano,color):
    font = pygame.font.Font('Minecraft.ttf',tamano)
    superficie,rectangulo = texto_aux(texto, font,color)
    rectangulo.center= ((x),(y))
    MEDIEVAL.blit(superficie,rectangulo)


#===============================================   MANEJO DE ARCHIVOS  ==============================================    


#E: El path del archivo, un string con formato de lista
#S: Ninguna
#D: Guarda el archivo
def guardar (archivo, strLista):
     fo = open(archivo, "w")
     fo.write(strLista)
     fo.close()

#E:El path del archivo
#S:Un string con el contenido del archivo
#D: Lee el archivo
def leer (archivo):
     fo = open(archivo, "r")
     resultado = fo.read()
     fo.close()
     return resultado


#E: El path del archivo
#S:Una lista
#D:lee un archivo y hace las validaciones para colocarlo en la lista
def cargarArchivo(archivo):
     strResultado = leer(archivo)
     if strResultado != "":
          return eval(strResultado)
     else:
          return []


def refreshGame():
	global DADO
	global JUGADOR1
	global JUGADOR2
	global JUGADOR3
	global JUGADOR4
	global INDICEP1
	global INDICEP2
	global INDICEP3
	global INDICEP4
	global SELECTION1
	global SELECTION2
	global SELECTION3
	global SELECTION4
	global GAMEBOARD
	global ORDER
	global ALEATORIO
	global TURNO
	global DADO
	global DADO_STATE
	global RIVAL


	#NOMBRE DE JUGADORES

	JUGADOR1 = "NAME"
	JUGADOR2 = "NAME"
	JUGADOR3 = "NAME"
	JUGADOR4 = "NAME"

	#INDICES DE JUGADORES

	INDICEP1 = 0
	INDICEP2 = 0
	INDICEP3 = 0
	INDICEP4 = 0

	#ESTADO DE SELECCION

	SELECTION1 = False
	SELECTION2 = False
	SELECTION3 = False
	SELECTION4 = False

	#TABLERO DE JUEGO
	GAMEBOARD = numpy.zeros((5,8))

	#ORDEN DE JUGADORES

	ORDER = []
	ALEATORIO = 0
	TURNO = 0

	#MOVIMIENTO JUGADORES

	DADO = 0 
	DADO_STATE = True
	RIVAL = ''

####################################################################################################
#                                                                                                  #
#                                              TURNOS                                              #
#                                                                                                  #
####################################################################################################



#INICIO DEL JUEGO NUMERO 1 - 1000------------------------

#PRINCUPAL     
#E: Cuatro Numeros
#S: Una lista
#D: Analiza los numeros insertados por los jugadores


def registroPlayers(num):
    listaNumeros = []

    if num==4:
        player1= Player1.getName()
                 
        num1= int(JUGADOR1)

        player2= Player2.getName()

        num2= int(JUGADOR2)

        player3= Player3.getName()

        num3= int(JUGADOR3)

        player4= Player4.getName()

        num4= int(JUGADOR4)


        listaNumeros+=[[num1,player1]]+[[num2,player2]]+[[num3,player3]]+[[num4,player4]]

    elif num ==3:
                  
        player1= Player1.getName()
                 
        num1= int(JUGADOR1)

        player2= Player2.getName()

        num2= int(JUGADOR2)

        player3= Player3.getName()

        num3= int(JUGADOR3)

        listaNumeros+=[[num1,player1]]+[[num2,player2]]+[[num3,player3]]

    elif num == 2:
        player1= Player1.getName()
                 
        num1= int(JUGADOR1)

        player2= Player2.getName()

        num2= int(JUGADOR2)

        listaNumeros+=[[num1,player1]]+[[num2,player2]]

    return numeroInicioJuego(listaNumeros)
 
#AUXILIAR-----------------------------------------------------------------
#E: Cuatro Numeros
#S: Una lista
#D: Analiza los numeros insertados por los jugadores

def numeroInicioJuego(listaNumeros):
    global ALEATORIO

    listaPlayers = []
    ALEATORIO = random.randint(1,1000)

    listaOnlyNumeros = []

    for element in listaNumeros:
        element[0] = abs(element[0] - ALEATORIO)
        listaOnlyNumeros += [element[0]]

    while listaOnlyNumeros != []:

        closest = min(listaOnlyNumeros)

        for player in listaNumeros:
            if closest == player[0]:
                listaPlayers += [player[1]]
            else:
                continue
        listaOnlyNumeros.remove(closest)

    return listaPlayers


#--------------------------------------------------------------------------

#E: 1 int
#S: 1 int
#D: Retorna el turno correspondiente

def changeTurno():

    global TURNO

    if TURNO == len(ORDER)-1:
        TURNO = 0
    else:
        TURNO +=1
        return TURNO

#--------------------------------------------------------------------------

def setOrder():

    cont = 0

    for name in ORDER:

        if name == Player1.getName():
            Player1.setTurno(cont)

        elif name == Player2.getName():
            Player2.setTurno(cont)

        elif name == Player3.getName():
            Player3.setTurno(cont)

        elif name == Player4.getName():
            Player4.setTurno(cont)

        cont += 1

        continue


####################################################################################################
#                                                                                                  #
#                                              CLASES                                              #
#                                                                                                  #
####################################################################################################

#=======================================   JUGADORES   =============================================

class Player:

    #Constructor:

    def __init__(self):
        self.ID = 0
        self.nombre = "nombre"
        self.personaje = "personaje"

        #Da la posicion x,y donde se imprime el personaje
        self.track = (0,0)

        #Recorren la matriz del tablero
        self.I = 0
        self.J = 0
        self.turno = 999
        self.state = True
        self.freeze = [False,0]
        self.victory = False


    #E: nada
    #S: un booleano
    #D: obtiene el estado de victoria del jugador

    def getState(self):
        return self.state

    #E: nada
    #S: un int
    #D: obtiene el estado de victoria del jugador

    def getID(self):
        return self.ID

    #E: nada
    #S: un string
    #D: obtiene el nombre del jugador

    def getName(self):
        return self.nombre

    #E: nada
    #S: un string
    #D: el personaje seleccionado por el jugador

    def getCharacter(self):
        return self.personaje

    #E: nada
    #S: 1 int
    #D: retorna la posicion de la celda en la que se encuentra
    def getTrack(self):
        return self.track

    #E: nada
    #S: 1 int
    #D: retorna la posicion de la celda en la que se encuentra
    def getI(self):
        return self.I

    #E: nada
    #S: 1 int
    #D: retorna la posicion de la celda en la que se encuentra
    def getJ(self):
        return self.J

    #E: nada
    #S: 1 int
    #D: retorna el numero de turno del jugador
    def getTurno(self):
        return self.turno

    #E: un string
    #S: un string
    #D: Actualiza el objeto

    def setName(self,name):
        self.nombre = name

    #E: un string
    #S: un string
    #D: Actualiza el objeto

    def setCharacter(self,personaje):
        self.personaje = personaje

    #E: un int
    #S: class object
    #D: Actualiza el objeto

    def setTrack(self,x,y):
        self.track = (x,y)

    #E: un int
    #S: class object
    #D: Actualiza el objeto

    def setI(self,i):
        self.I = i

    #E: un int
    #S: class object
    #D: Actualiza el objeto

    def setJ(self,j):
        self.J = j

    #E: un int
    #S: class object
    #D: Actualiza el objeto

    def setTurno(self,turn):
        self.turno = turn

    #E: un booleano
    #S: class object
    #D: Actualiza el objeto

    def setState(self,estado):
        self.state = estado

    #E: un booleano
    #S: class object
    #D: Actualiza el objeto

    def setCongelado(self,state,rounds=1):
        self.freeze = [state,rounds]

    def unfreeze(self):
        if self.freeze[1] != 0:
            self.freeze[1] -= 1

        elif self.freeze[1] == 0:
            self.setCongelado(False,0)


    #E: un int
    #S: class object
    #Actualiza el Track del Player

    def move(self,num,x,y,i,j):

        cont = 1

        while cont <= num:

            if y == 60: #COLOCA EN PRIMERA LINEA
                x += 80
                y += 150
                j = 0
                i = 0

            elif y == 210 and x <= 1430 : #AVANZA A LO LARGO DE LA PRIMERA LINEA
                x += 200

                j += 1

            elif y == 210 and x > 1430: #BAJA A LA PRIMERA PLATAFORMA INTERMEDIO
                y += 108
                j = 7
                i = 1

            elif x > 1430 and y == 318: #BAJA A LA SEGUNDA LINEA
                y += 108
                i = 2

            elif y == 426 and x >= 280: #AVANZAR EN SEGUNDA LINEA
                x -= 200
                j -= 1

            elif y == 426 and x < 280: #BAJA A LA SEGUNDA PLAATFORMA INTERMEDIO
                y += 128
                j = 0
                i = 3

            elif y == 554: #BAJA AL TERCER NIVEL
                y += 128
                i = 4

            elif x <= 1430 and y == 682: #AVANZA EN EL TERCER NIVEL
                x += 200
                j += 1

            elif x > 1430 and y == 682:
                x += 120
                y += 125 
                self.victory = True

            
            cont += 1


        self.setTrack(x,y)

        self.setI(i)

        self.setJ(j)

    def moveBack(self,x,y,i,j,num):

        cont = 1

        while cont <= num:

            if y == 210 and x <= 230: #MUEVE AL PRINCIPIO
                i = -1
                j = -1
                x -= 80
                y -= 150

            elif y == 210 and x >= 280:
                j -= 1
                x -= 200

            elif y == 318:
                i = 0
                y -= 108

            elif y == 426 and x > 1430:
                i = 1

                y -= 108

            elif y == 426 and x <= 1430:

                j += 1

                x += 200

            elif y == 554:

                i -= 1
                y -= 128

            elif y == 682 and x < 280:
                i -= 1
                y -= 128

            elif y == 682:
                j -= 1
                x -= 200

            cont += 1

        self.setTrack(x,y)

        self.setI(i)

        self.setJ(j)

#JUGADORES

Player1 = Player()

Player2 = Player()

Player3 = Player()

Player4 = Player()

####################################################################################################
#                                                                                                  #
#                                              INTERFAZ                                            #
#                                                                                                  #
####################################################################################################


#VENTANA JUEGO

MEDIEVAL = pygame.display.set_mode((1800,1000))

#NOMBRE VENTANA

pygame.display.set_caption('Clash of Warriors')

CLOCK = pygame.time.Clock()

#MUSICA

MUSIC = pygame.mixer.music.load("TAVERN_IN.mp3")


# Pone la musica
pygame.mixer.music.play(loops=-1)

#IMAGENES

BACKGROUND = pygame.image.load('Background.png')

BACKGROUND2 = pygame.image.load('Background2.png')

BACKGROUND3 = pygame.image.load('BACKGROUND3.png')

#VICTORIA = pygame.image.load('Victoria.png')

TITLE = pygame.image.load("Title.png")

PLAY = pygame.image.load("Play.png")

AUTORES = pygame.image.load("Autores.png")

LUNACERRAR = pygame.image.load("botonCerrar.png")

TWOP = pygame.image.load("TwoPlayers.png")

THREEP = pygame.image.load("ThreePlayers.png")

FOURP = pygame.image.load("FourPlayers.png")

PLAYER1 = pygame.image.load("PLAYER 1.png")

PLAYER2 = pygame.image.load("PLAYER 2.png")

PLAYER3 = pygame.image.load("PLAYER 3.png")

PLAYER4 = pygame.image.load("PLAYER 4.png")

FLECHAS = pygame.image.load("flechas.png")

SELECT = pygame.image.load("SELECT.png")

LUNAREGRESO2 = pygame.image.load("lunaRegresoJuego.png")

ESTURNO = pygame.image.load("Es el turno de.png")

READY = pygame.image.load("READY.png")

SELECTED = pygame.image.load("Selected.png")

#PERSONAJES====================================================================

#1-------------------------------------------------------
LADRON = pygame.image.load("Ladron.png")

#VERSION PEQUENA
LADRON_S = pygame.image.load("ladronPeque.png")
#2-------------------------------------------------------

LEGOLAS = pygame.image.load("Legolas.png")
#VERSION PEQUENA
LEGOLAS_S = pygame.image.load("LegolasPeque.png")

#3-------------------------------------------------------

GLADIADOR = pygame.image.load("Gladiador.png")
#VERSION PEQUENA
GLADIADOR_S = pygame.image.load("GladiadorPeque.png")

#4-------------------------------------------------------

CABALLERO = pygame.image.load("Caballero.png")
#VERSION PEQUENA
CABALLERO_S = pygame.image.load("CaballeroPeque.png")

#5-------------------------------------------------------

KAKASHI = pygame.image.load("Kakashi.png")

#VERSION PEQUENA
KAKASHI_S = pygame.image.load("KakashiPeque.png")

#6-------------------------------------------------------

FORAJIDO = pygame.image.load("Forajido.png")
#VERSION PEQUENA
FORAJIDO_S = pygame.image.load("ForajidoPeque.png")

#7-------------------------------------------------------

TERRORISTA = pygame.image.load("Terrorista.png")
#VERSION PEQUENA
TERRORISTA_S = pygame.image.load("TerroristaPeque.png")

#8-------------------------------------------------------

ASESINO = pygame.image.load("Asesino.png")
#VERSION PEQUENA
ASESINO_S = pygame.image.load("AsesinoPeque.png")

#9-------------------------------------------------------

OGRO = pygame.image.load("Ogro.png")
#VERSION PEQUENA
OGRO_S = pygame.image.load("OgroPeque.png")

#10-------------------------------------------------------

NINJA = pygame.image.load("NinjaAzul.png")
NINJA_S = pygame.image.load("NinjaAzulPeque.png")

#====================================================================================

#PERSONAJES ELEGIBLES

PERSONAJES = [KAKASHI,NINJA,OGRO,ASESINO,TERRORISTA,FORAJIDO,CABALLERO,GLADIADOR,LEGOLAS,LADRON]

CHOSEN = []

PERSONAJES_TABLERO = {LADRON:LADRON_S, NINJA:NINJA_S, OGRO:OGRO_S, ASESINO:ASESINO_S, TERRORISTA: TERRORISTA_S, FORAJIDO:FORAJIDO_S, KAKASHI:KAKASHI_S, CABALLERO:CABALLERO_S, GLADIADOR:GLADIADOR_S, LEGOLAS:LEGOLAS_S}

#FUENTE

#DADOS

IMAGENDADO= pygame.image.load("botonDado.png")

DADO1= pygame.image.load("DADO#1.png")

DADO2= pygame.image.load("DADO#2.png")

DADO3= pygame.image.load("DADO#3.png")

DADO4= pygame.image.load("DADO#4.png")

DADO5= pygame.image.load("DADO#5.png")

DADO6= pygame.image.load("DADO#6.png")

#SIMBOLOGIA

SYMBOLOGY = pygame.image.load("Symbology.png")

SIM_ATRAPARGATO= pygame.image.load("AtraparGato.png")

SIM_BOMBERMARIO = pygame.image.load("Bombermario.png")

SIM_CARCEL = pygame.image.load("Carcel.png")

SIM_COLA = pygame.image.load("Cola.png")

SIM_COLLECT_COINS = pygame.image.load("CollectCoins.png")

SIM_TICTACTOE = pygame.image.load("GatoNormal.png")

SIM_GUESS_WHO = pygame.image.load("GuessWho.png")

SIM_CARDS = pygame.image.load("Cards.png")

SIM_MEMORY = pygame.image.load("Memoria.png")

SIM_SOPA = pygame.image.load("SopaLetras.png")

SIM_MEMORY_PATH = pygame.image.load("MemoryPath.png")

SIM_FlOR_H = pygame.image.load("Flor de Hielo.png")

SIM_ESTRELLA = pygame.image.load("Estrella.png")

SIM_TUBOS = pygame.image.load("Tubos.png")

SIM_FlOR_F = pygame.image.load("FlorFuego.png")

#MINIJUEGOS

MINIJUEGOS = {1:SIM_ATRAPARGATO,2:SIM_MEMORY_PATH,3:SIM_SOPA,4:SIM_COLLECT_COINS,5:SIM_TICTACTOE, 6:SIM_BOMBERMARIO,7:SIM_CARDS,8:SIM_GUESS_WHO,9:SIM_MEMORY,10:SIM_CARCEL,11:SIM_COLA,12:SIM_ESTRELLA,13.1:SIM_TUBOS,13.2:SIM_TUBOS,13.3:SIM_TUBOS,14:SIM_FlOR_F,15:SIM_FlOR_H}

# Diccionario que llama minijuegos

MINIJUEGOS_NAME = {1:'Catch the Cat',2:'Memory Path',3:'Letter Soup',4: 'Collect the Coins',5: 'Gato', 6: 'Bomber',7: 'cards',8: 'Guess Who',9:'Memory',10:'Jail',11: 'Tail',12: 'Star',13.1: 'Tubes1',13.2: 'Tubes2',13.3:'Tubes3',14: 'Fire Flower',15: 'Ice Flower'}

#PLATAFORMA TABLERO

PLATAFROMA = pygame.image.load("platformmain.png")

#PLATAFORMA META E INICIO

PLATAFROMA2 = pygame.image.load("WINPLATFORM.png")

PLATAFROMA3 = pygame.image.load("FINISH.png")

#ESCALERA

LADDER = pygame.image.load("LADDER.png")

#START Y END

START_FANT = pygame.image.load("START.png")

END_FANT = pygame.image.load("END.png")

#========================================== BOTONES ==========================================

#BOTON CERRAR

#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton

def botonCerrar(x,y,ancho,altura):
    from sys import exit
    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:
            pygame.mixer.music.stop()
            pygame.display.quit()
            return exit()

#----------------------------------------------------------------------------------------------

#BOTON REGRESAR MENU PRINCIPAL

#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton

def botonRegreso(x,y,ancho,altura):

    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:
            return menuPrincipal()
#----------------------------------------------------------------------------------------------

#BOTON PLAY TABLERO

#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton

def botonPlayTablero(x,y,ancho,altura,ID):
    global JUGADOR1
    global JUGADOR2
    global JUGADOR3
    global JUGADOR4

    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:
            JUGADOR1 = ''
            JUGADOR2 = ''
            JUGADOR3 = ''
            JUGADOR4 = ''
            return menuStart(ID)
#----------------------------------------------------------------------------------------------


#BOTON REGRESAR MENU PLAY

#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton

def botonRegresoPlay(x,y,ancho,altura):

    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:
            return menuPlay()

#----------------------------------------------------------------------------------------------

#BOTON  MENU SELECCIÓN DE JUGADORES

#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton

def botonPlay(x,y,ancho,altura):

    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:
            return menuPlay()
                                                  

#----------------------------------------------------------------------------------------------

#BOTON  MENU TWO PLAYERS

#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton

def botonTwoPlayers(x,y,ancho,altura):
    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:
            return menuTwoP()


#----------------------------------------------------------------------------------------------

#BOTON  MENU THREE PLAYERS

#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton

def botonThreePlayers(x,y,ancho,altura):
    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:
            return menuThreeP()

#----------------------------------------------------------------------------------------------

#BOTON  MENU FOUR PLAYERS

#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton

def botonFourPlayers(x,y,ancho,altura):
    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:
            return menuFourP()

#----------------------------------------------------------------------------------------------

#BOTON REGRESO TABLERO


#E: Cuatro Numeros
#S: Ventana menu play
#D: Reinicia todas las variables globales y regresa la menu principal

def botonRegresoTablero(x,y,ancho,altura):
    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:
            #JUGADORES NOMBRES

            JUGADOR1 = "NAME"

            JUGADOR2 = "NAME"

            JUGADOR3 = "NAME"

            JUGADOR4 = "NAME"

            #PERSONAJES

            INDICEP1 = 0

            INDICEP2 = 0

            INDICEP3 = 0

            INDICEP4 = 0

            #PERFIL JUGADORES

            Player1 = Player()

            Player2 = Player()

            Player3 = Player()

            Player4 = Player()

            return menuPrincipal()

#----------------------------------------------------------------------------------------------

#BOTON  DADO

#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton

def botonDado(x,y,ancho,altura):

    global DADO
    global DADO_STATE
    
    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:

            if DADO_STATE:

                num = random.randint(1,6)

                DADO = num

                DADO_STATE = False

            else:
                return

                


                                                  
#E: Un numero
#S: Una imagen
#D: Selecciona la imagen de la cara del dado de acuerdo a la jugada

def impresorDado(num):

    texto(1700,45,str(num),40,BLANCO)

    if num ==0:
        MEDIEVAL.blit(IMAGENDADO,(1600,10))

    if num==1:
        return MEDIEVAL.blit(DADO1,(1600,10))

    if num==2:
        return MEDIEVAL.blit(DADO2,(1600,10))

    if num==3:
        return MEDIEVAL.blit(DADO3,(1600,10))

    if num==4:
        return MEDIEVAL.blit(DADO4,(1600,10))

    if num==5:
        return MEDIEVAL.blit(DADO5,(1600,10))

    if num==6:
        return MEDIEVAL.blit(DADO6,(1600,10))
                                                  


#----------------------------------------------------------------------------------------------

#BOTON  INPUT PLAYERS

#E: Cinco numeros
#S: Una funcion
#D: Crea un boton

def botonInputPlayer(x, y, ancho, largo,ID):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:

            if ID == 1:
                inputPlayer1(x, y)
                                            
            if ID == 2:
                inputPlayer2(x, y)
                                              
            if ID == 3:
                inputPlayer3(x, y)
                                              
            else:
                inputPlayer4(x, y)


#----------------------------------------------------------------------------------------------

#BOTON  CORRER  DERECHA

#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton

def botonCorrerDerecha(x,y,ancho,altura,player,partida):
    global INDICEP1
    global INDICEP2
    global INDICEP3
    global INDICEP4

    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] == 1:

            if player == 1:
                if INDICEP1 == len(PERSONAJES)-1 or SELECTION1 == True:
                    return
                else:
                    INDICEP1 += 1
                    pygame.time.wait(300)

                    if partida == 2:
                        return menuTwoP()
                    if partida == 3:
                        return menuThreeP()
                    if partida == 4:
                        return menuFourP()
                                                                                                         
            if player == 2:
                if INDICEP2 == len(PERSONAJES)-1 or SELECTION2 == True:
                    return
                else:
                    INDICEP2 += 1
                    pygame.time.wait(300)

                    if partida == 2:
                        return menuTwoP()
                    if partida == 3:
                        return menuThreeP()
                    if partida == 4:
                        return menuFourP()
                                                                                                         
            if player == 3:
                if INDICEP3 == len(PERSONAJES)-1 or SELECTION3 == True:
                    return
                else:
                    INDICEP3 += 1
                    pygame.time.wait(300)

                    if partida == 2:
                        return menuTwoP()
                    if partida == 3:
                        return menuThreeP()
                    if partida == 4:
                        return menuFourP()
                     
            if player == 4:
                if INDICEP4 == len(PERSONAJES)-1 or SELECTION4 == True:
                    return

                else:
                    INDICEP4 += 1
                    pygame.time.wait(300)

                    if partida == 2:
                        return menuTwoP()
                    if partida == 3:
                        return menuThreeP()
                    if partida == 4:
                        return menuFourP()

#----------------------------------------------------------------------------------------------

#BOTON  CORRER  IZQUIERDA

#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton

def botonCorrerIzquierda(x,y,ancho,altura,player,partida):
    global INDICEP1
    global INDICEP2
    global INDICEP3
    global INDICEP4

    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:

        if click[0] == 1:

            if player == 1:

                if INDICEP1 == 0 or SELECTION1 == True:
                    return
                else:
                    INDICEP1 -= 1
                    pygame.time.wait(300)
                    if partida == 2:
                        return menuTwoP()
                    if partida == 3:
                        return menuThreeP()
                    if partida == 4:
                        return menuFourP()
             
            if player == 2:
                if INDICEP2 == 0 or SELECTION2 == True:
                    return
                else:
                    INDICEP2 -= 1
                    pygame.time.wait(300)
                    if partida == 2:
                        return menuTwoP()
                    if partida == 3:
                        return menuThreeP()
                    if partida == 4:
                        return menuFourP()
            if player == 3:
                if INDICEP3 == 0 or SELECTION3 == True:
                    return
                else:
                    INDICEP3 -= 1
                    pygame.time.wait(300)
                    if partida == 2:
                        return menuTwoP()
                    if partida == 3:
                        return menuThreeP()
                    if partida == 4:
                        return menuFourP()
            if player == 4:
                if INDICEP4 == 0 or SELECTION4 == True:
                    return
                else:
                    INDICEP4 -= 1
                    pygame.time.wait(300)
                    if partida == 2:
                        return menuTwoP()
                    if partida == 3:
                        return menuThreeP()
                    if partida == 4:
                        return menuFourP()

#----------------------------------------------------------------------------------------------


#BOTON  SELECT

#E: Cinco numeros
#S: Una funcion
#D: Crea un boton

def botonSelect(x, y, ancho, largo,ID):
    global CHOSEN

    global SELECTION1
    global SELECTION2
    global SELECTION3
    global SELECTION4

    global Player1
    global Player2
    global Player3
    global Player4

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:

            if ID == 1:
                for election in CHOSEN:
                    if PERSONAJES[INDICEP1] == election[0]:
                        if election[1] != 1:
                            return
                        else:
                            continue

                Player1.setName(JUGADOR1)
                Player1.ID = 1
                Player1.setCharacter(PERSONAJES[INDICEP1])
                Player1.setTrack(150,60)
                Player1.setI(-1)
                Player1.setJ(-1)
                CHOSEN += [[PERSONAJES[INDICEP1],1]]
                SELECTION1 = True

            if ID == 2:

                for election in CHOSEN:
                    if PERSONAJES[INDICEP2] == election[0]:
                        if election[1] != 2:
                            return
                        else:
                            continue

                Player2.setName(JUGADOR2)
                Player2.ID = 2
                Player2.setCharacter(PERSONAJES[INDICEP2])
                Player2.setTrack(100,60)
                Player2.setI(-1)
                Player2.setJ(-1)
                CHOSEN += [[PERSONAJES[INDICEP2],2]]
                SELECTION2 = True
              
            if ID == 3:

                for election in CHOSEN:
                    if PERSONAJES[INDICEP3] == election[0]:
                        if election[1] != 3:
                            return
                        else:
                            continue

                Player3.setName(JUGADOR3)
                Player3.ID = 3
                Player3.setCharacter(PERSONAJES[INDICEP3])
                Player3.setTrack(50,60)
                Player3.setI(-1)
                Player3.setJ(-1)
                CHOSEN += [[PERSONAJES[INDICEP3],3]]
                SELECTION3 = True

            if ID == 4:

                for election in CHOSEN:
                    if PERSONAJES[INDICEP4] == election[0]:
                        if election[1] != 4:
                            return
                        else:
                            continue

                Player4.setName(JUGADOR4)
                Player4.ID = 4
                Player4.setCharacter(PERSONAJES[INDICEP4])
                Player4.setTrack(0,60)
                Player4.setI(-1)
                Player4.setJ(-1)
                CHOSEN += [[PERSONAJES[INDICEP4],4]]
                SELECTION4 = True

def botonBackStart(x,y,ancho,largo,ID):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:

            if ID == 2:
                pygame.time.wait(800)
                return menuTwoP()
            if ID == 3:
                pygame.time.wait(800)
                return menuThreeP()
            if ID == 4:
                pygame.time.wait(800)
                return menuFourP()

def botonGame(x,y,ancho,largo,ID):

    global ORDER

    timer = 300

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:

            ORDER = registroPlayers(ID)

            menuStart(ID)


def botonPick(x,y,ancho,largo,game,player,playerO):
    global RIVAL
    global DADO

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:

            if game == 'Memory':
                proceso_Memory(playerO,player)

            if game == 'Gato':
                RIVAL = player.getName()
                procesoJuegoGato(playerO)

            if game == 'Ice Flower':
                DADO = 0
                changeTurno()
                player.setCongelado(True)
                tableroJuego()

            if game == 'Fire Flower':
                DADO = 0
                florF(player.ID)
                changeTurno()
                tableroJuego()


#========================================================================================================
#===========================================   INPUTS  ==================================================
#========================================================================================================

# E: nada
# S: un string
# D: Detecta cual tecla del teclado es presionada y la retorna

def tecla():
    while 1:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            return event.key
        else:
            pass


# --------------------------------------------------------------------------------------------------------------

# E: 2 ints y un string
# S: imprime un rectangulo en la pantalla
# D: Imprime un rectangulo negro donde se pueda escribir el numero del jugador

def cuadroPlayer1(x, y, message = JUGADOR1):
    global MAINFONT

    pygame.draw.rect(MEDIEVAL, BLANCO, (x, y, 230, 60))
    pygame.draw.rect(MEDIEVAL, NEGRO, (x + 3, y + 3, 230 - 7, 60 - 7))

    if len(message) != 0:
        MEDIEVAL.blit(MAINFONT.render(message, 1, BLANCO), (x + 30 , y - 5 ))

    pygame.display.flip()



# --------------------------------------------------------------------------------------------------------------


# E: 2 ints
# S: 1 string
# D: Crea una caja en pantalla para que el usuario digite su nombre

def inputPlayer1(x, y):
    global JUGADOR1

    currentString = []
    string = ""
    cuadroPlayer1(x, y, string.join(currentString))

    while 1:
        inkey = tecla()
        if inkey == pygame.K_BACKSPACE:
            currentString = currentString[0:-1]
        elif inkey == pygame.K_RETURN:
            break
        elif inkey == pygame.K_MINUS:
            currentString.append("_")
        elif inkey <= 127:
            currentString.append(chr(inkey))

        cuadroPlayer1(x, y, string.join(currentString))
    JUGADOR1 = string.join(currentString)
    return JUGADOR1



# --------------------------------------------------------------------------------------------------------------

# E: 2 ints y un string
# S: imprime un rectangulo en la pantalla
# D: Imprime un rectangulo negro donde se pueda escribir el numero del jugador

def cuadroPlayer2(x, y, message = JUGADOR2):
    global MAINFONT

    pygame.draw.rect(MEDIEVAL, BLANCO, (x, y, 230, 60))
    pygame.draw.rect(MEDIEVAL, NEGRO, (x + 3, y + 3, 230 - 7, 60 - 7))

    if len(message) != 0:
        MEDIEVAL.blit(MAINFONT.render(message, 1, BLANCO), (x + 30 , y - 5 ))

    pygame.display.flip()

# --------------------------------------------------------------------------------------------------------------


# E: 2 ints
# S: 1 string
# D: Crea una caja en pantalla para que el usuario digite su nombre

def inputPlayer2(x, y):
    global JUGADOR2

    currentString = []
    string = ""
    cuadroPlayer2(x, y, string.join(currentString))

    while 1:
        inkey = tecla()
        if inkey == pygame.K_BACKSPACE:
            currentString = currentString[0:-1]
        elif inkey == pygame.K_RETURN:
            break
        elif inkey == pygame.K_MINUS:
            currentString.append("_")
        elif inkey <= 127:
            currentString.append(chr(inkey))

        cuadroPlayer2(x, y, string.join(currentString))

    JUGADOR2 = string.join(currentString)

    return JUGADOR2


# --------------------------------------------------------------------------------------------------------------

# E: 2 ints y un string
# S: imprime un rectangulo en la pantalla
# D: Imprime un rectangulo negro donde se pueda escribir el numero del jugador

def cuadroPlayer3(x, y, message = JUGADOR3):
    global MAINFONT

    pygame.draw.rect(MEDIEVAL, BLANCO, (x, y, 230, 60))
    pygame.draw.rect(MEDIEVAL, NEGRO, (x + 3, y + 3, 230 - 7, 60 - 7))

    if len(message) != 0:
        MEDIEVAL.blit(MAINFONT.render(message, 1, BLANCO), (x + 30 , y - 5 ))

    pygame.display.flip()

# --------------------------------------------------------------------------------------------------------------


# E: 2 ints
# S: 1 string
# D: Crea una caja en pantalla para que el usuario digite su nombre

def inputPlayer3(x, y):
    global JUGADOR3

    currentString = []
    string = ""
    cuadroPlayer3(x, y, string.join(currentString))

    while 1:
        inkey = tecla()
        if inkey == pygame.K_BACKSPACE:
            currentString = currentString[0:-1]
        elif inkey == pygame.K_RETURN:
            break
        elif inkey == pygame.K_MINUS:
            currentString.append("_")
        elif inkey <= 127:
            currentString.append(chr(inkey))

        cuadroPlayer3(x, y, string.join(currentString))
    JUGADOR3 = string.join(currentString)

    return JUGADOR3

# --------------------------------------------------------------------------------------------------------------

# E: 2 ints y un string
# S: imprime un rectangulo en la pantalla
# D: Imprime un rectangulo negro donde se pueda escribir el numero del jugador

def cuadroPlayer4(x, y, message = JUGADOR4):
    global MAINFONT

    pygame.draw.rect(MEDIEVAL, BLANCO, (x, y, 230, 60))
    pygame.draw.rect(MEDIEVAL, NEGRO, (x + 3, y + 3, 230 - 7, 60 - 7))

    if len(message) != 0:
        MEDIEVAL.blit(MAINFONT.render(message, 1, BLANCO), (x + 30 , y - 5 ))

    pygame.display.flip()


# --------------------------------------------------------------------------------------------------------------


# E: 2 ints
# S: 1 string
# D: Crea una caja en pantalla para que el usuario digite su nombre

def inputPlayer4(x, y):
    global JUGADOR4

    currentString = []
    string = ""
    cuadroPlayer3(x, y, string.join(currentString))

    while 1:
        inkey = tecla()
        if inkey == pygame.K_BACKSPACE:
            currentString = currentString[0:-1]
        elif inkey == pygame.K_RETURN:
            break
        elif inkey == pygame.K_MINUS:
            currentString.append("_")
        elif inkey <= 127:
            currentString.append(chr(inkey))

        cuadroPlayer4(x, y, string.join(currentString))
    JUGADOR4 = string.join(currentString)

    return JUGADOR4

#===================================================================================================
#===============================================   PAINTS   ========================================
#===================================================================================================


'''
E: 4 numeros
S: un blit de pygame
D: Imprimer a los personajes en la pantalla
'''



def paintCharacter(indice,x,y,ID):
    global PERSONAJES

    #COLOCA AL PERSONAJE
    for election in CHOSEN:
        if PERSONAJES[indice] == election[0]:
            if ID != election[1]:
                MEDIEVAL.blit(SELECTED,(x + 40,y - 40))
                MEDIEVAL.blit(PERSONAJES[indice],(x + 20,y + 10))

            else:
                MEDIEVAL.blit(PERSONAJES[indice],(x + 20,y + 10))

        else:
            continue

    MEDIEVAL.blit(PERSONAJES[indice],(x + 20,y + 10))

def paintPlayers(ORDER):

    #FICHAS PALYERS

    if len(ORDER) == 2:

        MEDIEVAL.blit(PERSONAJES_TABLERO[Player1.getCharacter()],Player1.getTrack())

        MEDIEVAL.blit(PERSONAJES_TABLERO[Player2.getCharacter()],Player2.getTrack())

    elif len(ORDER) == 3:

        MEDIEVAL.blit(PERSONAJES_TABLERO[Player1.getCharacter()],Player1.getTrack())

        MEDIEVAL.blit(PERSONAJES_TABLERO[Player2.getCharacter()],Player2.getTrack())

        MEDIEVAL.blit(PERSONAJES_TABLERO[Player3.getCharacter()],Player3.getTrack())

    elif len(ORDER) == 4:

        MEDIEVAL.blit(PERSONAJES_TABLERO[Player1.getCharacter()],Player1.getTrack())

        MEDIEVAL.blit(PERSONAJES_TABLERO[Player2.getCharacter()],Player2.getTrack())

        MEDIEVAL.blit(PERSONAJES_TABLERO[Player3.getCharacter()],Player3.getTrack())

        MEDIEVAL.blit(PERSONAJES_TABLERO[Player4.getCharacter()],Player4.getTrack())

def loss():
    global TURNO

    if Player1.getState() == False and Player1.getTurno() == TURNO:
        Player1.moveBack(Player1.getTrack()[0],Player1.getTrack()[1],Player1.getI(),Player1.getJ(),DADO)
        Player1.setState(True)
        Player2.setState(True)
        Player3.setState(True)
        Player4.setState(True)

    if Player2.getState() == False and Player2.getTurno() == TURNO:
        Player2.moveBack(Player2.getTrack()[0],Player2.getTrack()[1],Player2.getI(),Player2.getJ(),DADO)
        Player1.setState(True)
        Player2.setState(True)
        Player3.setState(True)
        Player4.setState(True)

    if Player3.getState() == False and Player3.getTurno() == TURNO:
        Player3.moveBack(Player3.getTrack()[0],Player3.getTrack()[1],Player3.getI(),Player3.getJ(),DADO)
        Player1.setState(True)
        Player2.setState(True)
        Player3.setState(True)
        Player4.setState(True)
    
    if Player4.getState() == False and Player4.getTurno() == TURNO:
        Player4.moveBack(Player4.getTrack()[0],Player4.getTrack()[1],Player4.getI(),Player4.getJ(),DADO)
        Player1.setState(True)
        Player2.setState(True)
        Player3.setState(True)
        Player4.setState(True)

    else:
        Player1.setState(True)
        Player2.setState(True)
        Player3.setState(True)
        Player4.setState(True)


#===================================================================================================
#===============================================   MINIJUEGOS   ====================================
#===================================================================================================



def minijuego(i,j,ID): 
    global DADO

    minijuego = GAMEBOARD[i][j]

    minijuego = MINIJUEGOS_NAME[minijuego]


    if minijuego == 'cards':
        return cards()

    if minijuego == 'Catch the Cat':
        return trapTheCat(ID)

    if minijuego == 'Memory Path':
        memoryPath(ID)

    if minijuego == 'Letter Soup':
        letterSoupGame(ID)

    if minijuego == 'Collect the Coins':
        proceso_CC(ID)

    if minijuego == 'Gato':
        menuPick('Gato',ID)
        

    if minijuego == 'Bomber':
        proceso_Bomber(ID)

    if minijuego == 'Guess Who':
        guessWho(ID)

    if minijuego == 'Memory':
        menuPick('Memory',ID)

    if minijuego == 'Jail':
        DADO = 0
        if ID == 1:
            Player1.setCongelado(True)
            

        if ID == 2:
            Player2.setCongelado(True)
            

        if ID == 3:
            Player3.setCongelado(True)
            

        if ID == 4:
            Player4.setCongelado(True)
            

    if minijuego == 'Tail':
        DADO = random.randint(1,3)
        tableroJuego()

    if minijuego == 'Star':
        DADO = 0
        tableroJuego()

    if minijuego == 'Tubes1':
        return tubo1(ID)

    if minijuego == 'Tubes2':
        return tubo2(ID)

    if minijuego == 'Tubes3':
        return tubo3(ID)

    if minijuego == 'Fire Flower':
        menuPick('Fire Flower',ID)

    if minijuego == 'Ice Flower':
        menuPick('Ice Flower',ID)

#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                CELDA ESPECIAL 1
#                                                                       TUBOS
#----------------------------------------------------------------------------------------------------------------------------------------

def tubo1(ID):

    location = findTubo(13.2)

    if ID == 1:
        Player1.move(location,150,60,-1,-1)
        
    if ID == 2:
        Player2.move(location,100,60,-1,-1)

    if ID == 3:
        Player3.move(location,50,60,-1,-1)

    if ID == 4:
        Player4.move(location,0,60,-1,-1)

def tubo2(ID):

    location = findTubo(13.3)

    if ID == 1:
        Player1.move(location,150,60,-1,-1)
        
    if ID == 2:
        Player2.move(location,100,60,-1,-1)

    if ID == 3:
        Player3.move(location,50,60,-1,-1)

    if ID == 4:
        Player4.move(location,0,60,-1,-1)

def tubo3(ID):

    location = findTubo(13.1)

    if ID == 1:
        Player1.move(location,150,60,-1,-1)
        
    if ID == 2:
        Player2.move(location,100,60,-1,-1)

    if ID == 3:
        Player3.move(location,50,60,-1,-1)

    if ID == 4:
        Player4.move(location,0,60,-1,-1)

        

def findTubo(num):

    cont = 0

    anormal = -1

    for i in range(len(GAMEBOARD)):
        for j in range(len(GAMEBOARD[0])):

            if i != 2:

                if GAMEBOARD[i][j] == 0:
                    continue

                elif GAMEBOARD[i][j] != num:
                    cont += 1
                    continue

                else:
                    cont += 1
                    return cont
            else:

                if GAMEBOARD[i][anormal] != num:
                    cont += 1
                    anormal -= 1
                    continue

                else:
                    cont += 1
                    return cont

#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                CELDA ESPECIAL 2
#                                                                  FLOR DE FUEGO
#----------------------------------------------------------------------------------------------------------------------------------------

def florF(ID):

    if ID == 1:
        Player1.setTrack(150,60)
        Player1.setI(-1)
        Player1.setJ(-1)

    if ID == 2:
        Player2.setTrack(100,60)
        Player2.setI(-1)
        Player2.setJ(-1)
        

    if ID == 3:
        Player3.setTrack(50,60)
        Player3.setI(-1)
        Player3.setJ(-1)
        

    if ID == 4:
        Player4.setTrack(0,60)
        Player4.setI(-1)
        Player4.setJ(-1)
        




#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 1
#                                                                   TIC TAC TOE
#----------------------------------------------------------------------------------------------------------------------------------------

#IMAGENES
BG = pygame.image.load('BACKGROUND_TTT.png')

BOARD_TTT = pygame.image.load('TIC-TAC-TOE-BOARD.png')

ESCUDOAZUL = pygame.image.load('ESCUDOAZUL.png')

ESCUDOVERDE = pygame.image.load('ESCUDOVERDE.png')

#VARIABLES PARA GATO----------

TABLEROGATO=[0,0,0,0,0,0,0,0,0]



#---------------------------------------------------- FUNCIONES PROCESO DE JUEGO ----------------------------------------------------

#--------------------------------ANALISIS FICHA----------------------------------

#1----------------------------------------

#E: Una lista y un numero
#S: Una lista
#D: Analisa si la el espacio esta ocupado
               
def analisisFicha(jugada,turno):
     global TABLEROGATO
     
     if TABLEROGATO[jugada]!=0:
          return True
     elif TABLEROGATO[jugada]==0:
          return False

#2----------------------------------------
     
#E: Una lista y un numero
#S: Una lista
#D: Reemplaza la ficha del jugador
               
def reemplazaFicha(jugada,turno):
     global TABLEROGATO
     
     if TABLEROGATO[jugada]==0:
          TABLEROGATO[jugada]=turno

#--------------------------------GANADOR----------------------------------
#E: Ninguna
#S: Una expresion booleana
#D: Verifica si hay un ganador

def ganadorGato():
     global TABLEROGATO

     if verificadorFilas(TABLEROGATO) or verificadorColumnas(TABLEROGATO) or verificadorDiagonales(TABLEROGATO):
          return True
     else:
          return False

#--------------------------------VERIFICADORES----------------------------------

#1 FILAS
#E: Una lista
#S: Una expresion booleana
#D: Verifica si hay un ganador en las filas
     
def verificadorFilas(tablero):
     if tablero[0]==tablero[1]==tablero[2] and tablero[0]!=0:
          return True
     if tablero[3]==tablero[4]==tablero[5] and tablero[3]!=0:
          return True
     if tablero[6]==tablero[7]==tablero[8] and tablero[6]!=0:
          return True
     else:
          return False
#************************************************************

#2 COLUMNAS
#E: Una lista
#S: Expresion booleana
#D: Verifica si hay un ganador en las columnas

def verificadorColumnas(tablero):
     if tablero[0]==tablero[3]==tablero[6] and tablero[0]!=0:
          return True
     if tablero[1]==tablero[4]==tablero[7] and tablero[1]!=0:
          return True
     if tablero[2]==tablero[5]==tablero[8] and tablero[2]!=0:
          return True
     else:
          return False
     
#************************************************************

#3 DIAGONALES
#E: Una lista
#S: Expresion booleana
#D: Verifica si hay un ganador en las diagonales

def verificadorDiagonales(tablero):
     
     if tablero[2]!=0 and tablero[4]!=0 and tablero[6]!=0 or tablero[0]!=0 and tablero[4]!=0 and tablero[8]!=0:
          
          if tablero[0]==tablero[4]==tablero[8]:
               return True
          elif tablero[2]==tablero[4]==tablero[6]:
               return True
     else:
          return False



#--------------------------------ANALISIS EMPATE----------------------------------
#E: Una lista
#S: Una expresion booleana
#D: Analiza si hay un empate

def analisisEmpate_TTT(tablero):

     for celda in tablero:
          if celda == 0:
               return False
          continue
     return True

#------------------------------------------------------------- INTERFAZ -------------------------------------------------------------

#-------------------------------- COLOCA FICHA ----------------------------------

#E: Dos numeros y una imagen
#S: Una imagen
#D: Pone una imagen 

def fichaGato(x,y,ficha):
     MEDIEVAL.blit(ficha,(x,y))

#-------------------------------- SELECTOR DE JUGADA ----------------------------------
#E:Dos numeros
#S:Un numero
#D: Verifica la posicion del click y recorna jugada en donde quiere colocar la ficha


def input_Gato_Normal(positionX,positionY):

     if 520<= positionX <=750:
          
          if 140<= positionY <=370:
               return 0
          elif 390<= positionY <=620:
               return 3
          elif 660<= positionY <=890:
               return 6
          
     if 780<= positionX <=1010:
          
          if 140<= positionY <=370:
               return 1
          elif 390<= positionY <=620:
               return 4
          elif 660<= positionY <890:
               return 7

     if 1050<= positionX <=1280:
          
          if 140<= positionY <=370:
               return 2
          elif 390<= positionY <=620:
               return 5
          elif 660<= positionY <=890:
               return 8
#-------------------------------- IMPRESOR TABLERO ----------------------------------

#E: Una lista
#S: El tablero
#D: Proyecta el tablero en la interfaz

def mostrarTablero_TTT(tablero):
     positionY = 0
     positionX = 0
     for i in range(len(tablero)):

          if tablero [i] == 1:
               
               positionY = 140
               
               if i in range(0,3):
                    
                    if i == 0:
                         positionX = 550
                         MEDIEVAL.blit(ESCUDOVERDE,(positionX,positionY))
                    elif i == 1:
                         positionX=780
                         MEDIEVAL.blit(ESCUDOVERDE,(positionX,positionY))
                    elif i == 2:
                         positionX=1020
                         MEDIEVAL.blit(ESCUDOVERDE,(positionX,positionY))
                         
               if i in range(3,6):
                    
                    positionY = 390
                    
                    if i == 3:
                         positionX = 550
                         MEDIEVAL.blit(ESCUDOVERDE,(positionX,positionY))
                    elif i == 4:
                         positionX=780
                         MEDIEVAL.blit(ESCUDOVERDE,(positionX,positionY))
                    elif i == 5:
                         positionX=1020
                         MEDIEVAL.blit(ESCUDOVERDE,(positionX,positionY))
                         
               if i in range(6,9):
                    
                    positionY = 660

                    if i == 6:   
                         positionX = 550
                         MEDIEVAL.blit(ESCUDOVERDE,(positionX,positionY))
                    elif i == 7:
                         positionX=780
                         MEDIEVAL.blit(ESCUDOVERDE,(positionX,positionY))
                    elif i == 8:
                         positionX=1020
                         MEDIEVAL.blit(ESCUDOVERDE,(positionX,positionY))
               
          elif tablero [i] == 2:

               positionY = 140
               
               if i in range(0,3):
                    
                    if i == 0:
                         positionX = 550
                         MEDIEVAL.blit(ESCUDOAZUL,(positionX,positionY))
                    elif i == 1:
                         positionX=780
                         MEDIEVAL.blit(ESCUDOAZUL,(positionX,positionY))
                    elif i == 2:  
                         positionX=1020
                         MEDIEVAL.blit(ESCUDOAZUL,(positionX,positionY))
                         
               if i in range(3,6):
                    
                    positionY = 390
                    if i == 3:
                         positionX = 550
                         MEDIEVAL.blit(ESCUDOAZUL,(positionX,positionY))
                    elif i == 4:
                         positionX=780
                         MEDIEVAL.blit(ESCUDOAZUL,(positionX,positionY))
                    elif i == 5:
                         positionX=1020
                         MEDIEVAL.blit(ESCUDOAZUL,(positionX,positionY))

               if i in range(6,9):
                   
                    positionY = 660
                    if i == 6:
                         positionX = 550
                         MEDIEVAL.blit(ESCUDOAZUL,(positionX,positionY))
                    elif i == 7:
                         positionX=780
                         MEDIEVAL.blit(ESCUDOAZUL,(positionX,positionY))
                    elif i == 8:
                         positionX=1020
                         MEDIEVAL.blit(ESCUDOAZUL,(positionX,positionY))


#-----------------------   TIC TAC TOE   --------------------------------

#E: No tiene
#S: El juego de gato
#D: Procesa el juego de ambos jugadores

def procesoJuegoGato(player):

    #VARIABLES GLOBALES======
    global TABLEROGATO
    global RIVAL
    global DADO
     #========================
    pygame.init()

    #PONER JUGADORES

    if player.getID() == 1:
        jugador1 = Player1.getName()

    if player.getID() == 2:
        jugador1 = Player2.getName()

    if player.getID() == 3:
        jugador1 = Player3.getName()

    if player.getID() == 4:
        jugador1 = Player4.getName()

    jugador2 = RIVAL

     
     
    turno = 1
    while True:
        #BACKGROUND Y TABLERO
        MEDIEVAL.blit(BG,(0,0))
        MEDIEVAL.blit(BOARD_TTT,(500,100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
               
          #JUGADOR 1
                if turno == 1:
                     
                    positionX=int(event.pos[0])
                    positionY=int(event.pos[1])

                     #JUGADA
                    play = input_Gato_Normal(positionX,positionY)

                    if play == None:
                        continue
                     

                     #ANALISIS CELDA
                    if analisisFicha(play,turno):
                        continue
                    #REEMPLAZA FICHA
                    reemplazaFicha(play,turno)  
                    #VERIFICA GANADOR
                    if ganadorGato():
                        #BACKGROUND
                        MEDIEVAL.blit(BG,(0,0))
                        texto(850,200,'CONGRATULATIONS!',100,BLANCO)
                        texto(850,600,str(jugador1),100,BLANCO)
                        texto(900,400,'YOU WON!',100,BLANCO)
                        changeTurno()
                        DADO = 0
                        pygame.display.update()
                        TABLEROGATO=[0,0,0,0,0,0,0,0,0]

                        pygame.time.wait(2000)

                        tableroJuego()
                        

    
                    turno = 2
                    
      #JUGADOR 2
                elif turno == 2:
                    positionX=int(event.pos[0])
                    positionY=int(event.pos[1])

                    #JUGADA
                    play = input_Gato_Normal(positionX,positionY)

                    if play == None:
                        continue
                     

                    #ANALISIS CELDA
                    if analisisFicha(play,turno):
                        continue
                    #REEMPLAZA FICHA
                    reemplazaFicha(play,turno)
                    #VERIFICA GANADOR
                    if ganadorGato():
                        #BACKGROUND
                        MEDIEVAL.blit(BG,(0,0))
                        texto(850,200,'CONGRATULATIONS!',100,BLANCO)
                        texto(800,600,str(jugador2),100,BLANCO)
                        texto(900,400,'YOU WON!',100,BLANCO)

                        if player.getID() == 1:
                            Player1.setState(False)

                        if player.getID() == 2:
                            Player2.setState(False)

                        if player.getID() == 3:
                            Player3.setState(False)

                        if player.getID() == 4:
                            Player4.setState(False)

                        loss()

                        changeTurno()

                        DADO = 0

                        pygame.display.update()                            
                        TABLEROGATO=[0,0,0,0,0,0,0,0,0]

                        pygame.time.wait(2000)
                        tableroJuego()
                

                        
                    turno = 1
                        
          
        #REINICIA JUEGO SI HAY EMPATE
        if analisisEmpate_TTT(TABLEROGATO):
           mostrarTablero_TTT(TABLEROGATO)
           TABLEROGATO=[0,0,0,0,0,0,0,0,0]
          
        #IMPRIME TABLERO
        mostrarTablero_TTT(TABLEROGATO)
        #JUGADOR 1 CASILLA
        MEDIEVAL.blit(ESCUDOVERDE,(100,600))
        texto(200,900,jugador1,80,BLANCO)
        #JUGADOR 2 RETADO
        MEDIEVAL.blit(ESCUDOAZUL,(1490,600))
        texto(1600,900,jugador2,80,BLANCO)

        pygame.display.update()
        CLOCK.tick()


#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 2
#                                                                   MEMORY PATH
#----------------------------------------------------------------------------------------------------------------------------------------


#IMAGENES

FONDO_MEMORY = pygame.image.load('BACKGROUND_TTT.png')

MEMORY_PATH_NAME = pygame.image.load('MEMORY_PATH_NAME.png')

#CARTAS

JOKER = pygame.image.load('JOKER.png')

BACK_BLUE = pygame.image.load('BACKCARD_AZUL.png')

#VARIABLES PARA MEMORY PATH

TABLEROMEMORYP = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
TABLERO_LAYER = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
CARTA = 'X'
vidasMemoryPath = 3


#JUEGO-------------------------------------------------------------------------------
#E: No tiene
#S: El juego
#D: Crea el proceso del Juego Memory Path

def memoryPath(ID):
    #VARIABLES GLOBALES======
    global TABLEROMEMORYP
    global TABLERO_LAYER
    global vidasMemoryPath
    global DADO
    #========================
    pygame.init()

    #GENERADORES DEFAULT TABLERO
    generadorX()
    #CONTADOR DE COLUMNAS
    contador = 0
    
     
    while True:
        #BACKGROUND Y TABLERO
        MEDIEVAL.blit(FONDO_MEMORY,(0,0))
        MEDIEVAL.blit(MEMORY_PATH_NAME,(100,100))

        #MUESTRA TABLERO OFICIAL
        mostrarMemoryPath_JOKER(TABLEROMEMORYP)

        #IMPRIME TABLERO DELANTERO
        mostrarMemoryPath(TABLERO_LAYER)
          
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

          


          #JUGADA
            if event.type == pygame.MOUSEBUTTONDOWN:
               
                positionX=int(event.pos[0])
                          
                jugada = jugada_MemoryPath(positionX)

                
                if jugada == None:
                    continue
                    
                    
                for j in range(len(TABLEROMEMORYP[0])):
                         
                    if analizadorMemoryPath(TABLEROMEMORYP,contador,j,jugada):
                        #CAMBIA LAS JUGADAS
                        mostrarMemoryPath_Editor(TABLERO_LAYER,jugada,contador)
                        pygame.display.update()
                        contador+=1
                              
                        if contador>=8:
                            #BACKGROUND Y TABLERO
                            MEDIEVAL.blit(FONDO_MEMORY,(0,0))
                            #TEXTOS
                            texto(900,600,'YOU WON!',100,BLANCO)
                            texto(1180,100,'Lifes',20,BLANCO)
                            texto(1300,100,str(vidasMemoryPath),100,BLANCO)
                            texto(1400,100,'left!',20,BLANCO)

                            pygame.display.update()
                            DADO = 0 
                            changeTurno()
                            
                            pygame.time.wait(2000)

                            TABLEROMEMORYP = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
                            TABLERO_LAYER = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
                            vidasMemoryPath = 3

                            tableroJuego()
                              
                        break
                    
                    #REINICIA EL CONTADOR
                    contador=0
                    texto(1300,200,'YOU FAILED!',50,BLANCO)

                    #REINICIA TABLERO
                    TABLERO_LAYER = reinicio_MP(TABLERO_LAYER)
                    #ACTUALIZA VIDAS
                    vidasMemoryPath-=1
                    texto(1180,100,'Lifes',20,BLANCO)
                    texto(1300,100,str(vidasMemoryPath),100,BLANCO)
                    texto(1400,100,'left!',20,BLANCO)
                    pygame.display.update()
                        #ESPERA TIEMPO
                    pygame.time.wait(1000)

                    if vidasMemoryPath<=0:
                            #TEXTOS
                        texto(1180,100,'Lifes',20,BLANCO)
                        texto(1300,100,str(vidasMemoryPath),100,BLANCO)
                        texto(1400,100,'left!',20,BLANCO)

                        if ID == 1:

                            Player1.setState(False)

                        if ID == 2:

                            Player2.setState(False)

                        if ID == 3:

                            Player3.setState(False)

                        if ID == 4:

                            Player4.setState(False)

                        texto(1300,200,'YOU FAILED!',50,BLANCO)
                        loss()

                        DADO = 0 

                        changeTurno()


                        pygame.time.wait(2000)

                        
                        pygame.display.update()

                        TABLEROMEMORYP = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
                        TABLERO_LAYER = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
                        pygame.display.update()
                        vidasMemoryPath = 3

                              
                        tableroJuego() 
                    break
     
          
        #TEXTOS
        texto(1180,100,'Lifes',20,BLANCO)
        texto(1300,100,str(vidasMemoryPath),100,BLANCO)
        texto(1400,100,'left!',20,BLANCO)

        pygame.display.update()
        CLOCK.tick()
               

     
#IMPRESOR TABLERO DELANTERO--------------------------------------------------------------------

#E: Una matriz
#S: No tiene
#D: Imprime el tablero    
     
def mostrarMemoryPath(M):
     M = M [::-1]
     x = 700
     y = 100
     for i in range(len(M)):
          for j in range(len(M[0])):
               if M[i][j] == 0:
                    MEDIEVAL.blit(BACK_BLUE,(x,y))
                    x+=100
               elif M[i][j] == 1:
                    x+=100
                    
          x = 700
          y+=100
     
      
                    
     
#IMPRESOR TABLERO OFFICIAL (JOKERS)-----------------------------------------------------------

#E: Una matriz
#S: No tiene
#D: Imprime el tablero    
     
def mostrarMemoryPath_JOKER(M):
     M = M [::-1]
     x = 715
     y = 110
     for i in range(len(M)):
          for j in range(len(M[0])):
               if M[i][j] == 'X':
                    MEDIEVAL.blit(JOKER,(x,y))
                    x+=100
               x+=100
               
          x = 715
          y+=100

#EDITOR TABLERO------------------------------------------------------------------------------

#E: Una matriz
#S: No tiene
#D: Imprime el tablero    
     
def mostrarMemoryPath_Editor(M,jugada,fila):
     M[fila][jugada] = 1
     return M
     
     
#REINICIO TABLERO----------------------------------------------------------------------------
#E:Una matriz
#S:Una matriz
#D:Reinicia la matriz a ceros

def reinicio_MP(M):
     M=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
     return M

#GENERADOR RANDOM DE CARTA 'X'---------------------------------------------------------------

#E: No tiene
#S: No tiene
#D: Genera aleatoriamente el orden de las X en la matriz

def generadorX():
     global TABLEROMEMORYP
     global CARTA
     
     for fila in TABLEROMEMORYP:
          editor=random.randint(0,2)
          fila[editor]= CARTA
     return 

          
#VERIFICADOR ESPACIO-----------------------------------------------------------------

#E: Tres numeros y una matriz
#S: Una expresion booleana
#D: Verifica si la posicion dada es valida

def analizadorMemoryPath(M,fila,columna,jugada):

     if jugada in range(0,3):

          if M[fila][jugada] == 'X':
               return True
          else:
               return False

     else:
          return False
     
#JUGADAS----------------------------------------------------------------------------

#E: Un numero
#S: Un numero
#D: Detecta la position del click del mouse y devuelve una jugada

def jugada_MemoryPath(positionX):

     if 710<=positionX<810:
          return 0
     elif 810<=positionX<910:
          return 1
     elif 910<=positionX<1010:
          return 2
     

               
#IMPRESOR TABLERO CONSOLA--------------------------------------------------------------------

#E: Una matriz
#S: No tiene
#D: Imprime el tablero    
     
def mostrarMemoryPath_AUX(tablero):
     tablero = tablero[::-1]
     for i in range(len(tablero)):
          for j in range(len(tablero[i])):
               print(tablero[i][j],end=' ')
          print()
     print()

#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 3
#                                                                   LETTER SOUP
#----------------------------------------------------------------------------------------------------------------------------------------

#VARIABLES GLOBALES LETTER SOUP===========================

MATRIZ_SOPA=((10,10),(15,15),(20,20))

PALABRAS_SOPA = cargarArchivo('Sopa de Letras.txt')

PALABRAS_SELECCIONADAS = []

TABLERO_OFFICIAL_SOPA= []

PALABRA = ''

SELECTED_WORD = 'XXXXXXXX'

MATRIZSOPA_LAYER = []

TAMANO = 0

TIEMPO_LS = pygame.time.get_ticks()
#=========================================================

#E: No tiene
#S: Un numero
#D: Selecciona un numero aleatorio entre 0 y 2

def numeroTableroSopa():
     aleatorio = random.randint(0,2)

     return aleatorio

#=========================================================

#E: No tiene
#S: No tiene
#D: Crea el tablero de la sopa de letras

def crearMatrizSopa():

     #VARIABLES GLOBALES-----------
     global SELECTED_WORD
     global MATRIZSOPA_LAYER
     global MATRIZ_SOPA
     global PALABRAS_SELECCIONADAS
     global PALABRAS_SOPA
     global TABLERO_OFFICIAL_SOPA
     global TAMANO
     #-----------------------------

     #ESCOGE EL TAMANO DEL TABLERO 25/15/10
     TAMANO = numeroTableroSopa()
     #CREA TABLERO
     tablero = np.zeros(MATRIZ_SOPA[TAMANO],dtype=str)
     #CUENTA FILAS
     counter = counterFilas(tablero)
     #VARIABLES
     newTablero = []
     newFila =[]
     #LISTA DE PALABRAS SELECCIONADAS
     PALABRAS_SELECCIONADAS=seleccionadorPalabras(PALABRAS_SOPA,counter)
     #CREA LA MATRIZ DELANTERA
     MATRIZSOPA_LAYER = np.zeros(MATRIZ_SOPA[TAMANO],dtype=int)
     #COLOCA PALABRAS SELECCIONES
     #PALABRA #1--------------------------
     tablero = colocadorVertical(tablero,PALABRAS_SELECCIONADAS[0],counter)
     #PALABRA #2--------------------------
     tablero = colocadorHorizontal(tablero,PALABRAS_SELECCIONADAS[1],counter)
     #PALABRA #3--------------------------
     tablero= colocadorDerecha(tablero,PALABRAS_SELECCIONADAS[2],counter)
     #PALABRA #4--------------------------
     tablero = colocadorIzquierda(tablero,PALABRAS_SELECCIONADAS[3],counter)
          
          
          
     for fila in tablero:

          while fila.size > 0:
               #SELECCIONA LETRA RANDOM
               letra = random.choice(string.ascii_uppercase)
               #VERIFICA SI HAY UN 0 O LETRA, Y LA AGREGA A LA NUEVA FILA
               if fila[0]=='':
                    newFila+=[letra]
               elif fila[0]!='':
                    newFila+=[fila[0]]
               #ELIMINA EL ELEM DE LA NUEVA FILA
               fila=fila[1:]
          
          #AGREGA FILA AL TABLERO, Y LIMPIA LA VARIABLE
          newTablero+=[newFila]
          newFila=[]
          continue
     
     #mostrarTableroSopa(newTablero)
     
     #IGUALA LA VARIABLE GLOBAL TABLERO
     TABLERO_OFFICIAL_SOPA=newTablero
     
     return
          
     
#IMPRESOR TABLERO SOPA--------------------------------------------------------------------

#E: Una matriz
#S: No tiene
#D: Imprime el tablero    
     
def mostrarTableroSopa(tablero):
     global PALABRAS_SELECCIONADAS
     #tablero = tablero[::-1]
     for i in range(len(tablero)):
          for j in range(len(tablero[i])):
               print(tablero[i][j],end=' ')
          print()
     print(PALABRAS_SELECCIONADAS)

#SELECCIONA CUATRO PALABRAS---------------------------------------------------------------

#E: Una lista
#S: Una lista
#D: Selecciona 4 palabras de las 100 palabras del txt

def seleccionadorPalabras(palabras,filas):
     
     listaPalabras= []
     contador=0
     
     while contador < 4:
          #SELECCIONA PALABRA RANDOM DE LISTA
          palabra = random.choice(palabras)
          #DETERMINA SI LA MATRIZ ES DE 10X10 PARA NO ELEGIR PALABRAS DE 7
          if len(palabra)==6 or len(palabra)==7 and filas==10:
               
               continue
     
          if palabra not in listaPalabras:
               contador += 1
               listaPalabras += [palabra]
          
          
     #RETORNA LISTA CON CUATRO PALABRAS SELECCIONADAS     
     return listaPalabras
          

#ANALISIS LARGO DE PALABRAS========================================================
#E: Un string
#S: Un numero
#D: Analiza el largo de cada palabra

def analisisPalabra(palabra):

     largoPalabra = len(palabra)

     return largoPalabra

#ANALISIS CANTIDAD DE FILAS DE LA MATRIZ===========================================

#E: Una matriz
#S: Un numero
#D: Verifica la cantidad de letras de la matriz

def counterFilas(M):
     
     counter = 0
     
     for fila in M:
          counter+=1
     return counter
          
#--------------------------------------------------------------------COLOCADOR DE PALABRAS--------------------------------------------------------------------
#COLOCADOR PALABRAS VERTICAL==============================================

#E: Una matriz, un string y un numero
#S: Una matriz
#D: Coloca una palabra verticalmente

def colocadorVertical(M,palabra,filas):
     
     #ESCOGE EL RANGO SEGUN LA CANTIDAD DE LETRAS DE LA PALABRA
     rango = filas - len(palabra)
     #ESCOGE UNA COLUMNA Y UNA FILA AL AZAR
     columnaRandom = random.randint(0,rango)
     filaRandom = random.randint(0,rango)
     #PROCESO DE JUEGO
     
     while True:
          
          if colocadorVerticalVerficador(M,palabra,filas,columnaRandom,filaRandom):

               for i in range(filaRandom,filas):
                    while len(palabra)!=0:
                         if M[i][columnaRandom]=='':
                              M[i][columnaRandom] = palabra[0]
                              palabra=palabra[1:]
                              break
                    
                    if len(palabra)==0:
                         #mostrarTableroSopa(M)
                         return M
                         
          else:
               columnaRandom = random.randint(0,rango)
               filaRandom = random.randint(0,rango)
               
     

               

#COLOCADOR PALABRAS HORIZONTAL==============================================

#E: Una matriz, un string y un numero
#S: Una matriz
#D: 
     
     
def colocadorHorizontal(M,palabra,columnas):

     columnas=columnas-1
     #ESCOGE EL RANGO SEGUN LA CANTIDAD DE LETRAS DE LA PALABRA
     rango = columnas - len(palabra)
     #ESCOGE UNA COLUMNA Y UNA FILA AL AZAR
     columnaRandom = random.randint(0,rango)
     filaRandom = random.randint(0,columnas)
     while True:

          if colocadorHorizontalVerificador(M,palabra,columnas,columnaRandom,filaRandom):
     
               for i in range(columnaRandom,columnas):
                    while len(palabra)!=0:
                         if M[filaRandom][i]=='':
                              M[filaRandom][i] = palabra[0]
                              palabra=palabra[1:]
                              break
                         
                    if len(palabra)==0:
                         #mostrarTableroSopa(M)
                         return M
          else:
               columnaRandom = random.randint(0,rango)
               filaRandom = random.randint(0,rango)
               
                    
               
     
#COLOCADOR PALABRAS DIAGONAL DERECHA==============================================

#E: Una matriz, un string y un numero
#S: Una matriz
#D: 
     
     
def colocadorDerecha(M,palabra,columnas):

     #LARGO PALABRA
     largo=len(palabra)

     #ESCOGE EL RANGO SEGUN LA CANTIDAD DE LETRAS DE LA PALABRA
     rango = columnas - len(palabra)
     if rango>= 7 or rango <= 5:
          rango = random.randint(0,5)
     #ESCOGE UNA COLUMNA Y UNA FILA AL AZAR
     columnaRandom = random.randint(0,rango)
     filaRandom = random.randint(0,rango)

     while True:
          
          if colocadorDerechaVerificador(M,palabra,columnas,columnaRandom,filaRandom):
               for i in range(0,largo):
                    
                    while len(palabra)!=0:
                         #print(palabra)
                         M[filaRandom][columnaRandom] = palabra[0]

                         columnaRandom+=1
                         filaRandom+=1
                         palabra=palabra[1:]
                         
                         break
                    if len(palabra)==0:
                         #mostrarTableroSopa(M)
                         return M
          else:
               columnaRandom = random.randint(0,rango)
               filaRandom = random.randint(0,rango)
          
               
          

#COLOCADOR PALABRAS DIAGONAL IZQUIERDA==============================================

#E: Una matriz, un string y un numero
#S: Una matriz
#D: 
     
     
def colocadorIzquierda(M,palabra,columnas):

     columnas=columnas-1
     #LARGO PALABRA
     largo=len(palabra)

     #ESCOGE UNA COLUMNA Y UNA FILA AL AZAR
     columnaRandom = random.randint(6,columnas)
     filaRandom = random.randint(0,5)

    
     while True:
          if colocadorIzquierdaVerificador(M,palabra,columnas,columnaRandom,filaRandom):
               
               for i in range(0,largo):

                    while len(palabra)!=0:
                         
                         M[filaRandom][columnaRandom] = palabra[0]

                         columnaRandom-=1
                         filaRandom+=1
                         palabra=palabra[1:]
                         
                         break
                    
                    if  len(palabra)==0:
                         #mostrarTableroSopa(M)
                         return M
          else:
               
               if columnas<=9:
                    columnaRandom = random.randint(6,columnas)
                    filaRandom = random.randint(0,5)
               elif columnas>9:
                    columnaRandom = random.randint(6,columnas)
                    filaRandom = random.randint(0,9)
                       

                  

                  
#ANALIZADOR ESPACIO PARA PALABRA=======================================================
                 
               
#VERIFICADOR PALABRAS VERTICAL==============================================

#E: Una matriz, un string y un numero
#S: Una matriz
#D: Coloca una palabra verticalmente

def colocadorVerticalVerficador(M,palabra,filas,columnaRandom,filaRandom):

     for i in range(filaRandom,filas):
          
          while len(palabra)!=0:
               if M[i][columnaRandom]=='':
                    palabra=palabra[1:]
                    break
               else:
                    return False
                    
               
     return True

               


#VERIFICADOR PALABRAS HORIZONTAL==============================================

#E: Una matriz, un string y un numero
#S: Una matriz
#D: 
     
     
def colocadorHorizontalVerificador(M,palabra,columnas,columnaRandom,filaRandom):

  
     for i in range(columnaRandom,columnas):
          while len(palabra)!=0:
               if M[filaRandom][i]!='':
                    return False
                    
               else:
                    palabra=palabra[1:]
                    break
                    
                    
               
     return True    

     

#VERIFICADOR PALABRAS DIAGONAL DERECHA==============================================

#E: Una matriz, un string y un numero
#S: Una matriz
#D: 
     
     
def colocadorDerechaVerificador(M,palabra,columnas,columnaRandom,filaRandom):

     while len(palabra)!=0:
          
          if M[filaRandom][columnaRandom] == '':

               columnaRandom+=1
               filaRandom+=1
               palabra=palabra[1:]
               
               
               
          elif M[filaRandom][columnaRandom] != '':
               return False
     
     return True
                    


     
#VERIFICADOR PALABRAS DIAGONAL IZQUIERDA==============================================

#E: Una matriz, un string y un numero
#S: Una matriz
#D: 
     
     
def colocadorIzquierdaVerificador(M,palabra,columnas,columnaRandom,filaRandom):

     while len(palabra)!=0:
          
          if M[filaRandom][columnaRandom] == '':

               columnaRandom-=1
               filaRandom+=1
               palabra=palabra[1:]
               
               
          elif M[filaRandom][columnaRandom] != '' :
               return False
          
     return True


#-------------------------------------------------------------------- INTERFAZ --------------------------------------------------------------------

#IMAGENES============================================
CIRCLE = pygame.image.load('CIRCLE.png')
#====================================================

# E: nada
# S: una ventana de pygame
# D: Crea una ventana de pygame

def letterSoupGame(ID):

    pygame.init()
    #VARIABLES GLOBALES===
    global PALABRAS_SELECCIONADAS
    global PALABRAS_SOPA
    global TABLERO_OFFICIAL_SOPA
    global MATRIZSOPA_LAYER
    global DADO
    global PALABRA 
    #=====================
    crearMatrizSopa()
    TIEMPO_LS = pygame.time.get_ticks()
    
    columnas = counterFilas(TABLERO_OFFICIAL_SOPA)
    intro = True

    while intro:

        #BACKGROUND-----------------------------
        MEDIEVAL.blit(BACKGROUND3,(0, 0))
        #TIEMPO---------------------------------
        segundos = (pygame.time.get_ticks()-TIEMPO_LS)/1000
        texto(1450,50,'Tienes',20,BLANCO)
        texto(1550,50,'120',60,BLANCO)
        texto(1650,50,'segundos!',20,BLANCO)
        #IMPRIME TABLERO------------------------
        imprimirSopa(TABLERO_OFFICIAL_SOPA,columnas)
        #IMPRIME PALABRAS A ENCONTRAR-----------
        imprimirPalabras(PALABRAS_SELECCIONADAS)
        #IMPRIME TABLERO DELANTERO--------------
        imprimirSopa_AUX(MATRIZSOPA_LAYER,columnas)
        #TITULO---------------------------------
        texto(850,100,'WORD  SEARCH',100,BLANCO)
        #TITULO---------------------------------
        texto(205,120,'LIST',40,BLANCO)
        texto(210,160,'OF',40,BLANCO)
        texto(205,200,'WORDS',40,BLANCO)
        #PALABRA SELECCIONADA-------------------
        texto(1500,400,SELECTED_WORD,40,BLANCO)
        #LETRAS ELEGIDAS------------------------
        texto(1500,600,PALABRA,40,BLANCO)
        #BOTON REINICIO-------------------------
        reinicio_LetterSoup(1400,800,100,100)
        MEDIEVAL.blit(LUNACERRAR,(1400,800))
        pygame.display.update()
        #---------------------------------------
        if checkPalabra(PALABRA):
             pygame.display.update()

             if PALABRAS_SELECCIONADAS == []:
                  MEDIEVAL.blit(BACKGROUND3,(0, 0))  
                  texto(850,100,'YOU WON!',100,BLANCO)
                  PALABRA = ''
                  DADO = 0
                  changeTurno()
                  pygame.display.update()
                  pygame.time.wait(2000)
                  tableroJuego()
                  
               
             
          
               
             
          
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

         
        if segundos>120:
             MEDIEVAL.blit(BACKGROUND3,(0, 0))  
             texto(850,100,'YOU FAILED!',100,BLANCO)
             pygame.display.update()

             if ID == 1:
                Player1.setState(False)

             if ID == 2:
                Player2.setState(False)

             if ID == 3:
                Player3.setState(False)

             if ID == 4:
                Player4.setState(False)

             loss()
             DADO = 0
             changeTurno()
             pygame.display.update()
             pygame.time.wait(2000)
             pygame.display.update()
             pygame.time.wait(2000)
             tableroJuego()
             
          
        segundos = round(segundos)     
        texto(1550,200,str(segundos),50,BLANCO)
        texto(1590,200,'s',30,BLANCO)
        
        pygame.display.update()
        CLOCK.tick()
        
#IMPRIMIR MATRIZ OFICIAL======================================================
        
#E: Una matriz y un numero
#S: La matrzi de letras
#D: Imprime la matriz de letras y la ubica de acuerdo a su tamano
        
def imprimirSopa(M,columnas):
     
    if columnas == 10:
         
         #POSICIONES BOTONES
        inicio_X2 = 640
        position_X2 = 640
        position_Y2 = 280
         #POSICIONES LETRAS
        inicioX = 650
        positionX = 650
        positionY = 300
        
    if columnas == 15:
         
         #POSICIONES BOTONES
        inicio_X2 = 540
        position_X2 = 540
        position_Y2 = 180
         #POSICIONES LETRAS
        inicioX = 560
        positionX = 560
        positionY = 200
        
    if columnas == 20:
         
        #POSICIONES BOTONES
        inicio_X2 = 473
        position_X2 = 473
        position_Y2 = 175
        #POSICIONES LETRAS
        inicioX = 490
        positionX = 490
        positionY = 200
        
    for i in range(len(M)):
        for j in range(len(M[0])):
             #AGREGA LETRA
            texto(positionX,positionY,str(M[i][j]),30,BLANCO)
            #AGREGA BOTON
            letras_Botones(position_X2,position_Y2,30,40,i,j)
            #SUMA AL EJE X Y EJE Y
            position_X2 += 40
            positionX += 40
            
     #REINICIA POSICIONES----------------
            
        #BOTONES
        position_X2 = inicio_X2
        position_Y2 += 40
        #LETRAS
        positionX = inicioX
        positionY += 40
    
#IMPRIMIR MATRIZ DELANTERO======================================================
        
#E: Una matriz y un numero
#S: La matrzi de letras
#D: Imprime la matriz de letras y la ubica de acuerdo a su tamano
     
def imprimirSopa_AUX(M,columnas):

    global COORDENADAS_CIRCULOS
     
    if columnas == 10:

         #POSICIONES CIRCULO
        inicioX = 630
        positionX = 630
        positionY = 280
        
    if columnas == 15:
         
         #POSICIONES CIRCULO
        inicioX = 540
        positionX = 540
        positionY = 180
        
    if columnas == 20:

        #POSICIONES CIRCULO
        inicioX = 470
        positionX = 470
        positionY = 175
        
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 1:
                 MEDIEVAL.blit(CIRCLE,(positionX, positionY))
                 
            positionX += 40
            
     #REINICIA POSICIONES----------------
            
        #CIRCULO
        positionX = inicioX
        positionY += 40
        

#IMPRIMIR PALABRAS====================================================

#E: Una lista
#S: Las palabras
#D: Imprime las palabras para encontrar en la matriz

def imprimirPalabras(lista):
     
    position_X2 = 160
    position_Y2 = 270
    positionX = 210
    positionY = 300
    
    for i in range(len(lista)):
        #IMPRIME BOTON
        palabra_Boton(position_X2,position_Y2,100,40,i)
        #IMPRIME PALABRA
        texto(positionX,positionY,str(lista[i]),20,BLANCO)
        #SUMA EJE X Y EJE Y
        position_Y2 += 100
        positionY += 100


     
        
#BOTONES==============================================================


#======== LETRAS SOPA ========       
#E: Seis numeros
#S: No tiene
#D: Encuentra la letra


def letras_Botones(x,y,ancho,altura,i,j):

    global MATRIZSOPA_LAYER
    
    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:
           MATRIZSOPA_LAYER[i][j] = 1
           agregaLetra_Lista(TABLERO_OFFICIAL_SOPA[i][j])
           pygame.time.wait(300)
           print(PALABRA)

            
#======== PALABRA ENCONTRADA ========       
#E: Seis numeros
#S: No tiene
#D: Selecciona la palabra de la lista

def palabra_Boton(x,y,ancho,altura,i):
     
    global  SELECTED_WORD
    
    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()
    
    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
         
        if click[0] != 0:  
           SELECTED_WORD = PALABRAS_SELECCIONADAS[i]
           print(SELECTED_WORD)


#======== BOTON RESTART ========

#E: Seis numeros
#S: No tiene
#D: Reinicia el juego


def reinicio_LetterSoup(x,y,ancho,altura):

    global SELECTED_WORD
    global PALABRA
    global MATRIZSOPA_LAYER
    
    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:
             MATRIZSOPA_LAYER = np.zeros(MATRIZ_SOPA[TAMANO],dtype=int)
             SELECTED_WORD = 'XXXXXXXX'
             PALABRA = ''
             
             

#CREA PALABRA========================================================

#E: Un string
#S: No tiene
#D: Agrega la lista a palabra

def agregaLetra_Lista(letra):
     
     global PALABRA
     
     PALABRA += str(letra)
     
#CHECK PALABRA========================================================

#E: Un string
#S: No tiene
#D: Agrega la lista a palabra

def checkPalabra(palabra):
     
    global SELECTED_WORD
    global PALABRAS_SELECCIONADAS
    global PALABRA
    
    if palabra == SELECTED_WORD:
         
         PALABRAS_SELECCIONADAS.remove(SELECTED_WORD)
         SELECTED_WORD = 'XXXXXXXX'
         PALABRA = ''
         
         
         return True
    else:
         return False


#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 4
#                                                                   COLLECT COINS 
#----------------------------------------------------------------------------------------------------------------------------------------

#IMAGENES=======================================================
CHINESE = pygame.image.load('CHINESE.png')
COIN = pygame.image.load('CC.png')
#VARIABLES GLOBALES COLLECT THE COINS===========================

TABLERO_COLLECT_COINS = np.zeros((25,25),dtype=int)

TIEMPOS_CC = (30,45,60)

MONEDAS_RANDOM_P = [1,2,3,4,5,6,7,8,9,10]

MONEDAS_RANDOM_N = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]

PUNTAJE = 0


TIEMPOS_CC = (30,45,60)
#===============================================================

#CREAR TABLERO OFFICIAL

def matriz_CC():

     global TABLERO_COLLECT_COINS

     #CONTADORES INICIALES DE MONEDAS
     contadorPositivos = 312
     contadorNegativos = 313

     TABLERO_COLLECT_COINS = monedasPositivas(TABLERO_COLLECT_COINS)
     TABLERO_COLLECT_COINS = monedasNegativos(TABLERO_COLLECT_COINS)

              

#MONEDAS POSITIVAS=========================================

#E: Una matriz
#S: Una matriz
#D: Pone 312 monedas positivas en la matriz


def monedasPositivas(M):

     contadorMonedas = 313
     conta = 0
     
     while contadorMonedas>0:
          
          #ESCOGE UNA COLUMNA Y UNA FILA AL AZAR
          columnaRandom = random.randint(0,24)
          filaRandom = random.randint(0,24)
          #MONEDA
          moneda = random.choice(MONEDAS_RANDOM_P)
          
          if M[filaRandom][columnaRandom] == 0:

               M[filaRandom][columnaRandom] = moneda

               #CONTADOR
               contadorMonedas-=1
               conta+=1
     return M
          
#MONEDAS NEGATIVAS=========================================

#E: Una matriz
#S: Una matriz
#D: Pone 313 monedas positivas en la matriz


def monedasNegativos(M):

     contadorMonedas = 312
     conta= 0
     
     while contadorMonedas>0:
          
          #ESCOGE UNA COLUMNA Y UNA FILA AL AZAR
          columnaRandom = random.randint(0,24)
          filaRandom = random.randint(0,24)

          #MONEDA
          moneda = random.choice(MONEDAS_RANDOM_N)
          if M[filaRandom][columnaRandom] == 0:

               M[filaRandom][columnaRandom] = moneda

               #CONTADOR
               contadorMonedas-=1
                    
     
     return M       


def refreshCC():

    global TABLERO_COLLECT_COINS

    TABLERO_COLLECT_COINS = np.zeros((25,25),dtype = int)

           
#========================================= INTERFAZ =========================================


#PROCESO DE JUEGO BOMBER===========================================

#E: Ninguna
#S: El juego
#D: Pone el juego de Bombermario en proceso

def proceso_CC(ID):
    pygame.init()
    global DADO
    global PUNTAJE
    TIEMPO_CC = pygame.time.get_ticks()
    #MATRIZ
    matriz_CC()
    #TIEMPO
    aleatorio = random.randint(0,2)
    aleatorio = TIEMPOS_CC[aleatorio]
     
    while True:
        #BACKGROUND
        MEDIEVAL.blit(CHINESE,(0, 0))
        #TIEMPO
        segundos = (pygame.time.get_ticks()-TIEMPO_CC)/1000
        texto(1450,100,'Tienes',20,BLANCO)
        texto(1550,100,str(aleatorio),60,BLANCO)
        texto(1650,100,'segundos!',20,BLANCO)
        #MONEDAS
        imprimirCoins(TABLERO_COLLECT_COINS)
        #TITULO
        texto(900,100,'COLLECT COINS',100,BLANCO)
        #PUNTAJE
        texto(1550,700,str(PUNTAJE),60,BLANCO)
        texto(1550,600,'Score',40,BLANCO)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        if segundos>aleatorio:
            if PUNTAJE<0:
                MEDIEVAL.blit(CHINESE,(0, 0))
                texto(900,100,'YOU FAILED!',100,BLANCO)

                if ID == 1:
                    Player1.setState(False)

                if ID == 2:
                    Player2.setState(False)

                if ID == 3:
                    Player3.setState(False)

                if ID == 4:
                    Player4.setState(False)

                loss()
                DADO = 0
                changeTurno()
                pygame.display.update()
                pygame.time.wait(2000)
                refreshCC()
                PUNTAJE = 0
                tableroJuego()

            elif PUNTAJE>=0:
                MEDIEVAL.blit(CHINESE,(0, 0))
                texto(900,100,'YOU WON!',100,BLANCO)
                DADO = 0
                changeTurno()
                pygame.display.update()
                pygame.time.wait(2000)
                refreshCC()
                PUNTAJE = 0 
                tableroJuego()
 
        segundos = round(segundos)     
        texto(1550,400,str(segundos),50,BLANCO)
        texto(1590,400,'s',30,BLANCO)
        pygame.display.update()
        CLOCK.tick()
          

#IMPRIME MONEDAS =====================================================

def imprimirCoins(M):
     
     #COINS
    inicioX = 400 
    positionX = 400
    positionY = 200
    #BUTTONS
    inicioX_2 = 408 
    positionX_2 = 408
    positionY_2 = 208
    
    for i in range(len(M)):
        for j in range(len(M[0])):
             #AGREGA LETRA
            if M[i][j] != 0:
                 #IMPRIME CUBOS
                 MEDIEVAL.blit(COIN,(positionX, positionY))
                 #pygame.draw.rect(MEDIEVAL,BLANCO,(positionX_2,positionY_2,25,25))
                 #IMPRIME BOTONES
                 botonesCOINS(positionX_2,positionY_2,25,25,i,j)
                 positionX += 40
                 positionX_2 += 40
                 continue
            #SUMA AL EJE X Y EJE Y
            positionX += 40
            positionX_2 += 40

     #REINICIA POSICIONES----------------

        #MONEDAS
        positionX = inicioX
        positionX_2 = inicioX_2
        positionY += 30
        positionY_2 += 30
        
#BOTONES=======================================================

#======== BOTONES CELDAS ========

#E: Seis numeros
#S: No tiene
#D: Encuentra la letra


def botonesCOINS(x,y,ancho,altura,i,j):

    global PUNTAJE 
    
    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:
             PUNTAJE += TABLERO_COLLECT_COINS[i][j]
             TABLERO_COLLECT_COINS[i][j] = 0     
#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 5
#                                                                      MEMORY 
#----------------------------------------------------------------------------------------------------------------------------------------
#IMAGENES

TITLE_MEMORY = pygame.image.load('MEMORY_TITLE.png')

CARTA_ROJA_XL= pygame.image.load('BACK_CARD_XL.png')

#VARIABLES GLOBALES MEMORY===========================

PAREJAS = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]

PAREJAS_SELECCIONADAS = []

TABLERO_Memory = np.zeros((3,6),dtype=int)

TABLERO_Memory_Aux = np.zeros((3,6),dtype=int)

FONDO_MEMORY = pygame.image.load('BK.png')

#PAREJAS SELECCIONADAS

CARTA_1 = []

CARTA_2 = []

#=========================================================
#CREA MATRIZ
#E: No tiene
#S: Una matriz
#D: Edita la matriz con las parejas
def matriz_Memory():
     #GLOBALES------------
     global PAREJAS
     global TABLERO_Memory

     while PAREJAS !=[]:

          #ESCOGE UNA COLUMNA Y UNA FILA AL AZAR
          columnaRandom = random.randint(0,5)
          filaRandom = random.randint(0,2)

          if TABLERO_Memory[filaRandom][columnaRandom] == 0:

               TABLERO_Memory[filaRandom][columnaRandom] = PAREJAS[0]
               PAREJAS = PAREJAS[1:]

          
     

     return TABLERO_Memory

#PROCESO JUEGO MEMORY===========================================================
#E: No tiene
#S:
#D:

def proceso_Memory(playerO,player):
     #VARIABLES GLOBALES------
    global TABLERO_Memory_Aux

    global CARTA_1

    global CARTA_2

    global DADO
     #------------------------
    pygame.init()
     
    tablero = matriz_Memory()

    turno = 1

     #LISTA DE POSICIONES
    listaPlays = []

     #MARCADOR DEL JUEGO
    marcadorP1 = 0
    marcadorP2 = 0
    while True:
        #BACKGROUND
        MEDIEVAL.blit(FONDO_MEMORY,(0,0))
        #TITULO
        MEDIEVAL.blit(TITLE_MEMORY,(755,50))
         #TURNO
        MEDIEVAL.blit(ESTURNO,(20,800))
          #MARCADOR (AGREGAR NOMBRE JUGADORES)
          #1-----------------------------------
        if turno == 1:
            texto(170,900,playerO.getName(),60,BLANCO)
        texto(800,900,playerO.getName(),20,BLANCO)
        texto(800,950,str(marcadorP1),40,BLANCO)
          #2-----------------------------------
        if turno == 2:
            texto(170,900,player.getName(),60,BLANCO)
        texto(1000,900,player.getName(),20,BLANCO)
        texto(1000,950,str(marcadorP2),40,BLANCO)
          #------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
          #JUGADA
            if event.type == pygame.MOUSEBUTTONDOWN:
               
                positionX=int(event.pos[0])
                positionY=int(event.pos[1])
                positionX = jugada_Memory_X(positionX)
                positionY = jugada_Memory_Y(positionY)
                
                #VERIFICA POSICION
                if positionX == None or positionY == None:
                    continue
                #P1------------------------------------------------------------------------------------
                if turno == 1:
                    
                    if int(len(CARTA_1)+len(CARTA_2))<4:
                        
                            
                        if CARTA_1==[]:
                            
                            CARTA_1+= [positionX]+[positionY]
                            #LEVANTA CARTAS
                            #1
                            editorTableroDelantero_1(CARTA_1[0],CARTA_1[1])
                            #REINICIA POSICIONES
                            positionX = 0
                            positionY = 0
                            continue
                        if CARTA_2==[]:
                            CARTA_2+= [positionX]+[positionY]
                            #2
                            editorTableroDelantero_1(CARTA_2[0],CARTA_2[1])
                            #IMPRIME PERSONAJES------------------
                            tableroOficialPrint(tablero)
                            #IMPRIME CARTAS----------------------
                            tableroDelanteroPrint(TABLERO_Memory_Aux)
                            pygame.display.update()
                            #REINICIA POSICIONES
                            positionX = 0
                            positionY = 0
                    #ANALIZA LA JUGADA
                    if analizadorJugada(CARTA_1[0],CARTA_1[1],CARTA_2[0],CARTA_2[1]):
                        #SUMA MARCADOR P1
                        marcadorP1+=1
                    #SI LA JUGADA ESTA MALA REINICIA EL TABLERO   
                    if not analizadorJugada(CARTA_1[0],CARTA_1[1],CARTA_2[0],CARTA_2[1]):
                        #ESPERA 1 SEGUNDO
                        pygame.time.wait(1000)
                        #REINICIA LAS CARTAS
                        editorTableroDelantero_2(CARTA_1[0],CARTA_1[1])
                        editorTableroDelantero_2(CARTA_2[0],CARTA_2[1])
                        #IMPRIME CARTAS----------------------
                        tableroDelanteroPrint(TABLERO_Memory_Aux)
                        pygame.display.update()
                        
                #P2----------------------------------------------------------------------------------            
                if turno == 2:
                    
                    #VERIFICA POSITION
                    if positionX == None or positionY == None:
                        continue
                    
                    if int(len(CARTA_1)+len(CARTA_2))<4:
                        
                            
                        if CARTA_1==[]:
                            
                            CARTA_1+= [positionX]+[positionY]
                            #LEVANTA CARTAS
                            #1
                            editorTableroDelantero_1(CARTA_1[0],CARTA_1[1])
                            #REINICIA POSICIONES
                            positionX = 0
                            positionY = 0
                            continue
                        
                        if CARTA_2==[]:
                            
                            CARTA_2+= [positionX]+[positionY]
                            #2
                            editorTableroDelantero_1(CARTA_2[0],CARTA_2[1])
                            #IMPRIME PERSONAJES------------------
                            tableroOficialPrint(tablero)
                            #IMPRIME CARTAS----------------------
                            tableroDelanteroPrint(TABLERO_Memory_Aux)
                            pygame.display.update()
                            #REINICIA POSICIONES
                            positionX = 0
                            positionY = 0
                            
                    #ANALIZA LA JUGADA
                    if analizadorJugada(CARTA_1[0],CARTA_1[1],CARTA_2[0],CARTA_2[1]):
                        #SUMA MARCADOR P2
                        marcadorP2+=1
                    #SI LA JUGADA ESTA MALA REINICIA EL TABLERO   
                    if not analizadorJugada(CARTA_1[0],CARTA_1[1],CARTA_2[0],CARTA_2[1]):
                        
                        #REINICIA LAS CARTAS
                        editorTableroDelantero_2(CARTA_1[0],CARTA_1[1])
                        editorTableroDelantero_2(CARTA_2[0],CARTA_2[1])
                        #ESPERA 1 SEGUNDO
                        pygame.time.wait(1000)
                        #IMPRIME CARTAS----------------------
                        tableroDelanteroPrint(TABLERO_Memory_Aux)
                        pygame.display.update()
                        
                #CUANDO YA NO HAY PAREJAS EN EL TABLERO ANALIZA CUAL PUNTAJE ES MAYOR
                if marcadorP1+marcadorP2 == 9:
                        
                    if marcadorP1>marcadorP2:
                        #BACKGROUND
                        MEDIEVAL.blit(FONDO_MEMORY,(0,0))
                        #TITULO
                        MEDIEVAL.blit(TITLE_MEMORY,(755,50))
                        texto(900,500, playerO.getName()+' '+'HAS WON!',80,BLANCO)
                        pygame.display.update()
                        changeTurno()
                        DADO = 0
                        pygame.time.wait(2000)
                        refreshMemory()
                        tableroJuego()

                    if marcadorP1<marcadorP2:
                        #BACKGROUND
                        MEDIEVAL.blit(FONDO_MEMORY,(0,0))
                        #TITULO
                        MEDIEVAL.blit(TITLE_MEMORY,(755,50))
                        texto(900,500,player.getName()+ ' ' +'HAS WON!',80,BLANCO)
                        pygame.display.update()
                        playerO.setState(False)
                        loss()
                        changeTurno()
                        DADO = 0
                        pygame.time.wait(2000)
                        refreshMemory()
                        tableroJuego()

                        
                            
              #REINICIA VARIABLES
                CARTA_1=[]
                CARTA_2=[]
              #CAMBIO TURNO
                if turno ==1:
                    turno = 2
                else:
                    turno = 1  
             
        #IMPRIME PERSONAJES------------------
        tableroOficialPrint(tablero)
        #IMPRIME CARTAS----------------------
        tableroDelanteroPrint(TABLERO_Memory_Aux)

        pygame.display.update()
        CLOCK.tick()
               
               
               

#ANALISIS DE JUGADA (OFICIAL)=========================================================================
          
#E: Cuatro Numero
#S: Una expresion booleana
#D: Analiza si la jugada es valida

def analizadorJugada(positionX,positionY,positionX_2,positionY_2):

     global TABLERO_Memory

     if TABLERO_Memory[positionY][positionX] == TABLERO_Memory[positionY_2][positionX_2] and TABLERO_Memory[positionY][positionX]!= 0:
          
          return True
     else:
          return False

#EDITOR DE JUGADA (DELANTERO)=========================================================================
          
#E: Cuatro Numero
#S: Una expresion booleana
#D: Analiza si la jugada es valida

def editorTableroDelantero_1(positionX,positionY):

     global TABLERO_Memory_Aux

     TABLERO_Memory_Aux[positionY][positionX] = 1
          
#EDITOR DE JUGADA (DELANTERO)=========================================================================
          
#E: Cuatro Numero
#S: Una expresion booleana
#D: Analiza si la jugada es valida

def editorTableroDelantero_2(positionX,positionY):

     global TABLERO_Memory_Aux

     TABLERO_Memory_Aux[positionY][positionX] = 0     
      

#IMPRIMIR TABLERO DELANTERO=================================================================
        
#E: Una matriz
#S: Un tablero
#D: Imprime las cartas por encima de los personajes

def tableroDelanteroPrint(M):
     posicionX = 300
     posicionY = 200
     for i in range(len(M)):
          for j in range(len(M[0])):
               if M[i][j] == 0:
                    MEDIEVAL.blit(CARTA_ROJA_XL,(posicionX,posicionY))
                    posicionX+=200
               if M[i][j] != 0:
                    posicionX+=200
                    continue
          posicionX = 300
          posicionY += 230
     return
                    
#IMPRIMIR TABLERO OFICIAL=====================================================================
#E: Una matriz
#S: Un tablero
#D: Imprime los personajes en la ventana
    
def tableroOficialPrint(M):
     posicionX = 350
     posicionY = 250
     for i in range(len(M)):
          for j in range(len(M[0])):
               if M[i][j] != 0:
                    personaje = levantarCarta_Memory(int(M[i][j]))
                    MEDIEVAL.blit(personaje,(posicionX,posicionY))
                    posicionX+=200
               if M[i][j] == 0:
                   posicionX+=200
                   continue
          posicionX = 350
          posicionY += 230
     return

#ANALISIS JUGADA===============================================================================
#E: Un numero
#S: Una variable
#D: Escoge al personaje entre la lista de personajes
def levantarCarta_Memory(numero):
    personaje = PERSONAJES[numero]
    return personaje

#JUGADAS----------------------------------------------------------------------------

#POSITION X****************************

#E: Un numero
#S: Un numero
#D: Detecta la position del click del mouse y devuelve una jugada

def jugada_Memory_X(positionX):

    if 330<=positionX<=480:
        return 0
    elif 530<=positionX<=680:
        return 1
    elif 730<=positionX<=880:
        return 2
    elif 930<=positionX<=1080:
        return 3
    elif 1130<=positionX<=1280:
        return 4
    elif 1330<=positionX<=1480:
        return 5

#POSITION Y****************************

#E: Un numero
#S: Un numero
#D: Detecta la position del click del mouse y devuelve una jugada

def jugada_Memory_Y(positionY):

    if 200<=positionY<=420:
        return 0
    elif 430<=positionY<=640:
        return 1
    elif 660<=positionY<=870:
        return 2
    
    
def refreshMemory():
    global TABLERO_Memory_Aux
    global TABLERO_Memory
    global CARTA_1
    global PAREJAS_SELECCIONADAS
    global CARTA_2
    global PAREJAS

    PAREJAS = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
    CARTA_2 =[]
    PAREJAS_SELECCIONADAS = []
    CARTA_1= []
    TABLERO_Memory = np.zeros((3,6),dtype=int)
    TABLERO_Memory_Aux = np.zeros((3,6),dtype=int)

    
#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 6
#                                                                  BOMBERMARIO 
#----------------------------------------------------------------------------------------------------------------------------------------

#VARIABLES GLOBALES BOMBERMARIO===========================

TAMANO_BOMBER = ((10,10),(15,15),(20,20))

CANTIDAD_BOMBAS = 10

MATRIZ_BOMBER_LAYER = []

CUBO = pygame.image.load('CUADRADO.png')

TESORO = pygame.image.load('TESORO.png')

BOMB = pygame.image.load('Bombermario_XL.png')

TABLERO_BOMBER = []

#=========================================================
#REFRESH

def refresh_Bomber():
    global TABLERO_BOMBER
    global CANTIDAD_BOMBAS
    global MATRIZ_BOMBER_LAYER
    CANTIDAD_BOMBAS = 10
    TABLERO_BOMBER = []
    MATRIZ_BOMBER_LAYER = []
#CREA MATRIZ-----------------------------------------------
#E: Ninguna
#S: Una matriz
#D: Crea la matriz del juego

def matriz_Bomber():

     global TAMANO_BOMBER
     global MATRIZ_BOMBER_LAYER
     global TABLERO_BOMBER
     #CREA LA MATRIZ
     aleatorio = random.randint(0,2)
     tablero = np.zeros(TAMANO_BOMBER[aleatorio],dtype=int)    
     MATRIZ_BOMBER_LAYER = np.zeros(TAMANO_BOMBER[aleatorio],dtype=int)
     #EDITA TABLERO
     tablero = editarBomber(tablero)
     #EDITA TABLEROS
     MATRIZ_BOMBER_LAYER = tablero

     #CREA NUEVA MATRIZ
     fila = []
     
     for i in range(len(MATRIZ_BOMBER_LAYER)):
          
          for j in range(len(MATRIZ_BOMBER_LAYER)):
               
               fila+=[MATRIZ_BOMBER_LAYER[i][j]]
               
          TABLERO_BOMBER+=[fila]
          
          fila=[]
          
     

#EDITA LA MATRIZ (AGREGA TESORO)-----------------

#E: Una matriz
#S: Una matriz
#D: Edita la matriz del juego

def editarBomber(M):

     #ESCOGE UNA COLUMNA Y UNA FILA AL AZAR

     #EMPIEZAN EN 7 PARA NO CHOCAR A LOS LADOS
     columnaRandom = random.randint(0,7)
     filaRandom = random.randint(0,7)

     #EDITA LA MATRIZ DE ACUERDO A LAS COORDENADAS, EL TESORO ES DONDE SE UBIQUE EL CUADRADO DE 1
     
     M[filaRandom][columnaRandom] = 1
     M[filaRandom+1][columnaRandom] = 1
     M[filaRandom][columnaRandom+1] = 1
     M[filaRandom+1][columnaRandom+1] = 1
     
     return M

#EDITA LA MATRIZ (AGREGA CASILLAS YA EXPLOTADAS)-----------------

#E: Una matriz
#S: Una matriz
#D: Edita la matriz del juego

def editarBomber_2(M,fila,columna):
    
     tamano = counterFilas_Bomber(M) - 1
     #VERIFICA SI LAS FILAS Y COLUMNAS EN LAS CUALES LAS OPERACIONES SON DISTINTAS
     if fila == tamano and columna == 0:
          M[fila][columna] = 2
          M[fila-1][columna] = 2
          M[fila][columna+1] = 2
          M[fila-1][columna+1] = 2
          
          return M
     
     #PRIMERA FILA Y ULTIMA COLUMNA
     elif fila == 0 and columna == tamano:

          M[fila][columna] = 2
          M[fila-1][columna] = 2
          M[fila][columna-1] = 2
          M[fila-1][columna-1] = 2
          
          return M
        
     #ULTIMA FILA Y COLUMNA-----------------
     elif fila == tamano or columna == tamano:
          M[fila][columna] = 2
          M[fila-1][columna] = 2
          M[fila][columna-1] = 2
          M[fila-1][columna-1] = 2
          
          return M
     #EDITA LA MATRIZ DE ACUERDO A LAS COORDENADAS, EL TESORO ES DONDE SE UBIQUE EL CUADRADO DE 1
     
     else:
          M[fila][columna] = 2
          M[fila+1][columna] = 2
          M[fila][columna+1] = 2
          M[fila+1][columna+1] = 2
     
          return M

#PROCESO DE JUEGO BOMBER===========================================

#E: Ninguna
#S: El juego
#D: Pone el juego de Bombermario en proceso

def proceso_Bomber(ID):
     global DADO
     global CANTIDAD_BOMBAS
     #CREA TABLERO
     matriz_Bomber()
     #TAMANO
     columnas = counterFilas_Bomber(TABLERO_BOMBER)
     #CONTADOR CASILLAS DESCUBIERTAS DEL TESORO
     #TABLERO PANTALLA
     tablero = TABLERO_BOMBER
     while True:
          #BACKGROUND-----------------------------
          MEDIEVAL.blit(BG,(0, 0))
          #IMPRIME MATRIZ TESORO------------------
          imprimirTesoroM(TABLERO_BOMBER,columnas)
          #IMPRIMIR DELANTERA---------------------
          imprimirCeldasM(MATRIZ_BOMBER_LAYER,columnas)
          #TITULO---------------------------------
          texto(850,100,'BOMBER',100,BLANCO)
          #VIDAS----------------------------------
          imprimirVidas()
          
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                 positionX=int(event.pos[0])
                 positionY=int(event.pos[1])
                 if restarBombas(positionX,positionY,columnas):
                    pygame.time.wait(500)
                    CANTIDAD_BOMBAS-=1
                 
            if analisisBomber_Winner(MATRIZ_BOMBER_LAYER):
               MEDIEVAL.blit(BG,(0, 0))
               texto(850,100,'YOU WON!',100,BLANCO)
               pygame.display.update()

               DADO = 0
               changeTurno()
               pygame.time.wait(2000)
               refresh_Bomber()
               tableroJuego()
               
            if CANTIDAD_BOMBAS==0:
                MEDIEVAL.blit(BG,(0, 0))
                texto(850,100,'YOU FAILED!',100,BLANCO)
                pygame.display.update()

                if ID == 1:
                    Player1.setState(False)

                if ID == 2:
                    Player2.setState(False)

                if ID == 3:
                    Player3.setState(False)

                if ID == 4:
                    Player4.setState(False)

                loss()

                DADO = 0
                changeTurno()
                pygame.time.wait(2000)
                refresh_Bomber()
                tableroJuego()

                
               
               
         
             
        
          pygame.display.update()
          CLOCK.tick()

          
     
#ANALISIS GANADOR====================================================

#E: Dos numeros y una matriz
#S: Una expresion booleana
#D: Analiza para verificar si hay un ganador

def analisisBomber_Winner(M):
     for i in range(len(M)):
          for j in range(len(M[0])):

               if  M[i][j] == 1:
                    return False
                    
               continue
                         
     return True
     
#ANALISIS CANTIDAD DE FILAS DE LA MATRIZ=============================

#E: Una matriz
#S: Un numero
#D: Verifica la cantidad de letras de la matriz

def counterFilas_Bomber(M):
     
     counter = 0
     
     for fila in M:
          counter+=1
          
     return counter

#IMPRIMIR MATRIZ DELANTERO======================================================
        
#E: Una matriz y un numero
#S: La matrzi de letras
#D: Imprime la matriz de letras y la ubica de acuerdo a su tamano
        
def imprimirCeldasM(M,columnas):
     
    if columnas == 10:
         
         #POSICIONES BOTONES
        inicioX_2 = 668
        positionX_2 = 668
        positionY_2 = 312
         #POSICIONES LETRAS
        inicioX = 650
        positionX = 650
        positionY = 300
        
    if columnas == 15:
         
         #POSICIONES BOTONES
        inicioX_2 = 578
        positionX_2 = 578
        positionY_2 = 212 

         #POSICIONES LETRAS
        inicioX = 560
        positionX = 560
        positionY = 200
        
    if columnas == 20:
         
        #POSICIONES BOTONES
        inicioX_2 = 460
        positionX_2 = 460
        positionY_2 = 140    
        #POSICIONES LETRAS
        inicioX = 443
        positionX = 443
        positionY = 130
        
    for i in range(len(M)):
        for j in range(len(M[0])):
             #AGREGA LETRA
            if M[i][j] == 0 or M[i][j] == 1:
                 #IMPRIME CUBOS
                 MEDIEVAL.blit(CUBO,(positionX,positionY))
                 #RECTANGULOS
                 #pygame.draw.rect(MEDIEVAL,BLANCO,(positionX_2,positionY_2,35,35))
                 #BOTONES
                 botonesCeldas(positionX_2,positionY_2,35,35,i,j)
                 positionX_2 += 40
                 positionX += 40
                 continue
            #SUMA AL EJE X Y EJE Y
            positionX += 40
            positionX_2 += 40
            
     #REINICIA POSICIONES----------------
            
        #BOTONES
        positionX_2 = inicioX_2    
        positionY_2 +=40
        #LETRAS
        positionX = inicioX
        positionY += 40
        

#IMPRIMIR MATRIZ TESORO======================================================
        
#E: Una matriz y un numero
#S: La matrzi de letras
#D: Imprime la matriz de letras y la ubica de acuerdo a su tamano
        
def imprimirTesoroM(M,columnas):
     
    if columnas == 10:
         
         #POSICIONES 
        inicioX = 650
        positionX = 650
        positionY = 300
        
    if columnas == 15:
         
         #POSICIONES 
        inicioX = 560
        positionX = 560
        positionY = 200
        
    if columnas == 20:

        #POSICIONES 
        inicioX = 443
        positionX = 443
        positionY = 130
        
    for i in range(len(M)):
        for j in range(len(M[0])):
             #AGREGA LETRA
            if M[i][j] == 1:
                 MEDIEVAL.blit(TESORO,(positionX,positionY))
                 positionX += 10
            #SUMA AL EJE X Y EJE Y
            positionX += 40

        #POSICIONES
        positionX = inicioX
        positionY += 40

#IMPRIMIR VIDA======================================================
        
#E: Lista y un numero
#S: Una imagen
#D: Imprime la cantidad de vidas

def imprimirVidas():
     texto(1400,100,'Bombs left:',30,BLANCO)
     texto(1450,200,str(CANTIDAD_BOMBAS),80,BLANCO)
     MEDIEVAL.blit(BOMB,(1270,150))
          
     
     
#BOTONES==============================================================


#======== CUENTA BOMBAS RESTANTES ========

#E: Seis numeros
#S: No tiene
#D: Encuentra la letra

def restarBombas(positionX,positionY,tamano):

     if tamano == 10:
          
          if 665<positionX<1065 and 310<positionY<711:
               return True
          else:
               return False

     if tamano == 15:

          if 570<positionX<1180 and 209<positionY<810:
               return True
          else:
               return False
        
     if tamano == 20:

         if 443<positionX<1260 and 140<positionY<940:
              return True
         else:
              return False

#======== BOTONES CELDAS ========

#E: Seis numeros
#S: No tiene
#D: Encuentra la letra


def botonesCeldas(x,y,ancho,altura,i,j):

    global MATRIZ_BOMBER_LAYER
    
    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:
             MATRIZ_BOMBER_LAYER = editarBomber_2(MATRIZ_BOMBER_LAYER,i,j)
             pygame.time.wait(200)
             return

            
#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 8
#                                                                      CARDS 
#----------------------------------------------------------------------------------------------------------------------------------------

#-----------------------   Globales del minijuego   --------------------------------

#IMAGENES DE LAS CARTAS

BACK_CARD = pygame.image.load('BACK_CARD.png')

A_AZUL = pygame.image.load('A_AZUL.png')

A_ROSA = pygame.image.load('A_ROSA.png')

A_VERDE = pygame.image.load('A_VERDE.png')

A_ROJA = pygame.image.load('A_ROJA.png')

DOS_AZUL = pygame.image.load('2_AZUL.png')

DOS_ROSA = pygame.image.load('2_ROSA.png')

DOS_VERDE = pygame.image.load('2_VERDE.png')

DOS_ROJA = pygame.image.load('2_ROJA.png')

TRES_AZUL = pygame.image.load('3_AZUL.png')

TRES_ROSA = pygame.image.load('3_ROSA.png')

TRES_VERDE = pygame.image.load('3_VERDE.png')

TRES_ROJA = pygame.image.load('3_ROJA.png')

CUATRO_AZUL = pygame.image.load('4_AZUL.png')

CUATRO_ROSA = pygame.image.load('4_ROSA.png')

CUATRO_VERDE = pygame.image.load('4_VERDE.png')

CUATRO_ROJA = pygame.image.load('4_ROJA.png')

CINCO_AZUL = pygame.image.load('5_AZUL.png')

CINCO_ROSA = pygame.image.load('5_ROSA.png')

CINCO_VERDE = pygame.image.load('5_VERDE.png')

CINCO_ROJA = pygame.image.load('5_ROJA.png')

SEIS_AZUL = pygame.image.load('6_AZUL.png')

SEIS_ROSA = pygame.image.load('6_ROSA.png')

SEIS_VERDE = pygame.image.load('6_VERDE.png')

SEIS_ROJA = pygame.image.load('6_ROJA.png')

SIETE_AZUL = pygame.image.load('7_AZUL.png')

SIETE_ROSA = pygame.image.load('7_ROSA.png')

SIETE_VERDE = pygame.image.load('7_VERDE.png')

SIETE_ROJA = pygame.image.load('7_ROJA.png')

OCHO_AZUL = pygame.image.load('8_AZUL.png')

OCHO_ROSA = pygame.image.load('8_ROSA.png')

OCHO_VERDE = pygame.image.load('8_VERDE.png')

OCHO_ROJA = pygame.image.load('8_ROJA.png')

NUEVE_AZUL = pygame.image.load('9_AZUL.png')

NUEVE_ROSA = pygame.image.load('9_ROSA.png')

NUEVE_VERDE = pygame.image.load('9_VERDE.png')

NUEVE_ROJA = pygame.image.load('9_ROJA.png')

DIEZ_AZUL = pygame.image.load('10_AZUL.png')

DIEZ_ROSA = pygame.image.load('10_ROSA.png')

DIEZ_VERDE = pygame.image.load('10_VERDE.png')

DIEZ_ROJA = pygame.image.load('10_ROJA.png')

J_AZUL = pygame.image.load('J_AZUL.png')

J_ROSA = pygame.image.load('J_ROSA.png')

J_VERDE = pygame.image.load('J_VERDE.png')

J_ROJA = pygame.image.load('J_ROJA.png')

Q_AZUL = pygame.image.load('Q_AZUL.png')

Q_ROSA = pygame.image.load('Q_ROSA.png')

Q_VERDE = pygame.image.load('Q_VERDE.png')

Q_ROJA = pygame.image.load('Q_ROJA.png')

K_AZUL = pygame.image.load('K_AZUL.png')

K_ROSA = pygame.image.load('K_ROSA.png')

K_VERDE = pygame.image.load('K_VERDE.png')

K_ROJA = pygame.image.load('K_ROJA.png')

BK = pygame.image.load('BK.png')

CARDS = [DOS_ROSA,DOS_AZUL,DOS_VERDE,DOS_ROJA,TRES_ROSA,TRES_AZUL,TRES_VERDE,TRES_ROJA,CUATRO_ROSA,CUATRO_AZUL,CUATRO_VERDE,CUATRO_ROJA, CINCO_ROSA,CINCO_AZUL,CINCO_VERDE,CINCO_ROJA,SEIS_ROSA,SEIS_AZUL,SEIS_VERDE,SEIS_ROJA,SIETE_ROSA,SIETE_AZUL,SIETE_VERDE,SIETE_ROJA,OCHO_ROSA,OCHO_AZUL,OCHO_VERDE,OCHO_ROJA,NUEVE_ROSA,NUEVE_AZUL,NUEVE_VERDE,NUEVE_ROJA,DIEZ_ROSA,DIEZ_AZUL,DIEZ_VERDE,DIEZ_ROJA,J_ROSA,J_AZUL,J_VERDE,J_ROJA,Q_ROSA,Q_AZUL,Q_VERDE,Q_ROJA,K_ROSA,K_AZUL,K_VERDE,K_ROJA,A_ROSA,A_AZUL,A_VERDE,A_ROJA]

CARDS_VALUE = {0:0,DOS_ROSA:2,DOS_AZUL:2.1,DOS_VERDE:2.2,DOS_ROJA:2.3,TRES_ROSA:3,TRES_AZUL:3.1,TRES_VERDE:3.2,TRES_ROJA:3.3,CUATRO_ROSA:4,CUATRO_AZUL:4.1,CUATRO_VERDE:4.2,CUATRO_ROJA:4.3, CINCO_ROSA:5,CINCO_AZUL:5.1,CINCO_VERDE:5.2,CINCO_ROJA:5.3,SEIS_ROSA:6,SEIS_AZUL:6.1,SEIS_VERDE:6.2,SEIS_ROJA:6.3,SIETE_ROSA:7,SIETE_AZUL:7.1,SIETE_VERDE:7.2,SIETE_ROJA:7.3,OCHO_ROSA:8,OCHO_AZUL:8.1,OCHO_VERDE:8.2,OCHO_ROJA:8.3,NUEVE_ROSA:9,NUEVE_AZUL:9.1,NUEVE_VERDE:9.2,NUEVE_ROJA:9.3,DIEZ_ROSA:10,DIEZ_AZUL:10.1,DIEZ_VERDE:10.2,DIEZ_ROJA:10.3,J_ROSA:11,J_AZUL:11.1,J_VERDE:11.2,J_ROJA:11.3,Q_ROSA:12,Q_AZUL:12.1,Q_VERDE:12.2,Q_ROJA:12.3,K_ROSA:13,K_AZUL:13.1,K_VERDE:13.2,K_ROJA:13.3,A_ROSA:14,A_AZUL:14.1,A_VERDE:14.2,A_ROJA:14.3}



#------------------------------------   BOTONES MINIJUEGO   ---------------------------------------

def botonCards(x,y,ancho,altura,card):
    
    global turnoCARDS
    global electionP1C
    global electionP2C
    global electionP3C
    global electionP4C

    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:

            if turnoCARDS == 0:
                electionP1C = card

            if turnoCARDS == 1:
                electionP2C = card

            if turnoCARDS == 2:
                electionP3C = card

            if turnoCARDS == 3:
                electionP4C = card
            turnoCARDS += 1

            


def printCards(turno):

    num = random.randint(0,51)
    card = CARDS[num]
    cont = 15
    x = 200
    y = 300

    while cont != 0:
        MEDIEVAL.blit(BACK_CARD,(x,y))
        botonCards(x,y,78,104,card)
        x+= 100
        cont -=1

def checkWin(players):
    global electionP1C
    global electionP2C
    global electionP3C
    global electionP4C


    ganador = max(players)

    if CARDS_VALUE[electionP1C] != ganador:
        Player1.setState(False)

    if CARDS_VALUE[electionP2C] != ganador:
        Player2.setState(False)

    if CARDS_VALUE[electionP3C] != ganador:
        Player3.setState(False)

    if CARDS_VALUE[electionP4C] != ganador:
        Player4.setState(False)

    if Player1.getState():
        return Player1.getName()

    if Player2.getState():
        return Player2.getName()

    if Player3.getState():
        return Player3.getName()

    if Player4.getState():
        return Player4.getName()


#========================================================= VENTANA =====================================================================



# E: nada
# S: una ventana de pygame
# D: Crea una ventana de pygame

def cards():

    global DADO
    global TURNO
    global turnoCARDS
    global electionP1C
    global electionP2C
    global electionP3C
    global electionP4C

    

    electionP1C = 0

    electionP2C = 0

    electionP3C = 0

    electionP4C = 0

    turnoCARDS = 0

    palyers = len(ORDER)

    intro = True

    while intro:

        # Pone el Background
        MEDIEVAL.blit(BK,(0, 0) )

        # Pone nombre del jugador
        texto(900,150,'SELECT A CARD',80,BLANCO)
        texto(900,200,'Starting by Player 1',40,BLANCO)

        printCards(turnoCARDS)

        pygame.display.update()


        if palyers == 2:
            texto(300,600,Player1.getName()+"'s election: ",50,BLANCO)
            if electionP1C != 0:
                MEDIEVAL.blit(electionP1C,(250,700))

            texto(1500,600,Player2.getName()+"'s election: ",50,BLANCO)
            if electionP2C != 0:
                MEDIEVAL.blit(electionP2C,(1450,700))

        if palyers == 3:
            texto(300,600,Player1.getName()+"'s election: ",40,BLANCO)
            if electionP1C != 0:
                MEDIEVAL.blit(electionP1C,(250,700))

            texto(900,600,Player2.getName()+"'s election: ",40,BLANCO)
            if electionP2C != 0:
                MEDIEVAL.blit(electionP2C,(850,700))

            texto(1500,600,Player3.getName()+"'s election: ",40,BLANCO)
            if electionP3C != 0:
                MEDIEVAL.blit(electionP3C,(1450,700))

        if palyers == 4:
            texto(300,600,Player1.getName()+"'s election: ",30,BLANCO)
            if electionP1C != 0:
                MEDIEVAL.blit(electionP1C,(250,700))

            texto(700,600,Player2.getName()+"'s election: ",30,BLANCO)
            if electionP2C != 0:
                MEDIEVAL.blit(electionP2C,(650,700))

            texto(1100,600,Player3.getName()+"'s election: ",30,BLANCO)
            if electionP3C != 0:
                MEDIEVAL.blit(electionP3C,(1050,700))

            texto(1500,600,Player4.getName()+"'s election: ",30,BLANCO)
            if electionP4C != 0:
                MEDIEVAL.blit(electionP4C,(1450,700))


        if turnoCARDS >= palyers:
            ganador = checkWin([CARDS_VALUE[electionP1C],CARDS_VALUE[electionP2C],CARDS_VALUE[electionP3C],CARDS_VALUE[electionP4C]])
            texto(900,500,str(ganador),50,BLANCO)
            texto(900,550,str('HAS WON!'),50,BLANCO)
            pygame.display.update()

            loss()

            DADO = 0
            changeTurno()

            pygame.time.wait(3000)


            tableroJuego()



        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        pygame.display.update()
        CLOCK.tick(5)

#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 9
#                                                                   TRAP THE CAT 
#----------------------------------------------------------------------------------------------------------------------------------------

#VARIABLES GLOBALES TRAP THE CAT===========================

TABLERO_TG= np.zeros((11,11), dtype = int)

TABLERO_TG[5][5] = 1

THIEF = pygame.image.load('THIEF.PNG')

BACK_CARD_CTC = pygame.image.load('BACK_CARDCTC_S.png')

JOKER = pygame.image.load('JOKER_S.png')

Escaped = False
Victoria = False

#----------------------------------------------------------------------------------------------------------------------------------------
def refreshTTC():
    global Victoria
    global TABLERO_TG

    TABLERO_TG= np.zeros((11,11), dtype = int)

    TABLERO_TG[5][5] = 1
    Victoria = False

def isValid(i,j):

    if TABLERO_TG[i][j] == 0:
        return True
    else:
        return False

def putPiece(i,j,piece):

    global TABLERO_TG

    if isValid(i,j):
        TABLERO_TG[i][j] = piece

    return


def findJoker():

    for fila in range(len(TABLERO_TG)):
        for columna in range(len(TABLERO_TG[0])):
            if TABLERO_TG[fila][columna] == 1:
                return (fila,columna)
            else:
                continue

def moveJoker():
    global Escaped
    global Victoria

    track = findJoker()

    i = track[0]
    j = track[1]

    try:
        if TABLERO_TG[i][j+1] == 0:
            TABLERO_TG[i][j] = 0
            return putPiece(i,j+1,1)

        elif TABLERO_TG[i+1][j-1] == 0:
            TABLERO_TG[i][j] = 0
            return putPiece(i+1,j-1,1)

        elif TABLERO_TG[i+1][j+1] == 0:
            TABLERO_TG[i][j] = 0
            return putPiece(i+1,j+1,1)

        elif TABLERO_TG[i+1][j] == 0:
            TABLERO_TG[i][j] = 0
            return putPiece(i+1,j,1)

        elif TABLERO_TG[i][j-1] == 0:
            TABLERO_TG[i][j] = 0
            return putPiece(i,j-1,1)

        elif TABLERO_TG[i-1][j] == 0:
            TABLERO_TG[i][j] = 0
            return putPiece(i-1,j,1)

        elif TABLERO_TG[i-1][j+1] == 0:
            TABLERO_TG[i][j] = 0
            return putPiece(i-1,j+1,1)

        elif TABLERO_TG[i+1][j+1] == 0:
            TABLERO_TG[i][j] = 0
            return putPiece(i+1,j+1,1)

        elif TABLERO_TG[i-1][j-1] == 0:
            TABLERO_TG[i][j] = 0
            return putPiece(i-1,j-1,1)

        else:
            Victoria = True

    except:
        Escaped = True
          



def botonCTC(x,y,ancho,altura,i,j):

    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:
            putPiece(i,j,2)
            moveJoker()



def printBoardCTC():
    global Victoria

    i = 0
    j = 0

    x = 320
    y = 0

    for fila in range(0,11):
        for columna in range(0,11):

            if TABLERO_TG[fila][columna] == 0:
                botonCTC(x,y,68,91,i,j)
                MEDIEVAL.blit(BACK_CARD_CTC,(x,y))
                x+= 117
                
            elif TABLERO_TG[fila][columna] == 1 :
                MEDIEVAL.blit(THIEF,(x,y))
                x += 117

            elif TABLERO_TG[fila][columna] == 2 :
                MEDIEVAL.blit(JOKER,(x,y))
                x += 117
            j += 1

        x = 320
        j = 0

        y += 90
        i += 1


     
def trapTheCat(ID):
    global DADO
    global Escaped
    global TABLERO_TG

    intro = True

    while  intro:


        # Pone el Background
        MEDIEVAL.blit(BK,(0, 0))

        texto(100,100,'Try',80,BLANCO)
        texto(100,175,'to',80,BLANCO)
        texto(130,250,'Catch',80,BLANCO)
        texto(100,325,'the',80,BLANCO)
        texto(110,400,'Thief',80,BLANCO)

        #Imprime el tablero
        printBoardCTC()

        if Escaped:
            if ID == 1:
                Player1.setState(False)

            if ID == 2:
                Player2.setState(False)

            if ID == 3:
                Player3.setState(False)

            if ID == 4:
                Player4.setState(False)

            texto(100,100,'Try',80,BLANCO)
            texto(100,175,'to',80,BLANCO)
            texto(130,250,'Catch',80,BLANCO)
            texto(100,325,'the',80,BLANCO)
            texto(110,400,'Thief',80,BLANCO)

            #Imprime el tablero
            printBoardCTC()

            texto(1680,100,'The',80,BLANCO)
            texto(1680,175,'Thief',80,BLANCO)
            texto(1680,250,'Escaped!',60,BLANCO)

            pygame.display.update()

            pygame.time.wait(3000)

            loss()

            changeTurno()

            Escaped = False

            DADO = 0
            refreshTTC()
            tableroJuego()

        if Victoria:
            texto(100,600,'You',80,BLANCO)
            texto(150,675,'Caught',80,BLANCO)
            texto(100,750,'The',80,BLANCO)
            texto(130,825,'Thief',80,BLANCO)

            texto(100,100,'Try',80,BLANCO)
            texto(100,175,'to',80,BLANCO)
            texto(130,250,'Catch',80,BLANCO)
            texto(100,325,'the',80,BLANCO)
            texto(110,400,'Thief',80,BLANCO)

            #Imprime el tablero
            printBoardCTC()

            pygame.display.update()

            pygame.time.wait(3000)

            loss()

            changeTurno()

            DADO = 0
            refreshTTC()
            tableroJuego()



        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        pygame.display.update()
        CLOCK.tick(5)

#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 7
#                                                                    GUESS WHO 
#----------------------------------------------------------------------------------------------------------------------------------------

#VARIABLES GLOBALES GUESS WHO===========================

BIG = pygame.image.load('BIG.png')
BILL = pygame.image.load('BILL.png')
BOB = pygame.image.load('BOB.png')
BOJACK = pygame.image.load('BOJACK.png')
DAVINCI = pygame.image.load('DAVINCI.png')
DRE = pygame.image.load('DRE.png')
EINSTEIN = pygame.image.load('Einstein.png')
ELON = pygame.image.load('ELON.png')
EMINEM = pygame.image.load('EM.png')
PEWDIEPIE = pygame.image.load('Pewdiepie.png')
SNOOP = pygame.image.load('SNOOP.png')
TESLA = pygame.image.load('TESLA.png')
THOR = pygame.image.load('THOR.png')
TONY = pygame.image.load('TONY.png')
TUPAC = pygame.image.load('TUPAC.png')
WICK = pygame.image.load('WICK.png')

CUBO_GUESS = pygame.image.load('CUBO_2.png')

GUESS_WHO_CHARACTERS = {BIG:'Notorious B.I.G', BILL:'Bill Gates',BOB:'Bob Marley',BOJACK:'Bojack',DAVINCI:'Da Vinci',DRE:'Dr.Dre',EINSTEIN:'Einstein',ELON:'Elon Musk',EMINEM: 'Eminem',PEWDIEPIE:'Pewdiepie',SNOOP:'Snopp Dog',TESLA:'Nicola Tesla',THOR:'Thor',TONY:'Tony Stark',TUPAC:'Tupac Shaqur',WICK:'Keanu Reeves'}

PERSONAJES_GUESS = [BIG,BILL,BOB,BOJACK,DAVINCI,DRE,EINSTEIN,ELON,EMINEM,PEWDIEPIE,PEWDIEPIE,SNOOP,TESLA,THOR,TONY,TUPAC,WICK]
TABLERO_GUESS = np.zeros((10,10),dtype=int)
VIDAS = 0
GUESS = ''


#----------------------------------------------------------------------------

def printNames():
    x = 1600
    y = 130

    for key in GUESS_WHO_CHARACTERS:
        texto(x,y,GUESS_WHO_CHARACTERS[key],40,BLANCO)
        botonNombresGuess(x-140,y-30,290,40,GUESS_WHO_CHARACTERS[key])

        y += 55

#----------------------------------------------------------------------------

def printCover():
    global TABLERO_GUESS

    x = 525
    y = 200

    for i in range(0,10):
        for j in range(0,10):
            botonCeldaGuess(x,y,70,70,i,j)
            if TABLERO_GUESS[i][j] == 0:
                MEDIEVAL.blit(CUBO_GUESS,(x,y))

            x += 70

        x = 525
        y += 70

#----------------------------------------------------------------------------

def botonNombresGuess(x,y,ancho,altura,respuesta):
    global GUESS

    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:

            if GUESS == '':
                GUESS = respuesta

            else:
                return


#----------------------------------------------------------------------------


def botonCeldaGuess(x,y,ancho,altura,i,j):
    global TABLERO_GUESS
    global VIDAS

    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
        if click[0] != 0:

            if TABLERO_GUESS[i][j] == 0 and VIDAS > 0:
                TABLERO_GUESS[i][j] = 1

                VIDAS -= 1

            else:
                return

#----------------------------------------------------------------------------

def refreshGuessWho():
    global TABLERO_GUESS
    global VIDAS
    global GUESS

    TABLERO_GUESS = np.zeros((10,10),dtype=int)
    VIDAS = 0
    GUESS = ''

#----------------------------------------------------------------------------

def guessWho(ID):
    global TABLERO_GUESS
    global VIDAS
    global DADO

    VIDAS = random.randint(4,8)

    intro = True

    personaje = random.randint(0,15)

    while intro:

        # Pone el Background
        MEDIEVAL.blit(BK,(0, 0) )

        texto(850,100,"Guess Who!",80,BLANCO)

        texto(1600,50,'Characters',60,BLANCO)

        texto(250,200,'Casillas disponobles: ',40,BLANCO)

        texto(250,250,str(VIDAS),40,BLANCO)

        #IMPRIME LOS NOMBRES A ELEGIR
        printNames()

        #IMPRIME LA IMAGEN A ADIVINAR
        MEDIEVAL.blit(PERSONAJES_GUESS[personaje],(525,200))

        #IMPRIME EL COVER
        printCover()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if GUESS != '':
            if GUESS == GUESS_WHO_CHARACTERS[PERSONAJES_GUESS[personaje]]:
                texto(250,400,'YOU WON!!',80,BLANCO)
                pygame.display.update()

                DADO = 0

                changeTurno()

                refreshGuessWho()

                pygame.time.wait(2000)

                tableroJuego()

            else:
                texto(250,400,'YOU LOST',80,BLANCO)
                pygame.display.update()

                if ID == 1:
                    Player1.setState(False)

                if ID == 2:
                    Player2.setState(False)

                if ID == 3:
                    Player3.setState(False)

                if ID == 4:
                    Player4.setState(False)

                loss()

                DADO = 0

                changeTurno()

                refreshGuessWho()

                pygame.time.wait(2000)

                tableroJuego()

        pygame.display.update()
        CLOCK.tick(5)


    
#===================================================================================================
#===============================================   TABLERO   =======================================
#===================================================================================================

'''
E: nada
S: un blit de pygame
D: Imprime las plataformas del tablero
'''

def paintTablero():

    x = 100

    #PLATAFORMA INICIO
    MEDIEVAL.blit(PLATAFROMA2,(0,90))

    #PRIMERA FILA

    for columna in range(len(GAMEBOARD[0])):
        MEDIEVAL.blit(PLATAFROMA,(x+(columna*200),235))
        x+=3


    #ESCALERA
    MEDIEVAL.blit(LADDER,(1680,300))

    #ESCALERA
    MEDIEVAL.blit(LADDER,(1680,260))

    #MITAD 
    MEDIEVAL.blit(PLATAFROMA,(1521,340))

    #ESCALERA 
    MEDIEVAL.blit(LADDER,(1640,410))

    #ESCALERA
    MEDIEVAL.blit(LADDER,(1640,370))


    #SEGUNDA FILA

    x = 100

    for columna in range(len(GAMEBOARD[0])):
        MEDIEVAL.blit(PLATAFROMA,(x+(columna*200),450))
        x+=3

    #ESCALERA
    MEDIEVAL.blit(LADDER,(135,500))

    #ESCALERA
    MEDIEVAL.blit(LADDER,(135,550))

    #ESCALERA
    MEDIEVAL.blit(LADDER,(135,550))

    #MITAD
    MEDIEVAL.blit(PLATAFROMA,(100,580))

    #ESCALERA
    MEDIEVAL.blit(LADDER,(170,620))

    #ESCALERA
    MEDIEVAL.blit(LADDER,(170,700))

    #TERCERA FILA

    x = 100

    for columna in range(len(GAMEBOARD[0])):
        MEDIEVAL.blit(PLATAFROMA,(x+(columna*200),710))
        x+=3

    #PLATAFORMA FINAL
    MEDIEVAL.blit(PLATAFROMA3,(1600,820))

    # -----------------------   SIMBOLOGIA   -----------------------

    MEDIEVAL.blit(SYMBOLOGY,(0,890))

    texto(300,940,'Mini Games',15,TURQUESA)

    #*************JUEGOS*************
                                  
    #ATRAPAR GATO
    MEDIEVAL.blit(SIM_ATRAPARGATO,(30,950))
    texto(50,990,'Trap the Cat',10,BLANCO)

    #BOMBERMARIO
    MEDIEVAL.blit(SIM_BOMBERMARIO,(105,950))
    texto(120,990,'Bomber',10,BLANCO)

                                  

    #CARDS
    MEDIEVAL.blit(SIM_CARDS,(215,950))
    texto(230,990,'Cards',10,BLANCO)

    #COLLECT COINS
    MEDIEVAL.blit(SIM_COLLECT_COINS,(280,950))
    texto(295,990,'Collect Coins',10,BLANCO)

    #GATO NORMAL
    MEDIEVAL.blit(SIM_TICTACTOE,(355,950))
    texto(365,990,'Tic Tac Toe',10,BLANCO)

    #GUESS WHO
    MEDIEVAL.blit(SIM_GUESS_WHO,(420,950))
    texto(440,990,'Guess Who',10,BLANCO)


    #MEMORY
    MEDIEVAL.blit(SIM_MEMORY,(160,950))
    texto(175,990,'Memory',10,BLANCO)

    #LETTER SOUP
    MEDIEVAL.blit(SIM_SOPA,(490,950))
    texto(510,990,'Letter Soup',10,BLANCO)

    #MEMORY PATH
    MEDIEVAL.blit(SIM_MEMORY_PATH,(560,950))
    texto(580,990,'Memory Path',10,BLANCO)

    #*************CASILLAS ESPECIALES*************
                                  
    texto(840,940,'Special Cells',15,TURQUESA)

    #CARCEL
    MEDIEVAL.blit(SIM_CARCEL,(700,950))
    texto(715,990,'Jail',10,BLANCO)
                                  
    #COLA
    MEDIEVAL.blit(SIM_COLA,(750,950))
    texto(765,990,'Tail',10,BLANCO)

    #ESTRELLA 
    MEDIEVAL.blit(SIM_ESTRELLA,(800,950))
    texto(815,990,'Star',10,BLANCO)
                                  
    #TUBOS
    MEDIEVAL.blit(SIM_TUBOS,(850,950))
    texto(865,990,'Tubes',10,BLANCO)
                                  
                                  
    #FLOR DE HIELO  
    MEDIEVAL.blit(SIM_FlOR_H,(900,950))
    texto(915,990,'Snow',10,BLANCO)

    #FLOR DE FUEGO
    MEDIEVAL.blit(SIM_FlOR_F,(950,940))
    texto(965,990,'Fire',10,BLANCO)


def paintCells():
    global GAMEBOARD

    cellRandomizer()

    for i in range(len(GAMEBOARD)):
        for j in range(len(GAMEBOARD[0])):

            if GAMEBOARD[i][j] == 0.0:
                continue

            if i == 0:
                y = 290
                MEDIEVAL.blit(MINIJUEGOS[GAMEBOARD[i][j]],(j*200+210,y))
            if i == 1:
                y == 300
                MEDIEVAL.blit(MINIJUEGOS[GAMEBOARD[i][j]],(j*200+210,y+100))
            if i == 2:
                y == 400
                MEDIEVAL.blit(MINIJUEGOS[GAMEBOARD[i][j]],(j*200+210,y+210))
            if i == 3:
                y == 500
                MEDIEVAL.blit(MINIJUEGOS[GAMEBOARD[i][j]],(j*200+210,y+340))
            if i == 4:
                y == 600
                MEDIEVAL.blit(MINIJUEGOS[GAMEBOARD[i][j]],(j*200+210,y+470))



def randomPick():
    global LISTA

    if LISTA == []:
        return

    number = random.choice(LISTA)
    LISTA.remove(number)

    return number


def cellRandomizer():
    global GAMEBOARD

    if LISTA == []:
        return

    for i in range(len(GAMEBOARD)):
        if i%2 == 0:
            for j in range(8):
                GAMEBOARD[i][j] = randomPick()
        else:
            continue

    GAMEBOARD[1][7] = randomPick()

    GAMEBOARD[3][0] = randomPick()
                                                

                                                  
#==========================================   MENU PRINCIPAL  ==========================================

# E: nada
# S: una ventana de pygame
# D: Crea una ventana de pygame


def menuPrincipal():
    pygame.display.update()


    intro = True

    while intro:

        # Pone el Background
        MEDIEVAL.blit(BACKGROUND,(0, 0) )

        # Pone el Titulo
        MEDIEVAL.blit(TITLE,(70,100))

        #Pone el Play
        MEDIEVAL.blit(PLAY,(750,500))

        #Pone el boton cerrar
        MEDIEVAL.blit(LUNACERRAR,(0,850))

        #Pone nombre de Autores
        MEDIEVAL.blit(AUTORES,(1000,350))

        #Pone figura
        MEDIEVAL.blit(KAKASHI,(500,860))

        #Pone figura
        MEDIEVAL.blit(OGRO,(650,860))

        #Pone figura
        MEDIEVAL.blit(NINJA,(800,860))

        #Pone figura
        MEDIEVAL.blit(ASESINO,(950,860))

        #Pone figura
        MEDIEVAL.blit(TERRORISTA,(1100,860))

        #Pone figura
        MEDIEVAL.blit(LEGOLAS,(1250,860))

                                    

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        #BOTON CERRAR
        botonCerrar(0,850,162,154)

        #BOTON PLAY
        botonPlay(750,500,226,146)
                            
        pygame.display.update()
        CLOCK.tick(5)


#==========================================   MENU PLAY  ==========================================


# E: nada
# S: una ventana de pygame
# D: Crea una ventana de pygame


def menuPlay():
    pygame.display.update()


    intro = True

    while intro:

        # Pone el Background
        MEDIEVAL.blit(BACKGROUND,(0, 0) )

        # Pone el Titulo
        MEDIEVAL.blit(TITLE,(70,80))

        # Pone el Titulo
        MEDIEVAL.blit(TWOP,(740,400))

        #Pone el Titulo
        MEDIEVAL.blit(THREEP,(720,600))

        #Pone el Titulo
        MEDIEVAL.blit(FOURP,(730,800))

        #Pone el boton cerrar
        MEDIEVAL.blit(LUNACERRAR,(0,850))


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        #BOTON REGRESAR
        botonRegreso(0,850,162,154)

        #BOTON TWO PLAYERS
        botonTwoPlayers(740,400,278,80)

        #BOTON THREE PLAYERS
        botonThreePlayers(720,600,278,80)

        #BOTON FOUR PLAYERS
        botonFourPlayers(730,800,278,80)
          



        pygame.display.update()
        CLOCK.tick(5)


#==========================================   MENU STARTGAME  ============================================

def menuStart(ID):
    global JUGADOR1
    global JUGADOR2
    global JUGADOR3
    global JUGADOR4


    pygame.display.update()

    intro = True

    while intro:

        # Pone el Background
        MEDIEVAL.blit(BACKGROUND3,(0,0))

        #Pone el boton cerrar
        MEDIEVAL.blit(LUNACERRAR,(1590,850))

        #Pone Texto
        MEDIEVAL.blit(MAINFONT.render("Digite un numero entre el 1 - 1000", 1, BLANCO), (450,50 ))

        #Pone informacion
        MEDIEVAL.blit(MAINFONT.render('Orden de jugadores',1,BLANCO),(1600/2-150,650))
        MEDIEVAL.blit(MAINFONT.render(str(ALEATORIO), 1, BLANCO), (100,50 ))
        #MEDIEVAL.blit(MAINFONT.render(str(ORDER),1,BLANCO),(1600/2-200,750))
        ordenPlayer_AUX(ORDER)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if ID == 2:

            #Pone Player1
            MEDIEVAL.blit(PLAYER1,(130,350))

            #Pone Plyaer2
            MEDIEVAL.blit(PLAYER2,(1350,350))

            #Pone el boton Start
            MEDIEVAL.blit(PLAY,(780,500))


            #CUADRO INPUT PLAYER 1-----------------------
            cuadroPlayer1(160, 450,JUGADOR1)
            #CUADRO INPUT PLAYER 2-----------------------
            cuadroPlayer2(1380, 450,JUGADOR2)

            #BOTON INPUT PLAYER 1
            botonInputPlayer(160, 450,230, 60,1)

            #BOTON INPUT PLAYER 2
            botonInputPlayer(1380, 450,230, 60,2)

            #BOTON START
            botonGame(780,500,226,146,2)

        if ID == 3:

            #Pone Player1
            MEDIEVAL.blit(PLAYER1,(160,350))

            #Pone Player2
            MEDIEVAL.blit(PLAYER2,(750,100))

            #Pone Player3
            MEDIEVAL.blit(PLAYER3,(1350,350))

            #Pone boton Start
            MEDIEVAL.blit(PLAY,(100,800))

            #--------------------------------------
            #CUADRO INPUT PLAYER 3
            cuadroPlayer3(1410, 450,JUGADOR3)
            #CUADRO INPUT PLAYER 2
            cuadroPlayer2(780, 200,JUGADOR2)
            #CUADRO INPUT PLAYER 1
            cuadroPlayer1(190, 450,JUGADOR1)

            #BOTON INPUT PLAYER 1
            botonInputPlayer(190, 450,230, 60,1)

            #BOTON INPUT PLAYER 2
            botonInputPlayer(780, 200,230, 60,2)

            #BOTON INPUT PLAYER3
            botonInputPlayer(1410, 450,230, 60,3)

            #BOTON START
            botonGame(100,800,226,146,3)
            

        if ID == 4:

            #Pone Player1
            MEDIEVAL.blit(PLAYER1,(160,350))

            #Pone Player2
            MEDIEVAL.blit(PLAYER2,(750,100))

            #Pone Player3
            MEDIEVAL.blit(PLAYER3,(1350,350))

            #Pone Player4
            MEDIEVAL.blit(PLAYER4,(750,500))

            #PONE BOTON START
            MEDIEVAL.blit(PLAY,(100,800))

            #--------------------------------------
            #CUADRO INPUT PLAYER 4
            cuadroPlayer4(790, 590,JUGADOR4)
            #CUADRO INPUT PLAYER 3
            cuadroPlayer3(1410, 450,JUGADOR3)
            #CUADRO INPUT PLAYER 2
            cuadroPlayer2(780, 200,JUGADOR2)
            #CUADRO INPUT PLAYER 1
            cuadroPlayer1(190, 450,JUGADOR1)
            
            #BOTON INPUT PLAYER 1
            botonInputPlayer(190, 450,230, 60,1)

            #BOTON INPUT PLAYER 2
            botonInputPlayer(780, 200,230, 60,2)

            #BOTON INPUT PLAYER3
            botonInputPlayer(1410, 450,230, 60,3)

            #BOTON INPUT PLAYER4
            botonInputPlayer(790, 590,230, 60,4)

            #BOTON START
            
            botonGame(100,800,226,146,4)


        botonBackStart(1590,850,162,154,ID)

        if ORDER !=[]:
            pygame.time.wait(3000)
            tableroJuego()

        pygame.display.update()
        CLOCK.tick(5)


#AUXILIAR
#E: Una lista
#S: El orden de los jugadores
#D: Imprime la lista segun el orden de los turnos

def ordenPlayer_AUX(lista):

    positionX = 800

    positionY = 750
    contador = 0 
    for player in lista:
        contador += 1
        MEDIEVAL.blit(MAINFONT.render(str(contador)+'.',1,BLANCO),(positionX-100,positionY))
        MEDIEVAL.blit(MAINFONT.render(str(player),1,BLANCO),(positionX,positionY))
        positionY+=50



#==========================================   MENU TWO PLAYERS  ==========================================


# E: nada
# S: una ventana de pygame
# D: Crea una ventana de pygame


def menuTwoP():
    pygame.display.update()


    intro = True


    while intro:

        # Pone el Background
        MEDIEVAL.blit(BACKGROUND2,(0, 0))

        # Pone el Titulo
        MEDIEVAL.blit(TITLE,(80,80))

        #Pone el boton cerrar
        MEDIEVAL.blit(LUNACERRAR,(1590,850))

        #Pone el Play
        MEDIEVAL.blit(PLAY,(780,500))
        botonPlayTablero(780,500,226,146,2)

        #------------------   PLAYER 1   ------------------
        
        #           Pone input player 1
        MEDIEVAL.blit(PLAYER1,(130,350))

        #Seleccion player 1
        paintCharacter(INDICEP1,210,545,1)
        
        #Flechas
        MEDIEVAL.blit(FLECHAS,(110,550))

        #SELECT
        MEDIEVAL.blit(SELECT,(210,700))
          
        #------------------   PLAYER 2   ------------------
        
        #           Pone input player 2
        MEDIEVAL.blit(PLAYER2,(1350,350))
        
        #Seleccion player 2
        paintCharacter(INDICEP2,1430,545,2)

        #Flechas
        MEDIEVAL.blit(FLECHAS,(1330,550))

        #SELECT
        MEDIEVAL.blit(SELECT,(1430,700))

        #=========================================================================
          
        #CUADRO INPUT PLAYER 1-----------------------
        cuadroPlayer1(160, 450, JUGADOR1)
        #CUADRO INPUT PLAYER 2-----------------------
        cuadroPlayer2(1380, 450, JUGADOR2)
        #-------------------------------------

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        #BOTON REGRESAR
        botonRegresoPlay(1590,850,162,154)

        #BOTON INPUT PLAYER 1
        botonInputPlayer(160, 450,230, 60,1)

        #BOTON INPUT PLAYER 2
        botonInputPlayer(1380, 450,230, 60,2)

        #BOTON CORRER IZQUIERDA P1
        botonCorrerIzquierda(110,570,75,75,1,2)

        #BOTON CORRER DERECHA P1
        botonCorrerDerecha(395,570,75,75,1,2)

        #BOTON CORRER DERECHA P2
        botonCorrerDerecha(1615,570,75,75,2,2)

        #BOTON CORRER IZQUIERDA P2
        botonCorrerIzquierda(1330,570,75,75,2,2)

        #BOTON SELECT PLAYER1
        botonSelect(210,700, 150,77,1)

        #BOTON SELECT PLAYER2
        botonSelect(1430,700, 150,77,2)

        #SLECTION STATE

        if SELECTION1 == True:
                        MEDIEVAL.blit(READY,(290,515))

        if SELECTION2 == True:
                        MEDIEVAL.blit(READY,(1500,515))
        
        

          
        pygame.display.update()
        CLOCK.tick(5)

#==========================================   MENU THREE PLAYERS  ==========================================


# E: nada
# S: una ventana de pygame
# D: Crea una ventana de pygame


def menuThreeP():
    pygame.display.update()


    intro = True

    while intro:

        # Pone el Background
        MEDIEVAL.blit(BACKGROUND2,(0, 0) )


        #Pone el boton cerrar
        MEDIEVAL.blit(LUNACERRAR,(1590,850))

        #Pone el Play
        MEDIEVAL.blit(PLAY,(780,800))
        botonPlayTablero(780,800,226,146,3)


        #------------------   PLAYER 1   ------------------

        #Pone input player 1-----------------------------
        MEDIEVAL.blit(PLAYER1,(160,350))


        #Seleccion player 1-----------------------------
        paintCharacter(INDICEP1,230,545,1)

        #Flechas
        MEDIEVAL.blit(FLECHAS,(130,550))

        #SELECT
        MEDIEVAL.blit(SELECT,(230,700))




        #------------------   PLAYER 2   ------------------

        #Pone input player 2-----------------------------
        MEDIEVAL.blit(PLAYER2,(750,100))


        #Seleccion player 2------------------------------
        paintCharacter(INDICEP2,790,300,2)

        #Flechas
        MEDIEVAL.blit(FLECHAS,(700,320))

        #SELECT
        MEDIEVAL.blit(SELECT,(790,450))




        #------------------   PLAYER 3   ------------------

        #Pone input player 3-----------------------------
        MEDIEVAL.blit(PLAYER3,(1350,350))

        #Seleccion player 3-----------------------------
        paintCharacter(INDICEP3,1450,545,3)

        #Flechas
        MEDIEVAL.blit(FLECHAS,(1360,550))

        #SELECT
        MEDIEVAL.blit(SELECT,(1450,700))


        #--------------------------------------
        #CUADRO INPUT PLAYER 3
        cuadroPlayer3(1410, 450, JUGADOR3)
        #CUADRO INPUT PLAYER 2
        cuadroPlayer2(780, 200, JUGADOR2)
        #CUADRO INPUT PLAYER 1
        cuadroPlayer1(190, 450, JUGADOR1)
        #---------------------------------------



        #==========================================================================  




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        #BOTON REGRESAR
        botonRegresoPlay(1590,850,162,154)

        #BOTON INPUT PLAYER 1
        botonInputPlayer(190, 450,230, 60,1)

        #BOTON INPUT PLAYER 2
        botonInputPlayer(780, 200,230, 60,2)

        #BOTON INPUT PLAYER3
        botonInputPlayer(1410, 450,230, 60,3)

        #BOTON CORRER IZQUIERDA P1
        botonCorrerIzquierda(110,570,75,75,1,3)

        #BOTON CORRER DERECHA P1
        botonCorrerDerecha(395,570,75,75,1,3)

        #BOTON CORRER DERECHA P2
        botonCorrerDerecha(985,370,75,75,2,3)

        #BOTON CORRER IZQUIERDA P2
        botonCorrerIzquierda(700,370,75,75,2,3)

        #BOTON CORRER DERECHA P3
        botonCorrerDerecha(1645,570,75,75,3,3)

        #BOTON CORRER IZQUIERDA P3
        botonCorrerIzquierda(1360,570,75,75,3,3)

        #BOTON SELECT PLAYER1
        botonSelect(230,700, 150,77,1)

        #BOTON SELECT PLAYER2
        botonSelect(790,450, 150,77,2)

        #BOTON SELECT PLAYER3
        botonSelect(1450,700, 150,77,3)


        #SLECTION STATE

        if SELECTION1 == True:
            MEDIEVAL.blit(READY,(310,515))

        if SELECTION2 == True:
            MEDIEVAL.blit(READY,(870,260))

        if SELECTION3 == True:
            MEDIEVAL.blit(READY,(1520,515))



        pygame.display.update()
        CLOCK.tick(5)


#==========================================   MENU FOUR PLAYERS  ==========================================


# E: nada
# S: una ventana de pygame
# D: Crea una ventana de pygame


def menuFourP():
    pygame.display.update()

    intro = True

    while intro:

        # Pone el Background
        MEDIEVAL.blit(BACKGROUND2,(0, 0) )


        #Pone el boton cerrar
        MEDIEVAL.blit(LUNACERRAR,(1590,850))

        #Pone el Play
        MEDIEVAL.blit(PLAY,(100,800))
        botonPlayTablero(100,800,226,146,4)

        #------------------   PLAYER 1   ------------------

        #Pone input player 1-----------------------------
        MEDIEVAL.blit(PLAYER1,(180,40))

        #Seleccion player 1
        paintCharacter(INDICEP1,240,230,1)

        #Flechas
        MEDIEVAL.blit(FLECHAS,(150,230))

        #SELECT
        MEDIEVAL.blit(SELECT,(250,400))

        

        #------------------   PLAYER 2   ------------------
        
        #Pone input player 2-----------------------------
        MEDIEVAL.blit(PLAYER2,(750,40))

        #Seleccion player 2
        paintCharacter(INDICEP2,830,230,2)
        
        #Flechas
        MEDIEVAL.blit(FLECHAS,(720,230))

         #SELECT
        MEDIEVAL.blit(SELECT,(830,400))

        #------------------   PLAYER 3   ------------------

        #Pone input player 3-----------------------------
        MEDIEVAL.blit(PLAYER3,(1350,40))
        

        #Seleccion player 3
        paintCharacter(INDICEP3,1430,230,3)
        
        #Flechas
        MEDIEVAL.blit(FLECHAS,(1340,230))

        #SELECT
        MEDIEVAL.blit(SELECT,(1450,400))


        

        #------------------   PLAYER 4   ------------------

        #Pone input player 4-----------------------------
        MEDIEVAL.blit(PLAYER4,(750,500))
        


        #Seleccion player 4
        paintCharacter(INDICEP4,820,710,4)
        
        #Flechas
        MEDIEVAL.blit(FLECHAS,(720,730))

        #SELECT
        MEDIEVAL.blit(SELECT,(830,880))

        #=========================================================================

        #--------------------------------------
        #CUADRO INPUT PLAYER 4
        cuadroPlayer4(790, 590, JUGADOR4)
        #CUADRO INPUT PLAYER 3
        cuadroPlayer3(1400, 130, JUGADOR3)
        #CUADRO INPUT PLAYER 2
        cuadroPlayer2(780, 130, JUGADOR2)
        #CUADRO INPUT PLAYER 1
        cuadroPlayer1(210, 130, JUGADOR1)
        #---------------------------------------


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        #BOTON REGRESAR
        botonRegresoPlay(1590,850,162,154)

        #BOTON INPUT PLAYER 1
        botonInputPlayer(210, 130,230, 60,1)

        #BOTON INPUT PLAYER 2
        botonInputPlayer(780, 130,230, 60,2)

        #BOTON INPUT PLAYER3
        botonInputPlayer(1400, 130,230, 60,3)

        #BOTON INPUT PLAYER4
        botonInputPlayer(790, 590,230, 60,4)

        #BOTON CORRER IZQUIERDA P1
        botonCorrerIzquierda(150,280,75,75,1,4)

        #BOTON CORRER DERECHA P1
        botonCorrerDerecha(435,280,75,75,1,4)

        #BOTON CORRER DERECHA P2
        botonCorrerDerecha(1005,280,75,75,2,4)

        #BOTON CORRER IZQUIERDA P2
        botonCorrerIzquierda(720,280,75,75,2,4)

        #BOTON CORRER DERECHA P3
        botonCorrerDerecha(1625,280,75,75,3,4)

        #BOTON CORRER IZQUIERDA P3
        botonCorrerIzquierda(1340,280,75,75,3,4)

        #BOTON CORRER DERECHA P4
        botonCorrerDerecha(1005,780,75,75,4,4)

        #BOTON CORRER IZQUIERDA P4
        botonCorrerIzquierda(720,780,75,75,4,4)

        #BOTON SELECT PLAYER1
        botonSelect(250,400, 150,77,1)

        #BOTON SELECT PLAYER2
        botonSelect(830,400, 150,77,2)

        #BOTON SELECT PLAYER3
        botonSelect(1450,400, 150,77,3)

        #BOTON SELECT PLAYER4
        botonSelect(830,880, 150,77,4)


        #SLECTION STATE

        if SELECTION1 == True:
            MEDIEVAL.blit(READY,(330,185))

        if SELECTION2 == True:
            MEDIEVAL.blit(READY,(900,185))

        if SELECTION3 == True:
            MEDIEVAL.blit(READY,(1520,185))

        if SELECTION4 == True:
            MEDIEVAL.blit(READY,(920,675))


        pygame.display.update()
        CLOCK.tick(5)




#==========================================   TABLERO DE JUEGO  ==========================================


# E: Ninguna
# S: una ventana de pygame
# D: Crea una ventana de pygame

def tableroJuego():
        global ORDER
        global TURNO
        global DADO_STATE
        global DADO

        setOrder()

        pygame.display.flip()

        while not VICTORIA:
            # Pone el Background
            MEDIEVAL.blit(BACKGROUND2,(0, 0) )

            #Es el turno de:
            MEDIEVAL.blit(ESTURNO,(200,10))

            #IMAGEN DE DADO
            MEDIEVAL.blit(IMAGENDADO,(1600,10))

            #LUNA DE REGRESO

            MEDIEVAL.blit(LUNAREGRESO2,(1740,950))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                                                                                                
            #BOTON REGRESO DE TABLERO (BORRA TODOS LOS DATOS)
            botonRegresoTablero(1740,950,162,154)

            #IMAGEN DADO #MEJORAR
            botonDado(1600,10,100,100)

            impresorDado(DADO)


            #-------------------------LOOP DEL JUEGO------------------------

            

            if Player1.getTurno() == TURNO:
                texto(470,45,ORDER[Player1.getTurno()],40,BLANCO)

                if Player1.freeze[0]:
                    Player1.unfreeze()
                    changeTurno()

                if DADO != 0:
                    Player1.move(DADO,Player1.getTrack()[0],Player1.getTrack()[1],Player1.getI(),Player1.getJ())
                    
                    #Imprime el tablero de nuevo
                    paintPlayers(ORDER)
                    paintTablero()
                    paintCells()
                    pygame.display.update()

                    if Player1.victory == True:
                    	pygame.time.wait(3000)
                    	chickenDinner(Player1)


                    else:
                        texto(900,45,MINIJUEGOS_NAME[GAMEBOARD[Player1.getI()][Player1.getJ()]],50,BLANCO)
                        pygame.time.wait(3000)
                        minijuego(Player1.getI(),Player1.getJ(),1)
                        changeTurno()



            elif Player2.getTurno() == TURNO:
                texto(470,45,ORDER[Player2.getTurno()],40,BLANCO)

                if Player2.freeze[0]:
                    Player2.unfreeze()
                    changeTurno()

                if DADO != 0:
                    Player2.move(DADO,Player2.getTrack()[0],Player2.getTrack()[1],Player2.getI(),Player2.getJ())
                    
                    #Imprime el tablero de nuevo
                    paintPlayers(ORDER)
                    paintTablero()
                    paintCells()
                    pygame.display.update()

                    if Player2.victory == True:
                    	pygame.time.wait(3000)
                    	chickenDinner(Player2)


                    else:
                        texto(900,45,MINIJUEGOS_NAME[GAMEBOARD[Player2.getI()][Player2.getJ()]],50,BLANCO)
                        pygame.time.wait(3000)
                        minijuego(Player2.getI(),Player2.getJ(),2)
                        changeTurno()


            elif Player3.getTurno() == TURNO:
                texto(470,45,ORDER[Player3.getTurno()],40,BLANCO)

                if Player3.freeze[0]:
                    Player3.unfreeze()
                    changeTurno()

                if DADO != 0:
                    Player3.move(DADO,Player3.getTrack()[0],Player3.getTrack()[1],Player3.getI(),Player3.getJ())
                    
                    #Imprime el tablero de nuevo
                    paintPlayers(ORDER)
                    paintTablero()
                    paintCells()
                    pygame.display.update()

                    if Player3.victory == True:
                    	pygame.time.wait(3000)
                    	chickenDinner(Player3)


                    else:
                        texto(900,45,MINIJUEGOS_NAME[GAMEBOARD[Player3.getI()][Player3.getJ()]],50,BLANCO)
                        pygame.time.wait(3000)
                        minijuego(Player3.getI(),Player3.getJ(),3)
                        changeTurno()

                         

            elif Player4.getTurno() == TURNO:
                texto(470,45,ORDER[Player4.getTurno()],40,BLANCO)

                if Player4.freeze[0]:
                    Player4.unfreeze()
                    changeTurno()

                if DADO != 0:
                    Player4.move(DADO,Player4.getTrack()[0],Player4.getTrack()[1],Player4.getI(),Player4.getJ())
                    
                    #Imprime el tablero de nuevo
                    paintPlayers(ORDER)
                    paintTablero()
                    paintCells()
                    pygame.display.update()

                    if Player4.victory == True:
                    	pygame.time.wait(3000)
                    	chickenDinner(Player4)


                    else:
                        texto(900,45,MINIJUEGOS_NAME[GAMEBOARD[Player4.getI()][Player4.getJ()]],50,BLANCO)
                        pygame.time.wait(3000)
                        minijuego(Player4.getI(),Player4.getJ(),4)
                        changeTurno()



            DADO = 0
            DADO_STATE = True



            paintPlayers(ORDER)

            #INICIO

            paintTablero()
            paintCells()

            

            pygame.display.update()
            CLOCK.tick(5)



#==================================   MENU PICK PLAYER  =====================================

def menuPick(game,ID):
    pygame.display.update()


    intro = True

    while intro:

        # Pone el Background
        MEDIEVAL.blit(FONDO_MEMORY,(0, 0) )

        texto(900,100,'Pick a Player',80,BLANCO)


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if len(ORDER) == 2:

            if ID == Player1.getID():

                texto(900,400,Player2.getName(),80,BLANCO)
                MEDIEVAL.blit(Player2.getCharacter(),(850, 450) )
                botonPick(750,350,300,400,game,Player2,Player1)

            elif ID == Player2.getID():

                texto(900,400,Player1.getName(),80,BLANCO)
                MEDIEVAL.blit(Player1.getCharacter(),(850, 450) )
                botonPick(750,350,300,400,game,Player1,Player2)


        if len(ORDER) == 3:

            if ID == Player1.getID():

                texto(400,400,Player2.getName(),80,BLANCO)
                MEDIEVAL.blit(Player2.getCharacter(),(350, 450) )
                botonPick(250,350,300,400,game,Player2,Player1)

                texto(1400,400,Player3.getName(),80,BLANCO)
                MEDIEVAL.blit(Player3.getCharacter(),(1350, 450) )
                botonPick(1250,350,300,400,game,Player3,Player1)

            elif ID == Player2.getID():

                texto(400,400,Player1.getName(),80,BLANCO)
                MEDIEVAL.blit(Player1.getCharacter(),(350, 450) )
                botonPick(250,350,300,400,game,Player1,Player2)

                texto(1400,400,Player3.getName(),80,BLANCO)
                MEDIEVAL.blit(Player3.getCharacter(),(1350, 450) )
                botonPick(1250,350,300,400,game,Player3,Player2)

            elif ID == Player3.getID():

                texto(400,400,Player2.getName(),80,BLANCO)
                MEDIEVAL.blit(Player2.getCharacter(),(350, 450) )
                botonPick(250,350,300,400,game,Player2,Player3)

                texto(1400,400,Player1.getName(),80,BLANCO)
                MEDIEVAL.blit(Player1.getCharacter(),(1350, 450) )
                botonPick(1250,350,300,400,game,Player1,Player3)

        if len(ORDER) == 4:

            if ID == Player1.getID():

                texto(400,400,Player2.getName(),80,BLANCO)
                MEDIEVAL.blit(Player2.getCharacter(),(350, 450) )
                botonPick(250,350,300,400,game,Player2,Player1)


                texto(1400,400,Player3.getName(),80,BLANCO)
                MEDIEVAL.blit(Player3.getCharacter(),(1350, 450) )
                botonPick(1250,350,300,400,game,Player3,Player1)

                texto(900,400,Player4.getName(),80,BLANCO)
                MEDIEVAL.blit(Player4.getCharacter(),(850, 450) )
                botonPick(750,350,300,400,game,Player4,Player1)

            elif ID == Player2.getID():

                texto(400,400,Player1.getName(),80,BLANCO)
                MEDIEVAL.blit(Player1.getCharacter(),(350, 450) )
                botonPick(250,350,300,400,game,Player1,Player2)


                texto(1400,400,Player3.getName(),80,BLANCO)
                MEDIEVAL.blit(Player3.getCharacter(),(1350, 450) )
                botonPick(1250,350,300,400,game,Player3,Player2)

                texto(900,400,Player4.getName(),80,BLANCO)
                MEDIEVAL.blit(Player4.getCharacter(),(850, 450) )
                botonPick(750,350,300,400,game,Player4,Player2)

            elif ID == Player3.getID():

                texto(400,400,Player2.getName(),80,BLANCO)
                MEDIEVAL.blit(Player2.getCharacter(),(350, 450) )
                botonPick(250,350,300,400,game,Player2,Player3)


                texto(1400,400,Player1.getName(),80,BLANCO)
                MEDIEVAL.blit(Player1.getCharacter(),(1350, 450) )
                botonPick(1250,350,300,400,game,Player1,Player3)

                texto(900,400,Player4.getName(),80,BLANCO)
                MEDIEVAL.blit(Player4.getCharacter(),(850, 450) )
                botonPick(750,350,300,400,game,Player4,Player3)

            elif ID == Player4.getID():

                texto(400,400,Player2.getName(),80,BLANCO)
                MEDIEVAL.blit(Player2.getCharacter(),(350, 450) )
                botonPick(250,350,300,400,game,Player2,Player4)


                texto(1400,400,Player3.getName(),80,BLANCO)
                MEDIEVAL.blit(Player3.getCharacter(),(1350, 450) )
                botonPick(1250,350,300,400,game,Player3,Player4)

                texto(900,400,Player1.getName(),80,BLANCO)
                MEDIEVAL.blit(Player1.getCharacter(),(850, 450) )
                botonPick(750,350,300,400,game,Player1,Player4)



          


        pygame.display.update()
        CLOCK.tick(5)


#----------------------------------------------------------------------------------------------------------------------------------------


VICTORY = pygame.image.load('VICTORY.png')

def chickenDinner(player):
    from sys import exit

    intro = True

    while  intro:

    	

    	# Pone el Background
    	MEDIEVAL.blit(VICTORY,(-40, 0))

    	#PONE TEXTO
    	texto(900,100,player.getName(),80,BLANCO)
    	texto(900,180,'HAS BECOME',80,BLANCO)
    	texto(900,260,'THE ULTIMATE',80,BLANCO)
    	texto(900,340,'WARRIOR',80,BLANCO)

    	#PONE AL PERSONAJE
    	MEDIEVAL.blit(player.getCharacter(),(860,500))



    	pygame.display.update()
    	for event in pygame.event.get():
    	    if event.type == pygame.QUIT:
    	        pygame.quit()
    	        quit()

    	pygame.time.wait(5000)

    	intro = False


    	pygame.display.update()
    	CLOCK.tick(5)
    exit()




#----------------------------------------------------------------------------------------------------------------------------------------



menuPrincipal()
