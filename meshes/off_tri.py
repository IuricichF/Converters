#convert a triangle mesh from .off to .tri format and viceversa

import sys
import os

if(len(sys.argv) == 1):
    url_in = raw_input('Insert the path to the input file\n');
    url_out = raw_input('Insert the path to the output file\n');
elif(len(sys.argv) == 2):
    url_in = sys.argv[1]
    url_out = raw_input('Insert the path to the output file\n');
else:
    url_in = sys.argv[1]
    url_out = sys.argv[2]


infile = open(url_in, 'r')
outfile = open(url_out, 'w')


if ".off" in url_in:

    line = infile.readline();
    line = infile.readline();
    simplexes = line.split();

    outfile.write(simplexes[0]+"\n");

    for i in range(0,int(simplexes[0])):
        outfile.write(infile.readline())

    outfile.write(simplexes[1]+"\n")

    for i in range(0,int(simplexes[1])):
        line = infile.readline()
        vertices = line.split()
        outfile.write(vertices[1]+" "+vertices[2]+" "+vertices[3]+"\n")
else:

    outfile.write("OFF\n");
    vertices = [];
    nV = infile.readline().split();
    for i in range(0,int(nV[0])):
        vertices.append(infile.readline())

    nT = infile.readline().split();
    outfile.write(nV[0] + " " + nT[0] + " 0\n");

    for i in vertices:
        outfile.write(i);

    for i in range(0,int(nT[0])):
        line = infile.readline()
        vertices = line.split()
        outfile.write("3 "+vertices[0]+" "+vertices[1]+" "+vertices[2]+"\n")

infile.close()
outfile.close()
