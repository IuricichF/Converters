# Converters
A collection of scripts for converting between various formats.
---
####Description
***

Each folder provides a set of converters for commonly used file formats. Current folders are:

- Meshes: providing converters for [vtk](formats/vtk.md), [tri](formats/tri.md) and [off](formats/off.md) formats
- GPS: providing a converter for points in [GPS coordinates](formats/gps.md) to [geometric coordinates](formats/xyz.md)
- weatherData: providing a converter for grids encoded in the [netcdf](http://unidata.github.io/netcdf4-python/) format to an [ascii](formats/ascii.md) description of the regular grid.



<br/>
<br/>

#####Meshes
***

Scripts provided:
- off_tri: to convert a file from the off format to tri format (and viceversa)
- off_vtk: to convert a file from the off format to vtk format (and viceversa)

Usage: ```python off_tri.py {input_file} {output_file}``` input and ouput files can be either provided as arguments or when the script is running.

<br/>
#####GPS
***

Scripts provided:
- LLHtoECEF: to convert from GPS coordinates described as longitude and latitude, to geometric coordinates (x,y,z).

Usage: ```python LLHtoECEF.py input_file] [output_file]```

<br/>
#####WeatherData
***

Scripts provided:
- netcdfToPng: to convert from netcdf format to a volume grid described as a list of values in ASCII format.

Additional libraries reguired:
- netCDF4: [http://unidata.github.io/netcdf4-python/](http://unidata.github.io/netcdf4-python/)

Usage: ```python netcdfToASCII.py {input_file}``` input file can be either provided as argument or when the script is running.
