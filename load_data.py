#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:37:38 2018

@author: yfkong
"""

'''
    Filename: str,the data filename
    Return: a tuple including a dic and a list:
        the dic: name -> value (string), contains all the parameters. 
        the list has the I-V curve data (float). 
        list[0]: voltage data
        list[1]: current data
        
'''
def load_data(Filename):
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
    
    
    
    
    
    
            
        
        
        
