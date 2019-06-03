# To do list

1. Note that the way the boundary effects are handled.
   We should be clipping against the pixel-array boundary, but instead just use
   min/max operators.  so there will be an error in the pixel areas around
   the pixel boundaries
