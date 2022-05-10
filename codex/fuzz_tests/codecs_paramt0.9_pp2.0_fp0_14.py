import codecs
codecs.register_error('PERCENT_REPLACE', ReplacePercent)

def format_percent(percent):
    return '%3.2f%%' % percent

# TODO move to a more convenient location
REPORT_HEADER = """<!DOCTYPE html>
<html>
<head>
<title>%s</title>
<style type="text/css">
body { font-family:sans-serif; font-size:13px; background:#ccc; }
h1,h2,h3,h4,h5,h6 { text-align:center; }
table.statistics_table, table.diff_table {
    width:100%%;
    font-family:sans-serif;
    font-size:14px;
    border-collapse:collapse;
}
.statistics_table th, .diff_table th { background:#226; color:#ffd; padding:6px; }
.statistics_table td, .diff_table td { background:#ddd; padding:6px; }
.pass>td { background:#cef
