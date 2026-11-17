# Diabetes Prediction Using Random Forest Classification

## Project Overview

This project implements a Machine Learning classification model to predict whether a person is likely to have diabetes based on medical diagnostic features.

The Random Forest Classifier from Scikit-learn is used to train and evaluate the prediction model.

## Dataset

The project uses the Pima Indians Diabetes Dataset.

**Dataset features:**
- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age

**Target variable:**
- Outcome (0 = Non-Diabetic, 1 = Diabetic)

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Machine Learning Workflow

1. Data loading and exploration
2. Data preprocessing
3. Handling invalid zero values
4. Missing-value imputation using median strategy
5. Feature selection
6. Train-test splitting
7. Random Forest model development
8. Model training and prediction
9. Model evaluation
10. Five-fold cross-validation

## Model Configuration

Random Forest Classifier:

- n_estimators = 200
- max_depth = 5
- min_samples_split = 5
- min_samples_leaf = 2
- max_features = sqrt
- class_weight = balanced

A Scikit-learn Pipeline is used to combine missing-value imputation and model training.

## Evaluation Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Five-fold Cross-Validation

## Project Objective

The objective is to understand and implement a supervised Machine Learning classification algorithm using a real-world healthcare dataset.

## Disclaimer

This project is developed for educational purposes only. It is not intended for medical diagnosis or clinical decision-making.
