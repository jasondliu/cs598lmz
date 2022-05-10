import threading
threading.stack_size(128*1024*1024)
###########################################################################

def main():
    """
    Main function for the program.
    """
    # Load the data from the csv file
    data = load_data()

    # Split the data into training, validation, and test sets
    data = split_data(data)

    # Fit a model on the training data
    model = fit_model(data)

    # Evaluate the model on the validation data
    predictions = predict(data, model)

    # Print the results of the model
    print_results(data, predictions)

def load_data():
    """
    Loads the data from the csv file and returns it.
    """
    # Load the data from the csv file
    data = pd.read_csv('data.csv')

    # Return the data
    return data

