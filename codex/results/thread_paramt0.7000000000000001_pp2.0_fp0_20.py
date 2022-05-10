import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

# Create a callback on_prediction that will be called on every prediction and add it to the model
def on_prediction(model, classes, scores):
    print('Predicted:', ' '.join(str(classes[0][i]) for i in range(5)))
    print('Scores:', ' '.join(str(scores[0][i]) for i in range(5)))
coco_model.set_forward_callback(on_prediction) 

# Run the model on the test image
coco_model.eval_image(input='images/cat.jpg')

# Check the predicted class
coco_model.predicted_class

# Check the predicted scores
coco_model.predicted_scores

# Check all the predictions
coco_model.predictions

# Check the category names of the predictions
coco_model.predicted_names

# Check the scores of the predictions
coco_model.predicted_scores

# Check the categories of the predictions
coco_model.
