import select_data
 
train_data,test_data,bad_data=read_data.get_data()
train_tfidf,test_tfidf,bad_tfidf=select_data.get_data()

param={}
param['num_round']=100
param['objective']='binary:logistic'
param['seed']=1
param['eta']=0.1


def model_fit(train_tfidf,train_data):
   
    param['eval_metric']='auc'
    num_round=param['num_round']
    param['silent']=1
    bst=xgb.train(param,train_tfidf,num_round,evals=[(train_tfidf,'train')])
    return bst
    
def model_predict(test_tfidf,bst):
    
    preds=bst.predict(test_tfidf)
    pred_class=[]
    for i in preds:
        if i<0.5:
            pred_class.append(
