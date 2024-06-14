# Algerian Forest Fires Prediction: An End-to-End Prediction model

## Project Overview

The Algerian Forest Fires Prediction project aims to predict the Fire Weather Index (FWI), an indicator of potential fire intensity, using meteorological data. This application provides a user-friendly interface for predicting FWI values based on input parameters such as temperature, relative humidity, wind speed, and other relevant factors. The project employs a LassoCV regression model for its predictions, with features carefully selected to optimize model performance.

## Dataset Details

The dataset used in this project is the Algerian Forest Fires dataset, which includes data collected from two regions in Algeria, Bejaia and Sidi Bel-Abbes, during the period from June to September 2012. The dataset consists of several meteorological factors that influence forest fires. The features used in the dataset are:

- **Temperature (°C)**: The temperature at noon (in Celsius degrees).
- **Relative Humidity (%)**: The relative humidity (in percentage).
- **Wind Speed (km/h)**: The wind speed (in kilometers per hour).
- **Rain (mm)**: The total daily rain (in millimeters).
- **Fine Fuel Moisture Code (FFMC)**: An index from the Fire Weather Index (FWI) system indicating the moisture content of surface litter and fine fuels.
- **Duff Moisture Code (DMC)**: An index from the FWI system indicating the moisture content of decomposed organic material in the upper soil layer.
- **Initial Spread Index (ISI)**: An index that combines the effects of wind and the FFMC to predict the rate of fire spread.
- **Region**: Categorical variable indicating the region of data collection (0 for Bejaia and 1 for Sidi Bel-Abbes).
- **Classes**: Binary variable indicating the occurrence of a fire (0 for no fire and 1 for fire).

## Methodology

### Data Preprocessing

The dataset underwent several preprocessing steps to ensure its suitability for the predictive model:
1. **Feature Selection**: Initially, all available features were considered. However, some features were removed due to high correlation with other features, which could lead to multicollinearity and affect model performance. Specifically, the DC (Drought Code) and BUI (Buildup Index) features were excluded.
2. **Scaling**: All numerical features were scaled using a StandardScaler to ensure they have a mean of 0 and a standard deviation of 1, which helps improve the performance of the Lasso regression model.

### Model Selection

The project utilizes a LassoCV (Least Absolute Shrinkage and Selection Operator with Cross-Validation) regression model. Lasso regression is a type of linear regression that uses shrinkage, where data values are shrunk towards a central point, like the mean. Cross-validation is used to determine the best model hyperparameters and to prevent overfitting.

### Training and Evaluation

The model was trained on the processed dataset, with cross-validation ensuring that it generalizes well to unseen data. The removal of highly correlated features like DC and BUI helped in reducing multicollinearity, which can adversely impact the model's performance.

## Application Details

### Frontend

The application has a simple and intuitive user interface with two main pages:

- **Landing Page (index.html)**: This page provides an overview of the project, including information about the dataset, the model used, and the features considered. It has a button that navigates to the prediction page.

- **Prediction Page (home.html)**: This page contains a form where users can input the required meteorological parameters. Based on the input values, the application predicts the Fire Weather Index (FWI). If no prediction is made (i.e., the page is refreshed or the form is reset), the form is displayed. If a prediction is made, the page shows the predicted FWI value and its implications.

### Dark Mode Feature

The application includes a dark mode toggle feature to enhance user experience. A slider at the top of each page allows users to switch between light and dark themes. This feature is designed to switch the overall template gradually between light and dark modes, providing a more comfortable viewing experience under different lighting conditions. Please note that the dark mode feature is currently under development and may undergo further improvements.

## Conclusion

The Algerian Forest Fires Prediction project leverages a robust LassoCV regression model to predict the Fire Weather Index based on various meteorological parameters. The frontend of the application is designed to be user-friendly, providing an easy way to input data and view predictions. The ongoing addition of the dark mode feature demonstrates a commitment to enhancing user experience.

## Future Work

- **Improving Dark Mode**: Complete the dark mode feature to ensure seamless transition and enhanced visual comfort for users.
- **Model Enhancement**: Explore other machine learning models and techniques to further improve prediction accuracy.
- **Feature Expansion**: Consider incorporating additional relevant features to potentially enhance the model's predictive power.

By providing detailed insights and accurate predictions, this project aims to be a valuable tool in the early detection and management of forest fire risks in Algeria.
