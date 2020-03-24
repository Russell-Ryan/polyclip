''' The python driver to polyclip '''

from dataclasses import dataclass
import numpy as np

from . import cpolyclip


@dataclass(frozen=True)
class PolyclipTypes(object):
    ''' A class to define datatypes for polyclip '''    
    INT: np.dtype = np.int32       # do not change this
    FLT: np.dtype = np.float32     # do not change this


class Polyclip(PolyclipTypes):
    ''' A class to call the polyclip by JD Smith '''

    def __init__(self,dim):
        ''' the input variable dim should be a tuple with 2 elements: 
        dim=(nx,ny)

        '''
        self._sx=dim[0]
        self._sy=dim[1]

    @property
    def naxis(self):
        return (self._sx,self._sy)

        

    def __call__(self,x,y):
        return self.multi(x,y)

        
        
    def multi(self,x,y):

        ''' Call the multi polygon clipping '''
        
        # compute bounding box
        l=np.clip(np.floor(x.min(axis=1)-1),0,self._sx).astype(self.INT)
        r=np.clip(np.floor(x.max(axis=1)+1),0,self._sx).astype(self.INT)
        b=np.clip(np.floor(y.min(axis=1)-1),0,self._sy).astype(self.INT)
        t=np.clip(np.floor(y.max(axis=1)+1),0,self._sy).astype(self.INT)
        npix=sum((r-l+1)*(t-b+1))
        
        # compute polygon indices --- technically, this does't work because
        # at this point x is a numpy array, so they have the same
        # number of polygon edges.  
        npoly=len(x)
        polyinds=np.zeros(npoly+1,dtype=self.INT)
        for i,xx in enumerate(x):
            polyinds[i+1]=polyinds[i]+len(xx)



        # the number of output pixels must be an array (this is a C-gotcha)
        nclip=np.array([0],self.INT)
        
        # output arrays 
        areas=np.zeros(npix,dtype=self.FLT)
        xx=np.zeros(npix,dtype=self.INT)
        yy=np.zeros(npix,dtype=self.INT)

        
        # call the compiled C-code
        cpolyclip.multi(l,r,b,t,\
                        x.astype(self.FLT).ravel(),\
                        y.astype(self.FLT).ravel(),\
                        npoly,polyinds,xx,yy,nclip,areas)

        
        # trim the results
        nclip=nclip[0]
        areas=areas[:nclip]
        xx=xx[:nclip]
        yy=yy[:nclip]
        return xx,yy,areas,polyinds


          
    
    def single(self,x,y):
        ''' call the single polygon clipping '''

        
        # compute the bounding box for this pixel
        l=np.array(np.clip(np.floor(np.min(x)),0,self._sx),dtype=self.INT)
        r=np.array(np.clip(np.ceil(np.max(x))+1,0,self._sx),dtype=self.INT)
        b=np.array(np.clip(np.floor(np.min(y)),0,self._sy),dtype=self.INT)
        t=np.array(np.clip(np.ceil(np.max(y))+1,0,self._sy),dtype=self.INT)

        # get number of vertices for the polygon
        nverts=np.array([len(x)],dtype=self.INT)

        # number of pixels that might be affected
        npix=(r-l+1)*(t-b+1)

        # recast some things for C
        nclip=np.array([0],dtype=self.INT)
        ri=np.zeros(npix+1,dtype=self.INT)

        # output polygon indices
        px_out=np.zeros((nverts[0]+24)*npix,dtype=self.FLT)
        py_out=np.zeros((nverts[0]+24)*npix,dtype=self.FLT)
        
        # main outputs (area, pixel coords and reverse indices)
        areas=np.zeros(npix,dtype=self.FLT)
        inds=np.zeros((npix,2),dtype=self.INT)
        ri_out=np.zeros(npix+1,dtype=self.INT)

        # call the pologyon clipper
        cpolyclip.single(l,r,b,t,\
                         np.array(x,dtype=self.FLT),\
                         np.array(y,dtype=self.FLT),\
                         nverts,px_out,py_out,inds,nclip,areas,ri_out)

        # extract data
        nclip=nclip[0]
        px_out=px_out[:nclip]
        py_out=py_out[:nclip]
        ri_out=ri_out[:nclip]

        # main outputs 
        xx=inds[:nclip,0]
        yy=inds[:nclip,1]
        areas=areas[:nclip]
        
        return xx,yy,areas
        
        
    def __str__(self):
        out="polyclip> python driver for the compiled C polyclip by JD Smith\n"
        out=out+'          image dimensions: {}\u00d7{}'.format(self._sx,self._sy)
        return out
