class Page(object):
    def _init_(self):
        self._title = "Welcome!"
        self.css = "css/styles.css"
        self._head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Enter your information:</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        
        self.body = ""
        self._error = ''
        self._close = """
    </body>
</html>
        """
        
    def print_out(self):
        all = self._head + self.body + self._error + self._close
        return all

