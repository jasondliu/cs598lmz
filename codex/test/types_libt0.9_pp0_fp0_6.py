import types
types.ClassType = type

def get_data_dir():
  """ Get the data dir """
  filepath = os.path.dirname(sys.argv[0])
  if os.path.isdir(os.path.join(filepath, 'data')):
    data_dir = os.path.join(filepath, 'data')
  else:
    data_dir = sys.path[0]
  return data_dir

# get the data_dir
DATA = get_data_dir()

# set the minidom parser
domimpl = xml.dom.minidom.getDOMImplementation()

def get_elem_content(elem, attr_name):
  """ Return the attribute as string """
  content = ''
