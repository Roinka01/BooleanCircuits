import os, sys

class Gate():
    def __init__(self, _type="", _entry1="", _entry2="", _output="", _pos=0, _nextGateEntry=None):
        self.GateType=_type.strip()
        self.FirstEntry=_entry1.strip()
        self.SecondEntry=_entry2.strip()
        self.GateOutput=_output.strip()
        self.position=_pos
        self.outputPtr=_nextGateEntry
    def setGateType(self, _type):
        GateType = _type.strip()
        print(GateType)
    def setPosition(self,_pos):
        self.position=_pos
    def setEntries(self, _entry1, _entry2=None):
        FirstEntry = _entry1.strip()
        SecondEntry = _entry2.strip()
        print(FirstEntry,",",SecondEntry)
    def setOutput(self, _output):
        GateOutput = _output.strip()
    def setOutputPtr(self, _nextGateEntry):
        outputPtr = _nextGateEntry
    def getEntries(self):
        return self.FirstEntry, self.SecondEntry
    def getListEntries(self):
        return self.FirstEntry+" , "+ self.SecondEntry
    def getOutput(self):
        return self.GateOutput
    def getOutputPtr(self):
        return self.outputPtr
    def getPosition(self):
        return self.position
    def getPositionStr(self):
        return str(self.position)
    def getGateType(self):
        return self.GateType
    def getGateCharectaristics(self):
        return "Gate type is: "+self.GateType+". Gate entries are: "+self.getEntries().__str__()+\
               ". Gate output is: "+self.getOutput()+". Gate position is: "+self.getPositionStr()


