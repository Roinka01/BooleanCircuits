import re

class filePrsing():
    def __init__(self):
        pass
    def getGates(self):
        gates= {'and','or','not'}
        listOfGates=[]
        with open("demofile.txt", "r") as fo:
            for line in fo:
                line=line.lower()
                if ' wire' in line:
                    #print(line)
                    beginInd=line.find('wire')+'wire'.__len__()
                    endInd=line.find('\n')
                    outPuts=re.split(',|;',line[beginInd:endInd-1])
                    #print(outPuts)
                    continue
                if ' and' in line:
                    #print(line)
                    listOfGates.append('AND')
                elif ' or' in line:
                    #print(line)
                    listOfGates.append('OR')
                elif ' not' in line:
                    #print(line)
                    listOfGates.append('NOT')
                else:
                    gateTpe=''
                    continue
                outIndxBegin=line.find('(')
                outIndxEnd = line.find(',')
                out.append(line[outIndxBegin+1:outIndxEnd])
        print (listOfGates)
        print(out)
        print(outPuts)

        if __name__ == '__main__':
            fp=filePrsing()
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


