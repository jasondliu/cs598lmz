import types
types.MethodType(self.plot_d3,self)

def plot_d3(self):
    bokeh.eval_js("Bokeh.embed.embed_items('div.bk-root', {docs: [%s]});" % ",".join(repr(plot) for plot in self.plots))
</code>

