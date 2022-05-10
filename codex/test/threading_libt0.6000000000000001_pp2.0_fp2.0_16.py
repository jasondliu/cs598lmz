import threading
threading.Thread(target=lambda: subprocess.call(["python", "./run_tests.py"])).start()

from app import app
app.run(debug=True, host='0.0.0.0', port=8000)
