import pygame
import game
import random
import os

#initializing pygame and music
pygame.init()
music = 'arcade_music.mp3'
pygame.mixer.music.load(music)
pygame.mixer.music.play(loops=-1)

#initializing the grid and score tracker
grid = game.Grid()
#score = game.Score()

# game window dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_DIMENSION = (SCREEN_WIDTH,SCREEN_HEIGHT)

#inside window create grid dimensions
play_width = 630
play_height = 630
PLAY_DIMENSION = (play_width,play_height)
block_size = 30
top_left_x = (SCREEN_WIDTH-play_width)//2
top_left_y = (SCREEN_HEIGHT - play_height) //2
top_left=(100,100)

#creating window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #win or surface
pygame.display.set_caption("Main Menu")

#game modes & states
game_modes = {"main_menu":0, "game":1, "pause":2,"game_select":3, 'map_select':4}
game_mode = game_modes["main_menu"]
menu_states = {"pause_menu":0, "options":1, "v_settings":2, "a_settings":3, "key_bindings":4}
menu_state = menu_states["pause_menu"]

#define fonts
#fonts are available in the fonts folder. edit following line to change fonts
font = pygame.font.Font(r".\fonts\Minecrafter.Reg.ttf", 40)
small_font = pygame.font.SysFont("comicsans", 15)

#define colours
TEXT_COL = (204, 251, 229)  #offset of white
BG_COLOR = (0, 81, 182) #blue background

#load button images
#button image are found in images folder. download images there and edit following lines to change images
#TODO: Build function for mixing or muting audio / changing background fill
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
video_img = pygame.image.load('images/button_video.png').convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()

