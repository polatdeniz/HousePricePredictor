# House Price Prediction

This project demonstrates the process of building and deploying machine learning models to predict house prices based on various features from a dataset.

## Project Structure
Housing.csv: The dataset used for training the models, containing various attributes of houses and their respective prices.

HousePricePrediction.ipynb: A Jupyter notebook that contains the entire workflow for data preprocessing, feature engineering, model building, and training. The notebook also includes saving the trained models for future use.

linear_regression_model.pkl, random_forest_model.pkl, ridge_model.pkl: Pre-trained machine learning models saved in pickle format. These models were trained using different algorithms: Linear Regression, Random Forest, and Ridge Regression.

ModelDeployment.py: The backend script responsible for loading the ridge_model.pkl and using it to predict house prices based on input data. This script is designed to demonstrate model deployment.

## Objective

The primary goal of this project was to explore the process of building, training, and saving machine learning models, and subsequently deploying one of the models (Ridge Regression) in a backend application. While the models may not be fully optimized for real-world accuracy, the project serves as a practical example of the end-to-end machine learning workflow.

## Note

This project was created as a learning exercise, focusing on the integration and deployment of pre-trained models. Future iterations may focus on improving the model's accuracy and fine-tuning its performance for production use.
