import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def main(): #pragma: no cover
    if len(sys.argv) == 1:
        print("Usage: {0} <junit-report-file>".format(sys.argv[0]))
        sys.exit(0)

    junit_report_file = sys.argv[1]
    if not os.path.exists(junit_report_file):
        print("File '{0}' not found.".format(junit_report_file))
        sys.exit(1)

    with open(junit_report_file, "r") as f:
        report_xml = f.read()

    junit_report = JUnitReport(report_xml)
    categories = junit_report.get_categories()

    for category in categories:
        start_time = None
        end_time = None

