import sys, threading

def run():
    subprocess.call(['python', '-m', 'SimpleHTTPServer', '9000'])

def open_browser():
    webbrowser.open('http://localhost:9000')

def main(output_path):
    build_dir = '_build'
    os.path.exists(build_dir) or os.mkdir(build_dir)
    os.path.exists(build_dir + '/assets') or shutil.copytree('assets', build_dir + '/assets')
    subprocess.call(['scss', '-t', 'compressed', '--sourcemap=none', 'css/style.scss', build_dir + '/style.css'])
    subprocess.call(['pug', '-O', '{"baseurl": "/"}', '--out', build_dir, '--obj', '{"title": "Feng Zeng", "bodyclass": "project", "project_name": "Hunting"}', 'pug/index.pug'])

    if os.path.exists(output_path):
        shutil.r
