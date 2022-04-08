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
    def printList(self):
        for gt in self.GateList:
            print(gt.getGateCharectaristics())
    def getFollowingGatePos(self,gt):
        for g in self.GateList:
            if (gt.getOutput() in g.getEntries()):
                return g.getPosition()

    def sortList(self):
        for gt in self.GateList:
            followingGatePos=self.getFollowingGatePos(gt)
            if (followingGatePos is not None):
                self.GateList[followingGatePos].setPosition(gt.getPosition()+1)

