import numpy as np
from musicpy import *
from tkinter import *

def make_cube():
    return [   [['W', 'W', 'W'],
                ['W', 'W', 'W'],
                ['W', 'W', 'W']], #up/white              
               [['G', 'G', 'G'],
                ['G', 'G', 'G'],
                ['G', 'G', 'G']], #front/green
               [['R', 'R', 'R'],
                ['R', 'R', 'R'],
                ['R', 'R', 'R']], #right/red
               [['O', 'O', 'O'],
                ['O', 'O', 'O'],
                ['O', 'O', 'O']], #left/orange              
               [['Y', 'Y', 'Y'],
                ['Y', 'Y', 'Y'],
                ['Y', 'Y', 'Y']], #down/yellow               
               [['B', 'B', 'B'],
                ['B', 'B', 'B'],
                ['B', 'B', 'B']]] #back/blue
def print_cube(a):
    print('\t\t'+str(a[5][0])+'\n\t\t'+str(a[5][1])+'\n\t\t'+str(a[5][2]))   
    print(str(a[3][0])+' '+str(a[0][0])+' '+str(a[2][0]))
    print(str(a[3][1])+' '+str(a[0][1])+' '+str(a[2][1]))   
    print(str(a[3][2])+' '+str(a[0][2])+' '+str(a[2][2]))
    print('\t\t'+str(a[1][0])+'\n\t\t'+str(a[1][1])+'\n\t\t'+str(a[1][2]))
    print('\t\t'+str(a[4][0])+'\n\t\t'+str(a[4][1])+'\n\t\t'+str(a[4][2]))


myCube = make_cube()
print_cube(myCube)


def clockwise_rotate(matrix):
    n = len(matrix)
    copy = [[matrix[r][c] for c in range(n)] for r in range(n)]
    for r in range(n):
        for c in range(n):
            tr = c
            tc = n - r - 1
            matrix[tr][tc] = copy[r][c]
def counterclockwise_rotate(matrix):
    n = len(matrix)
    copy = [[matrix[r][c] for c in range(n)] for r in range(n)]
    for r in range(n):
        for c in range(n):
            tc = r
            tr = n - c - 1
            matrix[tr][tc] = copy[r][c]

#0white, 1green, 2red, 3orange, 4yellow, 5blue 
def rotate_R(cube): #1054-4105; right color: left-up-right-down
    for i in range(0,3):
        cube[1][i][2], cube[0][i][2], cube[5][i][2], cube[4][i][2] = cube[4][i][2], cube[1][i][2], cube[0][i][2], cube[5][i][2]
        counterclockwise_rotate(cube[2])
def rotate_Ri(cube): #1054-0541, right side color changes counterclockwise
    for i in range(0,3):
        cube[1][i][2], cube[0][i][2], cube[5][i][2], cube[4][i][2] = cube[0][i][2], cube[5][i][2], cube[4][i][2], cube[1][i][2]
        clockwise_rotate(cube[2])
def rotate_L(cube): #1054-0541, left side color changes clockwise
    for i in range(0,3):
        cube[1][i][0], cube[0][i][0], cube[5][i][0], cube[4][i][0] = cube[0][i][0], cube[5][i][0], cube[4][i][0], cube[1][i][0] 
        counterclockwise_rotate(cube[3])
def rotate_Li(cube): #1054-4105, left side color changes counterclockwise
    for i in range(0,3):
        cube[1][i][0], cube[0][i][0], cube[5][i][0], cube[4][i][0] = cube[4][i][0], cube[1][i][0], cube[0][i][0], cube[5][i][0]
        clockwise_rotate(cube[3])


#0white, 1green, 2red, 3orange, 4yellow, 5blue 
def rotate_M(cube): #1054-0541
    for i in range(0,3):
        cube[1][i][1], cube[0][i][1], cube[5][i][1], cube[4][i][1] = cube[0][i][1], cube[5][i][1], cube[4][i][1], cube[1][i][1]
