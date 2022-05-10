import weakref


class ESM(RichComponent):
    """
    Exact sliding mode controller with delta-nerr integration.
    """

    def __init__(self, K, Cs, Cr, Kp, Ki, Kv, **kwargs):
        self.K = asarray(K).astype(float)
        self.Cs = asarray(Cs).astype(float)
        self.Cr = asarray(Cr).astype(float)
        self.Kp = Kp
        self.Ki = Ki
        self.Kv = Kv
        self.Kp_i = None
        self.Ki_i = None
        self.Kv_i = None
        self.e_i = None
        self.RUBI = None
        self.feedback_r = False
        ode = ode.RK45(lambda t, y1: - self.Cr @ y1, lambda t, y1, y2: - self.Cs @ y2 + self.K @ y1, 0, 1e-8)
