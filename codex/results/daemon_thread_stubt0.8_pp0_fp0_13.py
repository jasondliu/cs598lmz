import sys, threading

def run():
    sys.path = [os.path.join(os.path.dirname(__file__), "libs")] + sys.path
    try:
        print('ok')
        from kiteconnect import KiteConnect
        print('loaded')
        return KiteConnect(api_key="kitefront")
    except:
        print('error')
        traceback.print_exc()
        return None

threading.Thread(target=run).start()
</code>
When I run this, I get
<code>$ python3 
[...]
&gt;&gt;&gt; import kiteconnectproxy
ok

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "kiteconnectproxy.py", line 10, in &lt;module&gt;
    from kiteconnect import KiteConnect
ModuleNotFoundError: No module named 'kiteconnect'
&gt;&gt;&gt;
</code>
Apparently the import is asynchronous, not happening in the
