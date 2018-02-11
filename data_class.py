#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 21:44:50 2018

@author: yfkong
"""
import pylab as plt

class PV_cell_data(object):
    '''
    A container contains a single file of PV data.
    '''
    
    def __init__(self,filename):
        '''
        filename: string, a txt file contains one cell's data
        self.no:cell's label
        self.para_data: cell's parameters
        self.JV_data: cell's JV data
        '''
        self.para_data,self.IV_data = self.load_data(filename)
        
        if filename.endswith('.txt'):
            self.no = filename[:-4] # del '.txt'
        else:
            raise ValueError('This is not a txt file')
            
    def __str__(self):
        '''
        Display a string representation of cell's data.
        '''
        return 'CIGS thin film solar cell no.'+self.no
    
    def get_no(self):
        ''' str'''
        return self.no
            
    def get_para(self,key):
        '''
        key: string, the name of parameter
        return: str, need to be transferred into other format, eg. float.
        '''
        return self.para_data[key]
    
    def get_performance(self):
        '''
        return: a list including Voc, Jsc, FF, eff., Rs, Rsh
        '''
        item_list = ('Jsc (mA/cm2)','Fill Factor (%)','Efficiency (%)',
                'R at Voc','R at Isc')
        performance = []
        performance.append(round(float(self.get_para('Voc (V)'))*1e3,2))
        for i in item_list: 
            performance.append(round(float(self.get_para(i)),2))  
        return performance
        
    def get_J(self):
        l_J = []
        for i in range(len(self.IV_data[1])):
            J = round(self.IV_data[1][i]/
                      float(self.get_para('Sample Area'))*1e3,2)
            l_J.append(J)
        return l_J
    
    def get_V(self):
        l_V = []
        for i in range(len(self.IV_data[0])):
            V = round(self.IV_data[0][i]*1e3,2)
            l_V.append(V)
        return l_V
    
    def plot_JV(self):
        plt.plot(self.get_V(),self.get_J())
        
         
    def load_data(self,Filename):
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
    

        