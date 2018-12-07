# -*- coding: utf-8 -*-
from pygame import *
import fileIO
import character
import methods


def showtext(win, pos, text, Font, color, bgcolor):
    textimg = Font.render(text, 1, color, bgcolor)
    win.blit(textimg, pos)
    return pos[0] + textimg.get_width() + 5, pos[1]

def drawbg(win):
    bgcolor1 = 50, 50, 50
    bgcolor2 = 50, 80, 80
    win.fill(bgcolor1, (0, 0, 640, 120))
    win.fill(bgcolor2, (0, 120, 640, 240))
    win.fill(bgcolor1, (0, 360, 640, 120))

    Font1 = font.Font("C:/Windows/Fonts/simsun.ttc",16)
    color1 = 255, 255, 255
    showtext(win, (120,40), "忍:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (200,40), "体:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (280,40), "幻:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (360,40), "贤:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (120,65), "力:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (200,65), "速:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (280,65), "精:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (360,65), "印:".decode("UTF-8"), Font1, color1, None)
    
def drawdata(win, names, ninja, tsu, seq):
    Font1 = font.Font("C:/Windows/Fonts/simsun.ttc",16)
    Font2 = font.Font("C:/Windows/Fonts/simhei.ttf",20)
    color1 = 255, 255, 255
    showtext(win, (120,5), names[ninja[seq].name].decode("UTF-8"), Font2, color1, None)
    showtext(win, (145,40), str(ninja[seq].ren), Font1, color1, None)
    showtext(win, (225,40), str(ninja[seq].ti), Font1, color1, None)
    showtext(win, (305,40), str(ninja[seq].huan), Font1, color1, None)
    showtext(win, (385,40), str(ninja[seq].xian), Font1, color1, None)
    showtext(win, (145,65), str(ninja[seq].li), Font1, color1, None)
    showtext(win, (225,65), str(ninja[seq].su), Font1, color1, None)
    showtext(win, (305,65), str(ninja[seq].jing), Font1, color1, None)
    showtext(win, (385,65), str(ninja[seq].yin), Font1, color1, None)
    return 0

def getNinja():
    list_ch = []
    data = fileIO.readList(".\\ninja.data")

    for i in range(len(data)):
        tmp = character.ninja(data[i][0],data[i][1],data[i][2],data[i][3],
                            data[i][4],data[i][5],data[i][6],data[i][7],
                            data[i][8])
        list_ch.append(tmp)
    return list_ch

def getNinjutsu():
    list_tsu = []
    nins = fileIO.readList(".\\ninjutsu.data")

    for i in range(len(nins)):
        tmp = character.ninjutsu(nins[i][0],nins[i][1],nins[i][2],nins[i][3],
                                nins[i][4],nins[i][5],nins[i][6],nins[i][7])
        list_tsu.append(tmp)
    return list_tsu

def getName():
    dict_name = {}
    names = fileIO.readList(".\\name.data")

    for i in range(len(names)):
        dict_name[names[i][0]] = names[i][1]
    return dict_name

def main():
    init()

    win = display.set_mode((640,480))
    display.set_caption("Ninja Fight")

    drawbg(win)
    drawdata(win, getName(), getNinja(), getNinjutsu(), methods.rd(1,10))

    going = True
    while going:
        for e in event.get():
            if e.type == QUIT:
                going = False
            elif e.type == KEYUP and e.key == K_ESCAPE:
                going = False

        display.flip()
        time.wait(10)

    quit()

if __name__ == "__main__":
    main()
