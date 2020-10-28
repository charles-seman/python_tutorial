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

data = []

with open(filename, 'r') as datafile:

    # read the first three lines (header)
    #for i in [ 0, 1, 2 ]:
    for _ in range(3):
        print(_)
        datafile.readline()
    
    # read and parse the rest of the file
    for line in datafile:
        datum = line.split() #(',') or ('/t')
        data.append(datum)

# DEBUG

#for datum in data:
#    print(datum)

# above prints a lot of data!

# DEBUG

#print(data[0])
#print(data[9])
#print(data[-1]) # last index (-2 second to last)

#print(data[0:10])

for datum in data[0:10]:
    print(datum)

for datum in data[:10]:
    print(datum)

for datum in data[0:10:2]:
    print(datum)

print(data[8][4]) # doesn't work: print(data[8[4]])

#print(data[8][4][0]) # first character

print(data[8][:5]) # first 4 elements
print(data[8][::2]) # every other element

#print(data[5:8][4])
# gives:
#Traceback (most recent call last):
#  File "mysci.py", line 91, in <module>
#    print(data[5:8][4])
#IndexError: list index out of range

print(data[5:8][0])

print(data[5])
