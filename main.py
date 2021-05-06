# TODO addthe developer mode in jugador funtion
#Variables de modo de Juego:
mod=0
#1:Consola
#2.Consola+Graficos
#3.Graficos
from tkinter import *
import tkinter.messagebox
import threading, platform
from random import randrange
POSICION=1
OS = platform.system()
imgDados = []
arregloDados={}
Pan = ""
LB = ""
BTN = ""
desa=False
g = open("log.txt","w")
g.close()
def escribir(dato):
    f = open("log.txt","a")
    f.write(str(dato)+"\n")
    f.close()

imgFichas={}
def obtenerDadosIngresados():
    global caja_entrada_dados,texto_ingresado
    texto_ingresado = caja_entrada_dados.get()
def seleccionarOpcion():
    global seleccion
    seleccion=True
def Gra():
    """
    Starts the graphic mode

    @return: None
    """
    global LB, BTN,Pan  # Label and button for the start page
    Pan = Tk()  # Creates a new screen
    d1=PhotoImage(file="d1.gif")
    d2=PhotoImage(file="d2.gif")
    d3=PhotoImage(file="d3.gif")
    d4=PhotoImage(file="d4.gif")
    d5=PhotoImage(file="d5.gif")
    d6=PhotoImage(file="d6.gif")
    fRo=PhotoImage(file="fRo.gif")
    fVe=PhotoImage(file="fVe.gif")
    fAm=PhotoImage(file="fAm.gif")
    fAz=PhotoImage(file="fAz.gif")
    global imgFichas, arregloDados
    imgFichas["rojo"]=fRo
    imgFichas["verde"]=fVe
    imgFichas["amarillo"]=fAm
    imgFichas["azul"]=fAz
    arregloDados[1] = d1
    arregloDados[2] = d2
    arregloDados[3] = d3
    arregloDados[4] = d4
    arregloDados[5] = d5
    arregloDados[6] = d6
    Pan.configure(bg = "white")
    Pan.geometry("700x600+50+50")
    fondo = PhotoImage(file = "f.gif")
    LF = Label(Pan, image = fondo)
    LF.img = fondo
    LF.pack()
    LB = Label(Pan, text = "BIENVENIDOS A NUESTRO JUEGO", font = ("Times New Roman", 30))
    LB.place(x = 10, y = 10)
    if (OS == "Windows"):
        BTN = Button(Pan, text = "INICIAR", command = lambda: threading.Thread(target=IniciarJuego).start(),
                     font=("Algerian", 40))
    else:
        BTN = Button(Pan, text="INICIAR", command=IniciarJuego, font=("Algerian", 40))
    BTN.place(x=100, y=100)
    Pan.mainloop()


class jugador:

    def __init__(self, nombre, color, fichas, GanoJugador=False, UltimaFicha=None):
        """

        @param nombre:  player name
        @param color:  player color
        @param fichas:  List of elements of objects 'ficha'
        @return: None
        """
        self.nombre = nombre
        self.color = color
        self.fichas = fichas
        self.UltimaFicha = UltimaFicha
        self.GanoJugador = False
        self.Posicion=0

    def DefinirUltimaFicha(self, jugadorActual, Ficha):  # Cada jugador tendra una ultima ficha
        self.UltimaFicha = Ficha # Busca indice de la lista de fichas

    def TirarUnDado(self,desa):  # Para saber quien empieza
        global mod,texto_ingresado, caja_entrada_dados
        """
        @param desarrollador, if the user enter the die value this param is true
        Returns a random number, which represents the die thrown
        @return: Random number between 1 and 6
        """
        x=0
        if not desa:
            if mod<3:
                print("%s presione enter para tirar un dado:" % self.nombre)
                input()
                escribir("\n")
                x = randrange(1, 7)
                escribir(x)
                print("Su resultado es %d\n" % x)
            else:
                caja_entrada_dados.config(state="normal")
                caja_entrada_dados.delete(0,END)
                caja_entrada_dados.insert(0,"%s presione continuar"%self.nombre)
                caja_entrada_dados.config(state="readonly")
                inp=""
                texto_ingresado=""
                while inp=="":
                    inp=texto_ingresado
                x=randrange(1,7)
        else:
            x = 0
            if mod==3:
                caja_entrada_dados.config(state="normal")
                caja_entrada_dados.delete(0,END)
                caja_entrada_dados.insert(0,"Digite el valor del dado de "+self.nombre+":\n")
            texto_ingresado="7"
            while x <= 0 or x > 6:
                if mod<3:
                    x = input("Digite el valor del dado de "+self.nombre+":\n")
                else:
                    x=texto_ingresado
                escribir(x)
                try:
                    x = int(x)
                except:
                    x = 0
        if mod>1:
            global L_DADOS1,L_DADOS2
            L_DADOS1.config(image = arregloDados[x],bg = "green")
            L_DADOS1.img = arregloDados[x] 
            L_DADOS2.config(image=None,bg="white")
        return x
    def TirarDosDados(self,desa):
        """
        @param desarrollador, if the user enter the die value this param is true
        Returns a random number, which represents the die thrown
        @return: Random number between 1 and 6

        """
        global mod,texto_ingresado,caja_entrada_dados
        x = 0
        y = 0
        if not desa:
            if mod<3:
                print("%s presione enter para tirar dos dados:" % self.nombre)
                input()
                escribir("\n")
                x = randrange(1, 7)
                y = randrange(1, 7)
                escribir([x,y])
                print("Su resultado es %d %d\n" % (x, y))
            else:
                caja_entrada_dados.config(state="normal")
                caja_entrada_dados.delete(0,END)
                caja_entrada_dados.insert(0,"%s presione continuar"%self.nombre)
                caja_entrada_dados.config(state="readonly")
                inp=""
                texto_ingresado=""
                while inp=="":
                    inp=texto_ingresado
                x = randrange(1, 7)
                y = randrange(1, 7)
        else:
            if mod==3:
                caja_entrada_dados.config(state="normal")
                caja_entrada_dados.delete(0,END)
                caja_entrada_dados.insert(0,"Digite el valor de los dados de "+self.nombre+":\n")
            texto_ingresado="7"
            lis = []
            while x <= 0 or x > 6 or y <= 0 or y > 6:
                if mod<3:
                    print("%s digite el valor de los dados separados por un espacio" % self.nombre)
                    lis = input().split()
                else:
                    lis=texto_ingresado.split()
                escribir(lis)
                try:
                    x, y = tuple(map(int, lis))
                except:
                    x = 0
                    y = 0
        if mod>1:
            global L_DADOS1 , L_DADOS2 
            L_DADOS1.config(image = arregloDados[x],bg="green")
            L_DADOS1.img = arregloDados[x] 
            L_DADOS2.config(image = arregloDados[y],bg="green")
            L_DADOS2.img = arregloDados[y]
        return (x, y)


