import pygame

pygame.init()

image = r"C:\Users\FranciscoRodrigues\Documents\ctf\braille.png"
img = pygame.image.load(image)

size = img.get_size()
##surface = pygame.display.set_mode(size)
##pygame.display.set_caption("Braille")
##
##surface.blit(img, [0, 0])
##pygame.display.flip()

x_off = 7
y_off = -2
width = 15
height = 14.5

array = {}
c = 0
for y in range(0, int(size[1]/height), 3):
    for x in range(1, (size[0]//width), 2):
        for yy in range(3):
            for xx in range(2):
                array[y//3*198+ x*3 + yy*2 + xx -3] = 0
                p1 = sum(img.get_at([(xx+x)*width+2, int((yy+y)*height)+5]))
                p2 = sum(img.get_at([(xx+x)*width, int((yy+y)*height)+3]))
                p3 = sum(img.get_at([(xx+x)*width, int((yy+y)*height+6)]))
                #surface.set_at([(xx+x)*width+2, int((yy+y)*height)+5], [255, 255, 255])
                #surface.set_at([(xx+x)*width, int((yy+y)*height)+3], [255, 255, 255])
                #surface.set_at([(xx+x)*width, int((yy+y)*height+6)], [255, 255, 255])
                #print((p1+p2+p3)//3**2)
                if (p1+p2+p3)//3**2 > 150:
                    array[y//3*198+ x*3 + yy*2 + xx -3] = 1
                    #pygame.draw.circle(surface, [0, 255, 0], [(xx+x)*width, int((yy+y)*height)], 3)

strings = []
for i in range(0, len(array), 6):
    strings.append("")
    for j in range(0, 6):
        strings[i//6] += str(array[i+j])
        

#for i in range(size[0]//15):
#    pygame.draw.line(surface, [255, 255, 255], [x_off+i*width, 0], [x_off+i*width, size[1]], 1)

#for i in range(int(size[1]/14.5)+2):
#    pygame.draw.line(surface, [255, 255, 255], [0, y_off+height*i], [size[0], y_off+height*i], 1)
##
##pygame.display.flip()
##
##while True:
##    
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            quit()
