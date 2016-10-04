#!/bin/python
# -*- coding: utf-8 -*-

# Fenrir TTY screen reader
# By Chrys, Storm Dragon, and contributers.

from core import debug
from utils import word_utils
initialized = False
try:
    import enchant
    initialized = True
except:
    pass
    
class command():
    def __init__(self):
        self.language = ''
        self.spellChecker = None
    def initialize(self, environment):
        self.env = environment
        self.updateSpellLanguage()
    def shutdown(self):
        pass 
    def getDescription(self):
        return 'adds the current word to the exceptions dictionary'        
    def updateSpellLanguage(self):  
        self.spellChecker = enchant.Dict(self.env['runtime']['settingsManager'].getSetting('general', 'spellCheckLanguage'))
        self.language = self.env['runtime']['settingsManager'].getSetting('general', 'spellCheckLanguage')      
    
    def run(self):
        if not initialized:
           self.env['runtime']['outputManager'].presentText('pychant is not installed', interrupt=True) 
           return
        if self.env['runtime']['settingsManager'].getSetting('general', 'spellCheckLanguage') != self.language:
            try:
                self.updateSpellLanguage()
            except:
                return    

        cursorPos = self.env['runtime']['cursorManager'].getReviewOrTextCursor()
            
        # get the word
        newContent = self.env['screenData']['newContentText'].split('\n')[cursorPos['y']]
        x, y, currWord =  word_utils.getCurrentWord(cursorPos['x'], 0, newContent)                  

        if currWord != '':
            if self.spellChecker.is_added(currWord):
                self.env['runtime']['outputManager'].presentText(currWord + ' is already in dict',soundIcon='Cancel', interrupt=True)                
            else:
                self.spellChecker.add(currWord)             
                self.env['runtime']['outputManager'].presentText(currWord + ' added',soundIcon='Accept', interrupt=True)               

    def setCallback(self, callback):
        pass