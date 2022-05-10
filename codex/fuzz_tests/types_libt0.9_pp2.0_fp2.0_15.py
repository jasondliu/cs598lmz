import types
types.

def get_mcc_class(name):
    classes = inspect.getmembers(MCC_classification,inspect.isclass)
    for c, t in classes:
        if t.__name__ == name:
            return t
    return None


def get_transition_class(name):
    classes = inspect.getmembers(transition_classification,inspect.isclass)
    for c, t in classes:
        if t.__name__ == name:
            return t
    return None

def get_classes(path):
    with open('{}_truth.txt'.format(path),'r') as f:
        content = f.readlines()
    with open('{}_predicted.txt'.format(path),'r') as f:
        content_predicted = f.readlines()
    if len(content) != len(content_predicted):
        raise Exception("Predicted values not the same length as ground truth")
    y_true = [l.replace("\n","") for l in content]
    y_pred = [
