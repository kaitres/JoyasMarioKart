# -*- coding: utf-8 -*-

import sys
import time
from random import randint
from random import choice
import pygame
import copy
from pygame.locals import *
def genera_tablero(): #Funcion que genera una matriz llena de -9 (Vacia) y la retorna  
	M=[]
	i=0
	while i<largo:
		L=[]
		j=0
		while j<ancho:
			L.append(-9)
			j+=1
		M=M+[L]
		i+=1
	return M 
def patron_inicial(tablero,a):#Funcion que se encarga de colocar las figuras( Numeros) en diferente orden y patron;
							  #Argumentos: la matriz (tablero) y la dificultad del juego (a);  
	j=0
	b=[]
	s=0
	helper=[6,8,5,6,6,6,7,8,7,6]
	while s<10:
		x=choice(helper)      #Se le da a elegir entre los numeros que estan en la lista (helper), para el patron;  
		b.append(x)
		s+=1
	while j<=ancho-1:         #Desde el numero seleccionado hacia arriba se le empieza a agregar un numero entre 0 y la difilcultad
		x=largo-1
		while x>b[j]:
			tablero[x][j]=randint(0,a)
			x-=1
		j+=1
	return tablero
def estado_fig(fig): #Funcion que carga las figuras con y sin brillo en una matriz (fig);
					 #Argumentos: la lista (fig)
	fig[0]=pygame.image.load("/asset/peach.png")
	fig[1]=pygame.image.load("/asset/mario verde.png")
	fig[2]=pygame.image.load("/asset/mario.png")
	fig[3]=pygame.image.load("/asset/toad.png")
	fig[4]=pygame.image.load("/asset/bowser.png")
	fig[5]=pygame.image.load("/asset/bowserm.png")
	fig[6]=pygame.image.load("/asset/peach1.png")
	fig[7]=pygame.image.load("/asset/mario verde1.png")
	fig[8]=pygame.image.load("/asset/mario1.png")
	fig[9]=pygame.image.load("/asset/toad1.png")
	fig[10]=pygame.image.load("/asset/bowser1.png")
	fig[11]=pygame.image.load("/asset/bowserm1.png")
def validar(i,j): #Funcion que se encargar de validar las cordenadas i, j dentro de la matriz
	if i>=0 and j>=0 and i<largo and j<ancho:
		return True
	else:
		return False
def posible_jugada(tablero,i,j,y,x,num,cont): #Funcion de tipo backtracking que busca cuantas figuras colindantes hay cerca de la argumentada
											  # mientras cambia las figuras colindantes a la argumentada por su version brillante y retorna la cantidad; 
                                              #Argumentos: la matriz (tablero),posicion "X" en la matriz (i),posicion "Y" en la matriz (j),
                                              #            posicion "Y" en la ventana (y),posicion "X" en la ventana(x),figura a buscar(num),
                                              #            cantidad de figuras colindantes(cont)
	a=[1,0,-1,0]
	b=[0,1,0,-1]
	z=0
	while z<4:
		cont2=0
		if validar(i+a[z], j+b[z]) and num==tablero[i+a[z]][j+b[z]] and tablero[i+a[z]][j+b[z]]>-1:
			while cont2<6:		
				if num==cont2:
					screen.blit(fig[cont2+6],(x+(b[z])*50,y+(a[z])*50))
				cont2+=1
			tablero[i][j]=-1
			cont+=1
			cont=posible_jugada(tablero,i+a[z],j+b[z],y+(a[z])*50,x+(b[z])*50,num,cont)
		z+=1
	return cont
def mostrar_figuras(tablero): #Funcion que muestra las figuras de acuerdo a la matriz y genera el cuadrado de juego; 
							  #Argumentos: la matriz(tablero)
	rect=[(251,207,8),(69,175,73)]
	i=0
	y=100
	cont=0

	while i<largo:
		j=0
		x=150
		while j<ancho:
			pygame.draw.rect(screen, rect[j%2-i%2], [x, y, 50, 50], 2)
				
			cont2=0
			while cont2<12:		
				if tablero[i][j]==cont2:
					screen.blit(fig[cont2],(x,y))
				cont2+=1
			j+=1
			x+=50
		y+=50
		i+=1
