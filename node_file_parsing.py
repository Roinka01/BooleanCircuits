import re
from Gate import Gate

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
        ConcatenatedGateList=[]
        i=0
        with open("demofile.txt", "r") as fo:
            for line in fo:
                line = line.lower()
                if ' wire' in line:
                    # print(line)
                    # beginInd = line.find('wire') + 'wire'.__len__()
                    # endInd = line.find('\n')
                    # outPuts = re.split(',|;', line[beginInd:endInd - 1])
                    # print(outPuts)
                    continue
                if ' and' in line:
                    # print(line)
                    listOfGates.append('AND')
                    inputPair=line[line.find(',')+1:line.find(')')].split(',')
                    inputPair.append(i)
                    inputs.append(inputPair)
                    outputPair=[line[line.find('(')+1:line.find(',')],i]
                    #print(outputPair)
                    outPuts.append(outputPair)
                    ConcatenatedGateList.append(Gate("AND", inputs[i][0],inputs[i][1],outPuts[i][0],i))
                    #print("And {}".format(i))
                    #print(outPuts)
                    i += 1
                elif ' or' in line:
                    # print(line)
                    listOfGates.append('OR')
                    inputPair = line[line.find(',') + 1:line.find(')')].split(',')
                    inputs.append(inputPair)
                    inputPair.append(i)
                    outputPair=[line[line.find('(') + 1:line.find(',')],i]
                    outPuts.append(outputPair)
                    ConcatenatedGateList.append(Gate("OR", inputs[i][0], inputs[i][1], outPuts[i][0], i))
                    #print("Or {}".format(i))
                    i += 1
                elif ' not' in line:
                    # print(line)
                    listOfGates.append('NOT')
                    in1 = line.find(',') + 1
                    in2 = line.find(')')
                    in3 = line[in1:in2]
                    inputPair = in3.split(',')
                    inputPair.append(i)
                    inputs.append(inputPair)
                    outputPair=[line[line.find('(') + 1:line.find(',')],i]
                    outPuts.append(outputPair)
                    ConcatenatedGateList.append(Gate("NOT", inputs[i][0],"", outPuts[i][0], i))
                    #print("Not {}".format(i))
                    i += 1
                else:
                    gateTpe = ''
                    continue
                # outIndxBegin=line.find('(')
                # outIndxEnd = line.find(',')
                # out.append(line[outIndxBegin+1:outIndxEnd])
        for gt in ConcatenatedGateList:
            #print(gt.GateType,gt.getPositionStr(),gt.getEntries(),gt.getOutput())
            print(gt.getGateCharectaristics())
        print(listOfGates)
        print("inputs={}".format(inputs))
        # print(out)
        print("outPuts={}".format(outPuts))

if __name__ == '__main__':
    fp = filePrsing()
    fp.getGates()
        #     if (gates[0])
        #
        # txt = f.read()
        # num_of_and = txt.count('and ')
        # num_of_or = txt.count(' or ')
        # num_of_not = txt.count('not ')
        # #print("num_of_not={0},num_of_or={1}, num_of_and={2}".format(num_of_not, num_of_or, num_of_and))
        # f.close()
        # return num_of_and, num_of_or, num_of_not
        #
        #
