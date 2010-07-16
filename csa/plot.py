#
#  This file is part of the Connection-Set Algebra (CSA).
#  Copyright (C) 2010 Mikael Djurfeldt
#
#  CSA is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  CSA is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import numpy as _numpy
import matplotlib
import matplotlib.pyplot as _plt

import elementary

def show (cset, N0 = 30, N1 = None):
    N1 = N0 if N1 == None else N1
    _plt.clf ()
    _plt.axis ('equal')
    a = _numpy.zeros ((N0, N1))
    for (i, j) in elementary.cross (xrange (N0), xrange (N1)) * cset:
        a[i,j] += 1.0
    _plt.imshow (a, interpolation='nearest')
    _plt.show ()

def gplotsel2d (g, cset, source = elementary.N, target = elementary.N, N0 = 900, N1 = None, value = None, range=[], lines = True):
    N1 = N0 if N1 == None else N1
    _plt.clf ()
    _plt.axis ('equal')
    gplot2d (g, N1, color = 'grey', show = False)
    cset = elementary.cross (source, target) * cset
    N = len (cset)
    if lines:
        marker = 'ro-'
    else:
        marker = 'ro'
    if elementary.arity (cset):
        if value != None:
            if range:
                normalize = matplotlib.colors.Normalize (*range)
            else:
                normalize = matplotlib.colors.Normalize ()
                normalize.autoscale ([v[value] for (i, j, v) in cset.c])
            cmap = matplotlib.cm.get_cmap ()
            for (i, j, v) in cset.c:
                color = cmap (normalize (v[value]))
                _plt.plot ([g (i)[0], g (j)[0]], [g (i)[1], g (j)[1]], \
                           marker, color = color, mfc = color)
        else:
            for (i, j, v) in cset.c:
                _plt.plot ([g (i)[0], g (j)[0]], [g (i)[1], g (j)[1]], marker)
    else:
        for (i, j) in cset:
            _plt.plot ([g (i)[0], g (j)[0]], [g (i)[1], g (j)[1]], marker)
    _plt.show ()

def gplot2d (g, N, color = None, show = True):
    if show:
        _plt.clf ()
        _plt.axis ('equal')
    x = []
    y = []
    for i in xrange (0, N):
        pos = g (i)
        x.append (pos[0])
        y.append (pos[1])
    if color != None:
        _plt.plot (x, y, 'o', color = color)
    else:
        _plt.plot (x, y, 'bo')
    if show:
        _plt.show ()

#del numpy, plt
