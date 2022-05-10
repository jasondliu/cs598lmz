import threading
threading.stack_size(32768)


## set the simulation parameters
pricing_date = QDate(8, 4, 2018)


## From this point, we just rely on the SmartDerivatives pricing engine
sde = sde_qt.SmartDerivativesEngine()


## set currency
sde.setCurrency('EUR')


## initialize the underlying object
sde.initHestonModel('EURO STOXX 50', pricing_date, spot=3504.05)


## set the risk free rate
sde.setRiskFreeRate('EONIA', risk_free_rate=0.21/100)


## set the volatility
sde.set_heston_model(
    heston_model_params=dict(
        kappa=3.220,
        theta=0.0375,
        sigma=0.4700,
        rho=-0.3700,
        v0=0.0461
    ),
    heston_model_variance_param_type='1F_constant'
)


## reference model based
