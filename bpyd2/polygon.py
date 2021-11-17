def polygon(xdata, ydata,
                xnorm = None, ynorm=None, zscale=None, colour=(1, 1, 1, 1)):
    if xnorm is not None:
        xdata = list(map(lambda x, seriesmax=max(xdata), seriesmin=min(xdata), norm=xnorm: (((x - seriesmin)/(seriesmax - seriesmin)) * (norm[1]-norm[0])) + norm[0], xdata))
    if ynorm is not None:
        ydata = list(map(lambda x, seriesmax=max(ydata), seriesmin=min(ydata), norm=ynorm: (((x - seriesmin)/(seriesmax - seriesmin)) * (norm[1]-norm[0])) + norm[0], ydata))
    verts = list(map(lambda x, y, z: (x, y, z), xdata, ydata, [0] * len(xdata)))
    if zscale is not None:
        verts += list(map(lambda x, y, z: (x, y, z), xdata, ydata, [zscale] * len(xdata)))
    edges = []
    faces = [tuple(range(0, len(xdata) - 1))]
    if zscale is not None:
        faces += [tuple(range(len(xdata), (len(xdata)*2) - 1))]
        faces += list(map(lambda x: (x, x+1, x+1+len(xdata), x+len(xdata)), range(0, len(xdata)-2)))
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