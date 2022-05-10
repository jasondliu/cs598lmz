import threading
threading._DummyThread._Thread__stop = lambda x: 42

if __name__ == '__main__':
    import sys
    import os
    os.getcwd()
    root = os.path.dirname(os.getcwd())
    import sys
    sys.path.append(root)
    from src.bayes_opt import BayesianOptimization
    from src.utility import Utility
    from src.progress_bar import ProgressBar
    from src.result import Result
    from src.plot_result import PlotResult
    from src.datareader import DataReader
    from src.quantile_regression import QuantileRegression
    from src.kriging import Kriging
    from src.k_fold_cross_validation import k_fold_cross_validation
    import pandas as pd
    import numpy as np
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
    import winsound

    result = Result()
    plot_result = PlotResult()