def eliminar_figuras(tablero,i,j,y,x,num): #Funcion de tipo backtracking que elimina las figuras colindantes a la argumentada;
										   #Argumentos: la matriz (tablero),posicion "X" en la matriz (i),posicion "Y" en la matriz (j),
                                           #            posicion "Y" en la ventana (y),posicion "X" en la ventana(x),figura a buscar(num)
	tablero[i][j]=-9
	a=[1,0,-1,0]
	b=[0,1,0,-1]
	z=0
	while z<4:
		cont2=0
		if validar(i+a[z], j+b[z]) and num==tablero[i+a[z]][j+b[z]] and tablero[i+a[z]][j+b[z]]>-1:
			while cont2<6:		
				if num==cont2:
					screen.blit(fig[cont2+6],(x+(b[z])*50,y+(a[z])*50))
				cont2+=1
			eliminar_figuras(tablero,i+a[z],j+b[z],y+(a[z])*50,x+(b[z])*50,num)
		z+=1
	return
def mostrar_resplandor(tablero,a): #Funcion que hace la brillar a la figura seleccionada para luego llamar a (posible_jugada)
                                   # retornar la cantidad de figuras colindantes iguales a la seleccionada y verificar si hace clic
                                   # a la vez que la cantidad de figuras colindantes es mayor que 1 para llamar a (eliminar_figuras),
                                   # seguido de (bajar_figuras) y (centrar_figuras) finalmente la funcion retorna la cantidad de figuras
                                   # eliminadas
                                   #Argumentos: la matriz(tablero), la dificultad(a)   
	i=0
	y=100
	cont=0
	rect=[(60,68,64),(30,34,32)]
	sonido = pygame.mixer.Sound("/asset/clic.ogg")
	while i<largo:
		j=0
		x=150
		while j<ancho:
			cont2=0
			pygame.draw.rect(screen, rect[j%2-i%2], [x, y, 50, 50], 1)		
			tablero2= copy.deepcopy(tablero)
			mx,my =pygame.mouse.get_pos()
			if mx>x and mx<x+50 and my>y and my<y+50:
				while cont2<6:	
					if tablero[i][j]==cont2:
						screen.blit(fig[cont2+6],(x,y))
					cont2+=1
				cont=posible_jugada(tablero2,i,j,y,x,tablero[i][j],0)
				if pygame.mouse.get_pressed() == (1,0,0) and cont>1:
					sonido.play()
					eliminar_figuras(tablero,i,j,y,x,tablero[i][j])
					bajar_figuras(tablero,a)
					centrar_figuras(tablero)
					return cont+1
			
			
			j+=1
			x+=50
		y+=50
		i+=1
	return 0
def bajar_figuras(tablero,a): #Funcion que genera la gravedad del tablero cuando se elimina una figura y hace caer las de arriba;
                              #Argumento: la matriz(tablero), la dificultad(a)  
	cont=0
	while cont <largo:
		i=0
		while i<largo:
			j=0
			while j<ancho:
				if tablero[i][j]>-1 and tablero[i][j]<a+1 and i+1<largo:
					if tablero[i+1][j]<-1:
						tablero[i+1][j]=tablero[i][j]
						tablero[i][j]=-9
				j+=1
			i+=1
		cont+=1
def centrar_figuras(tablero): #Funcion que verifica si hay un espacio en blanco (-9) en la ultima linea de juego para llamar a (mover_izq);
                              #Argumento: la matriz(tablero)
	cont=0
	while cont <largo:
		i=0
		while i<ancho :
			if tablero[largo-1][i]==-9:
				mover_izq(tablero,i)
			i+=1
		cont+=1
def mover_izq(tablero,y): #Funcion que mueve hacia la izquierda todas figuras desde la posicion "Y" (y) hasta la ultima columna del tablero;
                          #Argumento: la matriz(tablero), posicion "Y" dela matriz(y)
	while y<ancho:
		i=largo-1
		while i>=0:
			if y+1<ancho:
				if tablero[i][y]==-9 and tablero[i][y+1]>=0:
					tablero[i][y]=tablero[i][y+1]
					tablero[i][y+1]=-9
			i-=1
		y+=1
