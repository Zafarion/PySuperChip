import pygame
import sys
import os
import winsound
from random import seed
from random import randint
import time as t

pygame.init()
seed(1)

LoResFontSet = [(0b11110000),
                (0b10010000),
                (0b10010000),
                (0b10010000),
                (0b11110000),

                (0b00100000),
                (0b01100000),
                (0b00100000),
                (0b00100000),
                (0b01110000),

                (0b11110000),
                (0b00010000),
                (0b11110000),
                (0b10000000),
                (0b11110000),
               
                (0b11110000),
                (0b00010000),
                (0b11110000),
                (0b00010000),
                (0b11110000),
               
                (0b10010000),
                (0b10010000),
                (0b11110000),
                (0b00010000),
                (0b00010000),
               
                (0b11110000),
                (0b10000000),
                (0b11110000),
                (0b00010000),
                (0b11110000),

                (0b11110000),
                (0b10000000),
                (0b11110000),
                (0b10010000),
                (0b11110000),
               
                (0b11110000),
                (0b00010000),
                (0b00100000),
                (0b01000000),
                (0b01000000),

                (0b11110000),
                (0b10010000),
                (0b11110000),
                (0b10010000),
                (0b11110000),

                (0b11110000),
                (0b10010000),
                (0b11110000),
                (0b00010000),
                (0b11110000),

                (0b11110000),
                (0b10010000),
                (0b11110000),
                (0b10010000),
                (0b10010000),
 
                (0b11100000),
                (0b10010000),
                (0b11100000),
                (0b10010000),
                (0b11100000),
                
                (0b11110000),
                (0b10000000),
                (0b10000000),
                (0b10000000),
                (0b11110000),
             
                (0b11100000),
                (0b10010000),
                (0b10010000),
                (0b10010000),
                (0b11100000),

                (0b11110000),
                (0b10000000),
                (0b11110000),
                (0b10000000),
                (0b11110000),

                (0b11110000),
                (0b10000000),
                (0b11110000),
                (0b10000000),
                (0b10000000)]

HiResFontSet = [(0b11111111),
                (0b11111111),
                (0b11000011),
                (0b11000011),
                (0b11000011),
                (0b11000011),
                (0b11000011),
                (0b11000011),
                (0b11111111),
                (0b11111111),

                (0b00011000),
                (0b00111000),
                (0b01111000),
                (0b11111000),
                (0b00011000),
                (0b00011000),
                (0b00011000),
                (0b00011000),
                (0b11111111),
                (0b11111111),

                (0b11111111),
                (0b11111111),
                (0b00000011),
                (0b00000011),
                (0b11111111),
                (0b11111111),
                (0b11000000),
                (0b11000000),
                (0b11111111),
                (0b11111111),

                (0b11111111),
                (0b11111111),
                (0b00000011),
                (0b00000011),
                (0b11111111),
                (0b11111111),
                (0b00000011),
                (0b00000011),
                (0b11111111),
                (0b11111111),
               
                (0b11000011),
                (0b11000011),
                (0b11000011),
                (0b11000011),
                (0b11111111),
                (0b11111111),
                (0b00000011),
                (0b00000011),
                (0b00000011),
                (0b00000011),

                (0b11111111),
                (0b11111111),
                (0b11000000),
                (0b11000000),
                (0b11111111),
                (0b11111111),
                (0b00000011),
                (0b00000011),
                (0b11111111),
                (0b11111111),

                (0b11111111),
                (0b11111111),
                (0b11000000),
                (0b11000000),
                (0b11111111),
                (0b11111111),
                (0b11000011),
                (0b11000011),
                (0b11111111),
                (0b11111111),

                (0b11111111),
                (0b11111111),
                (0b00000011),
                (0b00000110),
                (0b00001100),
                (0b00011000),
                (0b00110000),
                (0b01100000),
                (0b11000000),
                (0b11000000),

                (0b11111111),
                (0b11111111),
                (0b11000011),
                (0b11000011),
                (0b11111111),
                (0b11111111),
                (0b11000011),
                (0b11000011),
                (0b11111111),
                (0b11111111),

                (0b11111111),
                (0b11111111),
                (0b11000011),
                (0b11000011),
                (0b11111111),
                (0b11111111),
                (0b00000011),
                (0b00000011),
                (0b11111111),
                (0b11111111)]

