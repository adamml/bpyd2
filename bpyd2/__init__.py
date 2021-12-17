"""A module to help with working with data driven Blender scenes"""

import bpy
import math

def circle(xdata, ydata, zdata, radius, segments=720, colour=(0, 0, 0, 1), name='Foo'):
    """Add a filled circle in the x-y plane to the scene
    
    :param xdata: The x-axis location of the centre point of the circle
    :type xdata: int or float
    :param ydata: The y-axis location of the centre point of the circle
    :type ydata: int or float
    :param zdata: The z-axis location of the centre point of the circle
    :type zdata: int or float
    :param radius: The radius of the circle on the x-y plane
    :type radius: int or float
    :param segments: The number of segments to use in calculating the circle
    :type segments: int, defaults to 720
    :param colour: A tuple giving the RGB value of the colour in which to plot the line, with an opacity value
    :type colour: tuple, dfaults to (0, 0, 0, 1)
    :param name: The name assigned to the returned object
    :type name: str, defaults to 'Foo'
    
    :return: A Blender object containing the mesh to plot
    :rtype: bpy.types.Object
    
    """
    angles = [(math.pi*2)*(i/segments) for i in range(0, segments)]
    verts = [[(math.cos(angle)*radius)+x, (math.sin(angle)*radius)+y, z] for angle in angles]
    verts.append([x, y, z])
    edges = [[i, i+1] for i in range(segments)]
    edges.append([segments-1, 0])
    faces = [[i, i+1, z] for i in range(segments-1)]
    faces.append([segments-1, 0, z])
    __mesh = bpy.data.meshes.new(name)
    __mesh.from_pydata(verts, edges, faces)
    __material = bpy.data.materials.new("{} Material".format(name))
    __material.diffuse_color = colour
    __mesh.materials.append(__material)    
    __mesh.update()
    __object = bpy.data.objects.new(name, __mesh)    
    return __object

def clear(type=['MESH', 'FONT']):
    """Clear data from a scene
    
        :param type: Blender object classes to clean up. 
        :type type: list of strs, defaults to ["MESH", "FONT"]
        
        :return: None
        :rtype: None
    """
    
    [obj.select_set(True) if obj.type in type else obj.select_set(False) for obj in bpy.context.scene.objects]
    bpy.ops.object.delete()
    [bpy.data.collections.remove(col) for col in bpy.data.collections if not len(col.objects[:])]


def normalise(data, series_min=None, series_max=None,):
    """Normalise a data series to a set of values between 0 and 1
    
        :param data: The data series to be normalised
        :type data: list of numeric values
        :param series_min: An alternative minimum value of the series
        :type series_min: numeric
        :param series_max: An alternative maximum value of the series
        :type series_max: numeric
        
        :return: The normalised data series
        :rtype: list
    """
    if series_max is None:
        series_max = max(data)
    if series_min is None:
        series_min = min(data)
    return [(x - series_min) / (series_max - series_min) for x in data]


