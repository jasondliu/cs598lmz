import types
types._check_isinstance()

from vispy.testing import run_tests_if_main, requires_testing_data


@requires_testing_data
def test_occlusion_fbo_app():
    """Test occlusion culling on meshes with a 0.8 near and a 1000. far plane.
    Ensure that the objects are outside of the frustum and the number of draw
    calls is 0"""

    import numpy as np
    from vispy import gloo
    from vispy.gloo import FrameBuffer
    from vispy import app
    from vispy.gloo import Texture2D
    # create dummy mesh and set position to be outside of frustum
    n = 3

    verts = np.random.rand(n, 3).astype(np.float32) * 10.0
    fbofrag = """
        precision mediump float;
        varying vec2 v_texcoord;
        void main(){
            gl_FragColor = vec4(v_texcoord,0.0,0.0);
        }
        """