class espacio(object):
    
    """
    Represents each space in the board. It considers all the spaces in the board, including the special spaces (exits, safe spaces, arrival spaces)
    """

    def __init__(self, numeroEspacio, etiqueta,x,y,tipoEspacio="normal", colorCasillaEspecial="ninguno",orientacion="Ninguna"):
        """
        @param nombre:  Int between 1 and 101 representing one space in the board
        @param tipo:  Type of space (String) [inicio (requires color),llegada,especial    (requires color),seguro,salida]
        @param color:  (String)Represents the arrival spaces for each player
        @return: None
        """
        global mod
        self.colorCasillaEspecial = colorCasillaEspecial
        self.tipoEspacio = tipoEspacio
        self.numeroEspacio = numeroEspacio
        self.etiqueta = etiqueta
        if mod>1:
            self.etiqueta.bind("<Enter>",self.Entra)
            self.etiqueta.bind("<Leave>",self.Sale)
        self.orientacion = orientacion
        self.NoFichas = 0
        self.PosFicha = ""
        self.x = x
        self.y = y
    def Entra(self,event):
        global L_NOMBRES
        L_NOMBRES.config(text = str(self.numeroEspacio))
    def Sale(self,event):
        global L_NOMBRES
        L_NOMBRES.config(text = "NOMBRES")
class ficha:  # Declara la clase ficha
    """
    Represents each player token
    """

    def __init__(self, nombreFicha, colorFicha, espacioActual,estadoJuego = "inicio"):
        """
        @param nombreFicha: (String)Each token has a unique value, with is composed by the color and a unique number i.e('rojo1', 'rojo2', ...)
        @param colorFicha: (String)The color of the token
        @param espacioActual: Object of class 'espacio'
        @param estadoJuego: (String) The current space of the token

        @return: None
        """
        global mod
        self.colorFicha = colorFicha
        self.espacioActual = espacioActual
        self.estadoJuego = estadoJuego
        self.nombreFicha = nombreFicha
        self.espacioActual = espacioActual
        etiqueta=""
        if mod>1:
            etiqueta = Label(Pan,image = imgFichas[colorFicha])
            etiqueta.img=imgFichas[colorFicha]
            if self.espacioActual.NoFichas == 0:
                etiqueta.place(x = self.espacioActual.x + 40,y = self.espacioActual.y + 40,width = 14,height = 14)
                self.xI = self.espacioActual.x + 40
                self.yI = self.espacioActual.y + 40
            elif self.espacioActual.NoFichas == 1:
                etiqueta.place(x=self.espacioActual.x+80,y=self.espacioActual.y+40,width=14,height=14)
                self.xI = self.espacioActual.x + 80
                self.yI = self.espacioActual.y + 40
            elif self.espacioActual.NoFichas == 2:
                etiqueta.place(x=self.espacioActual.x+40,y=self.espacioActual.y+80,width=14,height=14)
                self.xI = self.espacioActual.x + 40
                self.yI = self.espacioActual.y + 80
            elif self.espacioActual.NoFichas == 3:
                etiqueta.place(x=self.espacioActual.x+80,y=self.espacioActual.y+80,width=14,height=14)
                self.xI = self.espacioActual.x + 80
                self.yI = self.espacioActual.y + 80
        self.espacioActual.NoFichas+=1
        self.etiqueta = etiqueta
        if mod>1:
            self.etiqueta.bind("<Enter>",self.Entra)
            self.etiqueta.bind("<Leave>",self.Sale)
        self.PosFicha = ""
    def Entra(self,event):
        global L_NOMBRES
        L_NOMBRES.config(text=self.nombreFicha)
    def Sale(self,event):
        global L_NOMBRES
        L_NOMBRES.config(text="NOMBRES")
    def imprimirPropiedades(self):
        """
        Returns the current state of the token
        @return: None
        """
        return "Ficha %s: color= %s espacio=%s estado=%s" % (
            self.nombreFicha, self.colorFicha, self.espacioActual.numeroEspacio, self.estadoJuego)
    def eliminarFicha(self):
        self.etiqueta.destroy()
    def cambiarPosicion(self, NuevoEspacio):
        """
        Actualiza la posicion
        """
        global mod
        self.espacioActual.NoFichas-=1
        if self.espacioActual.NoFichas==1 and self.PosFicha=="A":
          self.espacioActual.PosFicha="B"
        elif self.espacioActual.NoFichas==1 and self.PosFicha=="B":
          self.espacioActual.PosFicha="A"
        self.espacioActual = NuevoEspacio
        if self.espacioActual.tipoEspacio=="inicio":
            if mod>1:
                self.etiqueta.place(x=self.xI,y=self.yI)
        elif self.espacioActual.NoFichas==0 and self.espacioActual.orientacion=="vertical":
            if mod>1:
                self.etiqueta.place(x=self.espacioActual.x,y=self.espacioActual.y+7)
            self.espacioActual.PosFicha="A"
            self.PosFicha="A"
        elif self.espacioActual.NoFichas==0 and self.espacioActual.orientacion=="horizontal":
            if mod>1:
                self.etiqueta.place(x=self.espacioActual.x+7,y=self.espacioActual.y)
            self.espacioActual.PosFicha="A"
            self.PosFicha="A"
        elif self.espacioActual.NoFichas==1:
            if self.espacioActual.orientacion=="vertical" and self.espacioActual.PosFicha=="B":
              if mod>1:
                  self.etiqueta.place(x=self.espacioActual.x,y=self.espacioActual.y+7)
              self.PosFicha="A"
            elif self.espacioActual.orientacion=="vertical" and self.espacioActual.PosFicha=="A":
              if mod>1:
                  self.etiqueta.place(x=self.espacioActual.x,y=self.espacioActual.y+33)
              self.PosFicha="B"
            elif self.espacioActual.orientacion=="horizontal" and self.espacioActual.PosFicha=="B":
              if mod>1:
                  self.etiqueta.place(x=self.espacioActual.x+7,y=self.espacioActual.y)
              self.PosFicha="A"
            elif self.espacioActual.orientacion=="horizontal" and self.espacioActual.PosFicha=="A":
              if mod>1:
                  self.etiqueta.place(x=self.espacioActual.x+33,y=self.espacioActual.y)
              self.PosFicha="B"
        NuevoEspacio.NoFichas+=1
    def num(self):
        return self.nombreFicha


def CrearTablero():
    """
    Creates the game board, which is composed by
    68 common spaces,
    7 spaces for each color (28 in total), 4 starting spaces and one arrival space

    @return: List of objects of class 'espacio'
    """
    global mod
    tablero = []
    for x in range(68):
        #5 22 39 56 (r v a z)
        labelF = ""
        labelI = ""
        orientacion = ""
        #if x+1 in ([x1 for x1 in range(1,8)]+[x2 for x2 in range(61,68)]+[x3 for x3 in range(27,34)]+[x4 for x4 in range(35,42)]):
        xF=0
        yF=0
        if mod>1:
            if x+1 in [y1 for y1 in range(1,9)]:
                    orientacion = "vertical"
                    z = x
                    if x + 1 == 5:
                        labelF=Label(Pan,bg="black",borderwidth=0)
                        labelF.place(x=z*18+250,y=252,width=18,height=54)
                        labelI=Label(Pan,bg="#ED0D0D",borderwidth=0)
                        labelI.place(x=z*18+252,y=254,width=14,height=50)
                    else:
                        labelF=Label(Pan,bg="black",borderwidth=0)
                        labelF.place(x=z*18+250,y=252,width=18,height=54)
                        labelI=Label(Pan,bg="white",borderwidth=0)
                        labelI.place(x=z*18+252,y=254,width=14,height=50)
                    xF = z * 18 + 252
                    yF = 254
            elif x+1 in [y1 for y1 in range(9,17)]:
                orientacion="horizontal"
                z= x - 8
                if x+1 == 12:
                    labelF = Label(Pan,bg="black",borderwidth=0)
                    labelF.place(x=394,y=z*18+306,width=54,height=18)
                    labelI = Label(Pan,bg="#ED0D0D",borderwidth=0)
                    labelI.place(x=396,y=z*18+308,width=50,height=14)
                else:
                    labelF = Label(Pan,bg="black",borderwidth=0)
                    labelF.place(x=394,y=z*18+306,width=54,height=18)
                    labelI = Label(Pan,bg="white",borderwidth=0)
                    labelI.place(x=396,y=z*18+308,width=50,height=14)
                xF = 396
                yF = z * 18 + 308
            elif x+1 == 17:
                orientacion="horizontal"
                labelF = Label(Pan,bg="black",borderwidth=0)
                labelF.place(x=448,y=432,width=54,height=18)
                labelI = Label(Pan,bg="#04B112",borderwidth=0)
                labelI.place(x=450,y=434,width=50,height=14)
                xF = 450
                yF = 434
            elif x+1 in [y1 for y1 in range(18,26)]:
                orientacion="horizontal"
                z = x - 17
                if x+1 == 22:
                    labelF = Label(Pan,bg="black",borderwidth=0)
                    labelF.place(x=502,y=432-z*18,width=54,height=18)   
                    labelI = Label(Pan,bg="#04B112",borderwidth=0)
                    labelI.place(x=504,y=434-z*18,width=50,height=14)
                else:
                    labelF = Label(Pan,bg="black",borderwidth=0)
                    labelF.place(x=502,y=432-z*18,width=54,height=18)
                    labelI = Label(Pan,bg="white",borderwidth=0)
                    labelI.place(x=504,y=434-z*18,width=50,height=14)
                yF = 434 - z * 18
                xF = 504
            elif x+1 in [y1 for y1 in range(26,34)]:
                orientacion="vertical"
                z= x - 25
                if x+1 == 29:
                    labelF = Label(Pan,bg="black",borderwidth=0)
                    labelF.place(x=z*18+556,y=252,width=18,height=54)
                    labelI = Label(Pan,bg="#04B112",borderwidth=0)
                    labelI.place(x=z*18+558,y=254,width=14,height=50)
                else:
                    labelF = Label(Pan,bg="black",borderwidth=0)
                    labelF.place(x=z*18+556,y=252,width=18,height=54)
                    labelI = Label(Pan,bg="white",borderwidth=0)
                    labelI.place(x=z*18+558,y=254,width=14,height=50)
                yF = 254
                xF = z * 18 + 558
            elif x+1 == 34:
                orientacion = "vertical"
                labelF = Label(Pan,bg="black",borderwidth=0)
                labelF.place(x=682,y=198,width=18,height=54)
                labelI = Label(Pan,bg="#ECC811",borderwidth=0)
                labelI.place(x=684,y=200,width=14,height=50)
                yF = 200
                xF = 684
            elif x+1 in [y1 for y1 in range(35,43)]:
                orientacion="vertical"
                z = x - 34
                if x+1 == 39:
                    labelF = Label(Pan,bg="black",borderwidth=0)
                    labelF.place(x=682-z*18,y=144,width=18,height=54)
                    labelI = Label(Pan,bg="#ECC811",borderwidth=0)
                    labelI.place(x=684-z*18,y=146,width=14,height=50)
                else:
                    labelF = Label(Pan,bg="black",borderwidth=0)
                    labelF.place(x=682-z*18,y=144,width=18,height=54)
                    labelI = Label(Pan,bg="white",borderwidth=0)
                    labelI.place(x=684-z*18,y=146,width=14,height=50)
                yF = 146
                xF = 684 - z * 18
            elif x+1 in [y1 for y1 in range(43,51)]:
                orientacion="horizontal"
                z= x - 42
                if x+1 == 46:
                    labelF = Label(Pan,bg="black",borderwidth=0)
                    labelF.place(x=502,y=126-z*18,width=54,height=18)
                    labelI = Label(Pan,bg="#ECC811",borderwidth=0)
                    labelI.place(x=504,y=128-z*18,width=50,height=14)
                else:
                    labelF = Label(Pan,bg="black",borderwidth=0)
                    labelF.place(x=502,y=126-z*18,width=54,height=18)
                    labelI = Label(Pan,bg="white",borderwidth=0)
                    labelI.place(x=504,y=128-z*18,width=50,height=14)
                yF = 128 - z * 18
                xF = 504
            elif x+1 == 51:
                orientacion="horizontal"
                labelF=Label(Pan,bg="black",borderwidth=0)
                labelF.place(x=448,y=0,width=54,height=18)
                labelI=Label(Pan,bg="#2926DA",borderwidth=0)
                labelI.place(x=450,y=2,width=50,height=14)
                yF=2
                xF=450
            elif x+1 in [y1 for y1 in range(52,60)]:
                orientacion="horizontal"
                z=x-51
                if x+1==56:
                    labelF=Label(Pan,bg="black",borderwidth=0)
                    labelF.place(x=394,y=z*18,width=54,height=18)
                    labelI=Label(Pan,bg="#2926DA",borderwidth=0)
                    labelI.place(x=396,y=z*18+2,width=50,height=14)
                else:
                    labelF=Label(Pan,bg="black",borderwidth=0)
                    labelF.place(x=394,y=z*18,width=54,height=18)
                    labelI=Label(Pan,bg="white",borderwidth=0)
                    labelI.place(x=396,y=z*18+2,width=50,height=14)
                yF=z*18+2
                xF=396
            elif x+1 in [y1 for y1 in range(60,68)]:
                orientacion="vertical"
                z=x-59
                if x+1==63:
                    labelF=Label(Pan,bg="black",borderwidth=0)
                    labelF.place(x=376-z*18,y=144,width=18,height=54)
                    labelI=Label(Pan,bg="#2926DA",borderwidth=0)
                    labelI.place(x=378-z*18,y=146,width=14,height=50)
                else:
                    labelF=Label(Pan,bg="black",borderwidth=0)
                    labelF.place(x=376-z*18,y=144,width=18,height=54)
                    labelI=Label(Pan,bg="white",borderwidth=0)
                    labelI.place(x=378-z*18,y=146,width=14,height=50)
                yF=146
                xF=378-z*18
            elif x+1==68:
                orientacion="vertical"
                labelF=Label(Pan,bg="black",borderwidth=0)
                labelF.place(x=250,y=198,width=18,height=54)
                labelI=Label(Pan,bg="#ED0D0D",borderwidth=0)
                labelI.place(x=252,y=200,width=14,height=50)
                yF=200
                xF=252
        if x+1 in [5,22,39,56]:
             NuevaCasilla = espacio(x + 1,labelI,xF,yF, "salida","ninguno",orientacion)
        elif x + 1 in [12, 17, 29, 34, 46, 51, 63, 68]:
             NuevaCasilla = espacio(x + 1,labelI,xF,yF, "seguro","ninguno",orientacion)
        else:
             NuevaCasilla = espacio(x + 1,labelI,xF,yF, 'normal',"ninguno",orientacion)
        tablero.append(NuevaCasilla)
    label=""
    if mod>1:
        label=Label(Pan,bg="#ED0D0D",borderwidth=0)
        label.place(x=250,y=306,height=144,width=144)
        label=Label(Pan,bg="white",borderwidth=0)
        label.place(x=255,y=311,height=134,width=134)
    tablero.append(espacio(69, label,255,311,"inicio","rojo"))
    if mod>1:
        label=Label(Pan,bg="#04B112",borderwidth=0)
        label.place(x=556,y=306,height=144,width=144)
        label=Label(Pan,bg="white",borderwidth=0)
        label.place(x=561,y=311,height=134,width=134)
    tablero.append(espacio(70,label,561,311, "inicio", "verde"))
    if mod>1:
        label=Label(Pan,bg="#ECC811",borderwidth=0)
        label.place(x=556,y=0,height=144,width=144)
        label=Label(Pan,bg="white",borderwidth=0)
        label.place(x=561,y=5,height=134,width=134)
    tablero.append(espacio(71,label, 561,5,"inicio", "amarillo"))
    if mod>1:
        label=Label(Pan,bg="#2926DA",borderwidth=2)
        label.place(x=250,y=0,height=144,width=144)
        label=Label(Pan,bg="white",borderwidth=0)
        label.place(x=255,y=5,height=134,width=134)
    tablero.append(espacio(72, label,255,5,"inicio", "azul"))
    for x in range(28):
        if x < 7:
            z=x
            if mod>1:        
                labelF=Label(Pan,bg="black",borderwidth=0)
                labelF.place(x=z*18+268,y=198,width=18,height=54)
                labelF=Label(Pan,bg="#ED0D0D",borderwidth=0)
                labelF.place(x=z*18+270,y=200,width=14,height=50)
            NuevaCasilla = espacio(72 + x + 1, labelF,z*18+270,200,"especial", "rojo","vertical")
        elif x < 14:
            z=x-7
            if mod>1:
                labelF=Label(Pan,bg="black",borderwidth=0)
                labelF.place(x=448,y=414-z*18,width=54,height=18)
                labelF=Label(Pan,bg="#04B112",borderwidth=0)
                labelF.place(x=450,y=416-z*18,width=50,height=14)
            NuevaCasilla = espacio(72 + x + 1,labelF,450,416-z*18, "especial", "verde","horizontal")
        elif x < 21:
            z=x-14
            if mod>1:
                labelF=Label(Pan,bg="black",borderwidth=0)
                labelF.place(x=664-z*18,y=198,width=18,height=54)
                labelF=Label(Pan,bg="#ECC811",borderwidth=0)
                labelF.place(x=666-z*18,y=200,width=14,height=50)
            NuevaCasilla = espacio(72 + x + 1, labelF,666-z*18,200,"especial", "amarillo","vertical")
        else:
            z=x-21
            if mod>1:
                labelF=Label(Pan,bg="black",borderwidth=0)
                labelF.place(x=448,y=z*18+18,width=54,height=18)
                labelF=Label(Pan,bg="#2926DA",borderwidth=0)
                labelF.place(x=450,y=z*18+20,width=50,height=14)
            NuevaCasilla = espacio(72 + x + 1, labelF,450,z*18+20,"especial", "azul","horizontal")
        tablero.append(NuevaCasilla)
    lab=""
    if mod>1:
        imagen=PhotoImage(file="corona.gif")
        lab=Label(Pan,bg="black")
        lab.place(x=394,y=144,width=162,height=162)
        lab=Label(Pan,image=imagen)
        lab.img=imagen
        lab.place(x=399,y=149,width=152,height=152)
    tablero.append(espacio(101, lab,399,149,"llegada"))
    return tablero


