from flask import Flask, render_template, request
import segno
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generateQR():
    memory = BytesIO()  
    data = request.form.get('link')
    img = segno.make(data)
    img.save(memory, kind='png')  
    memory.seek(0)
    base64_img = "data:image/png;base64," + b64encode(memory.getvalue()).decode('ascii')
    return render_template('index.html', data=base64_img)

if __name__ == '__main__':
    app.run(debug=True)
