#!/bin/python
from utils import word_utils

class command():
    def __init__(self):
        self.initialized = False
        try:
            import enchant
            self.initialized = True
        except:
            pass
    
    def run(self, environment):
        if not environment['runtime']['settingsManager'].getSettingAsBool(environment, 'general', 'autoSpellCheck'):
            return environment

        if not self.initialized:
           environment['runtime']['outputManager'].presentText(environment, 'pychant is not installed', interrupt=True) 
        
        spellChecker = enchant.Dict(environment['runtime']['settingsManager'].getSetting(environment, 'general', 'spellCheckLanguage'))
   
        # just when cursor move worddetection is needed
        if environment['screenData']['newCursor']['x'] == environment['screenData']['oldCursor']['x']:
            return environment 
            
        # for now no new line
        if environment['screenData']['newCursor']['y'] != environment['screenData']['oldCursor']['y']:
            return environment 
        if len(environment['screenData']['newDelta']) > 1:
            return environment            
            
        # TTY Change is no new word
        if environment['screenData']['newTTY'] != environment['screenData']['oldTTY']:
            return environment
            
        # first place could not be the end of a word
        if environment['screenData']['newCursor']['x'] == 0:
            return environment
            
        # get the word
        newContent = environment['screenData']['newContentText'].split('\n')[environment['screenData']['newCursor']['y']]
        x, y, currWord =  word_utils.getCurrentWord(environment['screenData']['newCursor']['x'], 0, newContent)                  
        # was this a typed word?
        if environment['screenData']['newDelta'] != '':
            if not(newContent[environment['screenData']['oldCursor']['x']].strip() == '' and x != environment['screenData']['oldCursor']['x']):
                return environment
        else:
        # or just arrow arround?
            if not(newContent[environment['screenData']['newCursor']['x']].strip() == '' and x != environment['screenData']['newCursor']['x']):
                return environment            

        if currWord != '':
            if not spellChecker.check(currWord):
                environment['runtime']['outputManager'].presentText(environment, 'misspelled', interrupt=True)

        return environment
    def setCallback(self, callback):
        pass
    def shutdown(self):
        pass