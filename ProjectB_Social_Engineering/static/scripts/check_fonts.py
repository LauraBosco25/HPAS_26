import os

ROOT = os.path.join(os.path.dirname(__file__), '..')
FONTS_DIR = os.path.normpath(os.path.join(ROOT, 'fonts'))
EXPECTED = [
    'polimi_icons_line.eot',
    'polimi_icons_line.ttf',
    'polimi_icons_line.woff',
    'polimi_icons_line.svg',
    'polimi_icons_solid.eot',
    'polimi_icons_solid.ttf',
    'polimi_icons_solid.woff',
    'polimi_icons_solid.svg',
]

missing = []
for f in EXPECTED:
    p = os.path.join(FONTS_DIR, f)
    if not os.path.exists(p):
        missing.append(f)

if not missing:
    print('All expected polimi font files are present in', FONTS_DIR)
else:
    print('Missing font files in', FONTS_DIR)
    for m in missing:
        print(' -', m)

print('\nNote: add the fonts to the directory and re-run this script or restart the dev server to pick them up.')