#Minijuegos

#IMPORTS

import pygame
import sys
import time
import random
import numpy as np
import string

pygame.init()

#VARIABLES GLOBALES

#JUGADORES===========

player1=''
player2=''
player3=''
player4=''

BLANCO = (255,255,255)

RED = (255,127,80)

#====================


#ALGORITMOS PARA PROCESO DE JUEGO


#===================
#MANEJO DE ARCHIVOS=
#===================


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




     
#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 1
#                                                                   TIC TAC TOE
#----------------------------------------------------------------------------------------------------------------------------------------


#VARIABLES PARA GATO
TABLEROGATO=[0,0,0,0,0,0,0,0,0]
COMBINACIONES= ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

#JUEGO-------------------------------------------------------------------------------
#E: No tiene
#S: El juego de gato
#D: Procesa el juego de ambos jugadores

def procesoJuegoGato():
     global TABLEROGATO
     
     jugador1=input('Ingresa el nombre del jugador #1: ')
     print()
     print()
     jugador2=input('Ingresa el nombre del jugador #2: ')
     print()
     print()
     #mostrarTableroGato()
     turno = 1
     while True:

          #JUGADOR 1
          if turno == 1:
               
               #IMPRIME TABLERO
               mostrarTableroGato()
               
               #JUGADA
               print('Es el turno de: ',jugador1)
               play=int(input('Ingresa tu jugada: '))

               #ANALISIS CELDA
               if analisisFicha(play,turno):
                    print('Espacio ocupado')
                    continue
               #REEMPLAZA FICHA
               reemplazaFicha(play,turno)
               #VERIFICA GANADOR
               if ganadorGato():
                    print('Has ganado ',jugador1)
                    mostrarTableroGato()
                    TABLEROGATO=[0,0,0,0,0,0,0,0,0]
                    return
               
               #IMPRIME TABLERO
               mostrarTableroGato()
               turno = 2

          #JUGADOR 2
          if turno == 2:
               
               #JUGADA
               print('Es el turno de: ',jugador2)
               play=int(input('Ingresa tu jugada: '))
               #ANALISIS CELDA
               if analisisFicha(play,turno):
                    print('Espacio ocupado')
                    continue
               #REEMPLAZA FICHA
               reemplazaFicha(play,turno)
               #VERIFICA GANADOR
               if ganadorGato():
                    print('Has ganado ',jugador2)
                    mostrarTableroGato()
                    TABLEROGATO=[0,0,0,0,0,0,0,0,0]
                    return
               
               turno = 1   
          
#IMPRESOR TABLERO--------------------------------------------------               
#E: Ninguna
#S: Imprime el juego
#D: Imprimir el tablero de juego
     
def mostrarTableroGato():
     global TABLEROGATO
     print()
     print(TABLEROGATO[6],' ',TABLEROGATO[7],' ',TABLEROGATO[8])
     print('---------')
     print(TABLEROGATO[3],' ',TABLEROGATO[4],' ',TABLEROGATO[5])
     print('---------')
     print(TABLEROGATO[0],' ',TABLEROGATO[1],' ',TABLEROGATO[2])
     print()
     

#ANALISIS FICHA---------------------------------------------------

#1

#E: Una lista y un numero
#S: Una lista
#D: Analisa si la el espacio esta ocupado
               
def analisisFicha(jugada,turno):
     global TABLEROGATO
     
     if TABLEROGATO[jugada]!=0:
          return True
     elif TABLEROGATO[jugada]==0:
          return False

#2
     
#E: Una lista y un numero
#S: Una lista
#D: Reemplaza la ficha del jugador
               
def reemplazaFicha(jugada,turno):
     global TABLEROGATO
     
     if TABLEROGATO[jugada]==0:
          TABLEROGATO[jugada]=turno

#GANADOR----------------------------------------------------------------------------------------------------------
#E: Ninguna
#S: Una expresion booleana
#D: Verifica si hay un ganador

def ganadorGato():
     global TABLEROGATO

     if verificadorFilas(TABLEROGATO) or verificadorColumnas(TABLEROGATO) or verificadorDiagonales(TABLEROGATO):
          return True
     else:
          return False

#VERIFICADORES----------------------------------------------------------------------------------------------------

#1
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

#2
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

#3
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
#************************************************************
#---------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 2
#                                                                   MEMORY PATH
#----------------------------------------------------------------------------------------------------------------------------------------

