import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

 

# #### define a feature selection algorithm based on mutual information
# * the selection criterion is the feature that results in a minimal average information gain
# * calculate the mutual information between the labels and the feature
# * calculate the average information gain for each feature
# * select the feature with the lowest average information gain

# In[33]:


def mutual_info_feature_selection(X, Y, no_of_features):
    # calculates the mutual information between all features and the labels
    mi = mutual_info_classif(X,Y, discrete_features='auto', n_neighbors=3, copy=True, random_state=None)
    
    # merge the features and their mutual information score
    features_mi = list(zip(list(X), mi))
    
    # sort the features according to their mutual information
    sorted_features_mi = sorted(features_mi, key=lambda x: x[1], reverse=True)
    
    # keep the no_of_features features with the highest mutual information
    sorted_features_
