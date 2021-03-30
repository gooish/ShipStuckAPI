from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
ships = [
    {
    'name': 'Ever Given',
    'stuck': 'no'
    }
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Is The Ship Stuck API</h1>'''

@app.route('/api/v1/resources/stuck/all', methods=['GET'])
def api_all():
    return jsonify(ships)

if __name__ == "__main__":
    app.run()