def CrearJugadoresYFichas(tablero, numeroJugadores, nombres):
    """
    Creates the tokens of each player in the board and also initializes each object of class 'player'

    @param tablero: Object of class 'tablero'
    @param numeroJugadores: (int) The total number of players
    @param nombres: (tuple of strings) containing the name of each player

    """
    jugadores = []
    for x in range(numeroJugadores):  # Itera en el número de jugadores que hayan ingresado
        fichas = []
        if x == 0:  # Si x es 0, sera el primer jugador, y por ende fichas rojas
            """
            68-> Start position for red.
            69-> Start position for green.
            70-> Start position for yellow.
            71-> Start position for blue.
            """
            for z in range(4):  # Crea las 4 fichas rojas
                NuevaFicha = ficha("rojo%d" % (z + 1), "rojo",
                                   tablero[68])  # Le asigna el número de ficha con su posición
                fichas.append(NuevaFicha)  # Lo agrega en una lista de fichas
            jugadores.append(jugador(nombres[0], "rojo", fichas))  # Crea un objeto jugador y lo agrega a una lista
            jugadores[0].UltimaFicha=jugadores[0].fichas[3]
        elif x == 1:
            for z in range(4):
                NuevaFicha = ficha("verde%d" % (z + 1), "verde", tablero[69])
                fichas.append(NuevaFicha)
            jugadores.append(jugador(nombres[1], "verde", fichas))
            jugadores[1].UltimaFicha=jugadores[1].fichas[3]
        elif x == 2:
            for z in range(4):
                NuevaFicha = ficha("amarillo%d" % (z + 1), "amarillo", tablero[70])
                fichas.append(NuevaFicha)
            jugadores.append(jugador(nombres[2], "amarillo", fichas))
            jugadores[2].UltimaFicha=jugadores[2].fichas[3]
        elif x == 3:
            for z in range(4):
                NuevaFicha = ficha("azul%d" % (z + 1), "azul", tablero[71])
                fichas.append(NuevaFicha)
            jugadores.append(jugador(nombres[3], "azul", fichas))
            jugadores[3].UltimaFicha=jugadores[3].fichas[3]

    return jugadores


def pedirDatos():
    """
    Ask the user to input the total number of players, and then asks for the name of each player.
    """
    global mod,caja_entrada_dados,boton_entrada_dados,texto_ingresado
    texto_ingresado=""
    n = 0
    if mod>1:
        Esp = Label(Pan, text="Esperando Jugadores...", bg="white", fg="black", font=("Times New Roman", 32))   
        Esp.place(y=0, x=0)
        if mod<3:
            Ins = Label(Pan, text="Digite las entradas en su input de consola...", bg="black", fg="white",
                font=("Times New Roman", 17))
            Ins.place(y=400, x=0)
        if mod==3:
            caja_entrada_dados = Entry(Pan, font = 'Helvetica 20',borderwidth=0)
            caja_entrada_dados.place(x= 0, y = 500, width=550,height=50)
            boton_entrada_dados = Button(Pan, text='Continuar',font=("Times New Roman",20),fg="white", command = obtenerDadosIngresados, bg="blue", borderwidth=0)
            boton_entrada_dados.place(x=550,y=500,width=150,height=50)
            caja_entrada_dados.delete(0,END)
            caja_entrada_dados.insert(0,"¿Cuántos jugadores van a ingresar?")
    while (n <= 0 or n > 4):
        if mod<3:
            print("Cuántos jugadores ingresarán?:")
            n = input()
            escribir(n)
        else:
            n=texto_ingresado
        try:
            n = int(n)
        except:
            n = 0
    nombres = []
    Eti = []
    for z in range(n):
        # Eti.destroy()
        color = ""
        if (z == 0): color = "#ED0D0D"
        if (z == 1): color = "#04B112"
        if (z == 2): color = "#ECC811"
        if (z == 3): color = "#2926DA"
        if mod<3:
            print("Digite el nombre del jugador %d" % (z + 1))
            nombre = ""
        else:
            caja_entrada_dados.delete(0,END)
            caja_entrada_dados.insert(0,"Digite el nombre del jugador %d" % (z + 1))
        nombre = ""
        texto_ingresado=""
        while (len(nombre) <= 0 or len(nombre) > 10):
            if mod<3:
                nombre = input()
                escribir(n)
            else:
                nombre=texto_ingresado
        if mod>1:
            Eti.append(
            Label(Pan, text="Jugador %d: " % (z + 1) + nombre, font=("Times New Roman", 30), bg=color, fg="white"))
            Eti[z].place(y=60 * z + 100)
        nombres.append(nombre)
    x=""
    if mod==3:
        caja_entrada_dados.delete(0,END)
        caja_entrada_dados.insert(0,"Presione continuar (ó digite la contraseña para modo desarrollador):")
        texto_ingresado=""
        while x=="":
            x=texto_ingresado
    else:
        print("Presione enter para continuar (ó digite la contraseña para modo desarrollador):")
        x = input()
    if x == "mazamorra":  #:>   JAJAJA Nicolás si ves esto pues jajaja saludos bro :)
        global desa
        desa = True
    escribir("\n")
    if mod>1:
        for x in Eti:
            x.destroy()
        Esp.destroy()
        if mod<3:Ins.destroy()
    return nombres


