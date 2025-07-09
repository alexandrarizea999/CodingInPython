import pygame
import time
import random
pygame.font.init()

# Creating the window
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# Set the background
BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH  = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, stars):
  # Draw the image
  WIN.blit(BG, (0, 0))

  # Render the time
  time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
  WIN.blit((time_text), (10, 10))

  # Draw the player
  pygame.draw.rect(WIN, "yellow", player)

  # Draw the stars
  for star in stars:
    pygame.draw.rect(WIN, "white", star)

  # Refresh the display
  pygame.display.update()

# Main logic of the game
def main():
  run = True

  # The coordonates for the character
  player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

  # Setup a clock
  clock = pygame.time.Clock()

  start_time = time.time()
  elapsed_time = 0

  star_add_increment = 2000
  # When we should add another star
  star_count = 0

  stars = []
  hit = False

  while run:
    # Delay the while loop 60 times/sec
    star_count += clock.tick(60)
    # Keeping track of time
    elapsed_time = time.time() - start_time

    if star_count > star_add_increment:
      for _ in range(5):
        star_x = random.randint(0, WIDTH-STAR_WIDTH)
        star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
        stars.append(star)

      star_add_increment = max(200, star_add_increment - 50)
      star_count = 0

    # Check if the user wants to quit the game
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        break

    # Moving the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
      player.x -= PLAYER_VEL
    if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
      player.x += PLAYER_VEL

    # Move the stars
    for star in stars[:]:
      star.y += STAR_VEL
      if star.y > HEIGHT:
        stars.remove(star)
      elif star.y >= player.y and star.colliderect(player):
        stars.remove(star)
        hit = True
        break

    if hit:
      lost_text = FONT.render("You Lost!", 1, "yellow")
      WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
      pygame.display.update()
      pygame.time.delay(4000)
      break

    draw(player, elapsed_time, stars)

  pygame.QUIT

if __name__ == '__main__':
  main()
