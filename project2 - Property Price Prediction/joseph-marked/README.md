## Problem Statement

Using the Ames Housing Dataset, create a regression model to predict the price of a house at sale. The model should not be too complicated and allow for up to 25 features to use for price prediction. With the regression model, potential buyers can estimate the price of a house based on a set of features and not worry if a house is over valued. A property agent can likewise use the model to propose a guide price for the seller based on the features of the house being sold.


## Executive Summary

With a set of data containing 82 different variables for 2930 houses that were sold between 2006 to 2010, a regression model with 25 features was developed after going through data cleaning, exploratory data analysis, feature engineering, pre-processing, model tuning and recursive feature elimination.

Feature selection was done in 3 stages. First, a correlation between sale priceb and features with continuous values was used to drop the features with low correlation. Next, an ElasticNet regularization picked out features which had low coefficients. The remaining features were put through a recursive feature elimination process to pick out the top 25 features that predicts the sale price of a house.

The resulting model enables the user to predict the price of a house by giving details on 12 different areas, such as size of above grade living area, size of basement and overall quality. Other important factors include the neighbourhood that the house is in, the type of house and the age of the house. Accuracy of the model is close to 88%, with an error margin of around $23000.


## Data Dictionary

The data dictionary is available [here](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt).

Data used in the analysis has been sourced from [DSI-US-6 Regression Challenge](https://www.kaggle.com/c/dsi-us-6-project-2-regression-challenge).


## Conclusion:

Now we are able to make a prediction on the price of a property by answering these **10 most important questions**:

    1. What is the above grade living area in sqft?
    2. How is the overall quality of material and finish of the house?
    3. What is the garage area in sqft?
    4. What is the total basement area in sqft?
    5. How is the overall condition of the house?
    6. How is the quality of kitchen?
    7. Is there a bath in the basement?
    8. Level of basement exposure
    9. Is there a fireplace?
    10. How many baths are there?


- Certain neighbourhoods like Green Hills, Stone Brook, Northridge Heights, Somerset and Crawford add a premium to the price.


- Certain dwelling types like duplex and 2-storey Planned Unit Development (1946 & newer) reduces the price.


- Age of the property has the highest negative impact on the price.


## Recommendation:
#### Some recommendations for the business:
- `Gr Liv Area` (Above ground living area square feet) and `overall_qual` (overall material and finish of the house) adds the most value to a home.


- Combined effect of `Total Bsmt SF` (Total square feet of basement area) and `age_built` (Age of the property, calculated from year built) hurt the value of a home the most.


- To increase the value of their home, besides improving the `overall quality` and `condition` of the house, homehowners could add a `bathroom in the basement` and a `fireplace` to their home. 


- The neighbourhoods of `Green Hills`, `Stone Brook`, `Northridge Heights` might be good investments.


#### Can this model be adapted to other cities?
This model will not generalize well to other cities since it includes specific neighbourhoods by name. To make it more universal, neighbourhoods could be classified into different types, e.g. urban, suburban. This [link](https://www.hgtv.com/lifestyle/real-estate/12-kinds-of-neighborhoods) shows a possible breakdown for the types of neighbourhoods to be considered.