def ObtenerMayor(listaJugadores):
    """
    Gets the max element of a 'jugador' list

    @param listaJugadores: list of elements of class 'jugador'
    """
    arreglo = []
    for i in range(len(listaJugadores)):
        arreglo.append(listaJugadores[i].valor)
    return max(arreglo)


def OrdenDeJuego(ListaJugadores, modoDesarrollador=False):
    """
    Returns the index of the first player to start.
    Example:
    Two players have joined:
        First player: 3
        Second player: 6
        Second player starts the game, and the others players play in the same order of the list of players

    @param ListaJugadores: List of objects of class 'jugador'
    @param modoDesarrollador: For evaluation purposes only
    """
    global desa,mod
    aux = ListaJugadores[:]
    while (len(aux) != 1):
        for x in aux:
            x.valor = x.TirarUnDado(desa)
        aux2=[]
        for x in aux:
            if not(x.valor != ObtenerMayor(aux)):
                aux2.append(x)
        aux=aux2
    if mod<3:
        print(aux[0].nombre + " es el primero en iniciar")
    else:
        tkinter.messagebox.showinfo("Aviso",aux[0].nombre + " es el primero en iniciar")
    return ListaJugadores.index(aux[0])

    


def GameOver(Jugadores):
    """
    @param Jugadores: List ob object of class 'Jugador'

    """
    numberWonPlayers = 0  # Counts the number of players that have already won
    for jugadorActual in Jugadores:
        if jugadorActual.GanoJugador:
            numberWonPlayers += 1
    if (numberWonPlayers == len(Jugadores) - 1 and len(Jugadores) > 1) or (numberWonPlayers==1 and len(Jugadores)==1):
        global POSICION
        jugadorFaltante=[jug for jug in Jugadores if not jug.GanoJugador]
        if not len(jugadorFaltante)==0:
          jugadorFaltante[0].Posicion=POSICION
        return True
    return False