def subir_colocar(tablero,a): #Funcion que sube todas las fichas para luego introducir una nueva "Linea" si una de las columnas esta completa
                              # la funcion retorna True sino esta completa retorna False
                              # Argumento: la matriz(tablero), la dificultad(a)  
	i=0
	while i<ancho:
		if tablero[0][i]>-1:
			return True	
		i+=1
	i=0
	while i<largo:
		j=0
		while j<ancho:
			if tablero[i][j]<-1 and tablero[i][j]<a+1 and i+1<largo:
				tablero[i][j]=tablero[i+1][j]
				tablero[i+1][j]=-9
			j+=1
		i+=1
	i=0
	while i<ancho:
		tablero[largo-1][i]=randint(0,a)
		i+=1

	return False
def juego(a,fondo,tiempo): #Funcion que genera la pantalla de juego, comienza cargando la pista de acuerdo a la dificultad, luego carga las diferentes
                           # imagenes y fuentes para su posterior ejecucion mediante un ciclo infinito  en el que la unica forma de salir es que una 
                           # de las columnas este supere su capacidad para luego salir y retornar;
                           #Argumentos: la dificultad(a), el logo de mario (fondo), cantidad de segundos (tiempo)  
	if a==5:
		pygame.mixer.music.load("/asset/dificil.mp3")
		pygame.mixer.music.play(-1,0.0)
	if a==3:
		pygame.mixer.music.load("/asset/facil.mp3")
		pygame.mixer.music.play(-1,0.0)
	if a==4:
		pygame.mixer.music.load("/asset/normal.mp3")
		pygame.mixer.music.play(-1,0.0)
	estado_fig(fig)	

	gameover=pygame.image.load('/asset/gameover.png')
	fuente = pygame.font.Font("/asset/font8.ttf", 15)
	fuentenumero = pygame.font.Font("/asset/font1.ttf", 20)	
	tablero =genera_tablero()
	tablero =patron_inicial(tablero,a)
	puntaje=0
	marco=pygame.image.load("/asset/marco3.png")
	score=pygame.image.load("/asset/Puntaje.png")
	line=pygame.image.load("/asset/linea.png")
	planta=pygame.image.load("/asset/planta.png")
	goomba=pygame.image.load("/asset/goomba.png")
	linea=0
	espacio=pygame.time.get_ticks()
	reloj=tiempo
	i=True
	infinito=True
	up = pygame.mixer.Sound("/asset/up.ogg")
	while infinito:
		screen.fill((255,255,255))
		screen.blit(fondo,(270,0))
		screen.blit(marco,(15,140))
		screen.blit(marco,(15,250))
		screen.blit(planta,(555,300))
		screen.blit(goomba,(-30,400))
		screen.blit(fuentenumero.render( str(puntaje) ,0, (0,0,0)),(45,155))
		screen.blit(score,(15,110))
		screen.blit(line,(15,220))
		mx , my = pygame.mouse.get_pos()
		mostrar_figuras(tablero)
		cont=mostrar_resplandor(tablero,a)
		puntaje=puntaje+(cont)*10
		if ((pygame.time.get_ticks()-espacio)/1000)==tiempo :                #Condicion que pregunta el tiempo y genera (subir_colocar);
			linea+=1
			
			if subir_colocar(tablero,a) :
				screen.blit(gameover,(0,0))
				muerte=pygame.time.get_ticks()
				pygame.mixer.music.stop()
				pygame.mixer.music.load("/asset/perdio.ogg")
				pygame.mixer.music.play(-1,0.0)
				pygame.display.update()
				while (pygame.time.get_ticks()-muerte)<2100:                #Ciclo de tiempo muerto para ver la imagen y escuchar el sonido; 
					pass

				infinito=False
				pygame.mixer.music.stop()
				linea=-1
			
			
			if linea%5==0:
				up.play()
				screen.blit(pygame.image.load('/asset/levelup.png'),(15,300))
				screen.blit(fuentenumero.render( str(linea) ,0, (0,0,0)),(45,265))
				pygame.display.update()
				muerte=pygame.time.get_ticks()
				while (pygame.time.get_ticks()-muerte)<1000:
					pass
				reloj-=1
			tiempo+=reloj


			
		screen.blit(fuentenumero.render( str(linea) ,0, (0,0,0)),(45,265))

		pygame.display.update()
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit(); sys.exit();
	
