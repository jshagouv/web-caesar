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
from helpers import rotate_character, encrypt

# Initially tried to use textarea, but could not figure out how to read
# and change text. Google search of hte issue all used javascript. So
# reverted to an input element.
form = """
<form method ="post" name="main-text">
    <label>
        Enter some text
        <br>
        <input type="text" name="text-to-rot" value="%(current_text)s">
    </label>
    <br>
    <label>
        Enter amount of rotation:
        <br>
        <input type="text" name="rot-num" value="%(rot_num)s">
    </label>
    <br>
    <br>
    <input type="submit">
</form>
"""
def escape_html(s):
    return cgi.escape(s, quote=True)

class MainHandler(webapp2.RequestHandler):
    def write_form(self,current_text="",rot_num=""):
        self.response.out.write(form % {"current_text":current_text,
                                        "rot_num":rot_num})
    def get(self):
        self.write_form()
    def post(self):
        # Text from input box is of type unicode, rotate_character is expecting
        # string or integer, so must convert it first.
        user_text = str(self.request.get('text-to-rot'))
        user_rot_num = int(self.request.get('rot-num'))
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.out.write(self.request)
        rot_text = encrypt(user_text,user_rot_num)
        escaped_text = escape_html(rot_text)
        self.write_form(escaped_text,str(user_rot_num))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
