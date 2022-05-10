import codecs
codecs.register_error('strict', codecs.ignore_errors)

#==============================================================
#
#==============================================================

class Model:
    """
    The class to hold a model
    """
    def __init__(self, model_type, model_name, model_desc, model_file, model_path, model_languages, model_size):
        self.type = model_type
        self.name = model_name
        self.desc = model_desc
        self.file = model_file
        self.path = model_path
        self.languages = model_languages
        self.size = model_size
        
    def __str__(self):
        return "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (self.type, self.name, self.desc, self.file, self.path, self.languages, self.size)

#==============================================================
#
#==============================================================

def get_models(moses_dir, moses_model_dir):
   
