

class filePrsing():
    def __init__(self):
        pass
    def getGates(self):
        f = open("demofile.txt", "r")
        txt = f.read()
        num_of_and = txt.count('and ')
        num_of_or = txt.count(' or ')
        num_of_not = txt.count('not ')
        #print("num_of_not={0},num_of_or={1}, num_of_and={2}".format(num_of_not, num_of_or, num_of_and))
        f.close()
        return num_of_and, num_of_or, num_of_not




