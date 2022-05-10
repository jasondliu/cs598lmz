import _struct
import binascii
import time
import datetime

# local imports
import vtki
import pymol
import pymol.cmd
import pymol.cgo
import pymol.vfont

# import some shortcut names
draw_box = pymol.cgo.draw_box
draw_sphere = pymol.cgo.draw_sphere
draw_cylinder = pymol.cgo.draw_cylinder
draw_arrow = pymol.cgo.draw_arrow
draw_label = pymol.cgo.draw_label
draw_text = pymol.cgo.draw_text
draw_string = pymol.cgo.draw_string
draw_cone = pymol.cgo.draw_cone
draw_star = pymol.cgo.draw_star

# import some primitive names
sphere = pymol.cgo.sphere
cylinder = pymol.cgo.cylinder
arrow = pymol.cgo.arrow
cone = pymol.cgo.cone
label =
