# -*- coding: utf-8 -*-
from pygame import *
import fileIO
import character
import methods

history = []#记录实时数据
roles = []#当前选择角色
names = {}#忍者名字典
ninja = []#忍者列表
tsu_names = {}#忍术名字典
tsu = []#忍术列表

def showtext(win, pos, text, Font, color, bgcolor):#文字转化
    textimg = Font.render(text, 1, color, bgcolor)
    win.blit(textimg, pos)
    return pos[0] + textimg.get_width() + 5, pos[1]

def drawbg(win):#画背景及固定文字
    bgcolor1 = 50, 50, 50
    bgcolor2 = 50, 80, 80
    
    win.fill(bgcolor1, (0, 0, 640, 120))
    win.fill(bgcolor2, (0, 120, 640, 240))
    win.fill(bgcolor1, (0, 360, 640, 120))

    Font1 = font.Font("C:/Windows/Fonts/simsun.ttc",16)
    color1 = 255, 255, 255
    color2 = 255, 50, 50
    color3 = 50, 50, 250
    
    showtext(win, (250, 9), "HP:".decode("UTF-8"), Font1, color2, None)
    showtext(win, (330, 9), "MP:".decode("UTF-8"), Font1, color3, None)
    showtext(win, (120, 40), "忍:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (200, 40), "体:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (280, 40), "幻:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (360, 40), "贤:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (120, 65), "力:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (200, 65), "速:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (280, 65), "精:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (360, 65), "印:".decode("UTF-8"), Font1, color1, None)

    showtext(win, (250, 369), "HP:".decode("UTF-8"), Font1, color2, None)
    showtext(win, (330, 369), "MP:".decode("UTF-8"), Font1, color3, None)
    showtext(win, (120, 400), "忍:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (200, 400), "体:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (280, 400), "幻:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (360, 400), "贤:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (120, 425), "力:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (200, 425), "速:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (280, 425), "精:".decode("UTF-8"), Font1, color1, None)
    showtext(win, (360, 425), "印:".decode("UTF-8"), Font1, color1, None)

def drawdata(win, roles, names, ninja, tsu):#画动态数据   
    Font1 = font.Font("C:/Windows/Fonts/simsun.ttc",16)
    Font2 = font.Font("C:/Windows/Fonts/simhei.ttf",20)
    Font3 = font.Font("C:/Windows/Fonts/simhei.ttf",16)
    color1 = 255, 255, 255
    color2 = 255, 50, 50
    color3 = 50, 50, 250

    drawbg(win)

    showtext(win, (120, 7), names[roles[0][1]].decode("UTF-8"), Font2, color1, None)
    showtext(win, (280, 9), str(roles[0][2]), Font3, color2, None)
    showtext(win, (360, 9), str(roles[0][3]), Font3, color3, None)
    showtext(win, (145, 40), str(ninja[roles[0][0]].ren), Font1, color1, None)
    showtext(win, (225, 40), str(ninja[roles[0][0]].ti), Font1, color1, None)
    showtext(win, (305, 40), str(ninja[roles[0][0]].huan), Font1, color1, None)
    showtext(win, (385, 40), str(ninja[roles[0][0]].xian), Font1, color1, None)
    showtext(win, (145, 65), str(ninja[roles[0][0]].li), Font1, color1, None)
    showtext(win, (225, 65), str(ninja[roles[0][0]].su), Font1, color1, None)
    showtext(win, (305, 65), str(ninja[roles[0][0]].jing), Font1, color1, None)
    showtext(win, (385, 65), str(ninja[roles[0][0]].yin), Font1, color1, None)

    showtext(win, (120, 367), names[roles[1][1]].decode("UTF-8"), Font2, color1, None)
    showtext(win, (280, 369), str(roles[1][2]), Font3, color2, None)
    showtext(win, (360, 369), str(roles[1][3]), Font3, color3, None)
    showtext(win, (145, 400), str(ninja[roles[1][0]].ren), Font1, color1, None)
    showtext(win, (225, 400), str(ninja[roles[1][0]].ti), Font1, color1, None)
    showtext(win, (305, 400), str(ninja[roles[1][0]].huan), Font1, color1, None)
    showtext(win, (385, 400), str(ninja[roles[1][0]].xian), Font1, color1, None)
    showtext(win, (145, 425), str(ninja[roles[1][0]].li), Font1, color1, None)
    showtext(win, (225, 425), str(ninja[roles[1][0]].su), Font1, color1, None)
    showtext(win, (305, 425), str(ninja[roles[1][0]].jing), Font1, color1, None)
    showtext(win, (385, 425), str(ninja[roles[1][0]].yin), Font1, color1, None)

def drawfight(win, history, text):#画实时数据
    ypos = 330
    ypos_end = 120
    Font1 = font.Font("C:/Windows/Fonts/simsun.ttc",16)
    color1 = 50, 200, 150
    bgcolor1 = 50, 80, 80
    
    texting = Font1.render(text, 1, color1, bgcolor1)
    history.append(texting)
    history = history[-30:]

    win.fill(bgcolor1, (0, 120, 640, 240))
    
    h = list(history)
    m = (ypos - ypos_end) / Font1.get_height()
    n = len(history)
    h.reverse()
    for line in h:
        if m >= n:
            r = win.blit(line, (10, ypos - (m - n + 1) * Font1.get_height()))
            ypos -= Font1.get_height()
        elif m < n and ypos > ypos_end:
            r = win.blit(line, (10, ypos))
            ypos -= Font1.get_height()
    return history

def getRoles(ninja, seq1, seq2):#选择角色
    roles = []
    roles.append([seq1, ninja[seq1].name, methods.calc_HP(ninja, seq1), methods.calc_MP(ninja, seq1)])
    roles.append([seq2, ninja[seq2].name, methods.calc_HP(ninja, seq2), methods.calc_MP(ninja, seq2)])
    return roles

def getNinja():#获取忍者列表
    list_ch = []
    data = fileIO.readList(".\\ninja.data")

    for i in range(len(data)):
        tmp = character.ninja(data[i][0],data[i][1],data[i][2],data[i][3],
                            data[i][4],data[i][5],data[i][6],data[i][7],
                            data[i][8])
        list_ch.append(tmp)
    return list_ch

def getNinjutsu():#获取忍术列表
    list_tsu = []
    nins = fileIO.readList(".\\ninjutsu.data")

    for i in range(len(nins)):
        tmp = character.ninjutsu(nins[i][0],nins[i][1],nins[i][2],nins[i][3],
                                nins[i][4],nins[i][5],nins[i][6],nins[i][7])
        list_tsu.append(tmp)
    return list_tsu

def getName():#获取忍者名字
    dict_name = {}
    names = fileIO.readList(".\\name.data")

    for i in range(len(names)):
        dict_name[names[i][0]] = names[i][1]
    #print dict_name
    return dict_name

def getTsu_name():#获取忍术名字
    dict_tsu_name = {}
    names = fileIO.readList(".\\tsu_name.data")

    for i in range(len(names)):
        dict_tsu_name[names[i][0]] = names[i][1]
    #print dict_tsu_name
    return dict_tsu_name

def main():
    init()

    win = display.set_mode((640,480))
    display.set_caption("Ninja Fight")

    global names
    names = getName()
    global ninja
    ninja = getNinja()
    global tsu_names
    tsu_names = getTsu_name()
    global tsu
    tsu = getNinjutsu()
    global roles
    roles = getRoles(ninja, methods.rd(0, len(getNinja())-1), methods.rd(0, len(getNinja())-1))
    global history

    drawdata(win, roles, names, ninja, tsu)

    going = True
    while going:
        for e in event.get():
            if e.type == QUIT:
                going = False
            elif e.type == KEYUP and e.key == K_ESCAPE:
                going = False
            elif e.type == KEYUP and e.key == K_1:
                history = drawfight(win, history, "ddddd")

        display.flip()
        time.wait(10)

    quit()

if __name__ == "__main__":
    main()
