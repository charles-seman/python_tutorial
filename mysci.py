# Read the data file

filename = "data/wxobs20170821.txt"

#----------#
# Method 1 #
#----------#

datafile = open(filename, 'r')

print(datafile.readline())
print(datafile.readline())
print(datafile.readline())
print(datafile.readline())

datafile.close()

#----------#
# Method 2 #
#----------#

datafile = open(filename, 'r')

data = datafile.read()

datafile.close()

#----------#
# Method 3 #
#----------#

# following "context manager" is recommended since it closes datafile for you

with open(filename, 'r') as datafile:
  data = datafile.read()

# DEBUG

#print(data)
#print(type(data))
#print("data")