#VARIABLES PARA MEMORY PATH
TABLEROMEMORYP=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
CARTA = 'X'
contadorMemoryPath = 0
vidasMemoryPath = 3


#JUEGO-------------------------------------------------------------------------------
#E: No tiene
#S: El juego
#D: Crea el proceso del Juego Memory Path

def memoryPath():
     
     global TABLEROMEMORYP
     global vidasMemoryPath
     #GENERADORES DEFAULT TABLERO
     generadorX()
     print()
     print()
     contador=0
     
     while True:

          #for i in range(len(TABLEROMEMORYP)):
          print()
          print('Nivel', contador)
          print()
          mostrarMemoryPath(TABLEROMEMORYP)
               
          jugada = int(input('Inserta tu jugada: ' ))

          for j in range(len(TABLEROMEMORYP[0])):
                    
               if analizadorMemoryPath(TABLEROMEMORYP,contador,j,jugada):
                         
                    contador+=1
     
                    if contador>=8:
                              
                         print('Has Ganado!')
                              
                         return
                    break
               contador=0
               print()
               print()
               print('Has fallado')
               vidasMemoryPath-=1
               print()
               print()
               print('Te quedan',vidasMemoryPath,'vidas')
               print()
               print()
               if vidasMemoryPath<=0:
                    print('Has perdido')
                    return 
               break
                         

               

     
#IMPRESOR TABLERO--------------------------------------------------------------------

#E: Una matriz
#S: No tiene
#D: Imprime el tablero    
     
def mostrarMemoryPath(tablero):
     tablero = tablero[::-1]
     for i in range(len(tablero)):
          for j in range(len(tablero[i])):
               print(tablero[i][j],end=' ')
          print()
     print()


#GENERADOR RANDOM DE CARTA 'X'--------------------------------------------------------

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

          
#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 3
#                                                                   LETTER SOUP
#----------------------------------------------------------------------------------------------------------------------------------------

#VARIABLES GLOBALES LETTER SOUP===========================

MATRIZ_SOPA=((10,10),(15,15),(20,20))
PALABRAS_SOPA = cargarArchivo('Sopa de Letras.txt')
PALABRAS_SELECCIONADAS = []
TABLERO_OFFICIAL_SOPA= []
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
     
     global MATRIZ_SOPA
     global PALABRAS_SELECCIONADAS
     global PALABRAS_SOPA
     global TABLERO_OFFICIAL_SOPA

     #ESCOGE EL TAMANO DEL TABLERO 25/15/10
     tamano = numeroTableroSopa()
     #CREA TABLERO
     tablero = np.zeros(MATRIZ_SOPA[tamano],dtype=str)
     #CUENTA FILAS
     counter = counterFilas(tablero)
     #VARIABLES
     newTablero = []
     newFila =[]
     #LISTA DE PALABRAS SELECCIONADAS
     PALABRAS_SELECCIONADAS=seleccionadorPalabras(PALABRAS_SOPA,counter)
     
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
     
     mostrarTableroSopa(newTablero)
     
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
          

#ANALISIS LARGO DE PALABRAS=====
#E: Un string
#S: Un numero
#D: Analiza el largo de cada palabra

def analisisPalabra(palabra):

     largoPalabra = len(palabra)

     return largoPalabra

#ANALISIS CANTIDAD DE FILAS DE LA MATRIZ=====

#E: Una matriz
#S: Un numero
#D: Verifica la cantidad de letras de la matriz

def counterFilas(M):
     
     counter = 0
     
     for fila in M:
          counter+=1
     return counter
          
#COLOCADOR DE PALABRAS--------------------------------------------------------------------
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
                         mostrarTableroSopa(M)
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
                         mostrarTableroSopa(M)
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
                         mostrarTableroSopa(M)
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
                         mostrarTableroSopa(M)
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
               
#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 4
#                                                                   COLLECT COINS 
#----------------------------------------------------------------------------------------------------------------------------------------

#VARIABLES GLOBALES COLLECT THE COINS===========================
TABLERO_COLLECT_COINS = np.zeros((25,25),dtype=int)
TIEMPOS_CC = (30,45,60)
MONEDAS_RANDOM_P = [1,2,3,4,5,6,7,8,9,10]
MONEDAS_RANDOM_N = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
#===============================================================

#CREAR TABLERO OFFICIAL