def rotate_Mi(cube): #1054-4105
    for i in range(0,3):
        cube[1][i][1], cube[0][i][1], cube[5][i][1], cube[4][i][1] = cube[4][i][1], cube[1][i][1], cube[0][i][1], cube[5][i][1]
def rotate_r(cube): #1054-4105, right side color change
    for i in range(0,3):
        cube[1][i][2], cube[0][i][2], cube[5][i][2], cube[4][i][2] = cube[4][i][2], cube[1][i][2], cube[0][i][2], cube[5][i][2]
        cube[1][i][1], cube[0][i][1], cube[5][i][1], cube[4][i][1] = cube[4][i][1], cube[1][i][1], cube[0][i][1], cube[5][i][1]
        counterclockwise_rotate(cube[2])
def rotate_ri(cube): #1054-0541, right side color change
    for i in range(0,3):
        cube[1][i][2], cube[0][i][2], cube[5][i][2], cube[4][i][2] = cube[0][i][2], cube[5][i][2], cube[4][i][2], cube[1][i][2]
        cube[1][i][1], cube[0][i][1], cube[5][i][1], cube[4][i][1] = cube[0][i][1], cube[5][i][1], cube[4][i][1], cube[1][i][1]
        clockwise_rotate(cube[2])
def rotate_l(cube): #1054-0541
    for i in range(0,3):
        cube[1][i][0], cube[0][i][0], cube[5][i][0], cube[4][i][0] = cube[0][i][0], cube[5][i][0], cube[4][i][0], cube[1][i][0] 
        cube[1][i][1], cube[0][i][1], cube[5][i][1], cube[4][i][1] = cube[0][i][1], cube[5][i][1], cube[4][i][1], cube[1][i][1]
        counterclockwise_rotate(cube[3])
def rotate_li(cube): #1054-4105
    for i in range(0,3):
        cube[1][i][0], cube[0][i][0], cube[5][i][0], cube[4][i][0] = cube[4][i][0], cube[1][i][0], cube[0][i][0], cube[5][i][0]
        cube[1][i][1], cube[0][i][1], cube[5][i][1], cube[4][i][1] = cube[4][i][1], cube[1][i][1], cube[0][i][1], cube[5][i][1]
        clockwise_rotate(cube[3])

#0white, 1green, 2red, 3orange, 4yellow, 5blue 
def rotate_U(cube): #1352-2135, up color changes clockwise
    for i in range(0,3):
        cube[1][0][i], cube[3][i][2], cube[5][2][2-i], cube[2][2-i][0] = cube[2][2-i][0], cube[1][0][i], cube[3][i][2], cube[5][2][2-i]
        counterclockwise_rotate(cube[0])
def rotate_Ui(cube): #1352-3521, up color changes counterclockwise
    for i in range(0,3):
        cube[1][0][i], cube[3][i][2], cube[5][2][2-i], cube[2][2-i][0] = cube[3][i][2], cube[5][2][2-i], cube[2][2-i][0], cube[1][0][i]
        clockwise_rotate(cube[0])
def rotate_D(cube): #1352-3521, down color changes clockwise
    for i in range(0,3):
        cube[1][2][i], cube[3][i][0], cube[5][0][2-i], cube[2][2-i][2] = cube[3][i][0], cube[5][0][2-i], cube[2][2-i][2], cube[1][2][i]
        counterclockwise_rotate(cube[4])
def rotate_Di(cube): #1352-2135
    for i in range(0,3):
        cube[1][2][i], cube[3][i][0], cube[5][0][2-i], cube[2][2-i][2] = cube[2][2-i][2], cube[1][2][i], cube[3][i][0], cube[5][0][2-i]
        clockwise_rotate(cube[4])


#0white, 1green, 2red, 3orange, 4yellow, 5blue 
def rotate_u(cube): #1352-2135
    for i in range(0,3):
        cube[1][0][i], cube[3][i][2], cube[5][2][2-i], cube[2][2-i][0] = cube[2][2-i][0], cube[1][0][i], cube[3][i][2], cube[5][2][2-i]
        cube[1][1][i], cube[3][i][1], cube[5][1][2-i], cube[2][2-i][1] = cube[2][2-i][1], cube[1][1][i], cube[3][i][1], cube[5][1][2-i]
        counterclockwise_rotate(cube[0])
