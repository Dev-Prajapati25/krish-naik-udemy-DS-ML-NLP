def greet(time=None, name="Mr/Ms"):
    if time in range(8,13):
        print("Good Morning,", name)
    elif time in range(13, 18):
        print("Good Afternoon,", name)
    elif time in range(18, 24):
        print("Good Evening,", name)
    elif time == None:
        print("Hello There")