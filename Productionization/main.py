# Core Pkg
from fastapi import FastAPI, File, UploadFile
import uvicorn


# ML
import numpy as np
import tensorflow as tf
import librosa


# init app
app = FastAPI()


# Routes
@app.get('/')
async def index():
    return {"text: ": "Please go to the URL - http://127.0.0.1:8000/predict/"}


def pre_process(file):
    signal, sample_rate = librosa.load(file, sr=None)
    zero_padding = 22050 - len(signal)
    signal = np.pad(signal, (0, zero_padding), 'constant')
    MFCCs = librosa.feature.mfcc(signal, sample_rate, n_mfcc=13, n_fft=2048, hop_length=512)
    MFCCs = MFCCs.T
    MFCCs = MFCCs[np.newaxis, ..., np.newaxis]
    return MFCCs


model1 = tf.keras.models.load_model("/Users/deepak/Desktop/Data_Science/Springboard/SB_Capstone2/model.h5")


# ML Aspect
@app.post('/predict/')
async def create_upload_file(file: UploadFile = File(...)):
    MFCC = pre_process(file.file)
    mapping = ['right', 'eight', 'cat', 'tree', 'bed', 'happy', 'go', 'dog', 'no', 'wow', 'nine', 'left', 'stop',
               'three', 'sheila', 'one', 'bird', 'zero', 'seven', 'up', 'noise', 'marvin', 'two', 'house', 'down',
               'six', 'yes', 'on', 'five', 'off', 'four']
    predictions = model1.predict(MFCC)
    predicted_index = np.argmax(predictions)
    predicted_keyword = mapping[predicted_index]
    return predicted_keyword

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)