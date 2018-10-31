def parse_sessions(inputFile):
    resultDict = {} #dict is a useful data structure for this case
    splitFile = inputFile.split('\n') #split the string into a list. Separate the string on every newline
    for line in splitFile:
        l = line.strip() #using a stripped line normalizes the left side whitespace in order to count the columns accurately
        if 'Capacity=' in line: #locate the begining of a chunk
            key = l[:5] #slice the string to include the first 5 characters for the timestamp hh:mm
        if 'Total	Sessions' in line:
            splitLine = l.split('	')
            value = int(splitLine[4]) #must include the explicit conversion to int or the max function doesnt work right
            resultDict[key] = value
    return resultDict #return Dict of Key = Timestamp, Value = Total Sessions
def max_session(inputDict): #locates the highest value of the list passed in
    keys = inputDict.keys()
    values = inputDict.values()
    maxValue = max(values)
    maxSession = []
    for key, value in inputDict.items():
        if value == maxValue:
            maxSession.append(key + ': ' + str(value)) #explicitly change the session int back to string for printing
    return maxSession #returns a list of a timestamp and a value
with open('SIPCalls.txt', 'r') as f:
    file = f.read()
intermediate = parse_sessions(file)
result = max_session(intermediate)
print(result)        
