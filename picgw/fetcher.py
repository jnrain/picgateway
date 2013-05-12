#!/usr/bin/env python
# -*- coding: utf-8 -*-
# picgateway / processing module / fetcher
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

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

import requests
from PIL import Image

from .conf import BASE_URL_PREFIX


def get_absolute_url(url, prefix=None):
    if url.startswith('http://') or url.startswith('https://'):
        return url

    # NOTE: prefix should end with a '/'...
    return (BASE_URL_PREFIX if prefix is None else prefix) + url


def fetch_content(url):
    return requests.get(get_absolute_url(url)).content


# vim:set ai et ts=4 sw=4 sts=4 fenc=utf-8:
