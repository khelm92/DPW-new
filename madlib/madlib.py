print "Answer the questions to unlock a magical and devious story"

name = raw_input("What is your name? ")
gender = raw_input("Are you a boy or a girl? ")

first_year = raw_input("Enter a number between 5000-10000 ")
second_year = raw_input("Enter another number between 1-5 ")

location = raw_input("What is your favorite place in the world? ")

monster_1 = raw_input("What is a monster from your worst nightmare? ")
monster_2 = raw_input("What is an adorable animal from your best dream? ")

year_answer = 1. * first_year / second_year

if year_answer > 5000:
    year = 3015
elif year_answer < 5000:
    year = 1182
else:
    pass
    








story = ''' When a young {gender} named Little {name} was in class one day, the teacher asked Little {name} "if there was anywhere in the world you could go at anytime, where would it be?"
and Little {name} answered "Well I would go to {location} in {year}!", and instantly Little {name} was teleported there magically! Only to find out that the spell misfired, and the world was
filled with horrible {monster_1} and terrible {monster_2}. Next, a genie showed up, and said "I will get you out of here, but you must slay {number_1} of {monster_1} and capture {number_2} of
{monster_2}". So Little {name} set off on the arduous quest. Unbeknownst to Little {name}, the devious genie had his fingers cross behind his back. When Little {name} returned, the genie had
disappeared, and Little {name} was doomed to live in this magical world forever. '''