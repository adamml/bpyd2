from .plot import plot

def axis(xdata=None, ydata=None, zdata=None, strokewidth=0.05):
    plot(xdata, [max(ydata), max(ydata)], [min(zdata), min(zdata)], penwidth=strokewidth, penheight=strokewidth, colour=(0, 0, 0, 1))
    plot(xdata, [min(ydata), min(ydata)], [min(zdata), min(zdata)], penwidth=strokewidth, penheight=strokewidth, colour=(0.75, 0.75, 0.75, 1))
    plot(xdata, [((max(ydata) - min(ydata)) / 2) + min(ydata), ((max(ydata) - min(ydata)) / 2) + min(ydata)], [min(zdata), min(zdata)], penwidth=strokewidth, penheight=strokewidth, colour=(0.75, 0.75, 0.75, 1))
    plot(xdata, [((max(ydata) - min(ydata)) * 0.25) + min(ydata), ((max(ydata) - min(ydata)) * 0.25) + min(ydata)], [min(zdata), min(zdata)], penwidth=strokewidth, penheight=strokewidth, colour=(0.75, 0.75, 0.75, 1))
    plot(xdata, [((max(ydata) - min(ydata)) * 0.75) + min(ydata), ((max(ydata) - min(ydata)) * 0.75) + min(ydata)], [min(zdata), min(zdata)], penwidth=strokewidth, penheight=strokewidth, colour=(0.75, 0.75, 0.75, 1))
    plot([min(xdata), min(xdata)], ydata, [min(zdata), min(zdata)], penwidth=strokewidth, penheight=strokewidth, colour=(0, 0, 0, 1))
    plot([max(xdata), max(xdata)], ydata, [min(zdata), min(zdata)], penwidth=strokewidth, penheight=strokewidth, colour=(0, 0, 0, 1))
    plot([((max(xdata) - min(xdata)) * 0.5) + min(xdata), ((max(xdata) - min(xdata)) * 0.5) + min(xdata)], ydata, [min(zdata), min(zdata)], penwidth=strokewidth, penheight=strokewidth, colour=(0.75, 0.75, 0.75, 1))
    plot([((max(xdata) - min(xdata)) * 0.25) + min(xdata), ((max(xdata) - min(xdata)) * 0.25) + min(xdata)], ydata, [min(zdata), min(zdata)], penwidth=strokewidth, penheight=strokewidth, colour=(0.75, 0.75, 0.75, 1))
    plot([((max(xdata) - min(xdata)) * 0.75) + min(xdata), ((max(xdata) - min(xdata)) * 0.75) + min(xdata)], ydata, [min(zdata), min(zdata)], penwidth=strokewidth, penheight=strokewidth, colour=(0.75, 0.75, 0.75, 1))
    plot([min(xdata), min(xdata)], [max(ydata), max(ydata)], zdata, penwidth=strokewidth, penheight=strokewidth, colour=(0, 0, 0, 1))
    plot([min(xdata), min(xdata)], ydata, [max(zdata), max(zdata)], penwidth=strokewidth, penheight=strokewidth, colour=(0.75, 0.75, 0.75, 1))
    plot(xdata, [max(ydata), max(ydata)], [max(zdata), max(zdata)], penwidth=strokewidth, penheight=strokewidth, colour=(0.75, 0.75, 0.75, 1))
    plot([min(xdata), min(xdata)], ydata, [((max(zdata)-min(zdata))*.5)+min(zdata), ((max(zdata)-min(zdata))*.5)+min(zdata)], penwidth=strokewidth, penheight=strokewidth, colour=(0.75, 0.75, 0.75, 1))
    plot(xdata, [max(ydata), max(ydata)], [((max(zdata)-min(zdata))*.5)+min(zdata), ((max(zdata)-min(zdata))*.5)+min(zdata)], penwidth=strokewidth, penheight=strokewidth, colour=(0.75, 0.75, 0.75, 1))
 