#!/usr/bin/env python
# -*- coding: utf-8 -*-
# picgateway / processing module / shortcut functions
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

import functools

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

from PIL import Image

from .conf import EXPORT_OPTIONS
from .fetcher import fetch_content
from .minifier import shrink_image


def fetch_image(url):
    return Image.open(StringIO.StringIO(fetch_content(url)))


def shrink_image_from_url(url, target_size=None):
    return shrink_image(fetch_image(url), target_size)


def shrink_to_buf(url, fmt):
    im = shrink_image_from_url(url)

    buf = StringIO.StringIO()
    im.save(buf, fmt, **EXPORT_OPTIONS[fmt])

    return buf.getvalue()


shrink_to_jpg = functools.partial(shrink_to_buf, fmt='JPEG')


# vim:set ai et ts=4 sw=4 sts=4 fenc=utf-8:
