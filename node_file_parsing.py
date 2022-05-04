import re
from Gate import Gate
from ConcatenatedGateList import ConcatenatedGateList

class filePrsing():
    def __init__(self) -> object:
        """

        :rtype: object
        """
        pass

    def getGates(self):
        gates = {'and', 'or', 'not'}
        listOfGates = []
        inputs = []
        outPuts = []
        outputPair = []
        _list=ConcatenatedGateList()
        i=0
        with open("demofile.txt", "r") as file:
            for line in file:
                line = line.lower()
                if 'wire' in line:
                    # beginInd = line.find('wire') + 'wire'.__len__()
                    # endInd = line.find('\n')
                    # outPuts = re.split(',|;', line[beginInd:endInd - 1])
                    _list.addWire(line)
                elif 'time' in line:
                    _list.addTimeScale(line)
                elif ' and' in line:
                    listOfGates.append('AND')
                    inputPair=line[line.find(',')+1:line.find(')')].split(',')
                    inputPair.append(i)
                    inputs.append(inputPair)
                    outputPair=[line[line.find('(')+1:line.find(',')],i]
                    outPuts.append(outputPair)
                    #ConcatenatedGateList.append(Gate("AND", inputs[i][0],inputs[i][1],outPuts[i][0],i))
                    _list.addGate(Gate("AND", inputs[i][0],inputs[i][1],outPuts[i][0],0))
                    i += 1
                elif ' or' in line:
                    listOfGates.append('OR')
                    inputPair = line[line.find(',') + 1:line.find(')')].split(',')
                    inputs.append(inputPair)
                    inputPair.append(i)
                    outputPair=[line[line.find('(') + 1:line.find(',')],i]
                    outPuts.append(outputPair)
                    #ConcatenatedGateList.append(Gate("OR", inputs[i][0], inputs[i][1], outPuts[i][0], i))
                    _list.addGate(Gate("OR", inputs[i][0], inputs[i][1], outPuts[i][0], 0))
                    i += 1
                elif ' not' in line:
                    listOfGates.append('NOT')
                    in1 = line.find(',') + 1
                    in2 = line.find(')')
                    in3 = line[in1:in2]
                    inputPair = in3.split(',')
                    inputPair.append(i)
                    inputs.append(inputPair)
                    outputPair=[line[line.find('(') + 1:line.find(',')],i]
                    outPuts.append(outputPair)
                    #ConcatenatedGateList.append(Gate("NOT", inputs[i][0],"", outPuts[i][0], 0))
                    _list.addGate(Gate("NOT", inputs[i][0],"", outPuts[i][0], 0))
                    i += 1
                else:
                    gateTpe = ''
                    continue

        return _list


# if __name__ == '__main__':
#     fp = filePrsing()
#     fp.getGates()

