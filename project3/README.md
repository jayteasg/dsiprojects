## Problem Statement.
I am one of the moderators for a Spirituality discussion forum. The forum is focused on the subject of Spirituality but there have been frequent postings from religious groups that try to disrupt the discussion and we have received feedback from our senior forum members to remove such postings. However, there are hundreds of postings each day and we will need to develop a quick way to identify such posts and remove them quickly.

### Stakeholders:
Readers of our forum who are interested in the subject of Spirituality.

### Approach:
Using classification models such as Logistic Regression, Naive Bayes, KNN and DecisionTrees, correctly predict whether a post belongs to Spirituality or Religion. Data will be scrapped from reddit.com, using subreddits /r/spirituality and /r/religion. A classification model will be trained to predict Spirituality as the positive class and top prediction features will be identified.

### Measure of Success:
The classification model would be assessed on its test accuracy and specificity score. The model should reduce false positives as much as possible. We do not want posts related mostly to Religion getting classified as Spirituality.


## Executive Summary

To solve the problem of posting of religious content in our Spirituality forum, we built a Classification Model using postings from reddit.com/r/spirituality/ and reddit.com/r/religion/. A total of about 1300 posts from each subreddits were collected for training and testing the model.

A range of classification models including Logistic Regression, Naive-Bayes Multinomial and RandomForest Classifier were tested. The best performing model was the Naive-Bayes Classifier, with a test accuracy of 0.904, specificity of 0.880 and  less overfitting. On new data, the accuracy is also high at 0.917 while specificity score peaked at 0.971.

The final model can now be deployed with above 90% accuracy. To prevent false positives (i.e. post related to Religion being predicted as Spirituality), posts classified as Spirituality should be checked again should they contain keywords like phone, day, life, time and death as these are known to cause false positive misclassification by the model.


## Conclusion:

- The model is able to distinguish content of Spirituality and Religion quite well, with an ROC AUC score of 0.955 on test data.


- On new data, the model also performed well with a high accuracy score of 0.917 and a high specificity score of 0.971. 



## Recommendation:

- Deploy the model to start identify negative class postings quickly and remove them from the forum.


- For positive class posts, if they contain these 5 keywords `soul`, `day`, `life`, `time`, `thing` and `year`, look at them separately before allowing the post as these are likely candidates for false positives.