def rotate_ui(cube): #1352-3521
    for i in range(0,3):
        cube[1][0][i], cube[3][i][2], cube[5][2][2-i], cube[2][2-i][0] = cube[3][i][2], cube[5][2][2-i], cube[2][2-i][0], cube[1][0][i] 
        cube[1][1][i], cube[3][i][1], cube[5][1][2-i], cube[2][2-i][1] = cube[3][i][1], cube[5][1][2-i], cube[2][2-i][1], cube[1][1][i]
        clockwise_rotate(cube[0])
def rotate_d(cube): #1352-3521
    for i in range(0,3):
        cube[1][2][i], cube[3][i][0], cube[5][0][2-i], cube[2][2-i][2] = cube[3][i][0], cube[5][0][2-i], cube[2][2-i][2], cube[1][2][i]
        cube[1][1][i], cube[3][i][1], cube[5][1][2-i], cube[2][2-i][1] = cube[3][i][1], cube[5][1][2-i], cube[2][2-i][1], cube[1][1][i]
        counterclockwise_rotate(cube[4])
def rotate_di(cube): #1352-2135
    for i in range(0,3):
        cube[1][2][i], cube[3][i][0], cube[5][0][2-i], cube[2][2-i][2] = cube[2][2-i][2], cube[1][2][i], cube[3][i][0], cube[5][0][2-i] 
        cube[1][1][i], cube[3][i][1], cube[5][1][2-i], cube[2][2-i][1] = cube[2][2-i][1], cube[1][1][i], cube[3][i][1], cube[5][1][2-i]
        clockwise_rotate(cube[4])


#0white, 1green, 2red, 3orange, 4yellow, 5blue 
def rotate_F(cube): #0243-3024, front color changes clockwise
    for i in range(0,3):
        cube[0][2][i], cube[2][2][i], cube[4][0][2-i], cube[3][2][i] = cube[3][2][i], cube[0][2][i], cube[2][2][i], cube[4][0][2-i]
        counterclockwise_rotate(cube[1])
def rotate_Fi(cube): #0243-2430
    for i in range(0,3):
        cube[0][2][i], cube[2][2][i], cube[4][0][2-i], cube[3][2][i] = cube[2][2][i], cube[4][0][2-i], cube[3][2][i], cube[0][2][i] 
        clockwise_rotate(cube[1])
def rotate_B(cube): #0243-2430
    for i in range(0,3):
        cube[0][0][i], cube[2][0][i], cube[4][2][2-i], cube[3][0][i] = cube[2][0][i], cube[4][2][2-i], cube[3][0][i], cube[0][0][i]
        counterclockwise_rotate(cube[5])
def rotate_Bi(cube): #0243-3024
    for i in range(0,3):
        cube[0][0][i], cube[2][0][i], cube[4][2][2-i], cube[3][0][i] = cube[3][0][i], cube[0][0][i], cube[2][0][i], cube[4][2][2-i]
        clockwise_rotate(cube[5])


#0white, 1green, 2red, 3orange, 4yellow, 5blue 
def rotate_f(cube): #0243-3024
    for i in range(0,3):
        cube[0][2][i], cube[2][2][i], cube[4][0][2-i], cube[3][2][i] = cube[3][2][i], cube[0][2][i], cube[2][2][i], cube[4][0][2-i]
        cube[0][1][i], cube[2][1][i], cube[4][1][2-i], cube[3][1][i] = cube[3][1][i], cube[0][1][i], cube[2][1][i], cube[4][1][2-i]
        counterclockwise_rotate(cube[1])
