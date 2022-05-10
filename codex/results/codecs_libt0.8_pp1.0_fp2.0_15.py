import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

# from bokeh.plotting import figure, output_file, show
# from bokeh.sampledata.glucose import data

# import pandas as pd
# y=[1,2,3,4,5]
# x=[1,2,3,4,5]
# y2=[]
# x2=[]
# data1=pd.DataFrame({'p':y,'q':x})
# data2=pd.DataFrame({'p':y2,'q':x2})
# p = figure(plot_width=400, plot_height=400)
# p.line(x, y, line_width=2)
# p.scatter(x,y,fill_color="white", size=8)
# p.circle(x, y, fill_color="red", size=4)

# p.line(x2, y2, line_color="green", line_width=2)
# p.sc
