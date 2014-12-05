first_name = "Kasey"
last_name = "Helm"

#response = raw_input("Enter your name  ")
#print "Hello there, ", response

birth_year = 1992
current_year = 2014
age = current_year - birth_year
#print "You are " + str(age) + " years old"

budget = 90

if budget > 100:
    brand = "nike"
    #print "Yay! we can buy cool " + brand + " shoes!"
elif budget > 50:
    #print "We can at least get some generic sneaker."
    pass
else:
    pass

characters = ["leia","luke","chewy","lando"]
characters.append("obi won")
#print characters[0]

movies = dict()
movies = {"Star Wars":"Darth Vader", "Silence of the Lambs":"Hannibal"}
#print movies["Star Wars"]

'''
i = 0
while i<9:
    print "the count is", i
    i = i+1
'''

'''    
for i in range(0,10):
    print "the count is", i
    i = i+1
'''

rappers = ["Tupac", "Nas", "Biggie Smalls"]
for r in rappers:
    #print "One of the best rappers is " + r
    pass

def calcArea(h, w):
    area = h * w
    return area

a = calcArea(20, 40);
#print "My area is " + str(a) + "sqft"

weight = 200
height = 63
message = '''
Your height is {height} and your weight is {weight}
'''
message = message.format(**locals())
print message
    