def plot(xdata, ydata, zdata, penwidth=0.1, penheight=0.1, 
                                    colour=(0, 0, 0, 1), name='Foo'):
        """ Creates an x,y,z line plot in Blender

        :param xdata: X-axis values
        :type xdata: list
        :param ydata: Y-axis valuees
        :type ydata: list
        :param zdata: Z-axis values
        :type zdata: list
        :param penwidth: The width of the line-plot in x-y space
        :type penwidth: float, defaults to 0.1
        :param penheight: The height of the line-plot in x-z sspace
        :type penheight: float, defaults to 0.1
        :param colour: A tuple giving the RGB value of the colour in which to plot the line, with an opacity value
        :type colour: tuple, dfaults to (0, 0, 0, 1)
        :param name: The name assigned to the returned object
        :type name: str, defaults to 'Foo'

        :raises AttributeError:

        :return: A Blender object containing the mesh to plot
        :rtype: bpy.types.Object
        
        .. todo: Turn map/lambdas into list comprehensions
        
        """
        if len(xdata) != len(ydata):
                raise AttributeError('xdata and ydata must be of equal length')
        if len(ydata) != len(zdata):
                raise AttributeError('ydata and zdata must be of equal length')
        verts = list(map(lambda x, y, z: (x, y-(penwidth/2), z-(penheight/2)),  
                                                        xdata, ydata, zdata))
        verts += list(map(lambda x, y, z: (x, y+(penwidth/2), z-(penheight/2)), 
                                                        xdata, ydata, zdata))
        verts += list(map(lambda x, y, z: (x, y-(penwidth/2), z+(penheight/2)), 
                                                        xdata, ydata, zdata))
        verts += list(map(lambda x, y, z: (x, y+(penwidth/2), z+(penheight/2)), 
                                                        xdata, ydata, zdata))
        edges = []
        faces = list(map(lambda x, sizex=len(xdata): [x, x+1, x+sizex+1, x+sizex], range(0, len(xdata)-1)))
        faces += list(map(lambda x, sizex=len(xdata): [x+(sizex*2), x+(sizex*2)+1, x+(sizex*3)+1, x+(sizex*3)], range(0, len(xdata)-1)))
        faces += [[1, len(xdata), len(xdata)*3, len(xdata)*2]]
        faces += [[len(xdata)-1, (len(xdata)*2)-1, (len(xdata)*4)-1, (len(xdata)*3)-1]]
        faces += list(map(lambda x, sizex=len(xdata): [x, x+1, x+(sizex*2)+1, x+(sizex*2)], range(0, len(xdata)-1)))
        faces += list(map(lambda x, sizex=len(xdata): [x+(sizex), x+(sizex)+1,x+(sizex*3)+1, x+(sizex*3)], range(0, len(xdata)-1)))
        __mesh = bpy.data.meshes.new(name)
        __mesh.from_pydata(verts, edges, faces)
        __material = bpy.data.materials.new("{} Material".format(name))
        __material.diffuse_color = colour
        __mesh.materials.append(__material)
        
        __mesh.update()
        __object = bpy.data.objects.new(name, __mesh)
        
        return __object


def polygon2D(xdata, ydata, zscale=None, colour=(1, 1, 1, 1), name='Foo'):
    """Plots a flat (2D) polygon at 0 on the Z-axis
    
    :param xdata: X-axis values
    :type xdata: list
    :param ydata: Y-axis values
    :type ydata: list
    :param zscale: An offset to extrude the 2D ploygon into Z-space 
    :type zscale: float or int, defaults to None
    :param colour: :param colour: A tuple giving the RGB value of the colour in which to plot the line, with an opacity value
    :type colour: tuple, dfaults to (0, 0, 0, 1)
    :param name: The name assigned to the returned object
    :type name: str, defaults to 'Foo'
    
    :returns: A Blender object containing a mesh of the polygon to plot
    :rtype: bpy.types.Object
    
    .. todo: Replace map(lambda(..)) constructs with list comprehension
    
    """
    verts = list(map(lambda x, y, z: (x, y, z), xdata, ydata, [0] * len(xdata)))
    if zscale is not None:
        verts += list(map(lambda x, y, z: (x, y, z), xdata, ydata, [zscale] * len(xdata)))
    edges = []
    faces = [tuple(range(0, len(xdata) - 1))]
    if zscale is not None:
        faces += [tuple(range(len(xdata), (len(xdata)*2) - 1))]
        faces += list(map(lambda x: (x, x+1, x+1+len(xdata), x+len(xdata)), range(0, len(xdata)-2)))
    __mesh = bpy.data.meshes.new(name)
    __mesh.from_pydata(verts, edges, faces)
    __material = bpy.data.materials.new("{} Material".format(name))
    __material.diffuse_color = colour
    __mesh.materials.append(__material)  
    __mesh.update()
    __object = bpy.data.objects.new(name, __mesh)
    
    return __object


def scale(data, new_min, new_max):
    """Scales a normalised data series
    
        :param data: The norrmalised data series to be scaled
        :type data: List of numeric values
        :param new_min: The minimum value of the scaled data series
        :type new_min: numeric
        :param new_max: The new maximum of the scaled data series
        :type new_max: numeric
        
        :return: A scaled data series
        :rtype: list
    """
    return [(x*(new_max-new_min))+new_min for x in data]
    
