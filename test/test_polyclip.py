import pytest

import polyclip
import numpy as np

__MAXDIFF__=2e-7      # single global variable to test FP operations

''' 

A simple pytest script to verify that polyclip.py is working correctly.

'''





def test_multiclip():
    ''' A module to test clipping multiple polygons in a single pass. '''

    
    # define the size of the pixel grid
    nx,ny=100,100
    naxis=np.array([nx,ny])
    
    # initialize the clipper
    clip=polyclip.Polyclip(naxis)

    # print the clipping object
    print(clip)
    
    # create 2 polygons to clip... here they're an irregular quadralateral, but
    # this isn't a requirement
    px=np.array([[3.4,3.4,4.5,4.5],[3.5,3.5,5.5,5.5]])
    py=np.array([[1.4,2.0,2.0,1.4],[3.5,4.3,4.3,3.5]])
    
    # call the clipper
    xc,yc,area,polyindices = clip(px,py)
    
    # xc,yc are the coordinates in the grid
    # area is the relative pixel area in that grid cell
    # polyindices are the indices to relate the clipped pixels to the originals

    xc0=np.array([3,4,3,3,4,4,5,5])
    yc0=np.array([1,1,3,4,3,4,3,4])
    area0=np.array([0.36,0.3,0.25,0.15,0.5,0.3,0.25,0.15])
    polyindices0=np.array([0,2,8])
    
    # a temporary variable
    diff=np.amax(np.abs(area-area0))

    # apply assertion tests
    assert np.array_equal(xc,xc0)
    assert np.array_equal(yc,yc0)
    assert diff<__MAXDIFF__
    assert np.array_equal(polyindices,polyindices0)
    
    # how to decompose the polyindices
    #for j,(x,y) in enumerate(zip(px,py)):
    #    j0,j1=polyindices[j],polyindices[j+1]
    #    if j1 > j0:

def test_singleclip():
    ''' A module to test clipping a single polygon. '''

    
    # define the size of the pixel grid
    nx,ny=100,100
    naxis=np.array([nx,ny])
    
    # initialize the clipper
    clip=polyclip.Polyclip(naxis)

    # create a polygon
    px=np.array([1.2,1.5,2.7,2.5])
    py=np.array([4.5,3.2,1.4,1.9])

    # call the clipper    
    xc,yc,area = clip.single(px,py)

    # xc,yc are the coordinates in the grid
    # area is the relative pixel area in that grid cell
    # for the single, there is no notion of the polyindices


    # the correct values
    xc0=np.array([1,1,1,2,2])
    yc0=np.array([2,3,4,1,2])
    area0=np.array([0.09833333,0.26051286,0.03365386,0.0475,0.135])

    # a temporary variable
    diff=np.amax(np.abs(area-area0))

    # apply assertion tests
    assert np.array_equal(xc,xc0)
    assert np.array_equal(yc,yc0)
    assert diff<__MAXDIFF__
    
    
if __name__=='__main__':
    test_multiclip()
    test_singleclip()