def posiblesMovimientos(JugadorActual, resultadoDado, ListaJugadores):
    """
    Returns a list of all the possible movements of a player given a die result

    @param JugadorActual: Object of class 'Jugador'
    @param resultadoDado: The number of spaces to move forward
    @param ListaJugadores: List of Objects of class 'Jugador'
    """
    listaPosiblesMovimientos = []
    # Esto se va a cambiar de funcion
    listaCasillasCarcel = [69, 70, 71, 72]
    numeros = {}
    numeros2={}
    for jugador in ListaJugadores:
        for ficha in jugador.fichas:
            casillaActual = ficha.espacioActual.numeroEspacio
            if casillaActual in numeros and not casillaActual in listaCasillasCarcel:
                numeros[casillaActual][1] += 1
                if numeros[casillaActual][0].colorFicha!=ficha.colorFicha and casillaActual in [5,22,39,56]:
                    numeros2[casillaActual]=[numeros[casillaActual][0],ficha]
            elif not casillaActual in listaCasillasCarcel:
                numeros[casillaActual] = [ficha, 1]

    listaBloqueos = [item for item, valor in numeros.items() if valor[1] == 2]
    listaConUnaFicha = [(item, valor[0]) for item, valor in numeros.items() if valor[1] == 1]
    tuplaCasillasUnaFicha = tuple([valor for valor, ficha in listaConUnaFicha])
    dat = {"rojo": 5, "verde": 22, "amarillo": 39, "azul": 56}
    diccionarioSeguros = {"rojo": 68, "verde": 17, "amarillo": 34,
                          "azul": 51}  # Seguros donde inician las casillas especiales de cada color
    diccionarioPrimeraEspecial = {"rojo": 73, "verde": 80, "amarillo": 87, "azul": 94}  # Primera casilla especial

    numeroSeguroSalida = diccionarioSeguros[JugadorActual.color]
    numeroPrimeraEspecial = diccionarioPrimeraEspecial[JugadorActual.color]
    numeroDiccionarioSeguros = diccionarioSeguros[JugadorActual.color]

    colorJugador = JugadorActual.color

    

    for fichaActual in JugadorActual.fichas:
        bloqueo = False
        casillaFicha = fichaActual.espacioActual.numeroEspacio
        nombreFicha = fichaActual.nombreFicha
        posicionFinal = casillaFicha + resultadoDado
        if casillaFicha in listaCasillasCarcel and resultadoDado != 5:  # Evalua si la casilla esta en la ficha y saca diferente de 5
            continue
        if casillaFicha in listaCasillasCarcel and resultadoDado == 5:  # Si el dado da 5 y hay una casilla en la carcel sale automaticamente
            if not (dat[colorJugador] in listaBloqueos and not dat[colorJugador] in numeros2) :
                if (dat[colorJugador] in tuplaCasillasUnaFicha and numeros[dat[colorJugador]][0].colorFicha!=fichaActual.colorFicha):
                    return ([(nombreFicha + " sale de la carcel a la casilla: %d. Captura a %s." % (dat[colorJugador],numeros[dat[colorJugador]][0].nombreFicha), fichaActual,numeros[dat[colorJugador]][0])])
                elif dat[colorJugador] in numeros2:
                    if numeros2[dat[colorJugador]][0].colorFicha!= fichaActual.colorFicha and numeros2[dat[colorJugador]][1].colorFicha== fichaActual.colorFicha:
                        return ([(nombreFicha + " sale de la carcel a la casilla: %d. Captura a %s." % (dat[colorJugador],numeros2[dat[colorJugador]][0].nombreFicha), fichaActual,numeros2[dat[colorJugador]][0])])                            
                    elif numeros2[dat[colorJugador]][1].colorFicha!= fichaActual.colorFicha and numeros2[dat[colorJugador]][0].colorFicha== fichaActual.colorFicha: 
                        return ([(nombreFicha + " sale de la carcel a la casilla: %d. Captura a %s." % (dat[colorJugador],numeros2[dat[colorJugador]][1].nombreFicha), fichaActual,numeros2[dat[colorJugador]][1])])
                    else:
                        continue
                else:
                    return ([(nombreFicha + " sale de la carcel a la casilla: %d." % dat[colorJugador], fichaActual)])
            else:
                continue
        else:
            #  Condición 3
            for x in range(casillaFicha + 1, posicionFinal + 1):
                if (casillaFicha <= numeroSeguroSalida and x > numeroSeguroSalida) or (colorJugador=="verde" and casillaFicha>=51 and casillaFicha<=68 and x>85): 
                    if (colorJugador=="verde" and casillaFicha>=51 and casillaFicha<=68 and x>85):
                        if x%68 + (numeroPrimeraEspecial - numeroDiccionarioSeguros) - 1 in listaBloqueos:
                            bloqueo = True
                            break
                        elif x%68 + (numeroPrimeraEspecial - numeroDiccionarioSeguros) - 1>numeroPrimeraEspecial+7:
                            bloqueo=True
                            break
                    else:
                        if x + (numeroPrimeraEspecial - numeroDiccionarioSeguros) - 1 in listaBloqueos:
                            bloqueo = True
                            break
                        elif x + (numeroPrimeraEspecial - numeroDiccionarioSeguros) - 1>numeroPrimeraEspecial+7:
                            bloqueo=True
                            break
                elif casillaFicha <= 68 and x <= 68 and x in listaBloqueos:
                    bloqueo = True
                    break
                elif x % 68 in listaBloqueos:
                    bloqueo = True
                    break
                elif x in listaBloqueos or x > numeroPrimeraEspecial + 7:  #:()
                    bloqueo = True
                    break
                    
        CasillaEspecial = 0
        ListaCasillasSeguro=(12, 17, 29, 34, 46, 51, 63, 68)
        ListaCasillasSalida=(5, 22, 39, 56)
        if (casillaFicha <= numeroSeguroSalida and posicionFinal > numeroSeguroSalida) or (colorJugador=="verde" and casillaFicha>=51 and casillaFicha<=68 and posicionFinal>85):
            if (colorJugador=="verde" and casillaFicha>=51 and casillaFicha<=68 and posicionFinal>85):
              CasillaEspecial = posicionFinal%68 + (numeroPrimeraEspecial - numeroSeguroSalida - 1)
            else:
              CasillaEspecial = posicionFinal + (numeroPrimeraEspecial - numeroSeguroSalida - 1)
            if CasillaEspecial == numeroPrimeraEspecial + 7:
                CasillaEspecial = 101

        if not bloqueo:
            if CasillaEspecial == 101 or posicionFinal == numeroPrimeraEspecial + 7:
                textoRespuesta = '{} corona'.format(nombreFicha)
                listaPosiblesMovimientos.append((textoRespuesta, fichaActual))

            elif posicionFinal <= 68 and posicionFinal in tuplaCasillasUnaFicha and CasillaEspecial==0:
                fichaCapturada = numeros[posicionFinal][0]
                if fichaCapturada.colorFicha != colorJugador and not posicionFinal in ListaCasillasSeguro and not posicionFinal in ListaCasillasSalida:
                    textoRespuesta = '{} captura a {} en casilla {}'.format(nombreFicha, fichaCapturada.nombreFicha,
                                                                            posicionFinal)
                    listaPosiblesMovimientos.append((textoRespuesta, fichaActual, fichaCapturada))
                else:
                    textoRespuesta = '{} mueve a casilla {}'.format(nombreFicha, posicionFinal)
                    listaPosiblesMovimientos.append((textoRespuesta, fichaActual))

            elif posicionFinal > 68 and (posicionFinal%68 in tuplaCasillasUnaFicha) and CasillaEspecial==0 and casillaFicha<=68:
                fichaCapturada_2 = numeros[posicionFinal % 68][0]
                if fichaCapturada_2.colorFicha != colorJugador and not posicionFinal%68 in ListaCasillasSeguro and not posicionFinal%68 in ListaCasillasSalida:
                    textoRespuesta = '{} captura a {} en casilla {}'.format(nombreFicha, fichaCapturada_2.nombreFicha,
                                                                            posicionFinal % 68)
                    listaPosiblesMovimientos.append((textoRespuesta, fichaActual, fichaCapturada_2))
                else:
                    textoRespuesta = '{} mueve a casilla {}'.format(nombreFicha, posicionFinal % 68)
                    listaPosiblesMovimientos.append((textoRespuesta, fichaActual))

            elif CasillaEspecial != 0:
                textoRespuesta = '{} mueve a casilla {}'.format(nombreFicha, CasillaEspecial)
                listaPosiblesMovimientos.append((textoRespuesta, fichaActual))

            elif posicionFinal <= 68:
                textoRespuesta = '{} mueve a casilla {}'.format(nombreFicha, posicionFinal)
                listaPosiblesMovimientos.append((textoRespuesta, fichaActual))

            elif posicionFinal > 68 and casillaFicha > 68:
                textoRespuesta = '{} mueve a casilla {}'.format(nombreFicha, posicionFinal)
                listaPosiblesMovimientos.append((textoRespuesta, fichaActual))

            elif posicionFinal > 68:
                textoRespuesta = '{} mueve a casilla {}'.format(nombreFicha, posicionFinal % 68)
                listaPosiblesMovimientos.append((textoRespuesta, fichaActual))
    if len(listaPosiblesMovimientos) == 0:
        return None
    return listaPosiblesMovimientos


