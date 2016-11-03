import sys
import os

#convert a triangle mesh from .vtk to .off format and viceversa

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

vertices = []
simplices = []

if ".off" in url_in:

    line = infile.readline();
    line = infile.readline();
    simplexes = line.split();

    for i in range(0,int(simplexes[0])):
        vertices.append(infile.readline())

    for i in range(0,int(simplexes[1])):
        simplices.append(infile.readline())


    outfile.write("# vtk DataFile Version 2.0\n\n")
    outfile.write("ASCII\n")
    outfile.write("DATASET UNSTRUCTURED_GRID\n")
    outfile.write("POINTS " + simplexes[0] + " float\n")

    for ind in range(0,int(simplexes[0])):
        outfile.write(vertices[ind])

    outfile.write("CELLS " + simplexes[1] + " " + repr(int(simplexes[1])*4) +"\n")

    for ind in range(0,int(simplexes[1])):
        outfile.write(simplices[ind])


    outfile.write("CELL_TYPES " + simplexes[1] + "\n")

    for i in range(int(simplexes[1])):
        outfile.write(repr(5) + " "),
    outfile.write("\n")

else:
    line = infile.readline();
    line = infile.readline();
    line = infile.readline();
    line = infile.readline();
    line = infile.readline();
    vertex = line.split()

    print vertex

    for i in range(0,int(vertex[1])):
        vertices.append(infile.readline());

    line = infile.readline();
    triangle = line.split();

    for i in range(0,int(triangle[1])):
        simplices.append(infile.readline())

    outfile.write("OFF\n")
    outfile.write(vertex[1]+" "+triangle[1]+" 0\n")

    for ind in range(0,int(vertex[1])):
        outfile.write(vertices[ind])

    outfile.write(triangle[1])

    for ind in range(0,int(triangle[1])):
        outfile.write(simplices[ind])
