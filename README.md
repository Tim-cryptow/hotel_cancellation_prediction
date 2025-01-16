# Hotel Cancellation Prediction

This project aims to predict the likelihood of hotel bookings being canceled. It uses machine learning techniques to analyze various hotel booking attributes and provide an estimated cancellation probability.

# Table of Contents
- Project Overview
- Technologies Used
- Dataset
- Installation Instructions
- Model Training
- API
- Acknowledgements

# Project Overview

The goal of this project is to build a machine learning model that predicts whether a hotel booking will be canceled based on various features such as lead time, number of special requests, deposit type, and country of origin. The model will output a cancellation probability, which can be used by hotel management to optimize their booking and cancellation policies.

# Technologies Used

- **Python**: For data processing and model development.
- **Flask**: For creating a web API to serve the model.
- **Scikit-Learn**: For machine learning model development.
- **Joblib**: For saving and loading the trained model.
- **Heroku**: For hosting the web API.
- **GitHub**: For version control and repository hosting.

# Dataset

The dataset contains information about hotel bookings, including the following features:
- `lead_time`: Number of days between the booking date and the arrival date.
- `adr`: Average daily rate.
- `total_of_special_requests`: Number of special requests made by the guest.
- `deposit_type`: Type of deposit made (e.g., Non Refund).
- `country`: Country of origin of the guest.
- `cancellation`: Whether the booking was canceled (target variable).

> Note: The dataset used for this project is a cleaned and preprocessed version of the original hotel booking dataset.

# Installation Instructions
Note: the model has been excluded from the github repository since it is larger than the 100 MB limit except using lfs. If needed, contact me. goodluckogundare@gmail.com

# Model Training

The model is trained using various machine learning algorithms, including decision trees, logistic regression, and random forests. The performance of each model is evaluated, and the best-performing model is selected.

- **Model used**: Random Forest
- **Features**: Lead time, Average daily rate (ADR), Special requests, Deposit type, Country of origin.
- **Target variable**: Cancellation probability.

## API

The project exposes a simple Flask API with the following endpoint: https://hotel-cancellation-predictor-37d78d6df101.herokuapp.com/

- `POST /predict`: Accepts a JSON payload with booking details and returns a predicted cancellation probability.

Example request:
```bash
curl -v -POST -H "Content-Type: application/json" -d "{\"lead_time\": 40, \"adr\": 150, \"total_of_special_requests\": 1, \"deposit_type\": \"Non Refund\", \"country\": \"ESP\"}" https://hotel-cancellation-predictor-37d78d6df101.herokuapp.com/predict
```

Example response:
```json
{
  "cancellation_probability": 0.13
}
```

## Acknowledgements

- **Dataset**: The dataset used in this project is sourced from Kaggle ([https://www.kaggle.com/](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)).
- **Libraries**: Thanks to the creators of the libraries used in this project
---
