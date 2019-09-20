# Ian McLoughlin, 2019
# Run with: env FLASK_APP=distros.py flask run

# Import flask for web app stuff.
import flask as fl
# Import numpy for generating random numbers.
import numpy as np

# Create a flask web app.
app = fl.Flask(__name__)

# Add a route for the binomial distribution.
@app.route('/binomial')
def binomial():
  # The number of trials to run, default 1.
  trials = int(fl.request.args.get("trials", "1"))
  # The probability of a success, default 0.5.
  prob = float(fl.request.args.get("prob", "0.5"))
  # The number of samples, default 1.
  size = int(fl.request.args.get("size", "1"))
  return fl.jsonify(np.random.binomial(trials, prob, size).tolist())

@app.route('/normal')
def normal():
  # The mean, default 0.
  loc = float(fl.request.args.get("loc", "0.0"))
  # The standard deviation, default 1.0.
  scale = float(fl.request.args.get("scale", "1.0"))
  # The number of samples, default 1.
  size = int(fl.request.args.get("size", "1"))
  return fl.jsonify(np.random.normal(loc, scale, size).tolist())