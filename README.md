A Simple Logistic Regression prediction system that predicts if a Marvel Movie will become a Smash hit or not

<br/>

**-> Dataset**

The dataset is generated using LLM and located in dataset/marvel_movie_data.csv

The dataset lists all the Marvel movie from 2007 to 2024, which includes
- Original Marvel Studios Productions
- Sony & Fox universe collaboration movies like Spiderman, X-men, Wolverine, etc.

Each entry in the dataset has multiple genres, directors, cast members (categorical data)

Each entry has a worldwide_collection column which is used to determine if the movie is smash hit or not 

<br/>

**-> Implementation Details**

A Movie is considered a Smash hit only if it earns more than 800 Million dollars in its lifetime

Used Scikit-learn for data preprocessing, model training, predicting data & prediction metrics

<br/>

**-> Overfitting Issue**

The model currently suffers Overfitting due to 
- less data (only about 54 rows)
- inclusion of lots of highly precise features like genres, directors and cast members
