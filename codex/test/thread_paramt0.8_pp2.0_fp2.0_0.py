import sys, threading
threading.Thread(target=lambda: sys.stdout.write("""
<html><body>
<img src="https://cdn.theatlantic.com/static/mt/assets/science/surrogate.jpg" width=100%><br><br>
<p>
You are about to take part in an experiment for which you will receive compensation.
</p><p>
<form name="submit" method="POST">
<input type="submit" name="agree"
value="I agree to take part in this experiment">
</form>
</p>
</body></html>
"""
)).start()
