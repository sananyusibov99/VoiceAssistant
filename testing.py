import wmi


def inceeeese():
    c = wmi.WMI(namespace='wmi')
    current = c.WmiMonitorBrightness()[0]
    brightness = current.CurrentBrightness + 10
    if brightness < 100:
        methods = c.WmiMonitorBrightnessMethods()[0]
        methods.WmiSetBrightness(brightness, 0)
    else:
        print("Brightness is maximum")


def decreese():
    c = wmi.WMI(namespace='wmi')
    current = c.WmiMonitorBrightness()[0]
    brightness = current.CurrentBrightness - 10

    if brightness > 5:
        methods = c.WmiMonitorBrightnessMethods()[0]
        methods.WmiSetBrightness(brightness, 0)
    else:
        print("Brightness is minimum")



inceeeese()



