## Problem Statement
At the supermarket, most of the items are packed and their prices clearly labelled. There are however some grocery items, especially vegetables that needs to be weighed as they come in different sizes. For these vegetables, a price per kg is usually displayed and one will need to bring the vegetable to the weighing scale, select the vegetable from the screen and a label will then be printed based on the weight of the items on the scale and the type of vegetable selected.

**Problem**: There is usually a long list of vegetables to choose from, spanning multiple pages and it can be confusing as well as time consuming to find the right vegetable.


## Approach
Using Convolutional Neural Networks (CNN), I will build an image classification model to recognise some of the common vegetables found at the supermarket that needs to be weighed. The model will identify the vegetable and present to the customer so one need not scroll through the long list just to find the right vegetable. 


## Stakeholders
Possible stakeholders for this model includes all supermarket operators selling vegetables by weight. Deploying an image classification model which will recognise the vegetables will cut down on customers queueing to weigh the vegetables and increase customer satisfaction.


## Executive Summary
An image dataset consisting of 90K+ images belonging to 131 classes of fruits and vegetables found on Kaggle was used as the basis for the images needed for the training of the model. The 131 classes included both fruits and vegetables, and for the same vegetable, different varieties were classified separately. As the project is focused on classifying vegetables, 21 classes were shortlisted after excluding all fruits.

EDA was done for the 21 classes. Some classes were removed as they were not local, some were reclassed to reflect the correct class and some classes were merged as they would most likely be sold together. After EDA, 10 vegetable classes were finalized from the Kaggle dataset.

As quite a number of locally available vegetables were missing from the Kaggle dataset, 8 more classes were added. Photos of the 8 new classes were taken and further augmented using rotation, to maintain a well-balanced distribution of images for each class. An average of ~600 images per class was used for training.

A simple CNN model with 1 layer of 16 filters had yielded 0.916 validation accuracy, quite a high accuracy score. A 2nd model with 2 convolutional layers and 32 filters in the 2nd layer further improved the validation accuracy to 0.936. Finally, transfer learning from a VGG16 model with imagenet weights was used to train the model and validation accuracy increased further to 0.963. The model trained with VGG16 layers was chosen as the production model.


## Files
The project is split into two notebooks:
1. 01_data_prep.ipynb (creating the image dataset for training)
2. 02_modeling.ipynb (creating the model for image classificiation)