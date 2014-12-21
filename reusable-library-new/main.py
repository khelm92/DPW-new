#kasey helm - reusable library
#my app is as if I was a personaly trainer, and clients will be inputting their info including name, gender, age, and weight
import webapp2
from pages import View

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        p = View()
        
        self.response.write(p.print_out())
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
