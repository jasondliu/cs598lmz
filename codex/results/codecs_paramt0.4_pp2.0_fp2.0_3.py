import codecs
codecs.register_error('ignore', codecs.lookup('ignore'))

def main():
    # Read the file
    with codecs.open('../../data/parsed_data/parsed_data.csv', 'r', 'utf-8') as f:
        # Skip the header
        f.readline()
        # Read the rest of the file
        lines = f.readlines()
    # Parse the lines
    lines = [line.strip().split('\t') for line in lines]
    # Get the columns
    columns = [line[0] for line in lines]
    # Get the values
    values = [line[1:] for line in lines]
    # Convert the values to ints
    values = [[int(value) for value in line] for line in values]
    # Create the dataframe
    df = pd.DataFrame(values, columns=columns)
    # Plot the data
    df.plot(kind='bar', stacked=True)
    # Show the plot
    plt.show()

if __name__ == '__main__':
   