def realizarMovimiento(movimientoRealizar, tablero, jugadorActual,Jugadores): # Añadimos parametro jugador actual para poder definir la ultima ficha de cada jugador
    """
    Actualiza las posiciones de las fichas en el tablero


    @param movimientoRealizar: Es la tupla que contiene
    1. El movimiento a realizar (String)
    2. Objeto ficha a mover
    3. Objeto ficha capturado (String vacío si no captura)

    """
    global mod
    if movimientoRealizar == None:
        return
    FichaCapturada = None
    listaCasillasCarcel = {'rojo': 69, 'verde': 70, 'amarillo': 71, 'azul': 72}
    listaCasillasSalida = {'rojo': 5, 'verde': 22, 'amarillo': 39, 'azul': 56}
    FichaMover = movimientoRealizar[1]
    descripcionMovimiento = movimientoRealizar[0]

    if len(movimientoRealizar) == 3:
        FichaCapturada = movimientoRealizar[2]
    if 'sale' in descripcionMovimiento:
        if "Captura" in descripcionMovimiento:
            FichaCapturada=movimientoRealizar[2]
            FichaCapturada.estadoJuego = "inicio"
            casillaCarcel = listaCasillasCarcel[FichaCapturada.colorFicha]
            FichaCapturada.cambiarPosicion(tablero[casillaCarcel - 1])
            FichaMover.cambiarPosicion(tablero[listaCasillasSalida[FichaMover.colorFicha] - 1])
            FichaMover.estadoJuego = "activo"
            listaMovi=posiblesMovimientos(jugadorActual,20,Jugadores)
            if mod>1:
                tkinter.messagebox.showinfo("Captura",FichaMover.nombreFicha+" captura a "+FichaCapturada.nombreFicha)
                tkinter.messagebox.showinfo("Salida",FichaMover.nombreFicha +" sale de la carcel.")
            if listaMovi and len(listaMovi)==1:
                realizarMovimiento(listaMovi[0],tablero,jugadorActual,Jugadores)
            elif listaMovi and len(listaMovi)>1:
                realizarMovimiento(opciones(listaMovi,jugadorActual),tablero,jugadorActual,Jugadores)
        else:
            FichaMover.cambiarPosicion(tablero[listaCasillasSalida[FichaMover.colorFicha] - 1])
            FichaMover.estadoJuego = "activo"
            if mod>1:
                tkinter.messagebox.showinfo("Salida",FichaMover.nombreFicha +" sale de la carcel.")
    elif 'captura' in descripcionMovimiento:
        posicionFinal = int(descripcionMovimiento.split()[-1])
        casillaCarcel = listaCasillasCarcel[FichaCapturada.colorFicha]
        FichaCapturada.cambiarPosicion(tablero[casillaCarcel - 1])  # Cambia de posición
        FichaCapturada.estadoJuego = "inicio"
        FichaMover.cambiarPosicion(tablero[posicionFinal - 1])
        listaMovi=posiblesMovimientos(jugadorActual,20,Jugadores)
        if mod>1:
            tkinter.messagebox.showinfo("Captura",FichaMover.nombreFicha+" captura a "+FichaCapturada.nombreFicha)
        if listaMovi and len(listaMovi)==1:
            realizarMovimiento(listaMovi[0],tablero,jugadorActual,Jugadores)
        elif listaMovi and len(listaMovi)>1:
            realizarMovimiento(opciones(listaMovi,jugadorActual),tablero,jugadorActual,Jugadores)
    elif 'mueve' in descripcionMovimiento:
        posicionFinal = int(descripcionMovimiento.split()[-1])
        FichaMover.cambiarPosicion(tablero[posicionFinal - 1])  # Cambia posicion de la ficha
    elif 'corona' in descripcionMovimiento:
        if mod>1:
            FichaMover.eliminarFicha()
        jugadorActual.fichas.remove(FichaMover)
        if len(jugadorActual.fichas) == 0:
          global POSICION
          jugadorActual.Posicion = POSICION
          POSICION+=1
          jugadorActual.GanoJugador = True
        if mod>1:
            tkinter.messagebox.showinfo("Corona",FichaMover.nombreFicha+" corona.")
        listaMovi=posiblesMovimientos(jugadorActual,10,Jugadores)
        if listaMovi and len(listaMovi) == 1:
            realizarMovimiento(listaMovi[0],tablero,jugadorActual,Jugadores)
        elif listaMovi and len(listaMovi) > 1:
            realizarMovimiento(opciones(listaMovi,jugadorActual),tablero,jugadorActual,Jugadores)
        return
    jugadorActual.DefinirUltimaFicha(jugadorActual, FichaMover)


def imprimirEstado(Jugador):
    for ficha in Jugador.fichas:
        print(ficha.imprimirPropiedades())


def opciones(Lista, JugadorActual):
    eleccion = 0
    global mod,caja_entrada_dados,boton_entrada_dados,seleccion
    seleccion=False
    if mod==3:
        clicked = StringVar(Pan)
        caja_entrada_dados.config(state="normal")
        caja_entrada_dados.delete(0,END)
        caja_entrada_dados.insert(0,"%s seleccione una opcion de la lista y oprima continuar."%JugadorActual.nombre)
        caja_entrada_dados.config(state="readonly")
        options =[opcion[0] for opcion in  Lista]
        clicked.set("Seleccione una opción")
        drop = OptionMenu(Pan,clicked,clicked.get(),*options)
        drop.place(x=0,y=450,width=700,height=50)
        boton_entrada_dados.config(command=seleccionarOpcion)
        while(not seleccion):
            if clicked.get()=="Seleccione una opción":
                seleccion=False
            pass
        eleccion=options.index(clicked.get())+1
        boton_entrada_dados.config(command=obtenerDadosIngresados)
        drop.destroy()
    if mod<3:
        while eleccion <= 0 or eleccion > len(Lista):
            x = 1
            for opcion in Lista:
                print(f'{x} -> {opcion[0]}')
                x += 1
            print(f'{x}  ->  Ver estado de Fichas')
            eleccion = input()
            escribir(eleccion)
            try:
                eleccion = int(eleccion)
            except:
                eleccion = 0
            if eleccion == len(Lista)+1:
                imprimirEstado(JugadorActual)
    return Lista[eleccion - 1]

def FuncDados(etiqueta,accion):
    global dadoSeleccionado
    if accion==0:
        etiqueta.config(bg="red")
    elif accion==1:
        etiqueta.config(bg="green")
    elif accion==2:
        dadoSeleccionado=1
    elif accion==3:
        dadoSeleccionado=2
    
def IniciarJuego():
    """
    "main" function, its executed from the _main_ function of python
    """
    global desa,mod
    if mod>1:
        global LB,BTN
        LB.destroy()
        BTN.destroy()
    nom = tuple(pedirDatos())  # Retorna una tupla con los nombres de los jugadores
    if mod>1:
        global L_DADOS, L_NOMBRES, L_TABLERO,L_OPCIONES,L_TEXTO,L_DADOS1,L_DADOS2,caja_entrada_dados,boton_entrada_dados
        L_DADOS1=Label(Pan,bg="white",font=("Times New Roman",20))
        L_DADOS1.place(x=37,y=20,width=175,height=175)
        L_DADOS2=Label(Pan,bg="white",font=("Times New Roman",20))
        L_DADOS2.place(x=37,y=210,width=175,height=175)
        L_NOMBRES=Label(Pan,bg="orange",fg="white",text="NOMBRES",font=("Times New Roman",20))
        L_NOMBRES.place(x=0,y=400,width=250,height=50)
        L_TABLERO=Label(Pan,bg="white",fg="white",font=("Times New Roman",20))
        L_TABLERO.place(x=250,y=0,width=450,height=450)
    Tablero = CrearTablero()  # Se crea el tablero
    Jugadores = CrearJugadoresYFichas(Tablero, len(nom), nom)  # Retorna la lista de objetos jugador 'Jugadores'
    indicePrimerJugador = OrdenDeJuego(Jugadores)
    while not GameOver(Jugadores):
        repetirLanzamiento = True
        contadorParesSeguidos = 0  # contador de 3 seguidos
        jugadorActual = Jugadores[indicePrimerJugador % len(Jugadores)]
        if jugadorActual.GanoJugador:continue
        while repetirLanzamiento:
            resultadoDado1, resultadoDado2 = jugadorActual.TirarDosDados(desa)
            if resultadoDado1 == resultadoDado2:
                repetirLanzamiento = True
                contadorParesSeguidos += 1
                if contadorParesSeguidos == 3:
                    listaCasillasCarcel = {'rojo': 69, 'verde': 70, 'amarillo': 71, 'azul': 72}
                    UltimaFichaJugador = jugadorActual.UltimaFicha  # Invocamos la ultima ficha del jugador actual
                    nombreFicha = UltimaFichaJugador.nombreFicha  # Invocamos su nombre
                    posicionFinal = listaCasillasCarcel[UltimaFichaJugador.colorFicha]  # Sacamos la llave de su posicion en la carcel
                    realizarMovimiento(['{} mueve a casilla {}'.format(nombreFicha, posicionFinal),UltimaFichaJugador], Tablero,jugadorActual,Jugadores)
                    UltimaFichaJugador.estadoJuego = 'inicio'
                    repetirLanzamiento = False
                    contadorParesSeguidos = 0
                    imprimirEstado(jugadorActual)
                    continue
            else:
                contadorParesSeguidos = 0
                repetirLanzamiento = False
            if resultadoDado1+resultadoDado2==5:
                ListaMovi=posiblesMovimientos(jugadorActual, 5, Jugadores)
                if ListaMovi and len(ListaMovi)==1 and "sale" in ListaMovi[0][0]:
                    realizarMovimiento(ListaMovi[0],Tablero,jugadorActual,Jugadores)
                    continue
            ListaMovi1 = posiblesMovimientos(jugadorActual, resultadoDado1, Jugadores)
            ListaMovi2 = posiblesMovimientos(jugadorActual, resultadoDado2, Jugadores)
            ListaMoviF = ""
            if ListaMovi1 and 'sale' in ListaMovi1[0][0]:
                realizarMovimiento(ListaMovi1[0], Tablero, jugadorActual,Jugadores)
                ListaMovi2 = posiblesMovimientos(jugadorActual, resultadoDado2, Jugadores)
                ListaMoviF = ListaMovi2
            elif ListaMovi2 and "sale" in ListaMovi2[0][0]:
                realizarMovimiento(ListaMovi2[0], Tablero, jugadorActual,Jugadores)
                ListaMovi1 = posiblesMovimientos(jugadorActual, resultadoDado1, Jugadores)
                ListaMoviF = ListaMovi1
            if type(ListaMoviF) != list:
                if ListaMovi1 and ListaMovi2:
                    global dadoSeleccionado
                    dadoSeleccionado = 0
                    if mod<3:
                        while dadoSeleccionado <= 0 or dadoSeleccionado > 2:
                            print("Qué dado desea mover (?) :\n1. %d\n2. %d" % (resultadoDado1, resultadoDado2))
                            dadoSeleccionado = input()
                            escribir(dadoSeleccionado)
                            try:
                                dadoSeleccionado = int(dadoSeleccionado)
                            except:
                                dadoSeleccionado = 0
                    else:
                        caja_entrada_dados.config(state="normal")
                        caja_entrada_dados.delete(0,END)
                        caja_entrada_dados.insert(0,"%s seleccione uno de los dados"%jugadorActual.nombre)
                        caja_entrada_dados.config(state="readonly")
                        L_DADOS1.bind("<Enter>",lambda x:FuncDados(L_DADOS1,0))
                        L_DADOS2.bind("<Enter>",lambda x:FuncDados(L_DADOS2,0))
                        L_DADOS1.bind("<Button-1>",lambda x:FuncDados(L_DADOS1,2))
                        L_DADOS1.bind("<Leave>",lambda x:FuncDados(L_DADOS1,1))
                        L_DADOS2.bind("<Leave>",lambda x:FuncDados(L_DADOS2,1))
                        L_DADOS2.bind("<Button-1>",lambda x:FuncDados(L_DADOS2,3))
                        while dadoSeleccionado==0:
                            pass
                        L_DADOS1.config(bg="green")
                        L_DADOS2.config(bg="green")
                        L_DADOS1.unbind("<Enter>")
                        L_DADOS2.unbind("<Enter>")
                        L_DADOS1.unbind("<Button-1>")
                        L_DADOS1.unbind("<Leave>")
                        L_DADOS2.unbind("<Leave>")
                        L_DADOS2.unbind("<Button-1>")
                    for x in range(2):
                        if dadoSeleccionado==1 and not ListaMovi1:
                          continue
                        elif dadoSeleccionado==2 and not ListaMovi2:
                          continue
                        elif dadoSeleccionado == 1 and len(ListaMovi1) == 1:
                            realizarMovimiento(ListaMovi1[0], Tablero, jugadorActual,Jugadores)
                            ListaMovi2 = posiblesMovimientos(jugadorActual, resultadoDado2, Jugadores)
                            dadoSeleccionado = 2
                        elif dadoSeleccionado == 1 and len(ListaMovi1) > 1:
                            realizarMovimiento(opciones(ListaMovi1, jugadorActual), Tablero, jugadorActual,Jugadores)
                            ListaMovi2 = posiblesMovimientos(jugadorActual, resultadoDado2, Jugadores)
                            dadoSeleccionado = 2
                        elif dadoSeleccionado == 2 and len(ListaMovi2) == 1:
                            realizarMovimiento(ListaMovi2[0], Tablero, jugadorActual,Jugadores)
                            ListaMovi1 = posiblesMovimientos(jugadorActual, resultadoDado1, Jugadores)
                            dadoSeleccionado = 1
                        elif dadoSeleccionado == 2 and len(ListaMovi2) > 1:
                            realizarMovimiento(opciones(ListaMovi2, jugadorActual), Tablero, jugadorActual,Jugadores)
                            ListaMovi1 = posiblesMovimientos(jugadorActual, resultadoDado1, Jugadores)
                            dadoSeleccionado = 1
                        imprimirEstado(jugadorActual)
                elif ListaMovi1:
                    if len(ListaMovi1) == 1:
                        realizarMovimiento(ListaMovi1[0], Tablero, 
                        jugadorActual,Jugadores)
                        imprimirEstado(jugadorActual)
                    else:
                        realizarMovimiento(opciones(ListaMovi1, jugadorActual), Tablero, jugadorActual,Jugadores)
                        imprimirEstado(jugadorActual)
                elif ListaMovi2:
                    if len(ListaMovi2) == 1:
                        realizarMovimiento(ListaMovi2[0], Tablero, jugadorActual,Jugadores)
                    else:
                        realizarMovimiento(opciones(ListaMovi2, jugadorActual), Tablero,jugadorActual,Jugadores)
            elif ListaMoviF and len(ListaMoviF) == 1:
                realizarMovimiento(ListaMoviF[0], Tablero, jugadorActual,Jugadores)
                imprimirEstado(jugadorActual)
            elif ListaMoviF and len(ListaMoviF) > 1:
                realizarMovimiento(opciones(ListaMoviF, jugadorActual), Tablero, jugadorActual,Jugadores)
                imprimirEstado(jugadorActual)

        indicePrimerJugador += 1  # Defines the infinite cycle
    if mod>1:
        Pan.quit()
    Jugadores.sort(key=lambda x:x.Posicion)
    for x in Jugadores:
      print(x.nombre+" terminó en posición: %d"%x.Posicion)
ele=0
while(ele<=0 or ele>3):
  print("BiEnVeNiDoS a NuEsTrO jUeGo:\nSeleccione una de las siguientes:\n1.Modo Consola\n2.Modo Consola+Graficos\n3.Modo Graficos\n")
  ele=input()
  try:
    ele=int(ele)
  except:
    ele=0
mod=ele
if mod>1:
  if OS=="Windows":
      threading.Thread(target=Gra).start()
  else:
      Gra()
else:
  IniciarJuego()
#IniciarJuego()
#  Like si ves esto
#  Like ;)
#if (z == 0): color = "#ED0D0D"
#if (z == 1): color = "#04B112"
#if (z == 2): color = "#ECC811"
#if (z == 3): color = "#2926DA"
#pasa