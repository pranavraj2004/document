def findAngle(hours, minutes):
    hours = hours % 12
    a = (hours * 360) // 12 + (minutes * 360) // (12 * 60)
    b = (minutes * 360) // (60)
    angle = abs(a - b)
    if angle > 180:
        angle = 360 - angle
    return angle

if __name__ == '__main__':
    hours=5
    minutes=35 
    print('Input:',hours,':',minutes)
    print('Output:',findAngle(hours, minutes))
 