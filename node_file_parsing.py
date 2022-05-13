import re
from Gate import Gate
from ConcatenatedGateList import ConcatenatedGateList

class filePrsing():
    def __init__(self, fileName) -> object:
        """
        :rtype: object
        """
        self._fileName=fileName
        pass

    def getGates(self):
        gates = {'and', 'or', 'not'}
        listOfGates = []
        inputs = []
        outPuts = []
        outputPair = []
        _list=ConcatenatedGateList()
        i=0
        with open(self._fileName, "r") as file:
            for line in file:
                line = line.lower()
                if 'wire' in line:
                    # beginInd = line.find('wire') + 'wire'.__len__()
                    # endInd = line.find('\n')
                    # outPuts = re.split(',|;', line[beginInd:endInd - 1])

                    _list.addWire(line)
                    #wireList=line[line.find('wire')+4:].split(',')
                    #listOfGates.append('OUTPUT')
                    #inputPair = [outputName, outputName]
                    #inputPair.append(i)
                    #inputs.append(inputPair)
                    #outputPair = ["NoName",i]
                    #outPuts.append(outputPair)
                    #_list.addGate(Gate("OUTPUT", inputs[i][0],inputs[i][1],outPuts[i][0], 0))
                    #i += 1
                elif 'endmodule' not in line and 'module' in line:
                    outputName=line[line.find('output')+6:line.find(',')].strip()
                    ind1 = line.find('input') + 5  # first input
                    ind2 = line[ind1:].find(',') + ind1
                    input1 = line[ind1:ind2].strip()
                    ind3 = line[ind2:].find("input") + 5 + ind2  # second input
                    ind4 = line[ind3:].find(')') + ind3
                    input2 = line[ind3:ind4].strip()
                    ins=[input1,input2]
                    _list.setInputNames(ins)
                    _list.setOutputName(outputName)
                    #Add the first circle input to the list
                    listOfGates.append('INPUT')
                    inputPair = ["CircleInput"]
                    inputPair.append(i)
                    inputs.append(inputPair)
                    outputPair = [input1, i]
                    outPuts.append(outputPair)
                    _list.addGate(Gate("INPUT", inputs[i][0],"",outPuts[i][0], 0))
                    i += 1
                    # Add the second circle input to the list
                    listOfGates.append('INPUT')
                    inputPair = ["CircleInput"]
                    inputPair.append(i)
                    inputs.append(inputPair)
                    outputPair = [input2, i]
                    outPuts.append(outputPair)
                    _list.addGate(Gate("INPUT", inputs[i][0], "", outPuts[i][0], 0))
                    i += 1
                    #     inputs = line[line.find(',') :line.find(')')].split(',')
                    #     #_list.addGate(Gate("OUTPUT", '','', outputName, 0))
                    #     #i += 1
                    #     # print("output=",outputName)
                    #     # print("inputs=",inputs)
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
                    ind1 = line.find(',') + 1
                    ind2 = line.find(')')
                    subLine = line[ind1:ind2]
                    inputPair = subLine.split(',')
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

