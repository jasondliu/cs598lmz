import codecs
codecs.register_error('backslashreplace', lambda e: (u'\\x%02x' % ord(e.object[e.start]), e.end))

def my_load_json(path):
    with codecs.open(path, 'r', 'utf-8', 'backslashreplace') as f:
        return json.loads(f.read())


class Base(object):
    def __init__(self, name, data_dir, source_dir, target_dir, source_image_file_name, target_image_file_name,
                 source_image_ext, target_image_ext, source_json_file_name, target_json_file_name,
                 source_json_ext, target_json_ext, source_image_dir, target_image_dir,
                 image_dir_prefix, image_dir_suffix, additional_image_dir, output_image_dir, output_json_dir,
                 output_json_file_name, output_image_file_name, output_image_ext, output_json_ext,
                 source_json_dir, target