def menu_juego(): #Funcion que genera la pantalla de dificultad, he ingresa los argumetos correspondientes a cada opcion seleccionada
	pygame.mixer.music.load("/asset/menu.mp3")
	pygame.mixer.music.play(-1,0.0)
	global ancho
	global largo
	global tiempo
	global fig
	fig=[0,0,0,0,0,0,0,0,0,0,0,0]
	fondo=pygame.image.load('/asset/logo.png')
	screen.fill((255,255,255))
	fuente = pygame.font.Font("/asset/font8.ttf", 30)
	nivel1=pygame.image.load("/asset/buton00.png")
	nivel2=pygame.image.load("/asset/buton02.png")
	nivel3=pygame.image.load("/asset/buton04.png")
	nivel12=pygame.image.load("/asset/buton01.png")
	nivel13=pygame.image.load("/asset/buton03.png")
	nivel11=pygame.image.load("/asset/buton09.png")

	while True:
		screen.fill((255,255,255))
		screen.blit(fondo,(270,0))
		mx , my = pygame.mouse.get_pos()
		screen.blit(nivel1,(125,200) )
		screen.blit(nivel2,(285,200) )
		screen.blit(nivel3,(445,200) )


		if (mx>= 125 and mx<= 275) and (my>= 200 and my<=400):
				screen.blit(nivel11,(125,200) )
				if pygame.mouse.get_pressed() == (1,0,0):
					screen.fill((255,255,255))
					largo=10
					ancho=8
					
					tiempo=10
					juego(3,fondo,tiempo)
					pygame.display.update()



		if (mx>= 285 and mx<= 435) and (my>= 200 and my<=400):                        
				screen.blit(nivel12,(285,200))
				if pygame.mouse.get_pressed() == (1,0,0):
					screen.fill((255,255,255))
					largo=10
					ancho=9
					tiempo=8
					juego(4,fondo,tiempo)
					pygame.display.update()




		if (mx>= 445 and mx<= 595) and (my>= 200 and my<=400):                        
				screen.blit(nivel13,(445,200) )
				if pygame.mouse.get_pressed() == (1,0,0):
					screen.fill((255,255,255))
					largo=10
					ancho=10
					tiempo=6
					juego(5,fondo,tiempo)
					pygame.display.update()

		if not pygame.mixer.music.get_busy() :
			pygame.mixer.music.load("/asset/menu.mp3")
			pygame.mixer.music.play(-1,0.0)


		pygame.display.update()
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit(); sys.exit(); 
if __name__ == '__main__':  

	pygame.init()
	pygame.mixer.music.load('/asset/start.mp3')
	pygame.mixer.music.play(-1,0.0)
	screen=pygame.display.set_mode((700,650))

	fondo=pygame.image.load('/asset/logo.png')
	
	inicio=pygame.image.load("/asset/buton1.png")
	iniciob=pygame.image.load("/asset/buton0.png")
	salir=pygame.image.load("/asset/buton2.png")
	salirb=pygame.image.load("/asset/buton3.png")
	screen.fill((255,255,255))
	while True:
		screen.blit(fondo,(270,0))
		mx , my = pygame.mouse.get_pos()
		screen.blit(inicio,(175,115) )

		screen.blit(salir,(175,195) )
        

		if (mx>= 175 and mx<= 549) and (my>= 115 and my<=164): #Condicion del boton jugar 
				screen.blit(iniciob,(175,115) )
				if pygame.mouse.get_pressed() == (1,0,0):
					screen.fill((255,255,255))
					pygame.mouse.set_pos([350,500])
					time.sleep(1)
					menu_juego()
					pygame.display.update()




		if (mx>= 175 and mx<= 549) and (my>= 195 and my<=244): #Condicion del boton salir
				screen.blit(salirb,(175,195) )
				if pygame.mouse.get_pressed() == (1,0,0):
					screen.fill((255,255,255))
					pygame.quit(); sys.exit(); 


					pygame.display.update()
					


		pygame.display.update()

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit(); sys.exit(); 