def rotate_fi(cube): #0243-2430
    for i in range(0,3):
        cube[0][2][i], cube[2][2][i], cube[4][0][2-i], cube[3][2][i] = cube[2][2][i], cube[4][0][2-i], cube[3][2][i], cube[0][2][i]
        cube[0][1][i], cube[2][1][i], cube[4][1][2-i], cube[3][1][i] = cube[2][1][i], cube[4][1][2-i], cube[3][1][i], cube[0][1][i]
        clockwise_rotate(cube[1])
def rotate_b(cube): #0243-2430
    for i in range(0,3):
        cube[0][0][i], cube[2][0][i], cube[4][2][2-i], cube[3][0][i] = cube[2][0][i], cube[4][2][2-i], cube[3][0][i], cube[0][0][i]
        cube[0][1][i], cube[2][1][i], cube[4][1][2-i], cube[3][1][i] = cube[2][1][i], cube[4][1][2-i], cube[3][1][i], cube[0][1][i]
        counterclockwise_rotate(cube[5])
def rotate_bi(cube): #0243-3024
    for i in range(0,3):
        cube[0][0][i], cube[2][0][i], cube[4][2][2-i], cube[3][0][i] = cube[3][0][i], cube[0][0][i], cube[2][0][i], cube[4][2][2-i]
        cube[0][1][i], cube[2][1][i], cube[4][1][2-i], cube[3][1][i] = cube[3][1][i], cube[0][1][i], cube[2][1][i], cube[4][1][2-i]
        clockwise_rotate(cube[5])



#relationship between color and numbers: #0white, 1green, 2red, 3orange, 4yellow, 5blue  
number_to_chord_dict = {0:'CM7',1:'G7sus',2:'A7sus',3:'Em7',4:'FM7',5:'Am7',6:'Dm7',7:'F7sus',8:'Bm7',9:'GM7'}
chord_line_mapping = {'CM7':3,'G7sus':2,'A7sus':2,'Em7':2,'FM7':2,'Am7':2,'Dm7':3,'F7sus':2,'Bm7':2,'GM7':2}
#relationship between color and numbers: #0white, 1green, 2red, 3orange, 4yellow, 5blue  



def matrix_difference_list(color1, color2):
    difference = 0
    for i in range(0,3):
        for j in range(0,3):
            if color1[i][j] != color2[i][j]:
                difference = difference + 1
    return difference


def play_cube_music(cube):
    global guitar
    initial = make_cube()
    chord_list = []
    for i in range(6):
        chord_list.append(number_to_chord_dict.get(matrix_difference_list(initial[i],cube[i])))
    new_guitar = (C(chord_list[0], chord_line_mapping.get(chord_list[0]), 1/4, 1/8)^2 |
              C(chord_list[1], chord_line_mapping.get(chord_list[1]), 1/4, 1/8)^2 |
              C(chord_list[2], chord_line_mapping.get(chord_list[2]), 1/4, 1/8)^2 |
              C(chord_list[3], chord_line_mapping.get(chord_list[3]), 1/4, 1/8)@1 |
              C(chord_list[4], chord_line_mapping.get(chord_list[4]), 1/4, 1/8)^2 |
              C(chord_list[5], chord_line_mapping.get(chord_list[5]), 1/4, 1/8)^2)
    guitar = guitar + new_guitar
    play(new_guitar, bpm=100, instrument=25)


colors = {'W': 'white',
          'Y': 'yellow',
          'O': 'orange',
          'R': 'red',
          'B': 'blue',
          'G': 'green'
         }
