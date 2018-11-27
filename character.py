#!/usr/bin/python
# -*- coding: UTF-8 -*-
#角色类定义

sex = ("male","female")

class hero(object):
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age

    def show(self):
        print self.name,self.sex,self.age


class ninja(object):
    def __init__(self,name="",ren=1,ti=1,huan=1,xian=1,li=1,su=1,jing=1,yin=1):
        self.name = name  #名字
        self.ren = int(ren)  #忍：表示精通忍术的能力以及熟练使用的能力
        self.ti = int(ti)  #体：表示精通体术的能力以及熟练使用的能力
        self.huan = int(huan)  #幻：表示精通幻术的能力以及熟练使用的能力
        self.xian = int(xian)  #贤：表示知识的多少和IQ的高低,用作技能成功率计算
        self.li = int(li)  #力：以腕力和足力为始，来表示全身的体力
        self.su = int(su)  #速：表示速度以及动作和反应的灵敏度
        self.jing = int(jing)  #精：表示作为查克拉基础的“精力”
        self.yin = int(yin)  #印：表示印以及手印的精通及熟练度
    def show(self):
        print self.name,self.ren,self.ti,self.huan,self.xian,self.li,self.su,self.jing,self.yin


class ninjutsu(object):
    def __init__(self,name,chakra,scope,diff,kind,nature,damage,buff):
        self.name = int(name)  #名称
        self.chakra = int(chakra)  #查克拉消耗
        self.scope = int(scope)  #距离范围，1~10
        self.diff = int(diff)  #难度，1~10
        self.kind = int(kind)  #攻防种类,体术1，忍术2，幻术3
        self.nature = int(nature)  #属性，无0，火1，风2，雷3，土4，水5
        self.damage = int(damage)  #伤害值
        self.buff = int(buff)  #特殊效果

