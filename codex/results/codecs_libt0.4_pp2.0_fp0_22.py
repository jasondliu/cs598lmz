import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# create a Flask app
app = Flask(__name__)

# Load the model
model = load_model('model.h5')

# Load the encoder
with open('encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

# Load the vectorizer
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Define a route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the review from the POST request.
        review = request.form['review']
        
        # Vectorize the review
        vectorized_review = vectorizer.transform([review])
        # Make a prediction
        prediction = model.predict(vectorized_review)[0]
        # Get the predicted sentiment
        sentiment = encoder.inverse_transform(np
