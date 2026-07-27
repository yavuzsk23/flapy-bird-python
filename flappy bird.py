import pygame
import random

# --- SETTINGS ---
WIDTH = 400
HEIGHT = 600
GRAVITY = 0.25
JUMP_STRENGTH = -6.5
PIPE_SPEED = 3
PIPE_GAP = 150   # Vertical gap between pipes
PIPE_FREQUENCY = 1500  # Time interval for new pipes (ms)

# Colors
BLUE = (113, 197, 207)   # Sky
YELLOW = (255, 255, 0)   # Bird
GREEN = (115, 191, 46)   # Pipe
BROWN = (222, 216, 149)  # Ground

class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
        self.size = 30

    def move(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def jump(self):
        self.velocity = JUMP_STRENGTH

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, [self.x, self.y, self.size, self.size])
        # Eye and beak details
        pygame.draw.rect(screen, (0, 0, 0), [self.x + 20, self.y + 5, 5, 5])
        pygame.draw.rect(screen, (255, 165, 0), [self.x + 25, self.y + 15, 10, 5])

class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 60
        self.top_height = random.randint(50, HEIGHT - PIPE_GAP - 50)
        self.bottom_y = self.top_height + PIPE_GAP
        self.passed = False

    def move(self):
        self.x -= PIPE_SPEED

    def draw(self, screen):
        # Top Pipe
        pygame.draw.rect(screen, GREEN, [self.x, 0, self.width, self.top_height])
        # Bottom Pipe
        pygame.draw.rect(screen, GREEN, [self.x, self.bottom_y, self.width, HEIGHT - self.bottom_y])
        # Pipe Caps
        pygame.draw.rect(screen, (50, 100, 20), [self.x - 5, self.top_height - 20, self.width + 10, 20])
        pygame.draw.rect(screen, (50, 100, 20), [self.x - 5, self.bottom_y, self.width + 10, 20])

def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Cyberia Flappy Bird")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 32, bold=True)

    bird = Bird()
    pipes = []
    
    # Timer (for pipe generation)
    PIPE_EVENT = pygame.USEREVENT
    pygame.time.set_timer(PIPE_EVENT, PIPE_FREQUENCY)

    score = 0
    game_active = True

    while True:
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_active:
                        bird.jump()
                    else:
                        # Reset game
                        bird = Bird()
                        pipes = []
                        score = 0
                        game_active = True
            
            if event.type == PIPE_EVENT and game_active:
                pipes.append(Pipe(WIDTH))

        if game_active:
            bird.move()
            
            for pipe in pipes[:]:
                pipe.move()
                
                # Collision Check
                bird_rect = pygame.Rect(bird.x, bird.y, bird.size, bird.size)
                top_pipe_rect = pygame.Rect(pipe.x, 0, pipe.width, pipe.top_height)
                bottom_pipe_rect = pygame.Rect(pipe.x, pipe.bottom_y, pipe.width, HEIGHT - pipe.bottom_y)

                if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect):
                    game_active = False
                
                # Score Increase
                if not pipe.passed and pipe.x + pipe.width < bird.x:
                    score += 1
                    pipe.passed = True
                
                # Remove pipes that leave the screen
                if pipe.x < -pipe.width:
                    pipes.remove(pipe)

            # Ground or ceiling check
            if bird.y <= 0 or bird.y + bird.size >= HEIGHT:
                game_active = False

        # Draw everything
        for pipe in pipes:
            pipe.draw(screen)
        
        bird.draw(screen)
        
        # Score display
        score_text = font.render(str(score), True, (255, 255, 255))
        screen.blit(score_text, (WIDTH // 2 - 10, 50))

        if not game_active:
            message = font.render("GAME OVER!", True, (255, 0, 0))
            retry = font.render("Press SPACE to Retry", True, (0, 0, 0))
            screen.blit(message, (WIDTH // 2 - 80, HEIGHT // 2 - 50))
            screen.blit(retry, (WIDTH // 2 - 110, HEIGHT // 2 + 10))

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main_loop()
