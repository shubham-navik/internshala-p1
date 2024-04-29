from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for your Flask app

@app.route('/')
def index():
    return render_template('./Frontend/index.html')

@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.form.to_dict(flat=False)  # Convert form data to dictionary
    skills = data.pop('skills[]', [])  # Remove 'skills[]' from data and get its value as a list
    data['skills'] = skills  # Add skills list back to data under 'skills' key
    print(data)
    # Perform any processing or database operations here
    # For demonstration purposes, we'll simply return the received data as JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
