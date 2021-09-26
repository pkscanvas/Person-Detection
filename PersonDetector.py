#!/usr/bin/env python
# coding: utf-8

# import keras
import tensorflow_hub as hub
import cv2
# import tensorflow as tf
# import matplotlib.pyplot as plt
import numpy as np


def person_detector(input_image, prob_threshold = 0.5):
    detector = hub.load("https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2")
    im = Image.open(input_image)
    image_array = np.asarray(im)
    image_resized = cv2.resize(image_array,(224,224))
    image1 = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image1[0] = image_resized
#     image_array = np.asarray(input_image)
#     image_resized = cv2.resize(image_array,(224,224))
#     im1 = tf.expand_dims(image_resized,axis=0)
    detector_output = detector(image1)
    predicted_classes = np.array(detector_output["detection_classes"][0])
    person_indices = np.where(predicted_classes==1)[0]
    predicted_scores = np.array(detector_output["detection_scores"][0])
    person_prob = [predicted_scores[i] for i in person_indices]
    if max(person_prob) > prob_threshold:
        print('Person Detected')
        return 1
    else:
        print('No Person Detected')
        return 0




