import subprocess
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/vac', methods=['GET'])
def vaccine_db():
    print("vaccinedb Deployment created successfully")
    try:
        result = subprocess.run(['python', '/app/vac-dep.py'], capture_output=True, text=True)
        output = result.stdout
        return output
    except subprocess.CalledProcessError as e:
        return f"Error executing VaccineDB: {e.stderr}"
    

@app.route('/sic', methods=['GET'])
def sickleave_db():
    print("sickleavedb Deployment created successfully")
    try:
        result = subprocess.run(['python', '/app/sic-dep.py'], capture_output=True, text=True)
        output = result.stdout
        return output
    except subprocess.CalledProcessError as e:
        return f"Error executing VaccineDB: {e.stderr}"
    
@app.route('/qua', methods=['GET'])
def quarantine_db():
    print("quarantine Deployment created successfully.")
    try:
        result = subprocess.run(['python', '/app/qua-dep.py'], capture_output=True, text=True)
        output = result.stdout
        return output
    except subprocess.CalledProcessError as e:
        return f"Error executing quarantine: {e.stderr}"
@app.route('/ind', methods=['GET'])

def indvisuals_db():
    print("indvisuals Deployment created successfully.")
    try:
        result = subprocess.run(['python', '/app/ind-dep.py'], capture_output=True, text=True)
        output = result.stdout
        return output
    except subprocess.CalledProcessError as e:
        return f"Error executing quarantine: {e.stderr}"
    
@app.route('/hea', methods=['GET'])

def hea_db():
    print("healthymarriagedb Deployment created successfully.")
    try:
        result = subprocess.run(['python', '/app/hea-dep.py'], capture_output=True, text=True)
        output = result.stdout
        return output
    except subprocess.CalledProcessError as e:
        return f"Error executing quarantine: {e.stderr}"


if __name__ == '__main__':
    app.run()   





