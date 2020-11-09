# Read the data file

filename = "data/wxobs20170821.txt"

# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7}

# Data types for each column (only if non-string)
types = {'tempout':float, 'windspeed':float}

# Initialize my data variable
data = {}
for column in columns:
    data[column] = []

with open(filename, 'r') as datafile:

    # read the first three lines (header)
    for _ in range(3):
        #print(_)
        datafile.readline()
    
    # read and parse the rest of the file
    for line in datafile:
        split_line = line.split() #(',') or ('/t')
        for column in columns:
            i = columns[column]
            t = types.get(column,str)
            value = t(split_line[i])
            data[column].append(value)

# DEBUG

print(data['tempout'])
