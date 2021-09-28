#!/usr/bin/env python
# coding: utf-8

# import keras
import tensorflow_hub as hub
# import cv2
# import tensorflow as tf
# import matplotlib.pyplot as plt
import numpy as np
from PIL import Image,ImageOps


def person_detector(image, prob_threshold = 0.5):
    # Using mobilenet SSDs classification capabilities only and not localization
    detector = hub.load("https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2")
    im = ImageOps.fit(image, (224,224), Image.ANTIALIAS)
    image_array = np.asarray(im)
    # Can't use opencv as it's throwing error when deployed on Heroku
#     image_resized = cv2.resize(image_array,(224,224))
    image1 = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image1[0] = image_array
#     image_array = np.asarray(input_image)
#     image_resized = cv2.resize(image_array,(224,224))
#     im1 = tf.expand_dims(image_resized,axis=0)
    detector_output = detector(image1)
    predicted_classes = np.array(detector_output["detection_classes"][0])
    # Class 1 is Person in the data dictionary
    person_indices = np.where(predicted_classes==1)[0]
    predicted_scores = np.array(detector_output["detection_scores"][0])
    # Finding scores of person class present in detection
    person_prob = [predicted_scores[i] for i in person_indices]
    # Checking if there's any person detected with probability greater than threshold
    if max(person_prob) > prob_threshold:
        print('Person Detected')
        return 1
    else:
        print('No Person Detected')
        return 0




