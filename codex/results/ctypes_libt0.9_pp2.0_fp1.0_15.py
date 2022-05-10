import ctypes
ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)

#XGboost regression
import xgboost as xgb
regr = xgb.XGBRegressor(
                 colsample_bytree=0.2,
                 gamma=0.0,
                 learning_rate=0.05,
                 max_depth=6,
                 min_child_weight=1.5,
                 n_estimators=7200,                                                                  
                 reg_alpha=0.9,
                 reg_lambda=0.6,
                 subsample=0.2,
                 seed=42,
                 silent=1)

regr.fit(X_train, Y_train)

# Predict on testing set
y_pred = regr.predict(X_train)

# Print result
Y_train = Y_train.astype(int)
print("Train RMSE : ", sqrt(mean_squared_error(Y_train, y_pred)))

# Predict on testing set
y_pred = regr.predict(
