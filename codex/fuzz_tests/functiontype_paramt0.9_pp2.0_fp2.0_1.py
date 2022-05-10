from types import FunctionType
list(FunctionType(sum.__code__))
</code>
results in
<code>[&lt;function sum at 0x02A40A40&gt;, 'sum', 'builtins']
</code>
I wonder why <code>sum</code> is not in <code>__globals__</code> after all. If you run <code>print(sum)</code> it will print:
<code>&lt;built-in function sum&gt;
</code>
To fully answer your question, though, I think you need to wait for someone who fully understand the inner workings of Python but as you can see it is not a simple situation. :)

