# GMK / Signature Plastics Colours for OpenSCAD
This repository contains a Python 3 script that creates a file with definitions of
[GMK/Uniqey](https://uniqey.net/) and [Signature Plastics](https://www.solutionsinplastic.com/)
colours for use in [OpenSCAD](https://www.openscad.org/). The colour definitions are generated
from data from the excellent [Keyboard Layout Editor](https://github.com/ijprest/keyboard-layout-editor)
project.

## Usage
Simply run the script [kle2openscad.py](https://github.com/piit79/openscad_gmk_sp_colours/blob/master/kle2openscad.py)
using Python 3:
```shell script
./kle2openscad.py
```
or
```shell script
python3 kle2openscad.py
```

This will create the file `gmk_sp_colours.scad` which you can `include` in your OpenSCAD project:
```
include <openscad_gmk_sp_colours/gmk_sp_colours.scad>;
```

Then you can use all the colours as follows:
```
color(GMK_CR) {
  ...
}
```

## Acknowledgements
Many thanks to Ian Prest, the author of Keyboard Layout Editor, and other contributors for their excellent
project and for creating the colour definitions.
