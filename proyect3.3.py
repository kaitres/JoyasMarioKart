import sys
import time
from random import randint
import pygame
import copy
from pygame.locals import *

def genera_tablero():
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
def patron_inicial(tablero,a):
	j=0
	b=[5,4,3,2,2,3,4,5,4,3]
	while j<=ancho-1:
		x=largo-1
		while x>b[j]:
			tablero[x][j]=randint(0,a)
			x-=1
		j+=1
	return tablero
def mostrar(tablero):
	i=0
	while i<largo:
		j=0
		while j<ancho:
			print tablero[i][j],
			j+=1
		print
		i+=1
def estado_fig(fig):
	fig[0]=pygame.image.load("peach.png")
	fig[1]=pygame.image.load("mario verde.png")
	fig[2]=pygame.image.load("mario.png")
	fig[3]=pygame.image.load("donk.png")
	fig[4]=pygame.image.load("bowser.png")
	fig[5]=pygame.image.load("bowserm.png")
	fig[6]=pygame.image.load("peach1.png")
	fig[7]=pygame.image.load("mario verde1.png")
	fig[8]=pygame.image.load("mario1.png")
	fig[9]=pygame.image.load("donk1.png")
	fig[10]=pygame.image.load("bowser1.png")
	fig[11]=pygame.image.load("bowserm1.png")
def validar(i,j):
	if i>=0 and j>=0 and i<largo and j<ancho:
		return True
	else:
		return False
def posible_jugada(tablero,i,j,y,x,num,cont):
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
def mostrar_figuras(tablero):
	rect=[(60,68,64),(30,34,32)]
	i=0
	y=100
	cont=0

	while i<largo:
		j=0
		x=150
		while j<ancho:
			pygame.draw.rect(screen, rect[j%2-i%2], [x, y, 50, 50], 0)
				
			cont2=0
			while cont2<12:		
				if tablero[i][j]==cont2:
					screen.blit(fig[cont2],(x,y))
				cont2+=1
			j+=1
			x+=50
		y+=50
		i+=1
def eliminar_figuras(tablero,i,j,y,x,num):
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
def mostrar_resplandor(tablero,a):
	i=0
	y=100
	cont=0
	rect=[(60,68,64),(30,34,32)]
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
					eliminar_figuras(tablero,i,j,y,x,tablero[i][j])
					bajar_figuras(tablero,a)
					centrar_figuras(tablero)
					return cont+1
			
			
			j+=1
			x+=50
		y+=50
		i+=1
	return 0
def bajar_figuras(tablero,a):
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
def centrar_figuras(tablero):
	cont=0
	while cont <largo:
		i=0
		while i<ancho :
			if tablero[largo-1][i]==-9:
				mover_izq(tablero,i)
			i+=1
		cont+=1
def mover_izq(tablero,y):
	while y<ancho:
		i=largo-1
		while i>=0:
			if y+1<ancho:
				if tablero[i][y]==-9 and tablero[i][y+1]>=0:
					tablero[i][y]=tablero[i][y+1]
					tablero[i][y+1]=-9
			i-=1
		y+=1
