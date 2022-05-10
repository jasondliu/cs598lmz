import select_data
import sys
import os

def main():
    # get the argument from terminal
    #argvs = sys.argv
    #argc = len(argvs)
    #if (argc != 2):
    #    print "Usage: python %s filename" % argvs[0]
    #    quit()
    #filename = argvs[1]
    # read the data from the file
    #data = read_data.read_file(filename)
    # read the data from the db
    data = select_data.select_db()
    # convert the data to the json format
    json_data = convert_data.convert_to_json(data)
    # write the json data to the file
    write_data.write_to_file(json_data)
    return

if __name__ == '__main__':
    main()
