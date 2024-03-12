from flask import Flask, send_file, request
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/qrcode')
def generate_qrcode():
    # Get the data from the query parameter 'data'
    data = request.args.get('data', '')

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an in-memory binary stream to save the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    # Return the QR code image as a file
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
