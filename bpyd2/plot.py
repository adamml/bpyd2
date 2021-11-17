def plot(xdata, ydata, zdata, xnorm=None, ynorm=None, znorm=None,
                penwidth=0.1, penheight=0.1, colour=(0, 0, 0, 1)):
        """ Creates an x,y,z line plot in Blender

        :param xdata:
        :type xdata: list
        :param ydata:
        :type ydata: list
        :param zdata:
        :type zdata: list
        :param xnorm:
        :type xnorm: list, defaults to None
        :param ynorm:
        :type ynorm: list, defaults to None
        :param znorm:
        :type znorm: list, defaults to None
        :param penwidth:
        :type penwidth: float, defaults to 0.1
        :param penheight:
        :type penheight: float, defaults to 0.1

        :raises AttributeError:

        :return: None
        :rtype: None
        
        """
        if len(xdata) != len(ydata):
                raise AttributeError('xdata and ydata must be of equal length')
        if len(ydata) != len(zdata):
                raise AttributeError('ydata and zdata must be of equal length')
        if xnorm is not None and len(xnorm) != 2:
                raise AttributeError('xnorm must be None or length 2')
        if ynorm is not None and len(ynorm) != 2:
                raise AttributeError('ynorm must be None or length 2')
        if znorm is not None and len(znorm) != 2:
                raise AttributeError('znorm must be None or length 2')
        if xnorm is not None:
                xdata = list(map(lambda x, seriesmax=max(xdata), seriesmin=min(xdata), norm=xnorm: (((x - seriesmin)/(seriesmax - seriesmin)) * (norm[1]-norm[0])) + norm[0], xdata))
        if ynorm is not None:
                ydata = list(map(lambda x, seriesmax=max(ydata), seriesmin=min(ydata), norm=ynorm: (((x - seriesmin)/(seriesmax - seriesmin)) * (norm[1]-norm[0])) + norm[0], ydata))
        if znorm is not None:
                zdata = list(map(lambda x, seriesmax=max(zdata), seriesmin=min(zdata), norm=znorm: (((x - seriesmin)/(seriesmax - seriesmin)) * (norm[1]-norm[0])) + norm[0], zdata))
        verts = list(map(lambda x, y, z: (x, y-(penwidth/2), z-(penheight/2)), xdata, ydata, zdata))
        verts += list(map(lambda x, y, z: (x, y+(penwidth/2), z-(penheight/2)), xdata, ydata, zdata))
        verts += list(map(lambda x, y, z: (x, y-(penwidth/2), z+(penheight/2)), xdata, ydata, zdata))
        verts += list(map(lambda x, y, z: (x, y+(penwidth/2), z+(penheight/2)), xdata, ydata, zdata))
        edges = []
        faces = list(map(lambda x, sizex=len(xdata): [x, x+1, x+sizex, x+sizex+1], range(0, len(xdata)-1)))
        faces += list(map(lambda x, sizex=len(xdata): [x+(sizex*2), x+(sizex*2)+1, x+(sizex*3), x+(sizex*3)+1], range(0, len(xdata)-1)))
        faces += [[1, len(xdata), len(xdata)*2, len(xdata)*3]]
        faces += [[len(xdata)-1, (len(xdata)*2)-1, (len(xdata)*3)-1, (len(xdata)*4)-1]]
        faces += list(map(lambda x, sizex=len(xdata): [x, x+1, x+(sizex*2), x+(sizex*2)+1], range(0, len(xdata)-1)))
        faces += list(map(lambda x, sizex=len(xdata): [x+(sizex), x+(sizex)+1,x+(sizex*3), x+(sizex*3)+1], range(0, len(xdata)-1)))
        __mesh = bpy.data.meshes.new('foo')
        __mesh.from_pydata(verts, edges, faces)
        __material = bpy.data.materials.new("MaterialName")
        __material.diffuse_color = colour
        __mesh.materials.append(__material)
        
        __mesh.update()
        __object = bpy.data.objects.new('boo', __mesh)
        __collection = bpy.data.collections.new('baz')
        bpy.context.scene.collection.children.link(__collection)
        __collection.objects.link(__object)