def subir_colocar(tablero,a):
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
def juego(a,fondo,tiempo):
	estado_fig(fig)	
	gameover=pygame.image.load('gameover.png')
	fuente = pygame.font.Font("font8.ttf", 15)
	fuentenumero = pygame.font.Font("font1.ttf", 20)
	screen.blit(fondo,(0,0))	
	tablero =genera_tablero()
	tablero =patron_inicial(tablero,a)
	puntaje=0
	linea=0
	i=True
	infinito=True
	while infinito:
		screen.blit(fondo,(0,0))
		screen.blit(pygame.image.load("marco1.png"),(15,140))
		screen.blit(pygame.image.load("marco1.png"),(15,250))
		
		screen.blit(fuentenumero.render( str(puntaje) ,0, (0,0,0)),(45,155))
		screen.blit(fuentenumero.render( "Puntaje" ,0, (0,0,0)),(15,110))
		screen.blit(fuentenumero.render( "Linea" ,0, (0,0,0)),(15,220))
		mx , my = pygame.mouse.get_pos()
		mostrar_figuras(tablero)
		cont=mostrar_resplandor(tablero,a)
		puntaje=puntaje+(cont)*10
		if (pygame.time.get_ticks()/1000)%tiempo==0 and i:
			if subir_colocar(tablero,a) :
				screen.blit(gameover,(0,0))
				pygame.display.update()
				time.sleep(3)

				infinito=False
			linea+=1
			if linea%5==0:
				screen.blit(pygame.image.load('levelup.png'),(15,300))
				screen.blit(fuentenumero.render( str(linea) ,0, (0,0,0)),(45,265))
				pygame.display.update()
				time.sleep(2)
				tiempo-=1
			i=False
		screen.blit(fuentenumero.render( str(linea) ,0, (0,0,0)),(45,265))

		if (pygame.time.get_ticks()/1000)%(tiempo+1)==0:
			i=True

		pygame.display.update()

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit(); sys.exit(); 
def menu_juego():
	global ancho
	global largo
	global tiempo
	global fig
	fig=[0,0,0,0,0,0,0,0,0,0,0,0]
	fondo=pygame.image.load('fondiu+logo2.png')
	screen.blit(fondo,(0,0))
	fuente = pygame.font.Font("font8.ttf", 30)
	nivel1=pygame.image.load("buton00.png")
	nivel2=pygame.image.load("buton02.png")
	nivel3=pygame.image.load("buton04.png")
	nivel12=pygame.image.load("buton01.png")
	nivel13=pygame.image.load("buton03.png")
	nivel11=pygame.image.load("buton09.png")

	while True:
		screen.blit(fondo,(0,0))
		mx , my = pygame.mouse.get_pos()
		screen.blit(nivel1,(125,200) )
		screen.blit(nivel2,(285,200) )
		screen.blit(nivel3,(445,200) )


		if (mx>= 125 and mx<= 275) and (my>= 200 and my<=400):
				screen.blit(nivel11,(125,200) )
				if pygame.mouse.get_pressed() == (1,0,0):
					screen.fill((0,0,0))
					largo=10
					ancho=8
					fondo=pygame.image.load('fondiu+logo1.png')
					tiempo=10
					juego(3,fondo,tiempo)
					pygame.display.update()



		if (mx>= 285 and mx<= 435) and (my>= 200 and my<=400):
				screen.blit(nivel12,(285,200) )
				if pygame.mouse.get_pressed() == (1,0,0):
					screen.fill((0,0,0))
					largo=10
					ancho=9
					fondo=pygame.image.load('fondiu+logo3.png')
					tiempo=8
					juego(4,fondo,tiempo)
					pygame.display.update()




		if (mx>= 445 and mx<= 595) and (my>= 200 and my<=400):
				screen.blit(nivel13,(445,200) )
				if pygame.mouse.get_pressed() == (1,0,0):
					screen.fill((0,0,0))
					largo=10
					ancho=10
					fondo=pygame.image.load('fondiu+logo4.png')
					tiempo=6
					juego(5,fondo,tiempo)
					pygame.display.update()
					


		pygame.display.update()

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit(); sys.exit(); 
if __name__ == '__main__':
	pygame.init()
	screen=pygame.display.set_mode((700,650))
	fondo=pygame.image.load('fondiu+logo2.png')
	screen.blit(fondo,(0,0))
	inicio=pygame.image.load("buton1.png")
	iniciob=pygame.image.load("buton0.png")
	salir=pygame.image.load("buton2.png")
	salirb=pygame.image.load("buton3.png")

	while True:
		screen.blit(fondo,(0,0))
		mx , my = pygame.mouse.get_pos()
		screen.blit(inicio,(175,115) )

		screen.blit(salir,(175,195) )


		if (mx>= 175 and mx<= 549) and (my>= 115 and my<=164):
				screen.blit(iniciob,(175,115) )
				if pygame.mouse.get_pressed() == (1,0,0):
					screen.fill((0,0,0))
					pygame.mouse.set_pos([350,500])
					time.sleep(1)
					menu_juego()
					pygame.display.update()




		if (mx>= 175 and mx<= 549) and (my>= 195 and my<=244):
				screen.blit(salirb,(175,195) )
				if pygame.mouse.get_pressed() == (1,0,0):
					screen.fill((0,0,0))


					pygame.display.update()
					


		pygame.display.update()

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit(); sys.exit(); 
