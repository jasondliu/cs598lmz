import signal
signal.signal(signal.SIGINT, signal.default_int_handler)

import pprtdotnet

import PPRT
import PPRT.Constants
import PPRT.Utils

import PPRT.Material
import PPRT.Texture
import PPRT.TriMesh
import PPRT.ImageFormat

mat = PPRT.Material.Material(1)
nm = PPRT.Texture.Texture()
nm.Create('images/nm.jpg', 0, 0)
mat.AddTexture(nm, 'nm', PPRT.SHADER_INPUT_NORMAL)
d = PPRT.Texture.Texture()
d.Create('images/d.jpg', 0, 0)
mat.AddTexture(d, 'd', PPRT.SHADER_INPUT_DIFFUSE)
s = PPRT.Texture.Texture()
s.Create('images/s.jpg', 0, 0)
mat.AddTexture(s, 's', PPRT.SHADER_INPUT_SPECULAR)

tm = PPRT
