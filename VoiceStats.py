def parse_sessions(inputFile):
    inner = False
    resultList = list()
    
    if not isinstance(inputFile, list): #determines if the variable passed in is already a list
        splitFile = inputFile.split('\n') #split the string into a list. Separate the string on ever newline
    else:
        splitFile = inputFile
    itemList = list()
    for line in splitFile:
        if 'Capacity=' in line: #locate the begining of a chunk
            inner = True #set to true to capture other data point
            splitLine = line.strip().split(' ')
            itemList.append(splitLine[0])
        if inner and 'Total Sessions' in line:
            splitLine = line.split(' ')
            x = 1
            for line in splitLine:
                if line == '':
                    splitLine.pop(splitLine.index(line))            
            itemList.append(splitLine[3]) #adds datapoint to inner list
            inner = False #Set to false to show it's done with that time stamp
            resultList.append(itemList) #adds innerlist to result list
            itemList = list()
    return resultList #list returned is a list of lists containing a timestamp, and that times highest value

def max_session(inputList): #locates the highest value of the list passed in
    maxSession = list()
    current = 0
    max = 0
    for item in range(len(inputList)):
        session = inputList[item]
        current = int(session[1])
        if current > max:
            maxSession = inputList[item]
            max = current
    return maxSession #returns a list of a timestamp and a value


if __name__ == '__main__':
    #Read in a file named SIPCalls.txt
    with open('SIPCalls.txt', 'r') as f:
        file = f.read()
    intermediate = parse_sessions(file)
    result = max_session(intermediate)
    print(result)        
