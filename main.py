from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
import base64
from PIL import Image
import io
import numpy as np
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["OPTIONS", "POST", "GET"],
    allow_headers=["*"],
)

model = load_model('./models/Digit_classification.keras', compile=False)

print("Model is load successfully")

@app.post('/predict')
async def predict_digit(request: Request):
    data = await request.json()
    image_data = data['image'].split(',')[1]

    #Decode
    image = base64.b64decode(image_data)
    img = Image.open(io.BytesIO(image)).convert('L')

    img = img.resize((28,28))
    img_array = np.array(img)
    img_array = img_array - 255 #invert image
    img_array = img_array / 255 #normalize data
    img_array = img_array.reshape(1,784) #convert 28x28 to 1x784

    prediction = model.predict(img_array)

    digit = int(np.argmax(prediction))

    return {"prediction": digit}

