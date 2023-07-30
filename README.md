# Mlops-Final-Project
# Emotion Detection App

With this project we decided to build an app that would help detect emotions based on the facial attributes of the subject in the picture that is uploaded. We find that this could be very helpful as a data point for workplaces to determine the employee satisfaction, for mental health professionals to get relevant data about a patient, for businesses to determine customer satisfaction, etc. This is an interesting computer vision problem because emotions that one shows can be extremely subjective. For the purpose of this project we havent fintuned any model or trained our own models, because for a good enough accuracy we would need a diverse dataset with diverse subjects showing a range of emotions. For the pupose of this POC we have used the DeepFace model library and we use the  "analyze" function to recognise the facial attributes and provide a score for the different emotions we see in the image.For a real world usecase, we may need to adjest the threshold quite a bit to make sure we are estimating the subjectiveness of the emotions. So that finetuning will require quite a bit of experimentation to get right. The robustness of the model and the output metrics for evaluation also depend on the usecase that this app would look to support.
The app's UI and final deployment was done using the Dash framework which is built on top of Plotly.ja, React and Flask. It has 2 components- the html and the core components. The html components are used to build the UI and is how you would talk to the core components that would eventually be used to perform the required action.

## Features

- Upload an image: Users can upload an image using the upload button. The app currently supports one image at a time.
- View uploaded image: Once the image is uploaded, it is displayed on the screen.
- Emotion detection: After uploading, the image is analyzed immediately, and the detected emotions are displayed in a table below the image.

![Alt Text](demo.png)

## Installation

Make sure you have the following installed:

- Python 3.7+
- pip (Python package manager)

### Setup

1. Clone the repository:

```bash
[git clone https://github.com/yourgithubusername/emotion-detection-app.git](https://github.com/iqra0908/Mlops-Final-Project.git)
```

### Install the dependencies:

`pip install -r requirements.txt

### Running the App

1. Navigate to the project's root directory.
2. Run the app:
`python app.py
`
3. Visit http://127.0.0.1:8050 in your web browser.

## Alternative

We have a docker image that can be pulled and run directly as below
1. Pull the docker image
```bash
docker pull nehabardeduke/aipi561
```
2. Tag the image as required
```bash
docker tag nehabardeduke/aipi561 <image_name>:latest
```
3. Run the image
```bash
docker run -it -d --name <app_name> -p 7000:7000 <image_name>
```

This will make the app run locally.
## Deployment to a public endpoint using Azure:

### Azure technicalities:
1.Here we built the docker image, tagged it and pushed it to the Azure container Registry. This allows us to seamlessly use the docker image for the web app development. While Azure allowa for web apps to be created using any private registry as well as dockerhub, we found managing credentials and accesses more convinent with the ACR.
2. In Azure we put the container image and the webapp under the umbrella of the same resource group which further makes the deployment easy and since it is in the same region, the latency is also handled. 
![image](https://github.com/iqra0908/Mlops-Final-Project/assets/110474064/16974ab8-bc6e-48a4-a689-9f30d34c07c3)
3. For this deployment we enabled admin access keys since this is a POC. Ideally for a production level deployment it is wise to go with IAM rules instead.
![image](https://github.com/iqra0908/Mlops-Final-Project/assets/110474064/4b8d00d5-6bca-4f8a-86d1-685a7fb28c0c)
4. Setting up the web app was as easy as choosing the container registry, the image, the tag and configuring the correct website port as mentioned in the app.py script.
![image](https://github.com/iqra0908/Mlops-Final-Project/assets/110474064/55b8ac9b-2949-4c4f-bd55-c7cba0cff6d7)
![image](https://github.com/iqra0908/Mlops-Final-Project/assets/110474064/2bc3241a-550a-4b18-92e3-0280ddee5338)
5. The public endpoint can be accessed here - https://emodetection.azurewebsites.net/







