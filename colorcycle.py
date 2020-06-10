#!/usr/bin/python3
# import argparse
# ps = argparse.ArgumentParser(description='Parses and presents data from Discord\'s data dump')
# ps.add_argument("sublprefs", type=str, help='Path to Sublime Text\'s preferences file')
# args = ps.parse_args()

sublfile="/home/wcs/.config/sublime-text-3/Packages/User/Preferences.sublime-settings"
subllight="Packages/Solarized Color Scheme/Solarized (light).sublime-color-scheme"
subldark="Packages/Solarized Color Scheme/Solarized (dark).sublime-color-scheme"

# Sublime Text
sublprefs = open(sublfile, "r+")
outprefs = sublprefs.read()
if subllight in outprefs:
    outprefs = outprefs.replace(subllight, subldark)
else:
    outprefs = outprefs.replace(subldark, subllight)
sublprefs.seek(0)
sublprefs.write(outprefs)
sublprefs.close()