def plot_cube(cube):
    left_margin, up_margin = 100, 150
    canvas.create_rectangle(left_margin-20, up_margin-50, left_margin+380, up_margin+490, fill='white') # cube graph background
    canvas.create_rectangle(left_margin+400, up_margin-50, left_margin+680, up_margin+350, fill='white') # cube graph background
    i, j = 0, 0 #i: row; j: colomn ->cube[color][i][j]
    for i in range(0,3):
        for j in range (0,3):
            canvas.create_rectangle(left_margin+120+40*j, up_margin+40*i, left_margin+160+40*j, up_margin+40+40*i, 
                                    fill=colors.get(cube[5][i][j]))
            canvas.create_rectangle(left_margin+40*j, up_margin+120+40*i, left_margin+40+40*j, up_margin+160+40*i,
                                    fill=colors.get(cube[3][i][j]))
            canvas.create_rectangle(left_margin+120+40*j, up_margin+120+40*i, left_margin+160+40*j, up_margin+160+40*i,
                                    fill=colors.get(cube[0][i][j]))
            canvas.create_rectangle(left_margin+240+40*j, up_margin+120+40*i, left_margin+280+40*j, up_margin+160+40*i,  
                                    fill=colors.get(cube[2][i][j]))
            canvas.create_rectangle(left_margin+120+40*j, up_margin+240+40*i, left_margin+160+40*j, up_margin+280+40*i,
                                    fill=colors.get(cube[1][i][j]))
            canvas.create_rectangle(left_margin+120+40*j, up_margin+360+40*i, left_margin+160+40*j, up_margin+400+40*i,
                                    fill=colors.get(cube[4][i][j]))
    canvas.pack()


def R_button_event(cube):
    rotate_R(cube)
    plot_cube(cube)
    play_cube_music(cube)
def Ri_button_event(cube):
    rotate_Ri(cube)
    plot_cube(cube)
    play_cube_music(cube)
def L_button_event(cube):
    rotate_L(cube)
    plot_cube(cube)  
    play_cube_music(cube)
def Li_button_event(cube):
    rotate_Li(cube)
    plot_cube(cube) 
    play_cube_music(cube)
def M_button_event(cube):
    rotate_M(cube)
    plot_cube(cube)
    play_cube_music(cube)
def Mi_button_event(cube):
    rotate_Mi(cube)
    plot_cube(cube)
    play_cube_music(cube)
def r_button_event(cube):
    rotate_r(cube)
    plot_cube(cube)    
    play_cube_music(cube)
def ri_button_event(cube):
    rotate_ri(cube)
    plot_cube(cube) 
    play_cube_music(cube)
def l_button_event(cube):
    rotate_l(cube)
    plot_cube(cube)
    play_cube_music(cube)
def li_button_event(cube):
    rotate_li(cube)
    plot_cube(cube)   
    play_cube_music(cube)
def U_button_event(cube):
    rotate_U(cube)
    plot_cube(cube)
    play_cube_music(cube)
def Ui_button_event(cube):
    rotate_Ui(cube)
    plot_cube(cube)   
    play_cube_music(cube)
def D_button_event(cube):
    rotate_D(cube)
    plot_cube(cube)
    play_cube_music(cube)
def Di_button_event(cube):
    rotate_Di(cube)
    plot_cube(cube)   
    play_cube_music(cube)
def u_button_event(cube):
    rotate_u(cube)
    plot_cube(cube)    
    play_cube_music(cube)
def ui_button_event(cube):
    rotate_ui(cube)
    plot_cube(cube)  
    play_cube_music(cube)
def d_button_event(cube):
    rotate_d(cube)
    plot_cube(cube)
    play_cube_music(cube)
def di_button_event(cube):
    rotate_di(cube)
    plot_cube(cube)   
    play_cube_music(cube)
def F_button_event(cube):
    rotate_F(cube)
    plot_cube(cube)
    play_cube_music(cube)
def Fi_button_event(cube):
    rotate_Fi(cube)
    plot_cube(cube)
    play_cube_music(cube)
def B_button_event(cube):
    rotate_B(cube)
    plot_cube(cube)
    play_cube_music(cube)
def Bi_button_event(cube):
    rotate_Bi(cube)
    plot_cube(cube)
    play_cube_music(cube)
def f_button_event(cube):
    rotate_f(cube)
    plot_cube(cube)
    play_cube_music(cube)
def fi_button_event(cube):
    rotate_fi(cube)
    plot_cube(cube)
    play_cube_music(cube)
def b_button_event(cube):
    rotate_b(cube)
    plot_cube(cube)
    play_cube_music(cube)
def bi_button_event(cube):
    rotate_bi(cube)
    plot_cube(cube)
    play_cube_music(cube)



