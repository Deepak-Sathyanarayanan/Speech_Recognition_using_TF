# Speech_Recognition_using_TF
Predicting the labels of Audio inputs using Tensorflow

# Data:
https://docs.google.com/document/d/1HO2syjiyLY9uds18GokgaM9k4FIstlaHk87vUuQZhCg/edit?usp=sharing

# Processed Data:
https://drive.google.com/file/d/1DSNH1mchpgI0ns6mp204GTzryGe_4UKT/view?usp=sharing

# Model:
https://drive.google.com/file/d/1UWcaiqFF7xIU87q7QTJCKcDIIiIF22Ln/view?usp=sharing

# Predicted Data:
https://drive.google.com/file/d/1TYk2MPv2IOcU2vkC7tRjShOWRFO6x42r/view?usp=sharing

# Productionisation
  1. Go to the folder where audio files are there in zsh
  2. Execute the below command 
curl -X POST "http://127.0.0.1:8000/predict/" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "file=@1aeef15e_nohash_0.wav;type=audio/wav"

and give the filename in the highlighted part of the command

