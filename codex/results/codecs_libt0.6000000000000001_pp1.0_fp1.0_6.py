import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# 参考：https://github.com/jiexunsee/pyecharts-snapshot/blob/master/main.py

def render(chart, path):
    # make sure path.parent.exists()
    if not path.parent.exists():
        path.parent.mkdir(parents=True)
    # chart.render()
    if path.suffix in ['.html', '.htm']:
        chart.render(path=str(path))
    else:
        chart.render(path=str(path), template_name='simple_color')

def render_all_charts(charts, path):
    for chart in charts:
        render(chart, path/f'{chart.js_dependencies[0]}-{chart.theme}.html')
        # render(chart, path/f'{chart.js_dependencies[0]}.html')

def main():
    path = Path('ch
