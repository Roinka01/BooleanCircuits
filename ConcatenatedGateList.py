import os, sys
from Gate import Gate

class ConcatenatedGateList:
    def __init__(self):
        self.GateList=[]
        self.len=0
    def addGate(self, gate ):
        self.GateList.append(gate)
        self.len+=1
    def getGateList(self):
        return self.GateList
    def getConnectedGateInput(self,currGate):
        outputGateName = currGate.getOutput()
        ind=0
        for g in self.getGateList():
            if outputGateName in g.getListEntries():  # following gate found
                if outputGateName == g.getEntries()[0]:
                    return ind,0
                elif outputGateName == g.getEntries()[1]:
                    return ind, 1
            ind+=1
        return 0,0

    def printList(self):
        for gl in self.GateList:
            print(gl.getGateCharectaristics())
    def getListLength(self):
        return self.len
    def advanceGate(self,g,newPos):
        g.setPosition(newPos)
        #print(g.getGateCharectaristics())
        for gate in self.getGateList():
             if (g.getOutput() in gate.getEntries()):
               # gate.setPosition(currGate.getPosition()+1)
                 self.advanceGate(gate, g.getPosition() + 1)
    def switchGateInd(self,ind1,ind2):
        tmp=self.GateList[ind1]
        self.GateList[ind1]=self.GateList[ind2]
        self.GateList[ind2]=tmp

    def sortList(self):
        for currGate in self.getGateList():
            for gate in self.getGateList():
                if (currGate.getOutput() in gate.getEntries()):
                    self.advanceGate(gate,currGate.getPosition()+1)
        for i in range(0,self.len-1):
            for j in range(0,self.len-i-1):
                if (self.GateList[j].getPosition()>self.GateList[j+1].getPosition()):
                    self.switchGateInd(j,j+1)
