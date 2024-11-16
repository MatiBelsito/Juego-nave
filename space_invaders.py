
import pygame
import random

# Inicializar pygame
pygame.init()

# Configurar la pantalla: 800 x 600 píxeles
screen = pygame.display.set_mode((800, 600))  # Tupla inmutable / objeto pantalla
pygame.display.set_caption("Space Invaders")

# Clase Enemigo
class Enemy:
    def __init__(self): 
        self.image = pygame.image.load("enemigo.png")
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)
        self.x_change = 0.5  # Velocidad de movimiento en el eje x
        self.y_change = 40  # Cambio en y cuando el enemigo toca un borde

    def draw(self):  # Dibujar la nave en la pantalla
        screen.blit(self.image, (self.x, self.y))
        
    def move(self):  # Actualizar posición en x y manejar cambios de dirección
        self.x += self.x_change
       
        # Movimiento y cambio de dirección del enemigo
        if self.x <= 0 or self.x >= 736:
            self.x_change *= -1  # Invertir dirección
            self.y += self.y_change  # Al cambiar de dirección, el enemigo baja

# Clase Jugador
class Player: 
    def __init__(self):
        self.image = pygame.image.load("nave.png")
        self.x = 370  # Posición inicial en x
        self.y = 480  # Posición inicial en y
        self.x_change = 0  # Cambio de posición en x (para movimiento)
        
    def draw(self):  # Dibujar la nave en la pantalla
        screen.blit(self.image, (self.x, self.y))
        
    def move(self):  # Actualizar posición en x
        self.x += self.x_change
        # Limitar el movimiento dentro de la pantalla
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:  # Limitar al borde derecho (800 - ancho de la figura 64)
            self.x = 736

# Crear varios enemigos
num_enemigos = 5
enemigos = [Enemy() for _ in range(num_enemigos)]  # Usando comprensión de listas

# Crear una instancia de objeto para invocar al jugador
player = Player()

# Bucle principal
running = True
while running: 
    # Fondo de pantalla (negro)
    screen.fill((0, 0, 0))  # RGB
    
    # Gestión de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Detectar si se presiona una tecla (para eventos del teclado)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_change = -0.5
            elif event.key == pygame.K_RIGHT:
                player.x_change = 0.5
                
        # Detectar si se suelta la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.x_change = 0  # Detener el movimiento al soltar la tecla
    
    # Mover y dibujar el jugador
    player.move()
    player.draw()
    
    # Mover y dibujar los enemigos
    for enemigo in enemigos:
        enemigo.move()
        enemigo.draw()
    
    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()


#para salir del entorno en cmd: desactivate.bat