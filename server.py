import boto3
import base64
from flask import Flask, request

app = Flask(__name__)
client = boto3.client('rekognition',
                        aws_access_key_id="AKIA4A2WLRPPMWG2LK3G",
                        aws_secret_access_key="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",
                        region_name="us-east-1")
@app.route("/")
def hello():
  return ("Prueba de Flask")

@app.route('/tarea3-201503961',methods=["POST"])
def post():
    detalle = request.get_json(force=True)
    #print(detalle)
    imagen = detalle["imagen"]
    #print(imagen)

    base64_img_bytes = imagen.encode('utf-8')

    #with open('decoded_image.png', 'wb') as file_to_save:
    decoded_image_data = base64.decodebytes(base64_img_bytes)
      #file_to_save.write(decoded_image_data)

    #with open('decoded_image.png', 'rb') as image_data:
      #response_content = image_data.read() 
    face = client.detect_faces(Image={'Bytes':decoded_image_data}, Attributes=['ALL'])
    return face

if __name__ == "__main__":
  app.run()