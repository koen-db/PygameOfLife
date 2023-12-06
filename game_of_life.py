import pygame

SCHERM = BREEDTE, HOOGTE = 1280,720
SNELHEID = 10
TEGEL = 40

pygame.init()
speelveld = pygame.display.set_mode(SCHERM)
klok = pygame.time.Clock()

while True:

    speelveld.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [pygame.draw.line(speelveld, pygame.Color('darkslategray'), (x, 0), (x, HOOGTE)) for x in range(0, BREEDTE, TEGEL)]
    [pygame.draw.line(speelveld, pygame.Color('darkslategray'), (0, y), (BREEDTE, y)) for y in range(0, HOOGTE, TEGEL)]
    
    pygame.display.flip()
    klok.tick(SNELHEID)
