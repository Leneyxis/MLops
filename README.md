# Machine Learning Model Dockerization README

This repository contains a simple example of containerizing a Python-based machine learning model using Docker. The machine learning script (`main.py`) reads a dataset, performs data preprocessing, and trains a Linear Regression model. Additionally, it provides a Dockerfile to create a Docker image for your machine learning project.

## Python Script

The `main.py` script does the following:

1. Imports necessary libraries such as `pandas`, `numpy`, `matplotlib`, `sklearn.preprocessing`, `sklearn.model_selection`, `sklearn.linear_model`, and `sklearn.compose`.
2. Reads a CSV dataset named '50_Startups.csv' using `pandas`.
3. Splits the data into training and testing sets using `train_test_split`.
4. Trains a Linear Regression model.
5. Makes predictions on the testing data and prints the predicted and actual values.

To run this script, make sure you have the required dependencies installed. You can use the provided `requirements.txt` to set up the environment.

## Docker Setup

The Dockerfile provided in this repository is configured to create a Docker container for your machine learning project. Here are the key details:

- Base Image: Python 3.8
- Working Directory: /MLops
- Copies '50_Startups.csv,' 'main.py,' and 'requirements.txt' into the container.
- Installs the necessary Python packages specified in `requirements.txt` using `pip`.
- Exposes port 80 (you can customize this if needed).
- Defines the command to run the `main.py` script when the container is launched.

To build and run the Docker container, follow these steps:

1. Build the Docker image:
   ```bash
   docker build -t docker-ml-model .
   ```

2. Run a container based on the image:
   ```bash
   docker run -p 8080:80 docker-ml-model
   ```

Make sure to customize the Docker image name and port mapping as needed for your specific use case.

***
## Deploying Docker Image to Google Cloud
> Requirements: 
- Google Cloud Account 
- Google Cloud CLI

Create a new tag for deploying your docker file to Google Cloud:
```bash
docker tag docker-ml-model gcr.io/mlops-402118/docker-ml-model
```
Once done initiate Google Cloud using:

```bash
gcloud init
gcloud auth login
```
Set up the necessary permission for your porject on Google Cloud and then push the Docker:

```bash
docker push gcr.io/mlops-402118/docker-ml-model 
```
Once done create a new Kubernetes Instance on Google Cloud Console selecting the DockerImage you've deployed. In my instance, once deployed and an Instance is created, I got the following URL:

> https://mlop-ehhja2edgq-uc.a.run.app

## Contact Information

If you have any questions or need further assistance, please feel free to reach out to the project maintainers.

**Author:** Syed Umer Ahmed
**Email:** syedumerahmed97@gmail.com

Happy machine learning containerization!
