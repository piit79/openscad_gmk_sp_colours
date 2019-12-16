#!/usr/bin/env python3
"""
Create an OpenSCAD file with GMK / Signature Plastics colour definitions
based on the data from the Keyboard Layout Editor
"""

import json
import re
import urllib.request

# Input file from Keyboard Layout Editor
url = 'https://github.com/ijprest/keyboard-layout-editor/raw/master/colors.json'
filename = 'gmk_sp_colours.scad'

# Mapping of colour group names to variable prefixes
name2prefix = {
    'GMK / Uniqey Colors': 'GMK',
    'Signature Plastics ABS': 'SP_ABS',
    'Signature Plastics PBT': 'SP_PBT',
}

# Replacements to be made in the colour name
colour_code_replacements = [
    (' (not color corrected)', '_RAW'),
]

# Get the colors.json file from KLE
response = urllib.request.urlopen(url)
colours = json.load(response)

lines = []
for group in colours:
    prefix = name2prefix.get(group['name'])
    if not prefix:
        # Prefix not defined, skip this group
        continue
    lines.append('// ' + group['name'] + '\n')
    for c in group['colors']:
        code = c['name']
        # Make specific replacements in the colour name
        for old, new in colour_code_replacements:
            code = code.replace(old, new)
        # Ensure the colour name will make a valid identifier
        code = re.sub(r'\W', '_', code)
        line_format = '{prefix}_{code} = "#{r:02x}{g:02x}{b:02x}";\n'
        line = line_format.format(prefix=prefix, code=code, r=int(c['r']), g=int(c['g']), b=int(c['b']))
        lines.append(line)
    lines.append('\n')

# Write all but the last (blank) line to a file
with open(filename, 'w') as fp:
    fp.writelines(lines[:-1])
