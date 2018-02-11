#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:47:42 2018

@author: yfkong

使用前准备：
1. 建立一个单独的文件夹,例如：在桌面新建一个名为Data Reader的文件夹；
2. 将本程序移动到该文件夹；

使用步骤：
1. 将含有PV数据txt文件的**文件夹**移动到Data Reader文件夹运行本程序即可得到输出的txt文件；
2. 可以直接复制该txt的内容到excel，orign等进行下一步分析；


注意：
1. 必须确保Data Reader文件夹下仅有一个含有需要读取数据的文件夹
2. 数据文件夹内仅有txt文件

如果不符合以上设置可能会运行出错，今后会进一步优化程序功能和稳定性，敬请期待。
"""
import os

def load_data(Filename):
    '''
    Filename: str,the data filename
    Return: a tuple including a dic and a list:
        the dic: name -> value (string), contains all the parameters. 
        the list has the I-V curve data (float). 
        list[0]: voltage data
        list[1]: current data
        
    '''
    data = []
    performance = {}
    IV = [[],[]]
    
    # load the datafile   
    inFile = open(Filename,'r')
    for line in inFile:
        data.append(line)
    inFile.close()
    
    # get performance data
    list_p =[]
    for i in (0 , 1, 3, 4):
        list_p.append(data[i].split('\t'))
    
    for list_0 in list_p:
        #print(list_0)
        for i in range(len(list_0)): 
            list_0[i] = list_0[i].strip() 
            '''
            cannot use: 
            for  string in list_0: 
                string = string.strip() here, 
            because iterative changing doesn't change the range
            '''
        
    for i in (0,2):
        for x in range(len(list_p[i])):
            performance[list_p[i][x]]=list_p[i+1][x]
            
    del performance['']
    
    # get IV curve
    for i in range(7,len(data)):
        IV[0].append(float(data[i].split('\t')[0].strip()))
        IV[1].append(float(data[i].split('\t')[1].strip()))
        
    # return a tuple including all data
    return (performance, IV)

def load_file(wd):
    '''
    wd: str, working directry, under the same directry of the python code
    return: a list of name and data tuples by load_data function
        
    '''
    
    file_list = os.listdir(wd)
    file_data =[]
    for file in file_list:
        file_data.append((file,load_data(wd+os.sep+file)))
    return file_data

decimal_num = 2
def list_data(wd):
    '''
    wd: str, working directry, under the same directry of the python code
    return: a txt file contains all the PV parameters 
        
    '''
    para_list = ['Voc (V)','Jsc (mA/cm2)','Fill Factor (%)','Efficiency (%)','R at Voc','R at Isc']
    data_output = open( wd+'.txt' , 'w')
    data_output.write('Folder\tNo.\tVoc(mV)\tJsc (mA/cm2)\tFF(%)\tEfficiency(%)\tRs\tRsh\n')
    file_data = load_file(wd)
    for data in file_data:
        para_data = wd + '\t'+data[0]+'\t'
        for i in range(len(para_list)):  
            if i == 0:
                para_data +=str(round(float(data[1][0][para_list[i]])*1000,decimal_num))+'\t'
            else:
                para_data += str(round(float(data[1][0][para_list[i]]),decimal_num))+'\t'
        data_output.write(para_data+'\n')       
    data_output.close()

cwd_list = os.listdir(os.getcwd())
for name in cwd_list:
    if name != '__pycache__' and os.path.isdir(name):
        wd = name
list_data(wd)
    
#list_data('20180207-K')

        

    
    
    
    