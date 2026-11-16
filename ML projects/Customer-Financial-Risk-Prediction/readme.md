# Customer Financial Risk Prediction using Decision Tree Classifier 

## Project Overview

This project demonstrates a Machine Learning classification workflow using a Decision Tree Classifier to categorize customers into three educational financial-risk categories:

- Low Risk
- Medium Risk
- High Risk

The model uses customer financial information such as income, savings, debt and financial ratios.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab

## Dataset Information

- Total records: 1,000
- Total original features: 9 financial features and 1 customer identifier.
- Target variable: Risk_Level

### Features

- INCOME
- SAVINGS
- DEBT
- R_SAVINGS_INCOME
- R_DEBT_INCOME
- R_DEBT_SAVINGS
- T_CLOTHING_12
- T_CLOTHING_6
- R_CLOTHING

## Project Workflow

1. Data loading
2. Exploratory Data Analysis (EDA)
3. Data understanding and statistical analysis
4. Data visualization
5. Target variable creation
6. Feature selection
7. Train-test splitting
8. Decision Tree model training
9. Model evaluation
10. Feature importance analysis

## Model Details

Algorithm: Decision Tree Classifier

- Criterion: Entropy
- Maximum depth: 4
- Training data: 80%
- Testing data: 20%

## Model Evaluation

Test accuracy: 100%

The model achieved 100% accuracy on 200 test records.

**Important limitation:** The target labels were generated using predefined rules based on debt-to-income and savings-to-income ratios. These same ratios were included as model features. Therefore, the model learned to reproduce the predefined rules. This result does not demonstrate real-world financial-risk prediction or predict actual loan defaults.

## Learning Outcomes

- Understanding Exploratory Data Analysis.
- Working with financial datasets using Pandas.
- Understanding Decision Tree Classification.
- Learning entropy-based splitting.
- Understanding training and testing datasets.
- Evaluating classification models.
- Visualizing feature importance.

## Future Improvements

- Investigate alternative target-labeling methods.
- Evaluate different classification algorithms.
- Perform hyperparameter tuning.
- Apply cross-validation.
- Investigate fairness and potential bias in financial features.

## Author

**Adhithyan**

B.Tech Computer Science and Engineering

GitHub: [ADHITHYAN0520](https://github.com/ADHITHYAN0520)

LinkedIn: [Adhithyan](https://linkedin.com/in/adhithyan05)
