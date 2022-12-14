import string
import pygame
import random

LOWERCASE_LETTER = string.ascii_lowercase
UPPERCASE_LETTER = string.ascii_uppercase
MAX_X_SIZE = 21
MAX_Y_SIZE = 21
COLORS= [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
MAP_TYPE=['circle', 'triangle']
LINE_COLOR= (128,128,128)

S = [[
    '.00...',
    '00....',
    '.....',
    '.....',
    '.....'],
    [
    '0....',
    '00...',
    '.0...',
    '.....',
    '.....']]

Z = [[
    '00...',
    '.00..',
    '.....',
    '.....',
    '.....'],
    [
    '.0...',
    '00...',
    '0....',
    '.....',
    '.....']]

I = [[
    '0....',
    '0....',
    '0....',
    '0....',
    '.....'],
    [
    '0000.',
    '.....',
    '.....',
    '.....',
    '.....']]

O = [[
    '00...',
    '00...',
    '.....',
    '.....',
    '.....']]

J = [[
    '0....',
    '000..',
    '.....',
    '.....',
    '.....'],
    [
    '00...',
    '0....',
    '0....',
    '.....',
    '.....'],
    [
    '000..',
    '..0..',
    '.....',
    '.....',
    '.....'],
    [
    '.0...',
    '.0...',
    '00...',
    '.....',
    '.....']]

L = [[
    '..0..',
    '000..',
    '.....',
    '.....',
    '.....'],
    [
    '0....',
    '0....',
    '00...',
    '.....',
    '.....'],
    [
    '000..',
    '0....',
    '.....',
    '.....',
    '.....'],
    [
    '00...',
    '.0...',
    '.0...',
    '.....',
    '.....']]

T = [[
    '.0...',
    '000..',
    '.....',
    '.....',
    '.....'],
    [
    '0....',
    '00...',
    '0....',
    '.....',
    '.....'],
    [
    '000..',
    '.0...',
    '.....',
    '.....',
    '.....'],
    [
    '.0...',
    '00...',
    '.0...',
    '.....',
    '.....']]
    


SHAPES=[S,Z,I,O,J,L,T]



class Grid():
    def __init__(self, x_size=MAX_X_SIZE, y_size=MAX_Y_SIZE) -> None:
        self.game_grid = [[(UPPERCASE_LETTER[y],LOWERCASE_LETTER[x],False,False) for x in range(MAX_X_SIZE)] for y in range(MAX_Y_SIZE)] 
        #print(self.game_grid)#each cell in the grid is represented with a tuple, x-coordinate, y-coordinate, availability as bool value

    def refresh_grid(self,screen,block_size,top_left):
        sx,sy = top_left
        for i,row in enumerate(self.game_grid):
            complete_row = {}
            for j,cell in enumerate(row):
                x,y,a,o = cell
                complete_row.setdefault(cell,a or o)
                #print(cell)
                if o: 
                    pygame.draw.rect(screen,(0,0,0),(sx+block_size*j,sy+block_size*i,block_size,block_size))
                    #print(cell)
                
                else:
                    pass
                    #print('_',end='')
    def draw_map(self,screen,block_size,top_left):
        sx,sy = top_left
        for i,row in enumerate(self.game_grid):
            #print('')
            for j,cell in enumerate(row):
                x,y,a,o = cell
                #print(cell)
                
                if not a:
                    #print('0',end='')
                    pygame.draw.rect(screen,(255,255,255),(sx+block_size*j,sy+block_size*i,block_size,block_size))
                else:
                    pass
                    #print('_',end='')

    def draw_circle(self):
        pixels_in_line = 0
        pixels_per_line = []

        diameter = MAX_X_SIZE
        offset = (diameter/2) - 0.5
        for i in range(diameter):
            for j in range(diameter):
                x = i - offset
                y = j - offset
                if x*x + y*y <=offset * offset +1:
                    x_coord,y_coor,a,o = self.game_grid[i][j]
                    a=True
                    self.game_grid[i][j] = x_coord,y_coor,a,o
                    pixels_in_line += 1
                else:
                    x_coord,y_coor,a,o = self.game_grid[i][j]
                    a=False
                    self.game_grid[i][j] = x_coord,y_coor,a,o
            pixels_per_line.append(pixels_in_line)
            pixels_in_line = 0
        with open('test.txt', 'w') as file:
            for row in self.game_grid:
                file.write(str(f'{row}\n'))
        #print(self.game_grid)
        #print(pixels_per_line)

    def draw_lozenge(self):
        pixels_in_line = 0
        pixels_per_line = []
        long = MAX_Y_SIZE
        offset = (long/2) - 0.5
        for x in range(MAX_X_SIZE):
            for y in range(MAX_Y_SIZE):
                if x == (MAX_X_SIZE-1)//2: #Set the long side of lozenge
                    x_coord,y_coor,a,o = self.game_grid[x][y]
                    a=True
                    self.game_grid[x][y] = x_coord,y_coor,a,o
                    pixels_in_line += 1

                elif y ==(MAX_Y_SIZE-1)//2: #sets the short diagonal
                    x_coord,y_coor,a,o = self.game_grid[x][y]
                    a=True
                    self.game_grid[x][y] = x_coord,y_coor,a,o
                    pixels_in_line += 1

                elif y>=MAX_X_SIZE//2 and x<=MAX_Y_SIZE//2 and x>=y-MAX_X_SIZE//2: #sets the upper right quadrant
                    x_coord,y_coor,a,o = self.game_grid[x][y]
                    a=True
                    self.game_grid[x][y] = x_coord,y_coor,a,o
                    pixels_in_line += 1

                elif y<=MAX_X_SIZE//2 and x<=MAX_Y_SIZE//2 and x>=(MAX_X_SIZE//2)-y: #sets the upper left quadrant
                    x_coord,y_coor,a,o = self.game_grid[x][y]
                    a=True
                    self.game_grid[x][y] = x_coord,y_coor,a,o
                    pixels_in_line += 1
                elif y>=MAX_Y_SIZE//2 and x>=MAX_Y_SIZE//2 and y<=(3/2) * MAX_X_SIZE-x:#sets the lower right quadrant
                    x_coord,y_coor,a,o = self.game_grid[x][y]
                    a=True
                    self.game_grid[x][y] = x_coord,y_coor,a,o
                    pixels_in_line += 1
                elif y<=MAX_X_SIZE//2 and x>=MAX_Y_SIZE//2 and  y>=x - MAX_Y_SIZE//2:# sets the lower left quadrant
                    x_coord,y_coor,a,o = self.game_grid[x][y]
                    a=True
                    self.game_grid[x][y] = x_coord,y_coor,a,o
                    pixels_in_line += 1
                else:
                    x_coord,y_coor,a,o = self.game_grid[x][y]
                    a=False
                    self.game_grid[x][y] = x_coord,y_coor,a,o
                '''

                

                    '''
            pixels_per_line.append(pixels_in_line)
            pixels_in_line = 0
        with open('test.txt', 'w') as file:
            for row in self.game_grid:
                file.write(str(f'{row}\n'))       

    def draw_triangle(self):
        pixels_in_line = 0
        pixels_per_line = []
        long = MAX_Y_SIZE
        offset = (long/2) - 0.5
        for x in range(0,MAX_X_SIZE):
            for y in range(MAX_Y_SIZE):
                if x == MAX_X_SIZE-1: #Set the base of the triangle
                    x_coord,y_coor,a,o = self.game_grid[x][y]
                    a=True
                    self.game_grid[x][y] = x_coord,y_coor,a,o
                    pixels_in_line += 1
                elif y< x and y>MAX_X_SIZE-x-1:
                    self.game_grid[x][y]
                    x_coord,y_coor,a,o = self.game_grid[x][y]
                    a=True
                    self.game_grid[x][y] = x_coord,y_coor,a,o
                    pixels_in_line += 1
                else:
                    x_coord,y_coor,a,o = self.game_grid[x][y]
                    a=False
                    self.game_grid[x][y] = x_coord,y_coor,a,o
            pixels_per_line.append(pixels_in_line)
            pixels_in_line = 0

    def draw_grid(self, screen, row:int, col:int, top_left:tuple, play_dimension, block_size): 
        sx,sy = top_left
        pw,ph = play_dimension  
        for i in range(row):
            font = pygame.font.SysFont("comicsans",11)
            label_row = font.render(UPPERCASE_LETTER[i],1,(255,255,255))
            screen.blit(label_row,(sx- block_size, sy+i*block_size+10))
            pygame.draw.line(screen, LINE_COLOR,(sx, sy+i*block_size), (sx + pw, sy + i * block_size)) #horizontal lines
            for j in range(col):
               label_col = font.render(LOWERCASE_LETTER[j],1,(255,255,255))
               screen.blit(label_col, (sx+10 + j * block_size, sy-block_size))
               pygame.draw.line(screen, LINE_COLOR, (sx + j * block_size, sy), (sx + j * block_size, sy + ph))



class Piece():
        def __init__(self,color,shape,x,y):
            self.rotation = 0
            self.shape = shape
            self.color = color
            self.x = x
            self.y = y
            '''
            self.grid_coordinates = []
            for i,format in enumerate(self.shape):
                for j,row in enumerate(format):
                    for k,block in enumerate(row):
                        if block: self.grid_coordinates.append([]) #starting top left
'''

#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
if __name__=='__main__':

    pass

Grid()