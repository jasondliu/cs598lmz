from types import FunctionType
list(FunctionType(target_function).__code__.co_varnames)

# append
df["target_function_params"] = [{"p" + str(i): p for i,p in enumerate(list(FunctionType(target_function).__code__.co_varnames))}]

# preview
df.head()

# inspect
df[["target_function", "target_function_params"]].sample(1, random_state=42).values.tolist()[0]

# pickle
df.to_pickle("df_artificial_descriptions.pkl")

# ================================================================================
# not used, but important
# ================================================================================
def join_single_explain(x, y=None):
    """
    Join the results of a single explain into the usual format.
    """
    # override y
    if y is None:
        y = [0]

    # check that models were passed
    if isinstance(x, list):
        x = x[0]

    if isinstance(y[0], list):
        y = y
