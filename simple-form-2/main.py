#kasey helm; simple form assignment

import webapp2 #importing webapp from google app launcher

class MainHandler(webapp2.RequestHandler): #defining the MainHandler Class
    def get(self): #all HTML below, self explanatory I think :)
        page_head = '''<!DOCTYPE HTML> 
<html>
    <head>
        <title>Simple Form Assignment</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
        <link href='http://fonts.googleapis.com/css?family=Roboto' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Slabo+27px' rel='stylesheet' type='text/css'>
    </head>
    <body>'''
        #main body for the HTML
        page_body = '''<h1>Grocery Store Application</h1>
        <form method="GET" action="">
            <label><h3>Name:</h3> </label><input type="text" name="name"/>
            <br>
            <label><h3>Email:</h3> </label><input type="text" name="email"/>
            <br>
            <label><h3>Age:</h3> </label><input type="text" name="age"/>
            <br>
            <label><h3>Position:</h3> </label> <br>
                                      <input type="radio" name="position" value="cashier" checked>Cashier
                                      <br>
                                      <input type="radio" name="position" value="bagger" checked>Bagger
                                      <br>
                                      <input type="radio" name="position" value="stock clerk" checked>Stock Clerk
                                      <br>
            <label><h3>Location(s):</h3> </label> <br>
                                         <input type="checkbox" name="location" value="san diego">San Diego
                                         <br>
                                         <input type="checkbox" name="location" value="la jolla">La Jolla
                                         <br>
                                         <input type="checkbox" name="location" value="el cajon">El Cajon
                                         <br>
                                         <input type="checkbox" name="location" value="clairemont">Clairemont
                                         <br>
            <input type="submit" value="Submit" id="submit" />'''
        #closer for the HTML 
        page_close = '''</form>
    </body>
</html>'''

        #if else statement - if information is filled out, display results, if not then it displays the form again
        if self.request.GET: #getting information from the HTML to post on the results page
            name = self.request.GET['name'] #defining each object for when we 'write' the results to the page
            email = self.request.GET['email']
            age = self.request.GET['age']
            position = self.request.GET['position']
            location = self.request.GET['location']
            self.response.write(page_head + '<h1>Application Results:</h3>' + '<br>' + '<h3>Name:</h3> ' + name + '<br>' + '<h3>Email:</h3> ' + email + '<br>' + '<h3>Age:</h3> ' + age + '<br>' + '<h3>Position:</h3> ' + position + '<br>' + '<h3>Location:</h3> ' + location + page_close)
        else:
            self.response.write(page_head + page_body + page_close)
        
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
