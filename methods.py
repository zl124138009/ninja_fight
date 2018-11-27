#!/usr/bin/python
# -*- coding: UTF-8 -*-
#方法定义

import random
import character
import methods


#生成[x,y]的随机整数
def rd(x=0,y=1):
    if not (isinstance(x,(int,long)) and isinstance(y,(int,long))):
        print "Error:输入类型错误,请输入整数"
    elif x > y:
        r = int(( y - x - 1) * random.random() + x)
    elif x < y:
        r = int(( y - x + 1) * random.random() + x)
    else:
        r = x
    return r

#显示角色列表
def show_list(name,ch):
    for i in range(len(ch)):
        print i,(name[ch[i].name]).decode('UTF-8')

#血量计算，ch为角色数组，i为选定角色序号，返回血量
def calc_HP(ch,i):
    #hp=力*10+体*3-速*2
    hp = (ch[i].li * 10) + (ch[i].ti * 3) - (ch[i].su * 2)
    return hp

#查克拉量计算，ch为角色数组，i为选定角色序号，返回查克拉量
def calc_MP(ch,i):
    #mp=精*7+贤*3
    mp = (ch[i].jing * 7) + (ch[i].xian * 3)
    return mp

#选择角色,name为名字字典，ch为角色数组
def chs_main(name,ch):
    print "============================"
    flag = 0
    while(flag != 1):
        try:
            i = int(raw_input("choose your ninja :"))
        except:
            print "*Please input the sequence number*"
        else:
            if i >= 0 and i < len(ch):
                main = [i,
                           methods.calc_HP(ch,i),  #计算血量
                           methods.calc_MP(ch,i)]  #计算查克拉量
                flag = 1
                print "your choice is :",(name[ch[main[0]].name]).decode('UTF-8')
                print "your HP is :",main[1]
                print "your MP is :",main[2]
            else:
                print "*Illegal input*"
    return main

#选择对手,name为名字字典，ch为角色数组
def chs_enemy(name,ch):
    print "============================"
    flag = 0
    while(flag != 1):
        try:
            i = int(raw_input("choose your enemy :"))
        except:
            print "*Please input the sequence number*"
        else:
            if i >= 0 and i < len(ch):
                enemy = [i,
                           methods.calc_HP(ch,i),  #计算血量
                           methods.calc_MP(ch,i)]  #计算查克拉量
                flag = 1
                print "your enemy is :",(name[ch[enemy[0]].name]).decode('UTF-8')
                print "enemy's HP is :",enemy[1]
                print "enemy's MP is :",enemy[2]
            else:
                print "*Illegal input*"
    return enemy

#攻击方向判断，ch为角色数组,i为主角序号，j为对手序号，返回攻击次序
#0为主角攻击对手，1为对手攻击主角
def lgc_who(ch,main,enemy):
    if methods.rd(0,ch[main[0]].su) > methods.rd(0,ch[enemy[0]].su):
        flag = 0
    elif methods.rd(0,ch[main[0]].su) < methods.rd(0,ch[enemy[0]].su):
        flag = 1
    else:
        flag = methods.lgc_who(ch,main,enemy)
    return flag

#攻击类型判断
#ch为角色数组,i为主角序号，j为对手序号，su为忍术列表
#返回忍术序号
def lgc_atk(ch,main,enemy,lstsu):
    result = methods.rd(0,len(lstsu)-1)
    return result
    
#伤害计算
#ch为角色数组，hero1为攻击方，hero2为防守方
#atk为攻击方式序号，lstsu为忍术数组，su为忍术名
#返回攻击数值
def calc_atk(ch,hero1,hero2,atk,lstsu,su):
    result = 0
    #攻击命中计算
    #贤1<随机数，则未命中，返回0
    #随机数=(1,(10-贤1)/4+贤1)
    if(ch[hero1[0]].xian < methods.rd(1,(10-ch[hero1[0]].xian)/4
                                    +ch[hero1[0]].xian)):
        print "攻击未命中".decode('UTF-8')
        return int(result)
    #贤2-贤1>随机数(1,10)，则被闪避
    elif((ch[hero2[0]].xian - ch[hero1[0]].xian) >
         methods.rd(1,10)):
        print "攻击被闪避".decode('UTF-8')
        return int(result)
    #命中后伤害计算
    else:
        if(hero1[2] >= lstsu[atk].chakra):#判断剩余查克拉量
            if(lstsu[atk].kind == 1):
                result = methods.rd(ch[hero1[0]].ti * 2/3,
                                    ch[hero1[0]].ti + lstsu[atk].damage)
            elif(lstsu[atk].kind == 2):
                result = methods.rd(ch[hero1[0]].ren * 2/3,
                                    ch[hero1[0]].ren + lstsu[atk].damage)
            elif(lstsu[atk].kind == 3):
                result = methods.rd(ch[hero1[0]].huan * 2/3,
                                    ch[hero1[0]].huan + lstsu[atk].damage)
        else:
            print "Don't have enough chakra"
        result = methods.clac_fightback(ch,hero1,hero2,atk,lstsu,su,result)
        return int(result)

