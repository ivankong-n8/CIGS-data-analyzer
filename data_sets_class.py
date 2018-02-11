#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:48:00 2018

@author: yfkong
"""

import data_class
import os
import matplotlib.pyplot as plt


item_list = ('Voc (V)','Jsc (mA/cm2)','Fill Factor (%)','Efficiency (%)',
                'R at Voc','R at Isc')

class PV_series_data(object):
    '''
    from a folder import data for CIGS solar cells
    '''
    def __init__(self,foldername):
        '''
        foldername: string, a folder contains all cell's data
        self.series_name
        self.file_list
        self.cell_list: a list of cell object [PV_cell_data]
        self.group
        self.group_label
        self.sort_flag

        '''
        if os.path.isdir(foldername):
            self.series_name = foldername 
        else:
            raise ValueError('This is not a folder')
            
        self.file_list = os.listdir(self.series_name)
        
        print('There is/are: '+ str(len(self.file_list))+ ' file(s):\n')
        print(self.file_list)
        print('\n')

        self.cell_list = []
        os.chdir(foldername)
        # print(os.getcwd()) enter the child dir
        for i in self.file_list:
            self.cell_list.append(data_class.PV_cell_data(i))
        os.chdir(os.path.pardir)
        # print(os.getcwd()) back to the parent dir (the folder dir)
        
        self.group = {}
        self.group_label = []
        self.sort_flag = False
        
    def __str__(self):
        '''
        Display a string representation of a series of cells.
        '''
        string = 'The series '+ self.series_name +' of CIGS thin film solar cells.\n'
        string += 'This series contains '+str(len(self.cell_list))+' cells:\n'
        for i in self.cell_list:
            string +='\t' +i.get_no()+'\n '

        if self.sort_flag:
            string += 'Status: SORTED\n'
            string += 'Here are '+str(len(self.group)-1)+ ' groups:\n'
            for label in self.group:
                string += 'Group ' +'['+ label +']:\n'
                for cell in self.group[label]:
                    string += '\t'+ cell.get_no() + '\n'
                    
            
        else:
            string += 'Status: UNSORTED\n'
        return string
        
    def sort(self,group_label):
        '''
        group_label : list of labels (str)
        function:   sorting the cells into self.group.
                    switching the self.sort_flag to True
                    may sort cells by different condition for several times
        '''
        
        self.group_label = group_label
        
        # init the self.group
        self.group.clear()
        for label in self.group_label:
            self.group[label]=[]
        self.group['Unsorted']=[]
        
        for i in self.cell_list.copy():
            self.group[self.whichlabel(i.get_no())].append(i)
            
        self.sort_flag = True
        return self.sort_flag
        
    def whichlabel(self,no):
        '''
        group_label : list of labels (str)
        no: the number of the cell,splited by '-'
        Return: the label (str), if no label meets, return 'Unsorted'
        '''
        for i in no.split('-'):
            if i in self.group_label:
                return i
        else:
            return 'Unsorted'
        
    def get_data(self,item,cell_list_label = None):
        '''
        cell_list_label:str, self.cell_list or self.group[**]
        return: a list contains all the values of a specific item in the cell_list
        
        '''
        if cell_list_label == None:
            cell_list = self.cell_list
        else:
            cell_list = self.group[cell_list_label]
        value_list=[]
        for i in cell_list:
            if item == 'Voc (V)':
                value_list.append(round(float(i.get_para('Voc (V)'))*1e3,2))
            else:    
                value_list.append(round(float(i.get_para(item)),2))
        return value_list
    
    def get_performance(self,cell_list_label = None):
        '''
        cell_list_label:str, self.cell_list or self.group[**]
        item_list: global list 
        return: a dic contains all the bisic performance values of all cell in 
                the cell_list
        '''        
        performance_dict={}
        for item in item_list:
            performance_dict[item]=self.get_data(item,cell_list_label)
        return performance_dict
    
    def get_group_label(self):
        return self.group_label.copy()
    
    def get_plot_data(self):
        '''
        generate data for ploting
        '''
        data =[[],[]]
        data[0]=self.get_group_label()
        for label in group_label:
            data[1].append(self.get_performance(label))
        return data
    
    def get_boxplot(self):
        '''
        
        '''
        data = self.get_plot_data()
        for item in item_list:
            plt.figure()
            plt_data =[]
            max_list = []
            min_list = []
            for i in range(len(data[0])):
                plt_data.append(data[1][i][item])
                max_list.append(max(plt_data[i]))
                min_list.append(min(plt_data[i]))
                if item == 'R at Voc':
                   plt.text(i+1,0.95*min_list[i],str(min_list[i]),
                         horizontalalignment='center') 
                else:
                    plt.text(i+1, 1.1*max_list[i]-0.1*min_list[i],str(max_list[i]),
                         horizontalalignment='center')
            plt.boxplot(plt_data)
            plt.ylim(ymax=1.2*max(max_list)-0.2*min(min_list))
            if item == 'R at Voc':
                plt.ylim(ymin= 0.85*min(min_list))    
            plt.xticks(range(1,len(data[0])+1),data[0])
            plt.ylabel(item)
            plt.xlabel('Series Name')        
        plt.show()
        
    def get_boxplot_subplot(self,row_num,column_num):
        
        data = self.get_plot_data()
        plt.figure()
        sub_num = 0
        for item in item_list:
            sub_num += 1
            plt.subplot(row_num,column_num,sub_num)
            plt_data =[]
            max_list = []
            min_list = []
            for i in range(len(data[0])):
                plt_data.append(data[1][i][item])
                max_list.append(max(plt_data[i]))
                min_list.append(min(plt_data[i]))
                if item == 'R at Voc':
                   plt.text(i+1,0.95*min_list[i],str(min_list[i]),
                         horizontalalignment='center') 
                else:
                    plt.text(i+1, 1.1*max_list[i]-0.1*min_list[i],str(max_list[i]),
                         horizontalalignment='center')
            plt.boxplot(plt_data)
            plt.ylim(ymax=1.2*max(max_list)-0.2*min(min_list))
            if item == 'R at Voc':
                plt.ylim(ymin= 0.85*min(min_list))    
            plt.xticks(range(1,len(data[0])+1),data[0])
            plt.ylabel(item)
            plt.xlabel('Series Name')        
        plt.show()

if __name__ == '__main__':
        foldername ='20180207-K'
        group_label = ['MM_21', 'NR006_21','MM_22','NR006_22']
        a = PV_series_data(foldername)
        a.sort(group_label)
        print(a)
        a.get_boxplot()
        # a.get_boxplot_subplot(2,3)
        
        
