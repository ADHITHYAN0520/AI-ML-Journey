# Email Spam Detection Using TF-IDF and SVM

## Project Overview

This project implements an Email Spam Detection system using Machine Learning. It classifies email messages into two categories: Spam and Not Spam.

The model uses TF-IDF (Term Frequency–Inverse Document Frequency) for text feature extraction and Linear Support Vector Classification (LinearSVC) for classification.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Support Vector Machine (LinearSVC)
- Matplotlib

## Dataset

The dataset contains 3,000 email records with two columns:

- `email`: Email message text.
- `label`: Classification target.
  - `0` – Not Spam
  - `1` – Spam

Data preprocessing includes handling missing values and removing duplicate records.

## Machine Learning Workflow

1. Load the dataset.
2. Explore and understand the data.
3. Handle missing values and duplicates.
4. Separate input features and target labels.
5. Split the dataset into training and testing sets.
6. Convert email text into numerical features using TF-IDF.
7. Train the Linear SVM classifier.
8. Predict email categories.
9. Evaluate model performance.

## Model Architecture

The project uses a Scikit-learn Pipeline:

```python
model = make_pipeline(
    TfidfVectorizer(),
    LinearSVC(C=10)
)
```

- **TF-IDF Vectorizer:** Converts email text into numerical features.
- **LinearSVC:** Classifies emails as Spam or Not Spam.
- **Pipeline:** Combines text feature extraction and classification.

## Model Performance

Best observed result during manual C-parameter experiments:

| Metric | Score |
|---|---:|
| Accuracy | 99.30% |
| Spam Precision | 98.80% |
| Spam Recall | 96.47% |
| Spam F1-score | 0.98 |

The result was obtained using `LinearSVC(C=10)` on an 80:20 train-test split.

These are results from the current experiment, not a guarantee of performance on other datasets.

## Evaluation Metrics

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## Key Learning Outcomes

- Understanding text classification.
- Learning TF-IDF feature extraction.
- Implementing Linear Support Vector Machines.
- Using Scikit-learn Pipelines.
- Understanding train-test splitting.
- Evaluating classification models.
- Experimenting with SVM hyperparameters.

## How to Run

Clone the repository:

```bash
git clone https://github.com/ADHITHYAN0520/AI-ML-Journey.git
```

Navigate to the project folder:

```bash
cd "AI-ML-Journey/ML Projects/Email-Spam-Detection-SVM"
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Open the notebook using Jupyter:

```bash
jupyter notebook Email_Spam_Detection_SVM.ipynb
```

## Future Improvements

- Perform systematic hyperparameter tuning using GridSearchCV.
- Improve spam recall.
- Compare LinearSVC with other classification algorithms.
- Test the model with new email messages.
- Develop a simple web application for spam detection.

## Author

Adhithyan

GitHub: https://github.com/ADHITHYAN0520

LinkedIn: https://linkedin.com/in/adhithyan05
