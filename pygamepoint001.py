import pygame
from glob import glob


print("""
Welcome to Pygamepoint 2020
Images 800x600
    """)

size = w, h = 800, 600
screen = pygame.display.set_mode((size))
pygame.display.set_caption("PYGAMEPOINT")

# List of filenames of png files that are the slides
# used by function load_slides that returns a list of
# surfaces with the images that will be blitted on screen
slides = glob("slides/*.png")
def load_slides():
    "Create the surfaces for the slides images"
    images = []
    for img in slides:
        images.append(pygame.image.load(img).convert())
    return images

# counter for the slides to be increased on click or key press
slides_counter = 0
def main():

    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    slides = load_slides()

    def add_counter(n):
        global slides_counter

        slides_counter += n
        if slides_counter > len(slides) - 1 or slides_counter < 0:
            slides_counter = 0

    loop = 1
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                add_counter(1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    add_counter(1)
                if event.key == pygame.K_LEFT:
                    add_counter(-1)


        screen.blit(slides[slides_counter], (0, 0))
        pygame.display.update()
        clock.tick(10)
    # when you click the x quit button
    pygame.quit()


main()

