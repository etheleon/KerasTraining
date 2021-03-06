from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input,decode_predictions
from keras.applications.resnet50 import ResNet50
import numpy as np

# Step 1
img = image.load_img('../images/snake-224.jpg',target_size=(224,224))

x = image.img_to_array(img)
x = np.expand_dims(x,axis=0)
x = preprocess_input(x)

# Step 2
model = ResNet50()

# Step 3 Prediction

prediction = model.predict(x)
classes = decode_predictions(prediction,top=3)

for i,j,k in classes[0]:
    print("{}:{}".format(j,k))




