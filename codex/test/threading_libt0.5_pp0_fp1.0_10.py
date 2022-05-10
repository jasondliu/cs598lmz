import threading
threading.stack_size(67108864)

# import from the 21 Developer Library
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

# set up bitrequest client for BitTransfer requests
wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

# server address
server_url = 'http://localhost:5000/'

# endpoint
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # get the file
    file = request.files['image']
    # read the file
    file_bytes = io.BytesIO(file.read())
    # get the file name
    file_name = file.filename
    # save the file to the server
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
    # return the file name