keys = (pygame.K_x, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_z, pygame.K_c, pygame.K_4, pygame.K_r, pygame.K_f, pygame.K_v)

#Registers
V = [0] * 16
I = 0
PC = 0x200
DT = 0
ST = 0
SP = 0
Stack = [0] * 16
Flag = [0] * 8

#Control variables
cycles = 0
frame = 0
erasedPixels = []
scrolledRight, scrolledLeft, scrolledDown = 0, 0, 0
crashed = False

black = (0, 0, 0)
turquoise = (66, 233, 244)
white = (255, 255, 255)
pixelColor = (black, turquoise)
width, height = 64, 32
screen = pygame.display.set_mode((1024, 512))
frame_buffer = pygame.Surface((width + 30, height + 30))
game_surface = pygame.Surface((width, height))
pygame.display.set_caption("PySuperChip v1.0")
font = pygame.font.SysFont("Retro.ttf", 20)

screen.blit(font.render('Click the ROM filename to load (max 66 files in the dir):', True, turquoise), (0, 0))
dir = os.listdir()
list_x_axis = []
list_y_axis = []
x_axis = 0
y_axis = 15
for pos in range(len(dir)):
    text = font.render(dir[pos], True, white)
    screen.blit(text, (x_axis, y_axis))
    list_x_axis.append(x_axis)
    list_y_axis.append(y_axis)
    y_axis += 15
    if pos == 32:
        x_axis = 512
        y_axis = 15

pygame.display.flip()

click = False
while not click:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        for pos in range(len(dir)):
            if (mouse[0] <= list_x_axis[pos] + 512) and (mouse[1] >= list_y_axis[pos] and mouse[1] < list_y_axis[pos] + 15):
                ram = bytearray(open(dir[pos], "rb").read()) #Loading ROM into RAM
                click = True
                break

screen.fill(black)
screen.blit(font.render('Choose GAME SPEED. 8 is the approximate speed in the COSMAC VIP. Newer games and SCHIP games may need much faster speeds:', True, turquoise), (0, 0))
screen.blit(font.render('8 CPU instructions per frame', True, white), (0, 15))
screen.blit(font.render('16 CPU instructions per frame', True, white), (0, 30))
screen.blit(font.render('24 CPU instructions per frame', True, white), (0, 45))
screen.blit(font.render('32 CPU instructions per frame', True, white), (0, 60))
screen.blit(font.render('40 CPU instructions per frame', True, white), (0, 75))
screen.blit(font.render('48 CPU instructions per frame', True, white), (0, 90))
screen.blit(font.render('56 CPU instructions per frame', True, white), (0, 105))
screen.blit(font.render('64 CPU instructions per frame', True, white), (0, 120))
pygame.display.flip()

click = False
while not click:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        for pos in range(15, 135, 15):
            if (mouse[1] >= pos and mouse[1] < pos + 15):
                click = True
                break

match pos:
    case 15: speed = 8
    case 30: speed = 16
    case 45: speed = 24
    case 60: speed = 32
    case 75: speed = 40
    case 90: speed = 48
    case 105: speed = 56
    case 120: speed = 64

screen.fill(black)
screen.blit(font.render('Choose plataform bellow. Some games only run properly with the correct options:', True, turquoise), (0, 0))
screen.blit(font.render('ORIGINAL CHIP8 (VF Reset ON, Memory ON, Shifting OFF, Jumping OFF)', True, white), (0, 15))
screen.blit(font.render('CHIP48 & SCHIP (VF Reset OFF, Memory ON-1, Shifting ON, Jumping ON)', True, white), (0, 30))
screen.blit(font.render('SUPER CHIP 1.1 (VF Reset OFF, Memory OFF, Shifting ON, Jumping ON)', True, white), (0, 45))
screen.blit(font.render('XO-CHIP            (VF Reset OFF, Memory ON, Shifting OFF, Jumping OFF)', True, white), (0, 60))
pygame.display.flip()

