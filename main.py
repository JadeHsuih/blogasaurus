import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class BlogHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/new_post.html')
        self.response.write(template.render())

    def post(self):
        template = jinja_env.get_template('templates/view_post.html')
        title_var = self.request.get('title')
        content_var = self.request.get('content')
        author_var = self.request.get('aname')
        dict = {
            'titlev': title_var,
            'contentv': content_var,
            'anamev': author_var
        }
        self.response.write(template.render(dict))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/newp', BlogHandler),
], debug=True)