def matriz_CC():

     global TABLERO_COLLECT_COINS

     #CONTADORES INICIALES DE MONEDAS
     contadorPositivos = 312
     contadorNegativos = 313

     TABLERO_COLLECT_COINS = monedasPositivas(TABLERO_COLLECT_COINS)
     TABLERO_COLLECT_COINS = monedasNegativos(TABLERO_COLLECT_COINS)

     return TABLERO_COLLECT_COINS

     
     
                    

               

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

          


#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 5
#                                                                      MEMORY 
#----------------------------------------------------------------------------------------------------------------------------------------

#VARIABLES GLOBALES MEMORY===========================

PAREJAS = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
TABLERO_Memory = np.zeros((3,6),dtype=int)
#=========================================================

#CREA MATRIZ

def matriz_Memory():
     
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


def proceso_Memory():

     
     tablero = matriz_Memory()

     turno = 1

     #MARCADOR DEL JUEGO
     marcadorP1 = 0
     marcadorP2 = 0
     while True:
          print('EL MARCADOR ES :', 'JUGADOR#1:',marcadorP1, 'JUGADOR#2:',marcadorP2)
          print()
          if turno == 1:
               print(tablero)
               print()
               jugada = int(input('Selecciona una fila: '))
               print()
               jugada2 = int(input('Selecciona una columna: '))
               print()
               print('Selecciona la pareja')
               print()
               pareja = int(input('Selecciona una fila: '))
               print()
               pareja2 = int(input('Selecciona una columna: '))
               if analizadorJugada(jugada,jugada2,pareja,pareja2):
                    marcadorP1+=1
                    print(tablero)

          if turno == 2:
               print(tablero)
               print()
               print('Jugador #2')
               print()
               jugada = int(input('Selecciona una fila: '))
               print()
               jugada2 = int(input('Selecciona una columna:'))
               print()
               print('Selecciona la pareja')
               print()
               pareja = int(input('Selecciona una fila: '))
               print()
               pareja2 = int(input('Selecciona una columna:'))
               if analizadorJugada(jugada,jugada2,pareja,pareja2):
                    marcadorP2+=1
                    print(tablero)
                    
          if marcadorP1+marcadorP2 == 18:
               if marcadorP1>marcadorP2:
                    print(tablero)
                    print('El jugador #1 ha ganado')
                    return
               if marcadorP1<marcadorP2:
                    print(tablero)
                    print('El jugador #2 ha ganado')
                    return
          if turno ==1:
               turno = 2
          else:
               turno = 1

               
               
               

#ANALISIS DE JUGADA=========================================================================


def analizadorJugada(jugada,jugada2,pareja,pareja2):

     global TABLERO_Memory

     if TABLERO_Memory[jugada][jugada2] == TABLERO_Memory[pareja][pareja2] and TABLERO_Memory[jugada][jugada2]!= 0:

          TABLERO_Memory[jugada][jugada2] = 0
          TABLERO_Memory[pareja][pareja2] = 0
          
          return True
     else:
          return False


#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 6
#                                                                  BOMBERMARIO 
#----------------------------------------------------------------------------------------------------------------------------------------

#VARIABLES GLOBALES BOMBERMARIO===========================

TAMANO_BOMBER = ((10,10),(15,15),(20,20))

CANTIDAD_BOMBAS = 10

#=========================================================

#CREA MATRIZ-----------------------------------------------
#E: Ninguna
#S: Una matriz
#D: Crea la matriz del juego

def matriz_Bomber():

     global TAMANO_BOMBER

     #CREA LA MATRIZ
     aleatorio = random.randint(0,2)
     tablero = np.zeros(TAMANO_BOMBER[aleatorio],dtype=int)

     #EDITA TABLERO
     tablero = editarBomber(tablero)
     
     return tablero

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

def proceso_Bomber():
     
     global CANTIDAD_BOMBAS
     #CREA TABLERO
     tablero = matriz_Bomber()

     #CONTADOR CASILLAS DESCUBIERTAS DEL TESORO
     print(tablero)
     while CANTIDAD_BOMBAS!=0:
          print('Te quedan:',CANTIDAD_BOMBAS,'bombas!')
          print()
          #JUGADA PLAYER
          fila = int(input('Ingresa una fila: '))
          print()
          columna = int(input('Ingresa una columna: '))
          print()
          #SUSTITUYE CELDA
          tablero = editarBomber_2(tablero,fila,columna)
          #RESTA BOMBAS DISPONIBLES
          CANTIDAD_BOMBAS-=1
          #ANALIZA SI AUN QUEDAN 1S EN LA MATRIZ
          if analisisBomber_Winner(tablero,fila,columna):
               print('You Won')
               return
          #ANALIZA SI YA NO QUEDAN BOMBAS(VIDAS) AL JUGADOR
          if CANTIDAD_BOMBAS == 0:
               print('Game Over')
               return
          print(tablero)
          
     #ANALIZA SI YA NO QUEDAN BOMBAS(VIDAS) AL JUGADOR
     print('Game Over')
     return
          
     
