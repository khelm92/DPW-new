class View(object):
    def __init__(self):
        self.head = '''<!DOCTYPE HTML> 
<html>
    <head>
        <title>Reusable Library Assignment</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''
    
        self.body = '''<h2>Please enter your information for a personal training session:</h2> <br>
        <form method="GET" action="">
            <label>Full Name: </label> <input type="text" name="name">
            <br>
            <label>Gender: </label> <br>
                                    <input type="radio" name="gender" value="male" checked>Male
                                    <br>
                                    <input type="radio" name="gender" value="female" checked>Female
                                    <br>
            <label>Age: </label> <input type="text" name="age">
            <br>
            <label>Weight(lbs): </label> <input type="text" name="weight">
            <br>
            <input type="submit" value="Submit" id="submit" />
        '''
        self.close = '''
        </form>
    </body>
</html>'''

    def print_out(self):
        all = self.head + self.body + self.close
        return all
    


