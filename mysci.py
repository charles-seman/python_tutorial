# Read the data file

filename = "data/wxobs20170821.txt"

#----------#
# Method 1 #
#----------#

#datafile = open(filename, 'r')

#print(datafile.readline())
#print(datafile.readline())
#print(datafile.readline())
#print(datafile.readline())

#datafile.close()

#----------#
# Method 2 #
#----------#

#datafile = open(filename, 'r')

#data = datafile.read()

#datafile.close()

#----------#
# Method 3 #
#----------#

# following "context manager" is recommended since it closes datafile for you

#with open(filename, 'r') as datafile:
#  data = datafile.read()

# DEBUG

#print(data)
#print(type(data))
#print("data")

#-------------------------------------------------

data = {'date':[], 'time':[], 'tempout':[]}

#time = data['time']

with open(filename, 'r') as datafile:

    # read the first three lines (header)
    #for i in [ 0, 1, 2 ]:
    for _ in range(3):
        #print(_)
        datafile.readline()
    
    # read and parse the rest of the file
    for line in datafile:
        split_line = line.split() #(',') or ('/t')
        data['date'].append(split_line[0])
        data['time'].append(split_line[1])
        data['tempout'].append(float(split_line[2]))
