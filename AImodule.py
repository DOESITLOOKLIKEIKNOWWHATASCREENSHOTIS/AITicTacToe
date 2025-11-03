class classvalues:
    '''General varibles'''

    #Setting to false will prevent the AI from printing debug information.
    debugInformation = True

    #Standard the value a chance is set at when first created.
    standard = 100

    #If you want to AI to save to it's file. Setting this to false will mean once the program quits, the information is lost!
    saveToFile = True

    #The name of the file. DO NOT INCLUDE FILE EXTENSION OR IT WILL BREAK.
    fileName = "AIData" 

    #Makes a backup Save. Seting to False means there won't be any back up saves
    saveToBackUpFile = True

    #The name of the back up file 
    backUpFileName = "BACKUP.txt"

    #The chance to make back up file. High numbers means a lower chance to create a back up file, but also better performance. Should be a whole number
    backUpChance = 500

    '''Winner variables'''

    #Reward is how much a chance gets added to be more likely to picked later on.
    reward = 15

    #If the chance goes above or equal to stichup, the previous move will also get [reward varible] chance added to it 
    stichUp = 200

    #StichupMutipler is the mutipler that [reward variable] gets when affecting pervious moves.
    stichUpMutipler = 0.5

    #CapMax is the maximum number that a single move can achive. You should set this to be low when the AI is first starting out, and high when the AI starts to get good. 
    capMax = 500

    '''Loser variables'''

    #Condem is how much a chance gets subtracted by to be less likely to picked later on.
    condem = 100

    #If the chance goes above or equal to BleedThough, the previous move will also get [Condem varible] subtracted to it 
    bleedThough = 0.5

    #StichupMutipler is the mutipler that [reward] gets when affecting pervious moves.
    bleedThoughMutipler = 0.1

    #If any chance goes lower or equal to KILL variable, the chance gets set to the death varible. This is to make sure bad moves don't get picked and prevent a varaible 
    #from becoming 0
    KILL = 10

    #The varaible that any chance goes below KILL gets set to. DO NOT SET TO OR BELOW 0 OR IT WILL BREAK.
    death = 0.1

    '''Draw'''
    
    #When the game is a draw, the chance's value will subtracted or added to reach this number. If the chance's value is equal to drawValue, it will start
    #effecting previous moves.
    drawValue = 100
    
    #When the game is a draw, the chance's value will be added by drawReward unless it goes over drawValue. It that case, the chance will be sent to drawValue
    drawReward = 100
   
    #StichupMutipler is the mutipler that [drawReward] gets when affecting pervious moves that caused the draw.
    drawStichUpMutipler = 0.8 
   
    #When the game is a draw, the chance's value will be subtracted by drawCondem unless it goes under drawValue. It that case, the chance will be sent to drawValue
    drawCondem = 100

    #StichupMutipler is the mutipler that [drawCondem] gets when affecting pervious moves that caused the draw.
    drawBleedThough = 0.2

    #Keeps all the values that could be modifed so they can be reset after exectuion.
    resetdefault = {
        "standard" : standard,
        "reward" : reward,
        "stichup" : stichUp,
        "stichupMutipler" : stichUpMutipler,
        "capMax" : capMax,
        "condem" : condem,
        "bleedThough" : bleedThough, 
        "bleedThoughMutipler" : bleedThoughMutipler,
        "KILL" : KILL,
        "death" : death, 
        "drawValue" : drawValue, 
        "drawReward" : drawReward, 
        "drawStichupMutipler" : drawStichUpMutipler,
        "drawCondem" : drawCondem,
        "drawBleedThough" : drawBleedThough
    }

    def reset(self):
        self.Standard = self.resetdefault["standard"]
        self.reward = self.resetdefault["reward"]
        self.stichup = self.resetdefault["stichup"]
        self.stichupMutipler = self.resetdefault["stichupMutipler"]
        self.capMax = self.resetdefault["capMax"]
        self.condem = self.resetdefault["condem"]
        self.bleedThough = self.resetdefault["bleedThough"]
        self.bleedThoughMutipler = self.resetdefault["bleedThoughMutipler"]
        self.KILL = self.resetdefault["KILL"]
        self.death = self.resetdefault["death"]
        self.drawValue = self.resetdefault["drawValue"]
        self.drawReward = self.resetdefault["drawReward"]
        self.drawStichupMutipler = self.resetdefault["drawStichupMutipler"]
        self.drawCondem = self.resetdefault["drawCondem"]
        self.drawBleedThough = self.resetdefault["drawBleedThough"]
