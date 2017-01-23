#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
from helpers import rotate_character


form = """
<form method ="post" name="main-text">
    <label>
        Enter some text
        <br>
        <input type="text" name="text-to-rot" value="%(current_text)s">
    </label>
    <br>
    <br>
    <input type="submit">
</form>
"""
def escape_html(s):
    return cgi.escape(s, quote=True)

class MainHandler(webapp2.RequestHandler):
    def write_form(self,current_text=""):
        self.response.out.write(form % {"current_text":current_text})
    def get(self):
        self.write_form()
    def post(self):
        # Text from input box is of type unicode, rotate_character is expecting
        # string or integer, so must convert it first.
        user_text = str(self.request.get('text-to-rot'))
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.out.write(self.request)
        rot_text = ""
        for char in user_text:
            rot_text = rot_text + rotate_character(char,13)
        escaped_text = escape_html(rot_text)
        self.write_form(escaped_text)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
