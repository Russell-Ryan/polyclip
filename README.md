# polyclip

A python driver for [polyclip_multi](http://tir.astro.utoledo.edu/jdsmith/code/idl.php) written in C by JD Smith.

## Installation


## Example usage
```

# import relevant modules
import polyclip
import numpy as np

# define the size of the pixel grid
nx,ny=100,100
naxis=np.array([nx,ny])

# initialize the clipper
clip=polyclip.Polyclip(naxis)

# create 2 polygons to clip... here they're an irregular quadralateral, but
# this isn't a requirement
px=np.array([[3.4,3.4,4.5,4.5],[3.5,3.5,5.5,5.5]])
py=np.array([[1.4,2.0,2.0,1.4],[3.5,4.3,4.3,3.5]])

# call the clipper
xc,yc,area,polyindices = clip(px,py)

# xc,yc are the coordinates in the grid
# area is the relative pixel area in that grid cell
# polyindices are the indices to related the clipped pixels to the original

# use these things like
for j,(x,y) in enumerate(zip(px,py)):
    j0,j1=polyindices[j],polyindices[j+1]
    if j1 > j0:
       print(area[j0:j1])
```