click = False
while not click:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        for pos in range(15, 75, 15):
            if (mouse[1] >= pos and mouse[1] < pos + 15):
                click = True
                break

match pos:
    case 15: quirks = 0
    case 30: quirks = 1
    case 45: quirks = 2
    case 60: quirks = 3


#Inserting font sets in RAM and extending it
for pos in range(512 - len(LoResFontSet) - len(HiResFontSet)):
    ram.insert(0, 0)
ram = bytearray(LoResFontSet) + bytearray(HiResFontSet) + ram
ram.extend([0] * (4096 - len(ram)))

def drawPixel():

    global collision
    
    ##print(x, y, row, column)
    ##print(x + 15 + column, y + 15 + row)
    oldPixel = pixelColor.index(frame_buffer.get_at(((x + 15 + column), (y + 15 + row))))
    newPixel = ram[I + row] >> (7 - column) & 1
    if oldPixel and newPixel and (x + column) <= width and (y + row) <= height:
        erasedPixels.append([x + column, y + row])
        collision = True
    frame_buffer.set_at(((x + 15 + column), (y + 15 + row)), pixelColor[oldPixel ^ newPixel])
        
def natural(number):
    if number < 0: return 0
    else: return number

#Main Loop
while not crashed:
    time = t.time()
    match ram[PC] >> 4:
        case 0x0:
            match ram[PC + 1]:
                case 0xE0: # CLS
                    frame_buffer.fill(black)
                    PC += 2
                    #print('CLS')
                case 0xEE: # RET
                    SP -= 1
                    PC = Stack[SP]
                    #print('RET', PC)
                    PC += 2
                case 0xFB:
                    #print('Scroll display 4 pixels right')
                    frame_buffer.scroll(4, 0)
                    PC += 2
                case 0xFC:
                    #print('Scroll display 4 pixels left')
                    frame_buffer.scroll(-4, 0)
                    PC += 2
                case 0xFD:
                    print('Quit')
                    pygame.quit()
                    sys.exit()
                case 0xFE:
                    print('Changed to 64 x 32 resolution')
                    width, height = 64, 32
                    frame_buffer = pygame.Surface((width + 30, height + 30))
                    game_surface = pygame.Surface((width, height))
                    PC += 2
                case 0xFF:
                    print('Changed to 128 x 64 resolution')
                    width, height = 128, 64
                    frame_buffer = pygame.Surface((width + 30, height + 30))
                    game_surface = pygame.Surface((width, height))
                    PC += 2
                case _:
                    #print('Scroll ' + str(ram[PC + 1] & 0x0F) + ' pixels down')
                    frame_buffer.scroll(0, ram[PC + 1] & 0x0F)
                    PC += 2
                
        case 0x1: # JP addr
            PC = ((ram[PC] & 0x0F) << 8) + ram[PC + 1]
            #print('JP', PC)
        case 0x2: # CALL addr
            Stack[SP] = PC
            SP += 1
            PC = ((ram[PC] & 0x0F) << 8) + ram[PC + 1]
            #print('CALL', PC)
        case 0x3: # SE Vx, byte
            #print('SE V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ', ' + str(ram[PC + 1]))
            if V[ram[PC] & 0x0F] == ram[PC + 1]:
                PC += 2
            PC += 2
        case 0x4: # SNE Vx, byte
            #print('SNE V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ', ' + str(ram[PC + 1]))
            if V[ram[PC] & 0x0F] != ram[PC + 1]:
                PC += 2
            PC += 2
        case 0x5: # SE Vx, Vy
            #print('SE V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ', V' + str(V[ram[PC + 1] >> 4]) + '=' + str(V[ram[PC + 1] >> 4]))
            if V[ram[PC] & 0x0F] == V[ram[PC + 1] >> 4]:
                PC += 2
            PC += 2
        case 0x6: # LD Vx, byte
            #print('LD V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) +', ' + str(ram[PC + 1]))
            V[ram[PC] & 0x0F] = ram[PC + 1]
            PC += 2
        case 0x7: # ADD Vx, byte
            #print('ADD V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ', ' + str(ram[PC + 1]))
            V[ram[PC] & 0x0F] = (V[ram[PC] & 0x0F] + ram[PC + 1]) & 0xFF
            PC += 2
        case 0x8:
            match ram[PC + 1] & 0x0F: 
                case 0x0: # LD Vx, Vy
                    #print('LD V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ', V' + str(ram[PC + 1] >> 4) + '=' + str(V[ram[PC + 1] >> 4]))
                    V[ram[PC] & 0x0F] = V[ram[PC + 1] >> 4]
                    PC += 2
                case 0x1: #OR Vx, Vy
                    #print('OR V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ', V' + str(ram[PC + 1] >> 4) + '=' + str(V[ram[PC + 1] >> 4]))
                    V[ram[PC] & 0x0F] |= V[ram[PC + 1] >> 4]
                    if quirks == 0: V[0xF] = 0
                    PC += 2
                case 0x2: #AND Vx, Vy
                    #print('AND V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ', V' + str(ram[PC + 1] >> 4) + '=' + str(V[ram[PC + 1] >> 4]))
                    V[ram[PC] & 0x0F] &= V[ram[PC + 1] >> 4]
                    if quirks == 0: V[0xF] = 0
                    PC += 2
                case 0x3: #XOR Vx, Vy
                    #print('XOR V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ', V' + str(ram[PC + 1] >> 4) + '=' + str(V[ram[PC + 1] >> 4]))
                    V[ram[PC] & 0x0F] ^= V[ram[PC + 1] >> 4]
                    if quirks == 0: V[0xF] = 0
                    PC += 2
                case 0x4: #ADD Vx, Vy
                    #print('ADD V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ', V' + str(ram[PC + 1] >> 4) + '=' + str(V[ram[PC + 1] >> 4]))
                    temp = V[ram[PC] & 0x0F]
                    V[ram[PC] & 0x0F] = (V[ram[PC] & 0x0F] + V[ram[PC + 1] >> 4]) & 0xFF
                    if temp + V[ram[PC + 1] >> 4] > 255: V[0xF] = 1
                    else: V[0xF] = 0
                    PC += 2
                case 0x5: #SUB Vx, Vy
                    #print('SUB V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ', V' + str(ram[PC + 1] >> 4) + '=' + str(V[ram[PC + 1] >> 4]))
                    temp = V[ram[PC] & 0x0F]
                    V[ram[PC] & 0x0F] = (V[ram[PC] & 0x0F] - V[ram[PC + 1] >> 4]) & 0xFF
                    if temp >= V[ram[PC + 1] >> 4]: V[0xF] = 1
                    else: V[0xF] = 0
                    PC += 2
                case 0x6: #SHR Vx {, Vy}
                    #print('SHR V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ' {, V' + str(ram[PC + 1] >> 4) + '=' + str(V[ram[PC + 1] >> 4]) + '}')
                    temp = V[ram[PC] & 0x0F]
                    if quirks == 0 or quirks == 3: V[ram[PC] & 0x0F] = V[ram[PC + 1] >> 4] >> 1
                    else: V[ram[PC] & 0x0F] = V[ram[PC] & 0x0F] >> 1
                    if temp & 1: V[0xF] = 1
                    else: V[0xF] = 0
                    PC += 2
                case 0x7: #SUBN Vx, Vy
                    #print('SUBN V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ', V' + str(ram[PC + 1] >> 4) + '=' + str(V[ram[PC + 1] >> 4]))
                    temp = V[ram[PC] & 0x0F]
                    V[ram[PC] & 0x0F] = (V[ram[PC + 1] >> 4] - V[ram[PC] & 0x0F]) & 0xFF
                    if V[ram[PC + 1] >> 4] >= temp: V[0xF] = 1
                    else: V[0xF] = 0
                    PC += 2
                case 0xE: #SHL Vx {, Vy}
                    #print('SHL V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ' {, V' + str(ram[PC + 1] >> 4) + '=' + str(V[ram[PC + 1] >> 4]) + '}')
                    temp = V[ram[PC] & 0x0F]
                    if quirks == 0 or quirks == 3: V[ram[PC] & 0x0F] = (V[ram[PC + 1] >> 4] << 1) & 0xFF
                    else: V[ram[PC] & 0x0F] = (V[ram[PC] & 0x0F] << 1) & 0xFF
                    if (temp >> 7): V[0xF] = 1
                    else: V[0xF] = 0
                    PC += 2
                case _:
                    crashed = True
                    print('Undefined Opcode: 8', hex(ram[PC + 1]))
                    pygame.quit()
                    sys.exit()
                    
        case 0x9: #SNE Vx, Vy
            #print('SNE V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ', V' + str(ram[PC + 1] >> 4) + '=' + str(V[ram[PC + 1] >> 4]))
            if V[ram[PC] & 0x0F] != V[ram[PC + 1] >> 4]: PC += 2
            PC += 2
        case 0xA: #LD I, addr
            #print('LD I=' + str(I) + ',', ((ram[PC] & 0x0F) << 8) + ram[PC + 1])
            I = ((ram[PC] & 0x0F) << 8) + ram[PC + 1]
            PC += 2
        case 0xB: #JP V0, addr
            #print('JP VX=' + str(V[ram[PC] & 0x0F]) + ',', ((ram[PC] & 0x0F) << 8) + ram[PC + 1])
            if quirks == 0 or quirks == 3: PC = ((ram[PC] & 0x0F) << 8) + ram[PC + 1] + V[0]
            else: PC = ((ram[PC] & 0x0F) << 8) + ram[PC + 1] + V[ram[PC] & 0x0F]
        case 0xC: #RND Vx, byte
            V[ram[PC] & 0x0F] = randint(0, 255) & ram[PC + 1]
            #print('RND V' + str(ram[PC] & 0x0F) + ',', V[ram[PC] & 0x0F])
            PC += 2
        case 0xD: #DRW Vx, Vy, nibble
            
            x = (V[ram[PC] & 0x0F]) & (width - 1)
            y = (V[ram[PC + 1] >> 4]) & (height - 1)
            n = ram[PC + 1] & 0x0F
            
            #print('DRW V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ', V' + str(ram[PC + 1] >> 4) + '=' + str(V[ram[PC + 1] >> 4]) + ', ' + str(n))

            if n == 0:
                _16x16Sprite = True
                n = 16
            else: _16x16Sprite = False

            V[0xF] = 0
            collision = False

            for row in range(n):
                for column in range(8):
                    drawPixel()
                if _16x16Sprite == True:
                    x += 8
                    I += 1
                    for column in range(8):
                        drawPixel()
                    x -= 8
                if collision:
                    V[0xF] += 1
                    collision = False
                if width == 128 and (y + row) > height: V[0xF] += 1
                
            if _16x16Sprite == True:
                I -= 16
    
            game_surface.blit(frame_buffer, (0, 0), (15, 15, width, height))
            if len(erasedPixels) > 0:
                for pos in range(len(erasedPixels)):
                    game_surface.set_at((erasedPixels[pos][0], erasedPixels[pos][1]), pixelColor[1])
                erasedPixels = []
            pygame.transform.scale(game_surface, screen.get_size(), screen)
            #pygame.transform.scale(frame_buffer, screen.get_size(), screen)
            
            PC += 2
        case 0xE:
            match ram[PC + 1]:
                case 0x9E: #SKP Vx
                    #print('SKP V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    keycode = pygame.key.get_pressed()
                    if keycode[keys[V[ram[PC] & 0x0F]]]:
                        PC += 2
                    PC += 2
                case 0xA1: #SKNP Vx
                    #print('SKNP V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    keycode = pygame.key.get_pressed()
                    if not keycode[keys[V[ram[PC] & 0x0F]]]:
                        PC += 2
                    PC += 2
                case _:
                    crashed = True
                    print('Undefined Opcode: E', hex(ram[PC + 1]))
                    pygame.quit()
                    sys.exit()
        case 0xF:
            match ram[PC + 1]:
                case 0x07: #LD Vx, DT
                    #print('LD V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]) + ', ' + 'DT=' + str(DT))
                    V[ram[PC] & 0x0F] = DT
                    PC += 2
                case 0x0A: #LD Vx, K
                    #print('LD V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]), 'K')
                    DT = 0
                    ST = 0
                    vblank = 0
                    game_surface.blit(frame_buffer, (0, 0), (15, 15, width, height))
                    pygame.transform.scale(game_surface, screen.get_size(), screen)
                    #pygame.transform.scale(frame_buffer, screen.get_size(), screen)
                    pygame.display.flip()
                    click = False
                    while not click:
                        event = pygame.event.wait()
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            keycode = pygame.key.get_pressed()
                            for k in range(len(keys)):
                                if keycode[keys[k]]:
                                    V[ram[PC] & 0x0F] = k
                                    click = True
                                    break
                    PC += 2
                case 0x15: #LD DT, Vx
                    #print('LD DT=' + str(DT) + ', V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]))
                    DT = V[ram[PC] & 0x0F]
                    PC += 2
                case 0x18: #LD ST, Vx
                    #print('LD ST=' + str(ST) + ', V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]))
                    ST = V[ram[PC] & 0x0F]
                    PC += 2
                case 0x1E: #ADD I, Vx
                    #print('ADD I=' + str(I) + ', V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]))
                    I += V[ram[PC] & 0x0F]
                    if I > 0xFFF: V[0xF] == 1
                    else: V[0xF] == 0
                    PC += 2
                case 0x29: #LD F, Vx
                    #print('LD F, V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]))
                    I = V[ram[PC] & 0x0F] * 5
                    PC += 2
                case 0x30:
                    I = (V[ram[PC] & 0x0F] * 10) + 0x50
                    PC += 2
                case 0x33: #LD B, Vx
                    #print('LD B, V' + str(ram[PC] & 0x0F) + '=' + str(V[ram[PC] & 0x0F]))
                    ram[I] = (V[ram[PC] & 0x0F] // 100) % 10
                    ram[I + 1] = (V[ram[PC] & 0x0F] // 10) % 10
                    ram[I + 2] = (V[ram[PC] & 0x0F] // 1) % 10
                    PC += 2
                case 0x55: #LD [I], Vx
                    for pos in range((ram[PC] & 0x0F) + 1):
                        #print('LD [' + str(ram[I]) + '], V' + str(pos) + '=' + str(V[pos]))
                        if quirks == 2: ram[I + pos] = V[pos]
                        else:
                            ram[I] = V[pos]
                            I += 1
                    if quirks == 1: I -= 1
                    PC += 2
                case 0x65: #LD Vx, [I]
                    for pos in range((ram[PC] & 0x0F) + 1):
                        #print('LD V' + str(pos) + '=' + str(V[pos]) + ', [' + str(ram[I]) + ']')
                        if quirks == 2: V[pos] = ram[I + pos]
                        else:
                            V[pos] = ram[I]
                            I += 1 
                    if quirks == 1: I -= 1
                    PC += 2
                case 0x75:
                    for pos in range((ram[PC] & 0x0F) + 1):
                        #print('FLAG [' + str(i) + '], V' + str(i) + '=' + str(V[i]))
                        Flag[pos] = V[pos]
                    PC += 2
                case 0x85:
                    for pos in range((ram[PC] & 0x0F) + 1):
                        #print('FLAG V' + str(i) + '=' + str(V[i]) + ', [' + str(Flag[i]) + ']')
                        V[pos] = Flag[pos]
                    PC += 2
                case _:
                    crashed = True
                    #print('Undefined Opcode: F' + str(hex(ram[PC + 1])))
                    pygame.quit()
                    sys.exit()
        case _:
            crashed = True
            print('Undefined Opcode:', hex(ram[PC + 1]))
            pygame.quit()
            sys.exit()

    cycles += 1
    frame += t.time() - time
    if cycles == speed:
        t.sleep(natural(0.0166666666666667 - frame))
        if DT > 0: DT -= 1
        if ST > 0:
            winsound.Beep(2500, 1)
            ST -= 1
        cycles = 0
        frame = 0
        pygame.display.flip()

