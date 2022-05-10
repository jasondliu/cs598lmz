import codecs
codecs.register_error('ignore', codecs.lookup('utf-8') if codecs.lookup('utf-8') else codecs.lookup('latin-1'))


def _get_writer(writer_name):
    if writer_name == 'csv':
        return CSVWriter
    elif writer_name == 'xml':
        raise NotImplementedError
    elif writer_name == 'json':
        return JsonWriter
    elif writer_name == 'txt':
        return TextWriter
    elif writer_name == 'html':
        return HtmlWriter
    elif writer_name == 'xlsx':
        return ExcelWriter
    elif writer_name == 'excel':
        return ExcelWriter
    elif writer_name == 'xls':
        return ExcelWriter
    elif writer_name == 'excelx':
        return ExcelWriter
    else:
        raise NotImplementedError('Unsupported writer: ' + writer_name)


def setup_writer(config, channel):
    writer_name = channel.get('writer', 'csv')
    writer =
