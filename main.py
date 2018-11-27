#!/usr/bin/python
# -*- coding: UTF-8 -*-
#主逻辑控制

import time
import fileIO
import character
import methods

#########################################
#变量定义
#角色名字字典
name = {"zly":"自来也","yzby":"宇智波鼬","dsw":"大蛇丸","gs":"纲手",
        "qmkkx":"旗木卡卡西","xie":"蝎","yfrz":"猿飞日斩","gsgj":"干柿鬼鲛",
        "yfasm":"猿飞阿斯玛","jd":"角都","ddl":"迪达拉","ysd":"药师兜",
        "qd":"千代","yzbzz":"宇智波佐助","mtk":"迈特凯","fd":"飞段",
        "dh":"大和","xrh":"夕日红","wal":"我爱罗","zj":"佐井",
        "rxnc":"日向宁次","kjl":"勘九郎","xwmr":"漩涡鸣人","cyy":"春野樱",
        "sj":"手鞠","nllw":"奈良鹿丸","qzy":"犬冢牙","rxct":"日向雏田",
        "lkl":"洛克李","ynzn":"油女志乃","szjy":"山中井野","tt":"天天",
        "qddc":"秋道丁次"}    
#忍术名字字典
tsu = {101:"拳头",102:"手里剑",201:"豪火球",301:"月读"}
list_ch = []   #角色数组,元素为ninja类
list_tsu = []  #忍术数组,元素为ninjutsu类
main_ch = []    #所选角色数组
enemy_ch = []   #所选对手数组
atk_sq = 101    #攻击方式序号
flag_atk = 0    #攻击方向
flag_lgc = 99    #逻辑控制标识符，0退出，1自动攻击，2手动攻击

#########################################
#读取角色、忍术数据
data = fileIO.readList(".\\ninja.data")
nins = fileIO.readList(".\\ninjutsu.data") 

#将角色数据写入list_ch数组,元素为ninja类
print "============================"
for i in range(len(data)):
    tmp = character.ninja(data[i][0],data[i][1],data[i][2],data[i][3],
                          data[i][4],data[i][5],data[i][6],data[i][7],
                          data[i][8])
    list_ch.append(tmp)

#将忍术数据写入list_tsu数组,元素为ninjutsu类
for i in range(len(nins)):
    tmp = character.ninjutsu(nins[i][0],nins[i][1],nins[i][2],nins[i][3],
                          nins[i][4],nins[i][5],nins[i][6],nins[i][7])
    list_tsu.append(tmp)

#逻辑控制
while(flag_lgc != 0):
    print "============================"
    if(flag_lgc == 1):#自动攻击
        print "****************************"
        print "OK, Let's do it!"
        print "****************************"
        #选择角色
        main_ch = methods.chs_main(name,list_ch)
        #选择对手
        enemy_ch = methods.chs_enemy(name,list_ch)
        #自动攻击
        print "============================"
        while( main_ch[1] > 0 and enemy_ch[1] > 0):
            #攻击方向计算，0为主角攻击对手，1为对手攻击主角
            flag_atk = methods.lgc_who(list_ch,main_ch,enemy_ch)
            #攻击类型判断，返回技能编号
            atk_sq = methods.lgc_atk(list_ch,main_ch,enemy_ch,list_tsu)
            if(flag_atk == 0):#主角攻击数值计算
                enemy_ch = methods.show_atk(name,list_ch,main_ch,
                                            enemy_ch,flag_atk,
                                            atk_sq,list_tsu,tsu)
                main_ch = methods.show_ckl(name,list_ch,main_ch,
                                            enemy_ch,flag_atk,
                                           atk_sq,list_tsu,tsu)
            elif(flag_atk == 1):#对手攻击数值计算
                main_ch = methods.show_atk(name,list_ch,main_ch,
                                            enemy_ch,flag_atk,
                                           atk_sq,list_tsu,tsu)
                enemy_ch = methods.show_ckl(name,list_ch,main_ch,
                                            enemy_ch,flag_atk,
                                            atk_sq,list_tsu,tsu)
            else:
                pass
            #显示当前角色数据
            methods.show_ch(name,list_ch,main_ch,enemy_ch)
            raw_input()#用输入实现暂停
    elif(flag_lgc == 2):#手动攻击
        print "============================"
        print "not yet"
    else:
        methods.show_list(name,list_ch)
    #循环控制
    flag_lgc = 99  #重置
    print "============================"
    print "0(quit), 1(auto attack), 2(manual attack)"
    try:
        flag_lgc = int(raw_input("Please input :"))
    except:
        pass
