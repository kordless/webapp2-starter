# -*- coding: utf-8 -*-
import datetime
import webapp2
from webapp2_extras import jinja2


class BaseHandler(webapp2.RequestHandler):
    """
        BaseHandler for all requests all other handlers will
        extend this handler

    """
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_template(self, template_name, template_values):
        self.response.write(self.jinja2.render_template(
            template_name, **template_values))

    def render_string(self, template_string, template_values):
        self.response.write(self.jinja2.environment.from_string(
            template_string).render(**template_values))


class PageHandler(BaseHandler):
    def root(self):
        context = {'site': 'root site'}
        return self.render_template('home.html', context)

    def subdomain(self):
        context = {'site': 'subdomain_site'}
        return self.render_template('home.html', context)
