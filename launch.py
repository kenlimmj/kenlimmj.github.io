#!/usr/bin/env python

# Copyright (c) 2013 Matt Hodges (http://matthodges.com)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys
import webbrowser
import os
import SimpleHTTPServer
from SocketServer import TCPServer
from threading import Thread

full_path = os.path.realpath(__file__)
print "Changing directory to", os.path.dirname(full_path)
os.chdir(os.path.dirname(full_path));

if sys.argv[1:]:
    PORT = int(sys.argv[1])
else:
    PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = TCPServer(("", PORT), Handler)

print "Starting HTTP server on port", PORT
Thread(target=httpd.serve_forever).start()

print "Launching local instance of Empress"
webbrowser.open('http://localhost:' + str(PORT))
