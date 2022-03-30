from random import choices
class pregunta:
    def __init__(self,pregunta):
        self.pregunta  = pregunta
        self.dificultad = 0
        self.respuesta = 0
        self.premio = 0
    def dificultad_s(self,difi):
        self.dificultad = difi
    def respuesta_s(self,res):
        self.respuesta = res
    def premio_s(self,premio):
        self.premio = premio
class Banco:
    def __init__(self):
        self.lista = []
    def agregar_pregunta(self,pregunta):
        self.lista.append(pregunta)
preguntas = [
    "Cuanto es 1+99? \n1. 100 \n2. 99 \n3. 101 \n4. 98",
    "Cuantos dias tiene un años? \n1. 360 \n2. 365 \n3. 101 \n4. 364",
    "Cuantos dias tiene una semana? \n1. 6 \n2. 7 \n3. 5 \n4. 8",
    "Que objeto es mas pesado? \n1. boligrafo \n2. carro \n3. cama \n4. pluma",
    "Cual es la raiz cuadrada de 4? \n1. 2 \n2. 7 \n3. 5 \n4. 8",
    
    "¿Cual es el satelite de la tierra? \n1. Marte \n2. Fobos \n3. Pluton \n4. Luna",
    "Cuantos planetas hay en el sistema solar? \n1. 5 \n2. 6 \n3. 7 \n4. 8",
    "Cuanto es 1/4 de 20? \n1. 5 \n2. 4 \n3. 6 \n4. 3",
    "Un triangulo equilatero cuantos lados iguales tiene? \n1. 3 \n2. 2 \n3. 1 \n4. Ninguno",
    "Un radio en geometria hace referencia a \n1. Circulo  \n2. Cuadrado \n3. Rectangulo \n4. Estrella",
    
    "Cual es la velocidad de la luz en km/s \n1. 100.000 \n2. 250.000 \n3. 300.000 \n4. 299.792 ",
    "Cual es el animal mas grande del mundo \n1. Elefante \n2. Caballo \n3. Ballena \n4. Leon",
    "Cual es la velocidad del sonido en el aire \n1. 331\n2. 400\n3. 332\n4. 800",
    "Un siglo equivale a  \n1. 100 anños \n2. 99 anyos \n3. 101 anyos \n4. 98 anyos",
    "El numero de euler es un numero  \n1. Entero \n2. Fraccionario \n3. Trascendental \n4. Negativo",
    
    "El pinto de la monalisa fue \n1. Da'vinci \n2. Tesla \n3. Maquiavelo \n4. Louis ",
    "El autor de don quijote fue \n1. Richard \n2. Cervantes \n3. Lagrange \n4. Miguel",
    "Cuando se combina rojo con que color producira naranja \n1. Rojo\n2. Violeta\n3. Amarillo\n4. Negro",
    "La suma de los angulos internos de un triangulo es  \n1. 100  \n2. 150  \n3. 180  \n4. 190 ",
    "La cantidad imaginaria i es equivalente a la raiz cuadrada de   \n1. -2 \n2. -3 \n3. -4 \n4. -1",
    
    "La integral de x entre 0 y 1 es  \n1. 1/2 \n2. 2/5 \n3. 3/5 \n4. 1 ",
    "La segunda ley de newton puede ser escrita como \n1. F=ma \n2. F=2ma \n3. F=3ma \n4. F=4ma",
    "El pintor de las Meninas fue \n1. Victor Hugo\n2. Velasquez \n3. Da'vinci\n4. Dali",
    "La segunda guerra mundial termino en \n1. 1950 \n2. 1990 \n3. 1945 \n4. 1935",
    "America fue descubierta en  \n1. 1492 \n2. 1493 \n3. 1490 \n4. 1491",
    
]
respuestas = [1,2,2,2,1, 4,9,1,1,1, 4,3,1,1,3, 1,2,3,3,4, 1,1,2,3,1]
premios = [10,30,50,100,200]
b = Banco()
for i in range(len(preguntas)):
    p1 = pregunta(preguntas[i])
    if i<5:
        p1.dificultad_s(0)
        p1.premio_s(premios[0])
    if i>=5 and i<10:
        p1.dificultad_s(1)
        p1.premio_s(premios[1])
    if i>=10 and i<15:
        p1.dificultad_s(2)
        p1.premio_s(premios[2])
    if i>=15 and i<20:
        p1.dificultad_s(3)
        p1.premio_s(premios[3])
    if i>=20 and i<25:
        p1.dificultad_s(4)
        p1.premio_s(premios[4])
    p1.respuesta_s(respuestas[i])
    b.agregar_pregunta(p1)
    
jugadores = {}

while True:
    exe = True
    acumulado = 0
    nivel = 0
    jugador = input("Digite por favor el nombre del jugador nuevo o digite 0 para cerrar el programa ")
    if jugador == '0':
        print("Gracias por jugar")
        break
    jugadores[jugador] = acumulado
    while exe:
        
        
        x = choices(b.lista)
        while x[0].dificultad != nivel:
            x = choices(b.lista)
        print(x[0].pregunta)
        print("Ronda numero "+str(nivel) + " por un premio de "+str(premios[nivel]))
        r = input("Digite la respuesta o si desea retirarse e irse con "+str(acumulado)+" presione x: ")
        if r == 'x':
            break
        if int(r) == x[0].respuesta:
            print("¡Respuesta correcta! avanza")
            acumulado+=premios[nivel] 
            jugadores[jugador] = acumulado
            print("Premio total acumulado "+str(acumulado))
            nivel+=1
        else:
            print("Ha perdido, no ha respondido correctamente la pregunta!\n")
            print("El jugador"+jugador+" premio que ha perdido es el acumulado "+str(acumulado))
            break
            
        if nivel ==5:
            print("Ha ganando! terminaste el nivel 5! ")
            exe = False
            print(jugador + ' con un premio total acumulado de '+str(acumulado))

for jugador in jugadores:
    print(jugador +' acumulado: ' +str(jugadores[jugador]))   