#ANALISIS GANADOR====================================================

#E: Dos numeros y una matriz
#S: Una expresion booleana
#D: Analiza para verificar si hay un ganador

def analisisBomber_Winner(M,fila,columna):
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

CUBO = pygame.image.load('CUBO_2.png')

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
				VENTANA.blit(CUBO,(x,y))

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

def guessWho():
	global TABLERO_GUESS
	global VIDAS

	VIDAS = random.randint(4,8)

	intro = True

	personaje = random.randint(0,15)

	while intro:

	    # Pone el Background
	    VENTANA.blit(BK,(0, 0) )

	    texto(850,100,"Guess Who!",80,BLANCO)

	    texto(1600,50,'Characters',60,BLANCO)

	    texto(250,200,'Casillas disponobles: ',40,BLANCO)

	    texto(250,250,str(VIDAS),40,BLANCO)

	    #IMPRIME LOS NOMBRES A ELEGIR
	    printNames()

	    #IMPRIME LA IMAGEN A ADIVINAR
	    VENTANA.blit(PERSONAJES_GUESS[personaje],(525,200))

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

	    	else:
	    		texto(250,400,'YOU LOST',80,BLANCO)
	    		pygame.display.update()



	    pygame.display.update()
	    CLOCK.tick(5)
     

#----------------------------------------------------------------------------------------------------------------------------------------
#                                                                     JUEGO 8
#                                                                      CARDS 
#----------------------------------------------------------------------------------------------------------------------------------------

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
    VENTANA.blit(superficie,rectangulo)


VENTANA = pygame.display.set_mode((1800,1000))

CLOCK = pygame.time.Clock()

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


def botonCards(x,y,ancho,altura,card):
	global turno
	global electionP1
	global electionP2
	global electionP3
	global electionP4

	mouse= pygame.mouse.get_pos()
	click= pygame.mouse.get_pressed()

	if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
		if click[0] != 0:

			if turno == 0:
				electionP1 = card

			if turno == 1:
				electionP2 = card

			if turno == 2:
				electionP3 = card

			if turno == 3:
				electionP4 = card
			turno += 1

			


def printCards(turno):

	num = random.randint(0,51)
	card = CARDS[num]
	cont = 15
	x = 200
	y = 300

	while cont != 0:
		VENTANA.blit(BACK_CARD,(x,y))
		botonCards(x,y,78,104,card)
		x+= 100
		cont -=1

def checkWin(players):
	global electionP1
	global electionP2
	global electionP3
	global electionP4

	ganador = max(players)

	if CARDS_VALUE[electionP1] == ganador:
		return 'Player1'

	if CARDS_VALUE[electionP2] == ganador:
		return 'Player2'

	if CARDS_VALUE[electionP3] == ganador:
		return 'Player3'

	if CARDS_VALUE[electionP4] == ganador:
		return 'Player4'


#========================================================= VENTANA =====================================================================



# E: nada
# S: una ventana de pygame
# D: Crea una ventana de pygame

