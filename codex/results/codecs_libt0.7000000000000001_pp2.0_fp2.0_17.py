import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

def readCSV(csvFileName):
    """ Function that reads the input CSV file and formats the data properly.
        Input:
            csvFileName: The name of the CSV file that contains the input data.
        Returns:
            A list of lists of the data contained in the CSV file.
    """
    with open(csvFileName, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    # Convert strings to floats.
    for i in range(len(data)):
        for j in range(1, len(data[i])):
            data[i][j] = float(data[i][j])

    return data

def writeCSV(data, csvFileName):
    """ Function that writes the output data to a CSV file.
        Input:
            data: The data to be written to the CSV file.
            csvFileName: The name of the CSV file to write the data to.

