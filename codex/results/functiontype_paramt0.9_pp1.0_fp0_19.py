from types import FunctionType
list(FunctionType(lambda x:x.startswith('does_'), loc), filter(FunctionType(lambda x:x.startswith('does_'), loc)))



# print(pd.DataFrame(A,B,C,D,E,F,G,H,I,J))

# Read in results file
results_file = pd.read_csv(open(flname + "_results.csv")).set_index("Metric")
results_file.index = results_file.index.str.replace("_", " ")

# Read in model predictions
# predictions_df = pd.read_csv(open(root + flname + "_pred.csv")).set_index("file")
# predictions_df = predictions_df.iloc[:, :2]
#
# # Group the predictions into predictions for a given model
# predictions_df["model"] = predictions_df.index
# predictions_df.at[predictions_df.index[0], "model"] = predictions_df.index[0].split("_")[
#     0] + "_" + predictions_df.index
