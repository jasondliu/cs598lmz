import mmap

app = Flask(__name__)
app.config["DEBUG"] = True

PLACES = {
    "0": "mudd",
    "1": "wien",
    "2": "ferry",
    "3": "ludlow",
    "4": "claremont",
}

# if we have a db, this is how you would access it
#data = flaskr.get_db()

# initializing data dictionary to track number of checkins per location
# if we have a db, this is how you would access it
data = {}
for place in PLACES:
    data[PLACES[place]] = 0


@app.route("/")
def index():
    return render_template("main.html", places=PLACES)

@app.route("/total/")
def get_total():
    return render_template("total.html", data=data)

@app.route("/checkin/<place>")
def checkin(place):
    data[place] += 1
    print("checked in for
