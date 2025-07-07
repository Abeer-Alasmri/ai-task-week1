import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

# تحميل النموذج
model = tf.keras.models.load_model("keras_model.h5")

# تحميل labels
with open("labels.txt", "r") as f:
    labels = f.read().splitlines()

# تحميل الصورة
img_path = "test.jpg"
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

# التنبؤ
predictions = model.predict(img_array)
predicted_index = np.argmax(predictions[0])
predicted_label = labels[predicted_index]
confidence = predictions[0][predicted_index]

# عرض النتيجة
print(f"الصنف المتوقع: {predicted_label.strip()}")
print(f"نسبة الثقة: {confidence:.4f}")
plt.imshow(img)
plt.title(f"Prediction: {predicted_label.strip()} ({confidence:.2%})")
plt.axis('off')
plt.show()