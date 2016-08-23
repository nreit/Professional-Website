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
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

class MainHandler(webapp2.RequestHandler):
	def get(self):
		logging.info("GET")
		logging.info(self.request.path)
		try:
			path = self.request.path
			template = JINJA_ENVIRONMENT.get_template('templates%s'%path)
			if path == '/':
				self.response.write(template.render({'title': 'Nick Reitnour', 'pagetitle': 'About Me'}))
			elif path == '/aboutme.html':
				self.response.write(template.render({'title': 'Nick Reitnour', 'pagetitle': 'About Me'}))
			elif path == '/professional.html':
				self.response.write(template.render({'title': 'Experience', 'pagetitle': 'Experience'}))
			elif path == '/skillset.html':
				self.response.write(template.render({'title': 'Skill Set', 'pagetitle': 'Skill Set'}))
			elif path == '/knowledge.html':
				self.response.write(template.render({'title': 'Knowledge', 'pagetitle': 'Knowledge'}))
			else:
				self.response.write(template.render({'title': 'Nick Reitnour', 'pagetitle': 'About Me'}))
		except:
			template = JINJA_ENVIRONMENT.get_template('templates/aboutme.html')
			self.response.write(template.render({'title': 'Nick Reitnour', 'pagetitle': 'About Me'}))
		#outstr = template.render(temp, {})
		#self.response.out.write(outstr)

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/aboutme.html', MainHandler),
	('/professional.html', MainHandler),
	('/skillset.html', MainHandler),
	('/knowledge.html', MainHandler),
], debug=True)
