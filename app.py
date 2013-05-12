#!/usr/bin/env python
# -*- coding: utf-8 -*-
# picgateway / app / application file
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

from __future__ import unicode_literals, division, print_function

import sys
from urllib import urlencode

import web

from picgw.shortcuts import shrink_to_jpg


urls = (
        '/(.*)', 'Minifier',
        )


class Minifier(object):
    def GET(self, url):
        inp = web.input()

        qs = '?%s' % (urlencode(inp), ) if inp else ''
        cooked_url = (url + qs).lstrip('/')

        # strange thing...
        if cooked_url.lower().startswith('%2fattachments%2f'):
            cooked_url = cooked_url.replace('%2F', '/')[1:]

        print(cooked_url, file=sys.stderr)

        # workaround new-style attachments
        if cooked_url.startswith('attachments/'):
            cooked_url = 'http://bbs.jnrain.com/' + cooked_url

        #return '%s => %s' % (
        #        repr(url),
        #        repr(cooked_url),
        #        )

        result = shrink_to_jpg(cooked_url)

        web.header('Content-Type', 'image/jpeg')
        return result


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()


# vim:set ai et ts=4 sw=4 sts=4 fenc=utf-8:
