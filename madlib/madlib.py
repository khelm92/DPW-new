
#initial instructions-----------------------------------------------------------
print "Answer the questions to unlock a magical and devious story"

#all raw inputs collecting information from user--------------------------------
name = raw_input("What is your name? ")
gender = raw_input("Are you a boy or a girl? ")

first_year = raw_input("Enter a number between 5000-10000 ")
second_year = raw_input("Enter another number between 1-5 ")

location = raw_input("What is your favorite place in the world? ")

monster_1 = raw_input("What is a monster from your worst nightmare? ")
monster_2 = raw_input("What is an adorable animal from your best dream? ")


#mathematical operator----------------------------------------------------------
year_answer = 1. * int(first_year) / int(second_year)


#else if statement--------------------------------------------------------------
if year_answer > 5000:
    year = 3015
elif year_answer < 5000:
    year = 1182
else:
    pass

#functions----------------------------------------------------------------------
def calcNumOne(x, y):
    num_one = int(x) * int(y)
    return num_one

def calcNumTwo(a, b):
    num_two = int(a) - int(b)
    return num_two

#invoking the functions---------------------------------------------------------
number_1 = calcNumOne(first_year, second_year);
number_2 = calcNumTwo(first_year, second_year);


#finished story-----------------------------------------------------------------    
story = ''' When a young {gender} named Little {name} was in class one day, the teacher asked Little {name} "if there was anywhere in the world you could go at anytime, where would it be?"
and Little {name} answered "Well I would go to {location} in the year {year}!", and instantly Little {name} was teleported there magically! Only to find out that the spell misfired, and the world was
filled with horrible {monster_1}s and terrible {monster_2}s. Next, a genie showed up, and said "I will get you out of here, but you must slay {number_1} {monster_1}s and capture {number_2}
{monster_2}s". So Little {name} set off on the arduous quest. Unbeknownst to Little {name}, the devious genie had his fingers cross behind his back. When Little {name} returned, the genie had
disappeared, and Little {name} was doomed to live in this magical world forever. '''

story = story.format(**locals())
print story