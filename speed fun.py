def driver_speed(speed):
    if speed<=70:
        print("ok")
    elif speed>=70:
        print("point2")
    elif speed>120:
        print("licence suspend")
    else:
        print("speed over")
driver_speed(30)   
driver_speed(80)
driver_speed()                 


