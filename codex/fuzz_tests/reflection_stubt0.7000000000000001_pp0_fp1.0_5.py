fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'test'
fn()

# test_reactjs
print('test_reactjs')
import reactjs as rj
rj.render(rj.create_element('div', {'style': 'color: black'}, 'hello'))
rj.render(rj.create_element('div', {'style': 'color: black'}, 'hello world'))
rj.render(rj.create_element('div', {'style': 'color: black'}, 'hello world', '!'))
rj.render(rj.create_element('div', {'style': 'color: black'}, 'hello world', '!', '!'))
rj.render(rj.create_element('div', {'style': 'color: black'}, 'hello world', '!', '!', None, '!'))
rj.render(rj.create_element('div', {'style': 'color: black'}, 'hello world', rj.create_element('div')))
rj.render(rj.
