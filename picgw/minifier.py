#!/usr/bin/env python
# -*- coding: utf-8 -*-
# picgateway / processing module / minifier
#
# Copyright (C) 2013 JNRain
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals, division

from PIL import Image

from .conf import TARGET_SIZE


# helpers for shrinking image dimension
def maxW(w, h, dw):
    return (dw, int(h * dw / w)) if w > dw else (w, h)


def maxH(w, h, dh):
    return (int(w * dh / h), dh) if h > dh else (w, h)


def maxWH(w, h, dw, dh):
    sz_maxW = maxW(w, h, dw)
    sz_maxH = maxH(w, h, dh)

    if sz_maxW[1] > dh:
        return sz_maxH
    if sz_maxH[0] > dw:
        return sz_maxW
    return w, h


def get_shrunk_size(size, target=None):
    dw, dh = TARGET_SIZE if target is None else target
    return maxWH(size[0], size[1], dw, dh)


def shrink_image(im, target_size=None):
    return im.resize(get_shrunk_size(im.size, target_size), Image.ANTIALIAS)


# vim:set ai et ts=4 sw=4 sts=4 fenc=utf-8:
