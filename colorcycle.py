#!/usr/bin/python3
from os import system
import dbus

# Sublime Text
sublfile = "/home/wcs/.config/sublime-text-3/Packages/User/Preferences.sublime-settings"
subllight = "Packages/Solarized Color Scheme/Solarized (light).sublime-color-scheme"
subldark = "Packages/Solarized Color Scheme/Solarized (dark).sublime-color-scheme"

# urxvt
urxvtlight = "/home/wcs/.urxvt/themes/solarized-light"
urxvtdark = "/home/wcs/.urxvt/themes/solarized-dark"

# Wallpaper
# 1 screen
# walldict = {0: {"dark": "/path/to/darkwall.jpg", "light": "/path/to/lightwall.jpg"}}

# 2 or more screens
walldict = {0: {"dark": "/home/wcs/Pictures/Wallpapers/darkright.jpg", "light": "/home/wcs/Pictures/Wallpapers/lightright.jpg"},
            1: {"dark": "/home/wcs/Pictures/Wallpapers/darkleft.jpg", "light": "/home/wcs/Pictures/Wallpapers/lightleft.jpg"}
            }

# GTK
gtkcycle = False
gtkpath = "/home/wcs/.config/gtk-3.0/settings.ini"






ts = "dark"



# Sublime Text
sublprefs = open(sublfile, "r+")
outprefs = sublprefs.read()
if subllight in outprefs:
    ts = "dark"
    outprefs = outprefs.replace(subllight, subldark)
else:
    ts = "light"
    outprefs = outprefs.replace(subldark, subllight)
sublprefs.seek(0)
sublprefs.write(outprefs)
sublprefs.close()



# urxvt
if ts == "dark":
    system("xrdb -load "+urxvtdark)
else:
    system("xrdb -load "+urxvtlight)
system("kill -1 $(pidof urxvtd)")



# Wallpaper
def setwallpaper(filepath, screennum):
    jscript = """
    var allDesktops = desktops();
    print (allDesktops);
    d = allDesktops[%i];
    d.wallpaperPlugin = "org.kde.image";
    d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
    d.writeConfig("Image", "file://%s")
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    plasma.evaluateScript(jscript % (screennum, filepath))
for i in range(0, len(walldict)):
    if ts == "dark":
        setwallpaper(walldict[i]["dark"], i)
    else:
        setwallpaper(walldict[i]["light"], i)


# GTK retardation
if gtkcycle:
    gtkfile = open(gtkpath)
    gtksettings=gtkfile.read()
    if "gtk-application-prefer-dark-theme" not in gtksettings:
        if ts == "dark":
            gtksettings+="\ngtk-application-prefer-dark-theme=1"
        else:
            gtksettings+="\ngtk-application-prefer-dark-theme=0"
    else:
        if ts == "dark":
            gtksettings = gtksettings.replace("gtk-application-prefer-dark-theme=0", "gtk-application-prefer-dark-theme=1")
        else:
            gtksettings = gtksettings.replace("gtk-application-prefer-dark-theme=1", "gtk-application-prefer-dark-theme=0")
    gtkfile.seek(0)
    gtkfile.write(gtksettings)
    gtkfile.close()