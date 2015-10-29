# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:04:03 2015

@author: Magnus Dahl
"""

import datetime as dt
import os
import pickle

class Taxfee(object):
    """ This is a class to made to hold, manipulate and access data
        about a tax of fee over time.
        
        """ 
        
    def __init__(self, name, loadfile=None, loadpath=''):
        """ Initiate with a name for the tax of fee. Create empty
            or load a saved pickle file into the field data. 
            
            """
            
        self.name = name
        
        if loadfile==None:
            self.data = []
        else:
            with open(loadpath+loadfile) as currentfile:
                self.data = pickle.load(currentfile)
            
        
    def add_row(self, val, valid_from, valid_to):
        """ Adds a new row to the data in the form of a dictionary with
            the keys val, valid_from, valid_to.
            
            """
            
        self.data.append({'val':float(val), 'valid_from':valid_from, 'valid_to':valid_to})
        
        
    def add_row_quick(self, val, year_from, month_from, day_from,\
                                 year_to, month_to, day_to):
        """ Quick way to add row """
        
        self.add_row(val, dt.date(year_from, month_from, day_from), \
                          dt.date(year_to, month_to, day_to))
                          
    def del_row(self, index):
        """ Delete row of the specified index. """
        self.data.remove(self.data[index])       
        
    def save_data(self, filename, path='', overwrite=False):
        """ Save the content of the field data to the specified file.
            overwrite option must be set to True in order to overwrite
            existing files.
            
            """
            
        if not os.path.isfile(path+filename):
            print "Creating and writing to: ", path+filename
            with open(path+filename, 'w') as currentfile:
                pickle.dump(self.data, currentfile)
        else:
            if overwrite:
                print "Overwriting ", path+filename                
                with open(path+filename, 'w') as currentfile:
                    pickle.dump(self.data, currentfile)
            else:
                print """No write performed: 
                         File already exists, to overwrite 
                         call again with overwrite=True"""
                         
    def get_val(self, date):
        """ The the value of the tax of fee at the specified date.
            Raises execption if no value is found.
            
            """
            
        for row in self.data:
            if row['valid_from'] <= date <= row['valid_to']:
                return row['val']
                
        raise Exception, "No value for the given date: %s, for %s"% (str(date), self.name)
        