# Give the current speed of the diver in km/h and the average allowed speed of the road.

speed_of_the_driver = float(input("What was your average speed in km/h: "))
allowed_speed_on_the_road = float(input("What was the allowed speed on the road: "))

points = (speed_of_the_driver-allowed_speed_on_the_road)/5
if speed_of_the_driver > 60:
    print("Point:" +str(points))
    print("Time to go to jail.")
else:
    print("Ok")