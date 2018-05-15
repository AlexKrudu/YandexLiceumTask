import pygame
import socket


pygame.init()
display = pygame.display
screen = display.set_mode((500, 500))


def draw_arrow(surface, pos, pressed):
    width = int(not pressed)
    pygame.draw.rect(surface, pygame.Color("blue"), (pos, (50, 50)), width)
    pygame.draw.polygon(surface, pygame.Color("blue"), [(pos[0]+10, pos[1]+10), (pos[0]+25, pos[1]+25),
                                                        (pos[0]+10, pos[1]+40)], 1-width)


running = True
angle = 90
angle_differ = 0
velocity = 1500
velocity_differ = 0
counter = 0
brake = False

while running:
    screen.fill(pygame.Color('white'))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_DOWN:
                velocity = 1600
            if e.key == pygame.K_UP:
                velocity = 1300
            if e.key == pygame.K_LEFT:
                angle = 110
            if e.key == pygame.K_RIGHT:
                angle = 70
            if e.key == pygame.K_SPACE:
                brake = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_DOWN:
                velocity = 1500
            if e.key == pygame.K_UP:
                velocity = 1500
            if e.key == pygame.K_LEFT:
                angle = 90
            if e.key == pygame.K_RIGHT:
                angle = 90
            if e.key == pygame.K_SPACE:
                brake = False
    draw_arrow(screen, (225, 125), velocity == 1200)  # вверх
    draw_arrow(screen, (175, 175), angle > 90)  # влево
    draw_arrow(screen, (225, 175), velocity == 1700)  # вниз
    draw_arrow(screen, (275, 175), angle < 90)  # вправо
    display.update()
    velocity = 1500 * brake + velocity * (not brake)
    result = '00/'+str(int(velocity))+'/'+str(int(angle))
    if counter % 4 == 0:
        s = socket.socket()
        s.connect(('172.24.1.1', 1089))
        print(result)
        s.send(bytes(result, 'utf-8'))
        s.close()
    counter += 1
pygame.quit()
