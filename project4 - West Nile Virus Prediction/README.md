# West Nile Virus Prediction

## Problem Statement
West Nile Virus (Wnv), a mosquito-bourne arbovirus, has been causing significant and sometimes severe human diseases. Although pesticides are known to be effective in dealing with the virus-carrying mosquitoes, it is expensive to deploy pesticides throughout the city. As data scientists in the Division of Societal Cures in Epidemiology & New Creative Engineering, we want to understand the factors driving the spread of Wnv by leveraging on data collected by Chicago's weather stations and the surveillance system set up by the Chicago Department of Public Health. We also want to develop a classfication model that could predict the presence of Wnv within the area of Windy City. Through these studies, we hope to suggest a cost-efficient and effective method of deploying pesticides within the area.

## Summary

This project is part of a [Kaggle competition](https://www.kaggle.com/c/predict-west-nile-virus/overview) and explores data collected from various sources, namely:  
* Mosquito trap data collected by the surveillance and control system
* Location data of spraying efforts
* Weather data

The data from these three sources were combined to form a more wholesome dataset for analysis and modelling. The spray data was used to create a feature indicating if each mosquito trap was within the spray zone over a period of 30 days from the spray date. The weather data was added to the combined dataset based on date and location.

In this project, there are a total of six notebooks:
1) 01a Train EDA Cleaning
2) 01b Spray EDA Cleaning
3) 01c Weather EDA Cleaning
4) 02 Combined EDA Preparation
5) 03 Preprocessing Modeeling Evaluation
6) 04 Kaggle Predictions

## Contents:

1. [Datasets Used](#1-Datasets-Used)
2. [Exploratory Data Analysis & Data Cleaning](#2-Exploratory-Data-Analysis-&-Data-Cleaning)
3. [Modeling & Evaluation](#3-Modeling-&-Evaluation)
4. [Additional Modeling](#4-Additional-Modeling)
5. [Cost Benefit Analysis](#5-Cost-Benefit-Analysis)
6. [Conclusion and Recommendations](#6-Conclusion-and-Recommendations)
7. [Python Library Used](#7-Python-Library-Used)

### 1. Datasets Used 
The following datasets were created and used during this project:
- train
- spray
- weather
- samplesubmission
- train_final
- train_spray_cleaned
- train_spray_final
- trap_location
- test
- submission_predictions
- spray_cleaned
- spray_final
- weather_final
- combined_final
- combined_training
- X_train

### 2. Exploratory Data Analysis & Data Cleaning
In this section, we undergo studying, understanding and feature engineering of the datasets. After that, datasets were combined. The following actions are taken:
- Analyzing the train data and removing features that are not needed. Feature Engineering of species and distance of traps' locations and weather station.
- Analyzing the spray and trap data. Feature Engineering of trap_sprayed feature
- Analyzing the weather data and removing features that are not need. Creating weekly average and time-lagged features for all remaning weather conditions. Feature Engineering of Codesum feature.
- Combined all datasets together into one. Analyzing the combined dataset. Feature Engineering of traps feature. Drop features that will not be used and prepare for modeling.

We discovered that the time of the day where the sun is out was where the presence of Wnv was the strongest. Also, we observed that the more competent vectors for the spread of Wnv were the culex pipiens and culex restuans species. In order to deploy pesticides in a more cost-efficient way, we recommend spraying in areas where culex pipiens/restuans are most prominent and during the day as the Sun rises where the mosquitoes are most active.

### 3. Modelling & Evaluation
Several classifier models were developed, where the hyperparameters were tuned for each model to obtain the best cross-validated AUC scores. Because there were heavy imbalances in the data collected (about 95% of the data indicated no Wnv), an over-sampling method known as SMOTE (Synthetic Minority Over-sampling Technique) was adopted. It was also the reason for optimizing the models on AUC scores instead of accuracy. Comparing the AUC and recall scores, the production model selected was the AdaBoost model. Comparing the train and test accuracy scores of the selected model, there was evidence of slight overfitting of the data but the small difference was acceptable by our means

Models used:
- Logistic Regression
- Bernoulli Naive Bayes
- Random Forest Classifier
- ExtraTrees Classifier
- AdaBoost Classifier
- Gradient Boost Classifier
- Support Vector Classifier

Evaluation Metrics used:
- ROC-AUC score
- F1-Score
- Recall
- Precision
- Accuracy

### 4. Additional Modelling
We also explored into deep learning and neural networks. However, our neural network did not outperform the selected model, likely due to the fact it had low complexity. We decided not to further develop the deep learning model since it is not easily interpretable and we had to keep within the limited timeframe of this project.

### 5. Cost Benefit Analysis
For our project, we use trap-sprayed feature as a strong predictor of the presence of the Wnv in some of the models, suggesting that the spraying was effective in dealing with the Wnv to a large extent. Using our production model to predict where we should spray as a benchmark for future assessments, the benefits of $1,048,789.03 would out-weigh the cost, which is the amount that would be saved from excessively spraying the whole city. The cost of spraying the whole city is $$1,653,467.04, whereas the direct cost and indirect cost of targeted spraying are $145,060.68 and $459,617.30.

### 6. Conclusion & Recommendation
In this project,we gained many useful insights about the mosquito population in Windy City and its relation to the epidemic of West Nile Virus(Wnv). Using our production model which is AdaBoost algorithm which gave us a high AUC and recall score. From our model, we can see the top features of importance contain result speed, wet & dry condition, sunlight, station pressure and some of the traps. 

Moving forward, more geographic and demographics information could also be useful in studying the presence of Wnv. Since Wnv is spread through moquitoes, we could expect that proportion of open water sources, percentage of grass land, forests, and urban landscape are all factors of the livelihood of these mosquitoes. We can expand the studies to the rest of United States with more data on more mosquitoes species as other states have other species as the main vector species. 

### 7. Python Library Used
- Pandas
- Numpy
- Seaborn
- Matplotlib
- Pickle
- Sklearn
- Imblearn
- Tensorflow
- Folium
- Branca
- Datetime
- Suntime
- Pytz
- Geopy


