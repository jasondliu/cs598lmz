import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)

#==============================================================================
#
#   Example: 
#   
#   python convert_to_utf8.py --input_dir=C:\Users\user\Documents\test\test --output_dir=C:\Users\user\Documents\test\test\utf8 --encoding=Shift_JIS
#
#==============================================================================

def main(argv):
    input_dir = ''
    output_dir = ''
    encoding = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:e:",["input_dir=","output_dir=","encoding="])
    except getopt.GetoptError:
        print ('convert_to_utf8.py -i <input_dir> -o <output_dir> -e <encoding>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('convert_to_utf8.py -i <input_dir> -o <output_
