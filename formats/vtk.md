###VTK
ASCII format describing the set of vertices and the set of triangles composing the triangle mesh. More details on the vtk format che be found [here]("http://www.vtk.org/wp-content/uploads/2015/04/file-formats.pdf")


```
# vtk DataFile Version 2.0  // header

ASCII // type of the file
DATASET UNSTRUCTURED_GRID // type of the described format
POINTS 4 float // number of points and type of coordinates
0.0834504 0.0913934 0.0353825 // coordinates of each point
0.0420765 0.0989266 0.0400468
0.0894223 0.0848361 0.087783
0.0432475 0.101112 -0.00163271
CELLS 2 8 // number of cells and number of following integers
3 0 1 2 // number of following integers and vertex indices for each triangle
3 1 2 3
CELL_TYPES 2 // number of cell types
5 5 // type of each cell
```
