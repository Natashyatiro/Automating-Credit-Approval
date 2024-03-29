# Automating Credit Approval: Project Overview
* Created a tool that predict loan amount and customer’s default based on customer’s age and income to help bank in automating their credit approval process.
*	Optimized and compared Linear Regression, Decision Tree, Random Forest, GBoost, MLP Regressor, CNN, Random Forest Regressor Optimization to predict loan amount and to reach the best model using Python and Orange.
*	Optimized and compared Logistic Regression, Decision Tree, Random Forest, GBoost, MLP Classifier, CNN (Keras Sequential) with Keras Tuner to predict loan amount and to reach the best model using Python and Orange.
*	The best model performance is by Regressor Optimization for Random Forest with 2456.62 RMSE in loan amount prediction, and Gradient Boosting with 85.88% accuracy in default prediction.
* Deployed the model to the cloud and built a client facing API using flask.

## Background
In credit card approval process, loan eligibility is important to be checked because it helps to make sure that borrowers will be able to repay their loans. There are two crucial steps that can determine the credit card application decision. The first is determining the amount of loan, and the second is predicting whether the applicant will default or not. These are time-consuming and complicated task to do manually because bank employees must consider many different factors including the background of the applicants and income carefully. This often causes struggle for bank employees to decide on approval of low-risk loans accurately and in a timely manner. Other than that, if the bank approved risky loans due to human error, and the applicant turns out to default, bank will have higher risk of losing money. Therefore, the solution to improve credit card approval reliability and accuracy and make the process much more efficient is by automating these tasks using machine learning model. Machine learning can be used to automate the decision-making process for loan amount and predict whether applicant will default by using data from previous loan applications.

## Business Problem and Study Objective
Currently, the business problem that bank is facing is regarding the manual process of credit card approval that is too complicated, time-consuming, and sometimes inaccurate and unreliable. Therefore, this study will focus on developing and recommend an implementation plan of machine learning in tackling this issue. 