#攻击反制计算
#ch为角色数组，hero1为攻击方，hero2为防守方,res为伤害值
#atk为攻击方式序号，lstsu为忍术数组，su为忍术名
#返回攻击数值
def clac_fightback(ch,hero1,hero2,atk,lstsu,su,res):
    result = res
    if(lstsu[atk].kind == 1):#体术
        #随机数(-2,(体2-体1))>= 0, 防御成功
        if(methods.rd(-2,(ch[hero2[0]].ti - ch[hero1[0]].ti)) >= 0):
            print "成功防御".decode('UTF-8')
            result = 1
    elif(lstsu[atk].kind == 2):#忍术
        #随机数(1,10) < ti2 * 1/3, 替身术闪避成功
        if(methods.rd(1,10) < ch[hero2[0]].yin * 1/3):
            print "召唤替身".decode('UTF-8')
            result = 0
    return result
    

#查克拉消耗计算
#ch为角色数组，hero角色，atk为攻击方式序号，lstsu为忍术数组，su为忍术名
#返回消耗数值
def calc_ckl(ch,hero,atk,lstsu,su):
    if(hero[2] >= lstsu[atk].chakra):
        result = int(lstsu[atk].chakra)
    else:
        result = 0
    return result

#显示攻击结果
#name为名字字典，ch为角色数组，main为主角数组，enemy为对手数组
#flag为攻击方向，atk为攻击方式序号，lstsu为忍术数组，su为忍术名
#返回被攻击方数组
def show_atk(name,ch,main,enemy,flag,atk,lstsu,su):
    result = 0
    if(flag == 0):
        result = methods.calc_atk(ch,main,enemy,atk,lstsu,su)
        enemy[1] = enemy[1] - result
        print name[ch[main[0]].name].decode('UTF-8'),\
              "used",su[lstsu[atk].name].decode('UTF-8'),\
              "to attack",name[ch[enemy[0]].name].decode('UTF-8')+",",\
              "caused",result,"damages"
        return enemy
    elif(flag == 1):
        result = methods.calc_atk(ch,enemy,main,atk,lstsu,su)
        main[1] = main[1] - result
        print name[ch[enemy[0]].name].decode('UTF-8'),\
              "used",su[lstsu[atk].name].decode('UTF-8'),\
              "to attack",name[ch[main[0]].name].decode('UTF-8')+",",\
              "caused",result,"damages"
        return main
    else:
        pass
        return

#显示查克拉消耗
#name为名字字典，ch为角色数组，main为主角数组，enemy为对手数组
#flag为攻击方向，atk为攻击方式序号，lstsu为忍术数组，su为忍术名
#返回攻击方数组
def show_ckl(name,ch,main,enemy,flag,atk,lstsu,su):
    result = 0
    if(flag == 0):
        result = methods.calc_ckl(ch,main,atk,lstsu,su)
        main[2] = main[2] - result
        print name[ch[main[0]].name].decode('UTF-8'),\
              "consumed",result,"chakra"
        return main
    elif(flag == 1):
        result = methods.calc_ckl(ch,enemy,atk,lstsu,su)
        enemy[2] = enemy[2] - result
        print name[ch[enemy[0]].name].decode('UTF-8'),\
              "consumed",result,"chakra"
        return enemy
    else:
        pass
        return

#显示当前角色数据
def show_ch(name,ch,main,enemy):
    print ""    
    if(main[1] <= 0):
        main[1] = 0
        print (name[ch[enemy[0]].name]).decode('UTF-8'),"wins"
    elif(enemy[1] <= 0):
        enemy[1] = 0
        print (name[ch[main[0]].name]).decode('UTF-8'),"wins"
    else:
        pass
    print (name[ch[main[0]].name]).decode('UTF-8')+":",\
          "HP",main[1],", MP",main[2]
    print (name[ch[enemy[0]].name]).decode('UTF-8')+":",\
          "HP",enemy[1],", MP",enemy[2]
    print "--------------------------------------------"




