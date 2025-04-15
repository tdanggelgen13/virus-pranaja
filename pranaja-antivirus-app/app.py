from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import json
from datetime import datetime
import scanner
import security_check
import educational_content

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page of the application."""
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    """Initiate a scan of the device."""
    # In a real Android app, this would access system APIs
    # For this web app simulation, we'll perform basic checks
    scan_results = scanner.scan_device()
    return jsonify(scan_results)

@app.route('/scan_results')
def scan_results():
    """Display the results of the scan."""
    # This would retrieve actual scan results in a real app
    sample_results = scanner.get_last_scan_results()
    return render_template('scan_results.html', results=sample_results)

@app.route('/cleanup', methods=['POST'])
def cleanup():
    """Clean up detected threats."""
    threat_id = request.form.get('threat_id')
    success = scanner.clean_threat(threat_id)
    return jsonify({"success": success})

@app.route('/device_status')
def device_status():
    """Show the current security status of the device."""
    status = security_check.get_device_status()
    return render_template('device_status.html', status=status)

# Bagian edukasi telah dihapus sesuai permintaan

@app.route('/repair')
def repair():
    """Show device repair and recovery options."""
    return render_template('repair.html')

@app.route('/repair/execute', methods=['POST'])
def execute_repair():
    """Execute a repair operation."""
    repair_type = request.json.get('repair_type')
    
    # In a real app, this would implement actual repair functionality
    # For this simulation, we'll return success after a delay
    
    response = {
        "success": True,
        "repair_type": repair_type,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "message": f"Perbaikan {repair_type} berhasil dilakukan"
    }
    
    return jsonify(response)

@app.route('/repair/history', methods=['GET'])
def repair_history():
    """Get the repair history."""
    # In a real app, this would retrieve repair history from a database
    # For this simulation, we'll return a fixed history
    
    history = [
        {
            "type": "malware",
            "timestamp": (datetime.now()).strftime("%Y-%m-%d %H:%M:%S"),
            "status": "completed"
        }
    ]
    
    return jsonify(history)

@app.route('/repair/reset', methods=['POST'])
def reset_device():
    """Simulate a factory reset of the device."""
    # In a real app, this would trigger Android's factory reset
    # For this simulation, we'll just return success
    
    return jsonify({
        "success": True,
        "message": "Reset perangkat berhasil dimulai."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
