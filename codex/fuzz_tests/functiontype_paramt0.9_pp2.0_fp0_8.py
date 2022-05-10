from types import FunctionType
list(FunctionType())

plt.hist(df_train['SalePrice'])
plt.show()

#skewed to the right
print("Skew is:", df_train.SalePrice.skew())
plt.hist(df_train['GrLivArea'])
plt.show()

#does appear to be skewed
print("Skew is:", df_train.GrLivArea.skew())
plt.scatter(df_train['GrLivArea'], df_train['SalePrice'])
plt.show()

#log transformation of the target variable
target = np.log(df_train['SalePrice'])
print ("Skew is:", target.skew())
plt.hist(target)
plt.show()

#log transformation of the target variable (didnt use)
#Y = np.log(Y)
#Y.shape = (1458,1)

#all columns in the training set (to be used in selecting our final variables)
all_columns = df_train.