## Dataset Information
The dataset used consists of 4 columns, they are income (float), age (float), loan (float), and default (Boolean). The data do not contain any null values. As shown on Figure 1, before data cleaning, age variable has outliers. After checking the age data, there are 3 negative values, and assuming it is human error, the negative signs then removed. After removing the negative values, the boxplot no longer shows any outliers.
![image](https://user-images.githubusercontent.com/84263856/201728605-5dfe873b-2e95-4bd3-8a92-2291108d835c.png)
![image](https://user-images.githubusercontent.com/84263856/201728610-41764c34-6228-40a9-8fdd-434380a4c5f2.png)

To understand the data better, the variables are visualized in different plots. As shown in Figure 2, default applicants are under 40 years old, and the highest probability of default is applicants in their 20 to 30 years old.   As shown in Figure 3, there is a clear pattern on the loan amount above 4000, which is the higher the loan amount, the higher the income applicants (show positive correlation). 

![image](https://user-images.githubusercontent.com/84263856/201728680-da9ecefc-3f27-4e93-a08d-34ae8822cffc.png)
![image](https://user-images.githubusercontent.com/84263856/201728689-29d36876-e31c-444f-8817-88e646a4622d.png)

## Assumption and Approach
The key assumption used in this study is there are 2 target variables to be predicted which are loan and default because in real life situation, the loan amount and default status would not be available. Hence, in this study, predicting 2 target variables will be sequential process as shown on Figure 4. First, predicting the loan is done by using income, age variable. Then, default prediction is based on income, age, and the prediction of loan. Therefore, the result of loan prediction from the first test set will become an input data for the second test set to predict the default status, while all the data in the trainset is derived from the original dataset. There are 6 basic approaches each for predicting loan and default. There are two alternative approaches for predicting loan and an alternative approach for predicting default. All the models will be compared based on its performance measurements which is RMSE for loan prediction, and accuracy, False Negative Rate (FNR) for default prediction. False negative rate is the more important prediction error because we want to avoid predicting that applicant is not default, while in real situation, applicant will default, since this can put higher risk of losing money for the bank. Feature selection is not conducted because the features number is low. Normalization is not conducted because it results in worse model performance.
![image](https://user-images.githubusercontent.com/84263856/201728770-33f9f41a-8a80-46bf-8549-337ced681ee0.png)

## Result and Model Comparison
Basic approach models are done in both Python and Orange. The performance for predicting both loan and default are shown in Table 2. In Python, the best model performance for predicting loan is Gradient Boosting which achieves the lowest RMSE of 2472.87. Next, the prediction result from Gradient Boosting is used as a predictor variable in test set to predict default. The best model performance in predicting default is also Gradient Boosting which achieves the highest accuracy of 85.41%, and lowest FNR of 4.48%. In Orange, the best model performance for predicting loan is also Gradient Boosting which achieves the lowest RMSE of 2449.32 and the best model performance in predicting default is Gradient Boosting and Neural Network which achieves the highest accuracy of 83.40%.
Based on these results, Orange outperforms Python in predicting loan, but Python outperforms Orange in predicting default. Because the default is more significant variable that can directly result in approval of credit card, hence this study concludes that the best model performance in basic approaches is using Gradient Boosting in Python for predicting both loan and default because this pair results in highest accuracy in default prediction.
![image](https://user-images.githubusercontent.com/84263856/201729069-62c609c3-9efe-4dc7-8f19-1cdc876bcb9c.png)

In order to improve the model performance, this study developed several alternative approaches, and the model performance is shown on Table 3. In loan prediction, the first alternative approach using Keras Sequential managed to outperform 2 models in Python (Decision Tree, Neural Network), and 2 models in Orange (Decision Tree, Random Forest). The second alternative approach is using regressor optimization on max_depth of Random Forest. It managed to outperform every other approach in Python and Keras Sequential with RMSE of 2456.62. Next, the prediction result from Regressor Optimization of Random Forest is used as a predictor variable in test set to predict default. 
In predicting default, alternative approach used is Keras Sequential using Keras Tuner. Keras Tuner is a library that can pick the most optimal hyperparameters. But even with Keras Tuner, the accuracy achieved is really low which is 53.09%. Low performance of Keras Sequential can be resulted from model that has multiple inputs and outputs.  For improving Keras Sequential results, future study can split the training data into training and validation set, converting the dataframe into tf.data.Dataset objects, batch the datasets, conduct feature pre-processing with Keras Layers, and conduct normalization [1]. 
![image](https://user-images.githubusercontent.com/84263856/201729342-3a1fc953-99af-4a71-8ee0-f1a9c53bcee9.png)

The study also used basic approach models to see whether there is improvement in predicting default using loan prediction result from Regressor Optimization Random Forest. The result shows that all the basic approach models’ performances are improved, and the highest model performance is by Gradient Boosting with 85.88% accuracy. This result outperforms every other approach in Python and Orange. Therefore, the best model for this case is using Regressor Optimization of Random Forest in predicting Loan Amount and using the Gradient Boosting in predicting default status. However, if the bank prefers to have lower accuracy but with lower false negative rate, then the bank can also use Neural Network to predict default, since it has lowest FNR of 3.48% with good accuracy of 83.43%.

## Model Implementation Plan and Importance for the Bank
![image](https://user-images.githubusercontent.com/84263856/201729638-24a516fe-4e1d-4b37-969c-41dc1382e6f9.png)

## Conclusion
To solve the business problem that bank is facing which is regarding the manual process of credit card approval that is too complicated, time-consuming, and sometimes inaccurate and unreliable, this study developed several machine learning models. The best model performance is by Regressor Optimization for Random Forest with 2456.62 RMSE in loan amount prediction, and Gradient Boosting with 85.88% accuracy in default prediction. With such a high accuracy machine learning and the right implementation plan at the bank, bank can increase employee’s productivity, reduce labour cost, and reduce card approval time which also is beneficial for applicants. On top of that, with high approval accuracy and reliability, bank can reduce credit default rate and eventually reduce risk of financial loss. Overall, bank would be tremendously benefitted by utilizing machine learning in loan approval process.

## Productionization
In this step, I built a flask API endpoint that was hosted on a local webserver. The API endpoint takes in a request value of customer’s age, income and returns loan amount as well as predicts whether or not the customer will default.

## Code and Resources Used
**Python Version:** 3.8.8

**Packages:** pandas, seaborn, matplotlib, sklearn, scipy, imblearn, keras, os, joblib, flask

**Orange Version:** 3.32

**For Web Framework Requirements:** pip install -r requirements.txt

**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2




