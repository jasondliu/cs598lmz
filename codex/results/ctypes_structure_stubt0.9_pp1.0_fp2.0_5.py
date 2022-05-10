import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float
    s = ctypes.c_char_p

def main():
    prog = Prog()
    prog.add( shaders.vertex.textured, shaders.fragment.textured )
    prog.use()

    vertices = [
            # positions    # texture coords
            0.5,  0.5, 0.0, 1.0, 1.0, # top right
            0.5, -0.5, 0.0, 1.0, 0.0, # bottom right
            -0.5, -0.5, 0.0, 0.0, 0.0, # bottom left
            -0.5,  0.5, 0.0, 0.0, 1.0  # top left
            ]
    indices = [
        0, 1, 3,  # first Triangle
        1, 2, 3   # second Triangle
        ]

    #VAO Gen 
    VAO = glGenVertexArrays(1)

    #VBO GEN, DATA INTO BUFFER, BIND
    VBO
