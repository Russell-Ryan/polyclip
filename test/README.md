# Testing the Polyclip module

## PyTest
I recommend installing [pytest](https://pypi.org/project/pytest/): `pip install pytest`. Then you can simply test the code with:

``` 
pytest test_polyclip.py
```

But this will essentially run the same script as the test.py file, but with added `assert` calls to ensure the results are correct.  It also shows how to use the `polyindices` for the polyclip_multi to connect the output (clipped) pixels to the input polygons.

```
linux> python test.py

[3 4] [1 1] [0.35999995 0.3       ]
[3 3 4 4 5 5] [3 4 3 4 3 4] [0.25      0.1500001 0.5       0.3000002 0.25      0.1500001]
[3 4] [1 1] [0.35999995 0.3       ]

```
> There is no notion of `polyindices` for the polyclip_single.