def mode_button1_event():
    global mode_value
    mode_value = 1
    button_label2 = Label(root, text='Mode 1: Real-Time Improvisation', bg = 'white')
    button_label2_window = canvas.create_window(540, 300, anchor=NW, window=button_label2)
def mode_button2_event():
    global mode_value
    mode_value = 2
    button_label3 = Label(root, text='Mode 2: Download Your Music    ', bg = 'white')
    button_label3_window = canvas.create_window(540, 300, anchor=NW, window=button_label3)
def reset_button_event():
    global myCube
    myCube = make_cube()
    plot_cube(myCube)
    play_cube_music(myCube)



def play_button_event(): #play your music
    play(guitar,bpm=100, instrument=25)
def download_button_event():
    write(guitar,bpm=100,name='cubeMusic.mid',instrument=25,save_as_file=True)



guitar = chord([])
root = Tk()
root.wm_title("Cube Improvisation")
canvas = Canvas(root,width = 900, height = 720, bg = 'silver')
button_mode1 = Button(root, text="Mode 1", height=1, width=10, bg='silver', command=lambda:mode_button1_event())
button_mode1_window = canvas.create_window(0, 0, anchor=NW, window=button_mode1)
button_mode2 = Button(root, text="Mode 2", height=1, width=10, bg='silver', command=lambda:mode_button2_event())
button_mode2_window = canvas.create_window(80, 0, anchor=NW, window=button_mode2)

myCube = make_cube()

plot_cube(myCube)

cube_label = Label(root, text="Current Rubik's Cube Graph", bg = 'white')
cube_label_window = canvas.create_window(100, 110, anchor=NW, window=cube_label)

button_offset = 40 #left offset
button_R = Button(root, text="R", height=1, width=2, bg='white', command=lambda:R_button_event(myCube))
button_R_window = canvas.create_window(500+button_offset, 150, anchor=NW, window=button_R)
button_Ri = Button(root, text="R'", height=1, width=2, bg='white', command=lambda:Ri_button_event(myCube))
button_Ri_window = canvas.create_window(525+button_offset, 150, anchor=NW, window=button_Ri)
button_L = Button(root, text="L", height=1, width=2, bg='white', command=lambda:L_button_event(myCube))
button_L_window = canvas.create_window(550+button_offset, 150, anchor=NW, window=button_L)
button_Li = Button(root, text="L'", height=1, width=2, bg='white', command=lambda:Li_button_event(myCube))
button_Li_window = canvas.create_window(575+button_offset, 150, anchor=NW, window=button_Li)
button_r = Button(root, text="r", height=1, width=2, bg='white', command=lambda:r_button_event(myCube))
button_r_window = canvas.create_window(600+button_offset, 150, anchor=NW, window=button_r)
button_ri = Button(root, text="r'", height=1, width=2, bg='white', command=lambda:ri_button_event(myCube))
button_ri_window = canvas.create_window(625+button_offset, 150, anchor=NW, window=button_ri)
button_l = Button(root, text="l", height=1, width=2, bg='white', command=lambda:l_button_event(myCube))
button_l_window = canvas.create_window(650+button_offset, 150, anchor=NW, window=button_l)
button_li = Button(root, text="l'", height=1, width=2, bg='white', command=lambda:li_button_event(myCube))
button_li_window = canvas.create_window(675+button_offset, 150, anchor=NW, window=button_li)

