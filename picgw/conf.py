#!/usr/bin/env python
# -*- coding: utf-8 -*-
# picgateway / processing module / configuration
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

# Configuration
# target dimension
TARGET_SIZE = (240, 320)

# base URL
BASE_URL_PREFIX = 'http://bbs.jnrain.com/rainstyle/'

# options for Image.save()
EXPORT_OPTIONS = {
        'JPEG': {
            'quality': 70,
            'optimize': True,
            },
        }


# vim:set ai et ts=4 sw=4 sts=4 fenc=utf-8:
