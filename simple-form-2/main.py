#kasey helm; simple form assignment

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form Assignment</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''
    
        page_body = '''<h1>Grocery Store Application</h1>
        <form method="GET" action="">
            <label>Name: </label><input type="text" name="name"/>
            <br>
            <label>Email: </label><input type="text" name="email"/>
            <br>
            <label>Age: </label><input type="text" name="age"/>
            <br>
            <label>Position: </label> <br>
                                      <input type="radio" name="position" value="cashier" checked>Cashier
                                      <br>
                                      <input type="radio" name="position" value="bagger" checked>Bagger
                                      <br>
                                      <input type="radio" name="position" value="stock clerk" checked>Stock Clerk
                                      <br>
            <label>Location(s): </label> <br>
                                         <input type="checkbox" name="location" value="san diego">San Diego
                                         <br>
                                         <input type="checkbox" name="location" value="la jolla">La Jolla
                                         <br>
                                         <input type="checkbox" name="location" value="el cajon">El Cajon
                                         <br>
                                         <input type="checkbox" name="location" value="clairemont">Clairemont
                                         <br>
            <input type="submit" value="Submit" />'''
            
        page_close = '''</form>
    </body>
</html>'''


        if self.request.GET:
            name = self.request.GET['name']
            email = self.request.GET['email']
            age = self.request.GET['age']
            position = self.request.GET['position']
            location = self.request.GET['location']
            self.response.write(page_head + 'Name: ' + name + '<br>' + 'Email: ' + email + '<br>' + 'Age: ' + age + '<br>' + 'Position: ' + position + '<br>' + 'Location: ' + location + page_close)
        else:
            self.response.write(page_head + page_body + page_close)
        
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
