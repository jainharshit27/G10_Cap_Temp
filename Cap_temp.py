import pygame

class Hurdle:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
    
    def draw_hurdle(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)
    
    def paste_image(self, image):
        screen.blit(image, (self.rect.x, self.rect.y-14))

class Thief:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
    
    def draw_thief(self, surface):
        pygame.draw.rect(surface, (31,40,45), self.rect)
    
    def paste_image(self, image):
        screen.blit(image, self.rect)
        
pygame.init()
screen = pygame.display.set_mode((400, 400))
# Declare a variable for font

hurdle_1 = Hurdle(0, 200, 200, 2)
hurdle_2 = Hurdle(200, 198, 200, 2)

hurdle_img = pygame.image.load("hurdle.png")
hurdle_img = pygame.transform.scale(hurdle_img, (200,25))
# Declare a variable for changing hurdle position

thief = Thief(10, 380, 15, 15)
thief_x_change = 0
# Declare a variable for changing y coordinate

jewel = pygame.Rect(350, 10, 40, 40)
jewel_image = pygame.image.load("jewel.png")
jewel_image = pygame.transform.scale(jewel_image, (50,50))

while True:
    screen.fill((255,249,238))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    thief_x_change = -1
                # Declare other key based movements
                
        if event.type == pygame.KEYUP:
            thief_x_change = 0
            # Set value for variable which affects y coordinate
                    
    thief.rect.x += thief_x_change
    # Modify the y position of thief as well
    
    # Move the hurdles
    
    hurdle_1.paste_image(hurdle_img)
    hurdle_2.paste_image(hurdle_img)
    
    thief.draw_thief(screen)
    
    screen.blit(jewel_image, jewel)
    
    # Add Collision with Hurdles
    
    if thief.rect.colliderect(jewel):
        # Add message for winning the game
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    pygame.time.delay(10)
