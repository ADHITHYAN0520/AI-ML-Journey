# SMS Spam Detection Using Naive Bayes

## Project Overview

This project implements a Machine Learning classification model to identify whether an SMS message is Spam or Ham (Legitimate) using Multinomial Naive Bayes.

The project uses the SMS Spam Collection dataset and TF-IDF vectorization to convert text messages into numerical features for classification.

## Dataset

- Dataset: SMS Spam Collection
- Total Messages: 5,572
- Ham Messages: 4,825
- Spam Messages: 747
- Target Classes: Spam and Ham

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- TF-IDF Vectorization
- Multinomial Naive Bayes

## Project Workflow

1. Data Collection
2. Data Loading and Inspection
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Message Length Analysis
6. Word Count Analysis
7. Text Feature Extraction using TF-IDF
8. Train-Test Split
9. Multinomial Naive Bayes Model Training
10. Model Evaluation

## Algorithm

**Multinomial Naive Bayes**

Multinomial Naive Bayes is a probabilistic classification algorithm based on Bayes' Theorem. It is commonly used for text classification tasks.

TF-IDF (Term Frequency-Inverse Document Frequency) is used to transform SMS messages into numerical feature vectors.

## Model Performance

Test Set Accuracy: **96.05%**

### Classification Results

| Metric    |  Ham | Spam |
| --------- | ---: | ---: |
| Precision | 0.96 | 1.00 |
| Recall    | 1.00 | 0.70 |
| F1-Score  | 0.98 | 0.83 |

### Confusion Matrix

| Actual / Predicted | Ham | Spam |
| ------------------ | --: | ---: |
| Ham                | 966 |    0 |
| Spam               |  44 |  105 |

## Key Observations

- Achieved 96.05% classification accuracy.
- Spam precision reached 100%.
- Spam recall was approximately 70.47%.
- The model correctly identified 105 Spam messages.
- The model missed 44 Spam messages.

## Learning Outcomes

- Understanding Naive Bayes classification.
- Learning TF-IDF text vectorization.
- Performing exploratory data analysis.
- Understanding class imbalance.
- Evaluating classification models using precision, recall, F1-score and confusion matrix.

## Future Improvements

- Experiment with different alpha values.
- Explore N-gram features.
- Compare Multinomial and Bernoulli Naive Bayes.
- Improve Spam Recall.
- Compare Naive Bayes with SVM on the same dataset.

## Author

Adhithyan D

GitHub: [ADHITHYAN0520](https://github.com/ADHITHYAN0520)

LinkedIn: [Adhithyan](https://linkedin.com/in/adhithyan05)