def cards():
	global turno
	global electionP1
	global electionP2
	global electionP3
	global electionP4

	pygame.display.update()

	electionP1 = 0

	electionP2 = 0

	electionP3 = 0

	electionP4 = 0

	turno = 0

	palyers = 4

	intro = True

	while intro:

	    # Pone el Background
	    VENTANA.blit(BK,(0, 0) )

	    # Pone nombre del jugador
	    texto(900,150,'SELECT A CARD',80,BLANCO)
	    texto(900,200,'Starting by Player 1',40,BLANCO)

	    printCards(turno)

	    if palyers == 2:
	    	texto(300,600,"Player's 1 election: ",50,BLANCO)
	    	if electionP1 != 0:
	    		VENTANA.blit(electionP1,(250,700))

	    	texto(1500,600,"Player's 2 election: ",50,BLANCO)
	    	if electionP2 != 0:
	    		VENTANA.blit(electionP2,(1450,700))

	    if palyers == 3:
	    	texto(300,600,"Player's 1 election: ",40,BLANCO)
	    	if electionP1 != 0:
	    		VENTANA.blit(electionP1,(250,700))

	    	texto(900,600,"Player's 2 election: ",40,BLANCO)
	    	if electionP2 != 0:
	    		VENTANA.blit(electionP2,(850,700))

	    	texto(1500,600,"Player's 3 election: ",40,BLANCO)
	    	if electionP3 != 0:
	    		VENTANA.blit(electionP3,(1450,700))

	    if palyers == 4:
	    	texto(300,600,"Player's 1 election: ",30,BLANCO)
	    	if electionP1 != 0:
	    		VENTANA.blit(electionP1,(250,700))

	    	texto(700,600,"Player's 2 election: ",30,BLANCO)
	    	if electionP2 != 0:
	    		VENTANA.blit(electionP2,(650,700))

	    	texto(1100,600,"Player's 3 election: ",30,BLANCO)
	    	if electionP3 != 0:
	    		VENTANA.blit(electionP3,(1050,700))

	    	texto(1500,600,"Player's 4 election: ",30,BLANCO)
	    	if electionP4 != 0:
	    		VENTANA.blit(electionP4,(1450,700))

	    	if turno >= palyers:
	    		texto(900,550,'HAS WON!',50,BLANCO)
	    		ganador = checkWin([CARDS_VALUE[electionP1],CARDS_VALUE[electionP2],CARDS_VALUE[electionP3],CARDS_VALUE[electionP4]])
	    		texto(900,500,ganador,50,BLANCO)

			#texto()


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

	    elif TABLERO_TG[i+1][j-1] == 0:
	    	TABLERO_TG[i][j] = 0
	    	return putPiece(i+1,j-1,1)

	    elif TABLERO_TG[i+1][j+1] == 0:
	    	TABLERO_TG[i][j] = 0
	    	return putPiece(i+1,j+1,1)

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
			botonCTC(x,y,68,91,i,j)

			if TABLERO_TG[fila][columna] == 0:
				VENTANA.blit(BACK_CARD_CTC,(x,y))
				x+= 117
				
			elif TABLERO_TG[fila][columna] == 1 :
				VENTANA.blit(THIEF,(x,y))
				x += 117

			elif TABLERO_TG[fila][columna] == 2 :
				VENTANA.blit(JOKER,(x,y))
				x += 117
			j += 1

		x = 320
		j = 0

		y += 90
		i += 1


     
def trapTheCat():

	intro = True

	while  intro:

		

		# Pone el Background
		VENTANA.blit(BK,(0, 0))

		texto(100,100,'Try',80,BLANCO)
		texto(100,175,'to',80,BLANCO)
		texto(130,250,'Catch',80,BLANCO)
		texto(100,325,'the',80,BLANCO)
		texto(110,400,'Thief',80,BLANCO)

		#Imprime el tablero
		printBoardCTC()

		print(Escaped)

		if Escaped:
			texto(1680,100,'The',80,BLANCO)
			texto(1680,175,'Thief',80,BLANCO)
			texto(1680,250,'Escaped!',60,BLANCO)

		if Victoria:
			texto(100,600,'You',80,BLANCO)
			texto(150,675,'Caught',80,BLANCO)
			texto(100,750,'The',80,BLANCO)
			texto(130,825,'Thief',80,BLANCO)

			pygame.time.wait(3000)











		pygame.display.update()
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        pygame.quit()
		        quit()


		pygame.display.update()
		CLOCK.tick(5)




VICTORY = pygame.image.load('VICTORY.png')

#----------------------------------------------------------------------------------------------------------------------------------------

def chickenDinner(player):

	intro = True

	while  intro:

		

		# Pone el Background
		VENTANA.blit(VICTORY,(-40, 0))

		# VENTANA.blit(WIN1,(700,100))
		# VENTANA.blit(WIN2,(660,180))
		# VENTANA.blit(WIN3,(700,260))

		#PONE TEXTO
		texto(900,100,player.GetName(),80,BLANCO)
		texto(900,180,'HAS BECOME',80,BLANCO)
		texto(900,260,'THE ULTIMATE',80,BLANCO)
		texto(900,340,'WARRIOR',80,BLANCO)

		#PONE AL PERSONAJE
		VENTANA.blit(player.getCharacter(),(860,500))



		pygame.display.update()
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        pygame.quit()
		        quit()


		pygame.display.update()
		CLOCK.tick(5)




#----------------------------------------------------------------------------------------------------------------------------------------

chickenDinner('MARCADOR')