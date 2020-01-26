# GMK / Signature Plastics Colours for OpenSCAD
This repository contains a Python 3 script that creates a file with definitions of
[GMK/Uniqey](https://uniqey.net/) and [Signature Plastics](https://www.solutionsinplastic.com/)
colours for use in [OpenSCAD](https://www.openscad.org/). The colour definitions are generated
from data from the excellent [Keyboard Layout Editor](https://github.com/ijprest/keyboard-layout-editor)
project.

## Usage
Simply clone this repository to your project and run the script [kle2openscad.py](https://github.com/piit79/openscad_gmk_sp_colours/blob/master/kle2openscad.py)
using Python 3 (the script has no external dependencies):
```shell script
git clone https://github.com/piit79/openscad_gmk_sp_colours.git
cd openscad_gmk_sp_colours
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
Note the use of `include` and not `use` as the module needs to se the colour variables.

If you're tracking your project in Git, it's probably best to add this repository as a submodule:
```
git submodule add https://github.com/piit79/openscad_gmk_sp_colours.git
git submodule update --init
```

## Acknowledgements
Many thanks to Ian Prest, the author of Keyboard Layout Editor, and other contributors for their excellent
project and for creating the colour definitions.
