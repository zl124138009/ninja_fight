#!/usr/bin/python
# -*- coding: UTF-8 -*-
#文件输入输出方法定义

import os

# 遍历指定目录，返回文件列表
def listFile(path,method=2,show=0):
    if not (isinstance(path,(str)) and isinstance(method,(int)) and isinstance(show,(int))):
        print "Error:输入类型错误"
    else:
        try:
            pathDir = os.listdir(path)
        except:
            print "Error:路径错误,注意'\\'转义"
        else:
            fileList=[]
            if ( method == 1 ): # 带路径
                for fileseq,filename in enumerate(pathDir):
                    filepath = os.path.join('%s\\%s' % (path, filename))
                    filepath = filepath.decode('gbk') # 兼容中文
                    fileList.append(filepath)
                    if show == 1: # 输出结果
                        print ("%d %s" % (fileseq,filepath))
                    else:
                        pass
            elif ( method == 2 ): # 不带路径
                for fileseq,filename in enumerate(pathDir):
                    filename = filename.decode('gbk')
                    fileList.append(filename)
                    if show == 1:
                        print ("%d %s" % (fileseq,filename))
                    else:
                        pass
            else:
                pass
            return fileList

# 计算文件行数，返回行数
def sumLines(filepath):
    if not isinstance(filepath,(str)):
        print "Error:输入类型错误"
    else:
        fopen = open(filepath,'r')
        lines = len(fopen.readlines())
        fopen.close()
        return lines

# 读取文件内容并打印
def readFile(filepath):
    if not isinstance(filepath,(str)):
        print "Error:输入类型错误"
    else:
        fopen = open(filepath, 'r') # r 代表read
        for eachLine in fopen:
            print eachLine.strip('\r\n')
        fopen.close()

# 输入多行文字，添加模式写入指定文件并保存
def inputFile(filepath):
    if not isinstance(filepath,(str)):
        print "Error:输入类型错误"
    else:
        fopen = open(filepath, 'a')
        print "\r请输入多行文字(新行输入--save保存)"
        while True:
            aLine = raw_input()
            if aLine != "--save" and aLine != "--s":
                fopen.write('%s\n' % (aLine))
            else:
                print "文件保存成功"
                break
        fopen.close()

# 写入一序列的字符串
def writeFile(string,filepath):
    if not (isinstance(string,(str)) and isinstance(filepath,(str))):
        print "Error:输入类型错误"
    else:
        try:
            fopen = open(filepath,'a')
            string = string + "\n"
            fopen.writelines(string)
        except:
            print ("Error:写入文件失败").decode('UTF-8')
        else:
            print ("文件保存成功").decode('UTF-8')
            fopen.close()
        finally:
            pass

# 读取文件内容并返回列表
def readList(filepath):
    if not isinstance(filepath,(str)):
        print "Error:输入类型错误"
    else:
        fopen = open(filepath, 'r') # r 代表read
        data = fopen.readlines()
        for idx,eachLine in enumerate(data):
            data[idx] = eachLine.split()
        fopen.close()
        return data
    