button_U = Button(root, text="U", height=1, width=2, bg='white', command=lambda:U_button_event(myCube))
button_U_window = canvas.create_window(500+button_offset, 180, anchor=NW, window=button_U)
button_Ui = Button(root, text="U'", height=1, width=2, bg='white', command=lambda:Ui_button_event(myCube))
button_Ui_window = canvas.create_window(525+button_offset, 180, anchor=NW, window=button_Ui)
button_D = Button(root, text="D", height=1, width=2, bg='white', command=lambda:D_button_event(myCube))
button_D_window = canvas.create_window(550+button_offset, 180, anchor=NW, window=button_D)
button_Di = Button(root, text="D'", height=1, width=2, bg='white', command=lambda:Di_button_event(myCube))
button_Di_window = canvas.create_window(575+button_offset, 180, anchor=NW, window=button_Di)
button_u = Button(root, text="u", height=1, width=2, bg='white', command=lambda:u_button_event(myCube))
button_u_window = canvas.create_window(600+button_offset, 180, anchor=NW, window=button_u)
button_ui = Button(root, text="u'", height=1, width=2, bg='white', command=lambda:ui_button_event(myCube))
button_ui_window = canvas.create_window(625+button_offset, 180, anchor=NW, window=button_ui)
button_d = Button(root, text="d", height=1, width=2, bg='white', command=lambda:d_button_event(myCube))
button_d_window = canvas.create_window(650+button_offset, 180, anchor=NW, window=button_d)
button_di = Button(root, text="d'", height=1, width=2, bg='white', command=lambda:di_button_event(myCube))
button_di_window = canvas.create_window(675+button_offset, 180, anchor=NW, window=button_di)

button_F = Button(root, text="F", height=1, width=2, bg='white', command=lambda:F_button_event(myCube))
button_F_window = canvas.create_window(500+button_offset, 210, anchor=NW, window=button_F)
button_Fi = Button(root, text="F'", height=1, width=2, bg='white', command=lambda:Fi_button_event(myCube))
button_Fi_window = canvas.create_window(525+button_offset, 210, anchor=NW, window=button_Fi)
button_B = Button(root, text="B", height=1, width=2, bg='white', command=lambda:B_button_event(myCube))
button_B_window = canvas.create_window(550+button_offset, 210, anchor=NW, window=button_B)
button_Bi = Button(root, text="B'", height=1, width=2, bg='white', command=lambda:Bi_button_event(myCube))
button_Bi_window = canvas.create_window(575+button_offset, 210, anchor=NW, window=button_Bi)
button_f = Button(root, text="f", height=1, width=2, bg='white', command=lambda:f_button_event(myCube))
button_f_window = canvas.create_window(600+button_offset, 210, anchor=NW, window=button_f)
button_fi = Button(root, text="f'", height=1, width=2, bg='white', command=lambda:fi_button_event(myCube))
button_fi_window = canvas.create_window(625+button_offset, 210, anchor=NW, window=button_fi)
button_b = Button(root, text="b", height=1, width=2, bg='white', command=lambda:b_button_event(myCube))
button_b_window = canvas.create_window(650+button_offset, 210, anchor=NW, window=button_b)
button_bi = Button(root, text="b'", height=1, width=2, bg='white', command=lambda:bi_button_event(myCube))
button_bi_window = canvas.create_window(675+button_offset, 210, anchor=NW, window=button_bi)

button_M = Button(root, text="M", height=1, width=2, bg='white', command=lambda:M_button_event(myCube))
button_M_window = canvas.create_window(500+button_offset, 240, anchor=NW, window=button_M)
button_Mi = Button(root, text="M'", height=1, width=2, bg='white', command=lambda:Mi_button_event(myCube))
button_Mi_window = canvas.create_window(525+button_offset, 240, anchor=NW, window=button_Mi)

button_reset = Button(root, text="Reset", height=1, width=20, bg='white', command=lambda:reset_button_event())
button_reset_window = canvas.create_window(550+button_offset, 240, anchor=NW, window=button_reset)

button_label = Label(root, text='Operation Buttons', bg = 'white')
button_label_window = canvas.create_window(540, 110, anchor=NW, window=button_label)

button_play = Button(root, text="Play your music", height=1, width=20, bg='white', command=lambda:play_button_event())
button_play_window = canvas.create_window(500+button_offset, 350, anchor=NW, window=button_play)

button_download = Button(root, text="Download your music", height=1, width=20, bg='white', command=lambda:download_button_event())
button_download_window = canvas.create_window(500+button_offset, 380, anchor=NW, window=button_download)

root.mainloop()



