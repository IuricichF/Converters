#convert a point in GPS coordinates to X,Y,Z coordinates

import sys
import numpy as np
import math

def LLHtoECEF(lat, lon, alt):

    rad = np.float64(6378137.0)        # Radius of the Earth (in meters)
    f = np.float64(1.0/298.257223563)  # Flattening factor WGS84 Model
    cosLat = np.cos(lat)
    sinLat = np.sin(lat)
    FF     = (1.0-f)**2
    C      = 1/np.sqrt(cosLat**2 + FF * sinLat**2)
    S      = C * FF

    x = (rad * C + alt)*cosLat * np.cos(lon)
    y = (rad * C + alt)*cosLat * np.sin(lon)
    z = (rad * S + alt)*sinLat


    return (x, y, z)


target = open(sys.argv[2], 'w')

with open(sys.argv[1], 'r') as f:
    for line in f:
        words = line.split()
        ecef = LLHtoECEF(math.radians(float(words[0])),math.radians(float(words[1])),0)
        target.write(repr(ecef[0])+" "+repr(ecef[1])+" "+repr(ecef[2])+"\n")

target.close()
