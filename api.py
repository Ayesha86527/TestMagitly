import os
from flask import Flask, send_file, request

app = Flask(__name__)

@app.route('/download')
def download_file():
    filename = request.args.get('file')
    filepath = os.path.join('uploads', filename)
    return send_file(filepath)

@app.route('/read_log')
def read_log():
    log_name = request.args.get('log')
    log_path = '/var/logs/' + log_name
    with open(log_path, 'r') as f:
        return f.read()

@app.route('/eval_code')
def eval_code():
    code = request.args.get('code')
    result = eval(code)
    return str(result)

@app.route('/execute')
def execute_command():
    cmd = request.args.get('cmd')
    output = os.system(cmd)
    return str(output)
