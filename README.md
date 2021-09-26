# Person-Detection
Deep learning based solution for detecting humans in a scene, leveraged further to detect delivery person of Indian food delivery apps.

## Demo
Web app for the solution is created mainly using Streamlit which created frontend for the website and is deployed on Heroku which is a PAAS based
solution.
The web app can be accessed via following link : https://delivery-detector.herokuapp.com/

### Note:
As Heroku provides 500 MB of space to host a solution which includes installing all dependencies which includes Tensorflow which itself is of around
450 MB was preventing the solution to deployed online. To deal with this I've used cpu version of tensorflow which has made the inference slower
(so please be patient after uploading an image!).

### TO-DO:
As of now tf-hub instance is being created at every call, need to isolate it and test for speed

## Further Work:
As of now the solution detects the presence of human in a scene be it a delivery boy or not.
To achieve further capabilities following would be my approach:

1. Web scrape images having logos of required companies (be it over T-shirts, bags or vehicle)
2. Annotate the images with bounding boxes
3. Retrain the current object detector over collected examples
4. Now we need to make sure that the logo is somewhere on the clothes or cap of the delivery person. So to achieve this we will levarage the predicted bounding boxes from the detector and will check "whether the detected logo lies within the person bbox".
