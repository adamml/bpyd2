# Table of Contents

* [bpyd2](#bpyd2)
  * [circle](#bpyd2.circle)
  * [clear](#bpyd2.clear)
  * [normalise](#bpyd2.normalise)
  * [plot](#bpyd2.plot)
  * [polygon2D](#bpyd2.polygon2D)
  * [scale](#bpyd2.scale)

<a id="bpyd2"></a>

# bpyd2

A module to help with working with data driven Blender scenes

<a id="bpyd2.circle"></a>

#### circle

```python
def circle(xdata, ydata, zdata, radius, segments=720, colour=(0, 0, 0, 1), name='Foo')
```

Add a filled circle in the x-y plane to the scene

**Arguments**:

- `xdata` (`int or float`): The x-axis location of the centre point of the circle
- `ydata` (`int or float`): The y-axis location of the centre point of the circle
- `zdata` (`int or float`): The z-axis location of the centre point of the circle
- `radius` (`int or float`): The radius of the circle on the x-y plane
- `segments` (`int, defaults to 720`): The number of segments to use in calculating the circle
- `colour` (`tuple, dfaults to (0, 0, 0, 1)`): A tuple giving the RGB value of the colour in which to plot the line, with an opacity value
- `name` (`str, defaults to 'Foo'`): The name assigned to the returned object

**Returns**:

`bpy.types.Object`: A Blender object containing the mesh to plot

<a id="bpyd2.clear"></a>

#### clear

```python
def clear(type=['MESH', 'FONT'])
```

Clear data from a scene

**Arguments**:

- `type` (`list of strs, defaults to ["MESH", "FONT"]`): Blender object classes to clean up.

**Returns**:

`None`: None

<a id="bpyd2.normalise"></a>

#### normalise

```python
def normalise(data, series_min=None, series_max=None)
```

Normalise a data series to a set of values between 0 and 1

**Arguments**:

- `data` (`list of numeric values`): The data series to be normalised
- `series_min` (`numeric`): An alternative minimum value of the series
- `series_max` (`numeric`): An alternative maximum value of the series

**Returns**:

`list`: The normalised data series

<a id="bpyd2.plot"></a>

#### plot

```python
def plot(xdata, ydata, zdata, penwidth=0.1, penheight=0.1, colour=(0, 0, 0, 1), name='Foo')
```

Creates an x,y,z line plot in Blender

**Arguments**:

- `xdata` (`list`): X-axis values
- `ydata` (`list`): Y-axis valuees
- `zdata` (`list`): Z-axis values
- `penwidth` (`float, defaults to 0.1`): The width of the line-plot in x-y space
- `penheight` (`float, defaults to 0.1`): The height of the line-plot in x-z sspace
- `colour` (`tuple, dfaults to (0, 0, 0, 1)`): A tuple giving the RGB value of the colour in which to plot the line, with an opacity value
- `name` (`str, defaults to 'Foo'`): The name assigned to the returned object

**Raises**:

- `AttributeError`: 

**Returns**:

`bpy.types.Object
.. todo: Turn map/lambdas into list comprehensions`: A Blender object containing the mesh to plot

<a id="bpyd2.polygon2D"></a>

#### polygon2D

```python
def polygon2D(xdata, ydata, zscale=None, colour=(1, 1, 1, 1), name='Foo')
```

Plots a flat (2D) polygon at 0 on the Z-axis

**Arguments**:

- `xdata` (`list`): X-axis values
- `ydata` (`list`): Y-axis values
- `zscale` (`float or int, defaults to None`): An offset to extrude the 2D ploygon into Z-space
- `colour` (`tuple, dfaults to (0, 0, 0, 1)`): :param colour: A tuple giving the RGB value of the colour in which to plot the line, with an opacity value
- `name` (`str, defaults to 'Foo'`): The name assigned to the returned object

**Returns**:

`bpy.types.Object
.. todo: Replace map(lambda(..)) constructs with list comprehension`: A Blender object containing a mesh of the polygon to plot

<a id="bpyd2.scale"></a>

#### scale

```python
def scale(data, new_min, new_max)
```

Scales a normalised data series

**Arguments**:

- `data` (`List of numeric values`): The norrmalised data series to be scaled
- `new_min` (`numeric`): The minimum value of the scaled data series
- `new_max` (`numeric`): The new maximum of the scaled data series

**Returns**:

`list`: A scaled data series