#create button instances
#adjusted the coordinate in f(x) of text so that the buttons display in the middle of the screen
resume_button = game.Button((SCREEN_WIDTH//2)-100, (SCREEN_HEIGHT//2)-200, resume_img, 1)
options_button = game.Button((SCREEN_WIDTH//2)-110, (SCREEN_HEIGHT//2)-100, options_img, 1)
quit_button = game.Button((SCREEN_WIDTH//2)-70, SCREEN_HEIGHT//2, quit_img, 1)
#video_button = game.Button((SCREEN_WIDTH//2)-200, (SCREEN_HEIGHT//2)-200, video_img, 1)
#audio_button = game.Button((SCREEN_WIDTH//2)-200, (SCREEN_HEIGHT//2)-100, audio_img, 1)
#keys_button = game.Button((SCREEN_WIDTH//2)-175, (SCREEN_HEIGHT//2), keys_img, 1)
back_button = game.Button((SCREEN_WIDTH//2)-100, (SCREEN_HEIGHT//2)+100, back_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))


def spawn_piece(piece,surface):
  sx = piece.x
  sy = piece.y
  #current_piece.x=
  #current_piece.y=top_left_y + play_height/2 
  shape = piece.shape[piece.rotation % len(piece.shape)]
  for a, line1 in enumerate(shape):
      row = list(line1)
      for b, column in enumerate(row):
          if column == '0':
            pygame.draw.rect(surface, piece.color, (sx + b*block_size+50, sy + a*block_size, block_size, block_size), 0)
  


def get_shape():
  return game.Piece(color=random.choice(game.COLORS),shape=random.choice(game.SHAPES),x=top_left_x+ block_size*10,y=top_left_y + block_size*10 )

def draw_next_shapes(next_shape1,surface):
  font = pygame.font.SysFont("comicsans", 11)
  label = font.render('Press arrow keys to change and ENTER to select', 1, (255,255,255))
  sx = top_left_x + play_width 
  sy = top_left_y + play_height/2 - 200
  shape = next_shape1.shape[next_shape1.rotation % len(next_shape1.shape)]
  for a, line1 in enumerate(shape):
      row = list(line1)
      for b, column in enumerate(row):
          if column == '0':
              pygame.draw.rect(surface, next_shape1.color, (sx +b*block_size, sy + a*block_size, block_size, block_size), 0)
  
  surface.blit(label, (sx-50, sy- 50))

def place_piece(grid,piece):
  #print(piece.x)
  #print(piece.y)
  shape = piece.shape[piece.rotation]
  locked_blocks = set()
  sy= (piece.y-100)//30
  sx = (piece.x-50)//30
  #print(sx)
  #print(sy)
  for j,row in enumerate(shape):
    sy+=j
    #print(f'sy:{sy}')
    #print(f'j:{j}')
    for k,block in enumerate(row):
      sx+=k
      #print(f'sx:{sx}')
      #print(f'k:{k}')
      if block == '0':
        col,row,available,occupied = grid.game_grid[sy][sx]
        if available and not occupied:
          occupied = True
          grid.game_grid[sy][sx] = col,row,available,occupied
          #print(grid.game_grid[sy][sx])
          #print(sx)
          #print(sy)
          #print(grid.game_grid[sx][sy])
        else:
          pass

      sx = (piece.x-50)//30
    sy= (piece.y-100)//30
    #print(sy)
  #print(grid.game_grid[sx][sy])


  #locked_blocks.add()

  #grid.block()


def placing_piece_prompt(current_piece):
  current_piece.color = (125,125,125)
  font = pygame.font.SysFont("comicsans", 11)
  label = font.render(f'Place piece with arrows. Press Enter to confrim. {tries}/3',1,TEXT_COL)
  screen.blit(label, (top_left_x+play_width-50, top_left_y+play_height- 50))
#getting pieces

#print(current_piece.shape)
#print(current_piece.color)
#If strategy mode

current_piece=None
placing_piece = False
tries = 3


#game loop
run = True
while run:
  screen.fill(BG_COLOR)

  #check if game is paused
  if game_mode == game_modes["pause"]:
    #check   state
    if menu_state == menu_states["pause_menu"]:
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_mode = game_modes["game"]
      if options_button.draw(screen):
        menu_state = menu_states["options"]
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == menu_states["options"]:
      #draw the different options buttons
      if video_button.draw(screen):
        menu_state = menu_states["v_settings"]
        print("Video Settings")
      if audio_button.draw(screen):
        menu_state = menu_states["a_settings"]
        print("Audio Settings")
      if keys_button.draw(screen):
        menu_state = menu_states["key_bindings"]
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = menu_states["pause_menu"]
      
  elif game_mode == game_modes["game"]:
    grid.refresh_grid(screen, block_size, top_left)
    #draw_text(f"SCORE: {score.score}",pygame.font.SysFont('comicsans',15),TEXT_COL,SCREEN_WIDTH//4 + 500,SCREEN_HEIGHT//2+30)
    grid.draw_grid(screen,21,21,top_left,PLAY_DIMENSION,block_size)
    if map == 'triangle':
      grid.draw_triangle()
    elif map =='circle':
      grid.draw_circle()
    elif map =='lozenge':
      grid.draw_lozenge()
    else:
      raise "Couldnt choose map"
    grid.draw_map(screen,block_size,top_left)
    draw_next_shapes(next_piece, screen)
    if current_piece:
      spawn_piece(current_piece,screen)
      placing_piece_prompt(current_piece)
      placing_piece_prompt(current_piece)


  
  elif game_mode == game_modes["game_select"]:
    draw_text("SELECT GAME MODE:",font,TEXT_COL,SCREEN_WIDTH//4+50,SCREEN_HEIGHT//2-50)
    draw_text("S)trategy: Player can choose between all the shapes at each round",pygame.font.SysFont('comicsans',15),TEXT_COL,SCREEN_WIDTH//4,SCREEN_HEIGHT//2+30 )
    draw_text("H)ardcore: Player can only choose between three random shapes at each round",pygame.font.SysFont('comicsans',15),TEXT_COL,SCREEN_WIDTH//4,SCREEN_HEIGHT//2+60)
    draw_text("Please press key S or H", pygame.font.SysFont('comicsans',15),TEXT_COL,SCREEN_WIDTH//4 +150,SCREEN_HEIGHT//2 +100)
  
  elif game_mode == game_modes["map_select"]:
    draw_text("SELECT A MAP",font,TEXT_COL,SCREEN_WIDTH//4+50,SCREEN_HEIGHT//2-50)
    draw_text("T)riangle", pygame.font.SysFont('comicsans',15),TEXT_COL,SCREEN_WIDTH//4+100,SCREEN_HEIGHT//2+30)
    draw_text("L)ozenge",pygame.font.SysFont('comicsans',15),TEXT_COL,SCREEN_WIDTH//4+100,SCREEN_HEIGHT//2+60)
    draw_text("C)ircle", pygame.font.SysFont('comicsans',15),TEXT_COL,SCREEN_WIDTH//4+100,SCREEN_HEIGHT//2 +100)


  elif game_mode == game_modes["main_menu"]:
    draw_text("Press SPACE to start", font, TEXT_COL, SCREEN_WIDTH//4, SCREEN_HEIGHT//2)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_p:
        game_mode = game_modes["pause"]
        menu_state = menu_states["pause_menu"]

      if event.key == pygame.K_SPACE:
        if game_mode == game_modes["main_menu"]:
          game_mode = game_modes["game_select"]
      if event.key == pygame.K_s:
        if game_mode == game_modes["game_select"]:
            rule = 'strategy'
            next_piece = get_shape()
            game_mode = game_modes['map_select']
      elif event.key == pygame.K_h:
        if game_mode == game_modes["game_select"]:
            game_mode = game_modes['map_select']
            rule = 'hardcore'
            idx = 0
            piece1 = get_shape()
            piece2 = get_shape()
            piece3 = get_shape()
            pieces = [piece1,piece2,piece3]
            next_piece = pieces[idx%len(pieces)]
      if event.key == pygame.K_t:
        if game_mode == game_modes['map_select']:
          map = "triangle"
          game_mode = game_modes['game']
      if event.key == pygame.K_l:
        if game_mode == game_modes['map_select']:
          map = "lozenge"
          game_mode = game_modes['game']
      if event.key == pygame.K_c:
        if game_mode == game_modes['map_select']:
          map = "circle"
          game_mode = game_modes['game']
      if event.key == pygame.K_LEFT:
        if game_mode == game_modes['game'] and not placing_piece:
          i=0
          if rule == 'strategy':
            next_piece = get_shape()
          elif rule == 'hardcore':
            idx -= 1
            next_piece = pieces[idx%len(pieces)]
        if placing_piece:
          current_piece.x -= block_size

      if event.key == pygame.K_RIGHT:
        if game_mode == game_modes['game'] and not placing_piece:
          i=0
          if rule == 'strategy':
            next_piece = get_shape()
          elif rule == 'hardcore':
            idx += 1
            next_piece = pieces[idx%len(pieces)]
          else:
            raise "error determining rule"
        if placing_piece:
          current_piece.x += block_size
      if event.key == pygame.K_DOWN:
        if placing_piece:
          current_piece.y += block_size
      if event.key == pygame.K_UP:
        if placing_piece:
          current_piece.y -= block_size

      if event.key == pygame.K_RETURN:
        if placing_piece:
          place_piece(grid,current_piece)
          placing_piece=False
        elif game_mode == game_modes['game']:
          current_piece = next_piece
          placing_piece= True

    if event.type == pygame.QUIT:
      run = False
  pygame.display.update()


pygame.quit()