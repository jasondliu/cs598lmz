import threading
threading.Thread(target=start_server, daemon=True).start()

# Wait until the server is ready
# port=8888.wait_for_port()

# Connect to the server
from qiskit import IBMQ
IBMQ.load_accounts()
provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
backend = provider.get_backend('ibmq_valencia')

from qiskit.tools.monitor import job_monitor
job = execute(circ, backend)
job_monitor(job)

# Retrieve the results
result = job.result()
counts = result.get_counts(circ)
print("\nTotal count are:",counts)
