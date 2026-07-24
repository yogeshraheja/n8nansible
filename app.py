from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/monitoring')
def monitoring():
    return jsonify({
        "cpu": 97,
        "memory": 89,
        "recent_errors": 245
    })

@app.route('/incidents')
def incidents():
    return jsonify({
        "open_incidents": 3,
        "last_incident": "Database timeout",
        "incident_frequency": "High"
    })

@app.route('/metadata')
def metadata():
    return jsonify({
        "owner_team": "Payments Team",
        "criticality": "Tier-1",
        "dependencies": ["postgres-prod", "redis-prod"]
    })

app.run(host='0.0.0.0', port=5000)
 
