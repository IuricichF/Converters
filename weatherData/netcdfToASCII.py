#convert from a netcdf file to a regular grid (list of values) in ascii format

import netCDF4
import matplotlib.pyplot as plt
import math
import sys

#take the input file name
if(len(sys.argv) == 1):
    url_in = raw_input('Insert the path to the input file\n');
else:
    url_in = sys.argv[1]


#read nc data
nc = netCDF4.Dataset(url_in)

#output the variables stored
print "Variables stored in the netCDF file"
print nc.variables.keys()
print "\n"

#select the desired variables
readV = input('Please indicate the variables from which building your files. Use array notation, i.e. [1,3,5]\n');


#create one new file (extension .ascii) for each chosen variable
for fields in readV:

    #read variable
    topo = nc.variables[nc.variables.keys()[fields]][:,:,:]

    #create new file
    f1=open(url_in + "_" + str(nc.variables.keys()[fields]) + ".ascii", 'w')
    for grid in topo:
        for line in grid:
            for v in line:
                #if the value is nan put -1
                value = float(v)
                if math.isnan(value):
                    f1.write(str(-1)+" ")
                else:
                    f1.write(str(value)+" ")
