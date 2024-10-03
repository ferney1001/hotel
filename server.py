from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserva_confirmada')
def reserva_confirmada():
    return render_template('reserva_confirmada.html')

@app.route('/detalles.html')
def detalles():
    alojamiento_id = request.args.get('alojamientoId')
    return render_template('detalles.html', alojamientoId=alojamiento_id)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
