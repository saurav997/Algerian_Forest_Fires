## Algerian Forest Fire Prediction with Ridge Regression

This project utilizes machine learning to predict Forest Fire Weather Index (FWI) in Algeria. It's deployed as a web application using Flask on AWS Elastic Beanstalk.

**Project Overview**

* **Problem:** Forest fires are a major threat in Algeria. Predicting their occurrence can aid in prevention and mitigation efforts.
* **Solution:** This project leverages the Algerian Forest Fire dataset to train a Ridge Regression model for FWI prediction.
* **Deployment:** The model is deployed as a web application using Flask on AWS Elastic Beanstalk, allowing users to submit weather data and receive predicted FWI values.

**Data Description**

The project employs the Algerian Forest Fire dataset, publicly available on UCI Machine Learning Repository and Kaggle. The dataset covers a period from June to September 2012, focusing on two Algerian regions: Bejaia and Sidi Bel-abbes. It contains weather observations and FWI values for each day:

* **Date:** Day, month, and year (separate attributes)
* **Weather Observations:**
    * Temperature: Noontime temperature (°C)
    * Relative Humidity (%)
    * Wind Speed (km/h)
    * Rain (mm)
* **Fire Weather Indices (FWI):**
    * FFMC (Fine Fuel Moisture Code)
    * DMC (Duff Moisture Code)
    * DC (Drought Code) **(Removed due to high correlation)**
    * ISI (Initial Spread Index)
    * BUI (Buildup Index) **(Removed due to high correlation)**

**Model and Scaler**

The project employs a Ridge Regression model trained using cross-validation to enhance its generalization capabilities. This model is suitable for datasets with potentially high collinearity. Additionally, a StandardScaler is used for data normalization, ensuring all features contribute equally during prediction.

**Important Note:** Columns with high correlation, namely 'DC' and 'BUI', were removed during the training process to prevent redundancy and improve model performance.

**Deployment on AWS Elastic Beanstalk**

The web application is deployed on AWS Elastic Beanstalk, a service for provisioning and managing cloud applications. Elastic Beanstalk simplifies deployment by handling server provisioning, configuration, load balancing, and scaling. 

**How to Use the Application**

1. **Access the application:** (Provide deployment URL here once deployed)
2. **Enter Data:** The application provides a user-friendly form to enter relevant weather data points:
    * Date (DD/MM/YYYY)
    * Temperature (°C)
    * Relative Humidity (%)
    * Wind Speed (km/h)
    * FFMC (Fine Fuel Moisture Code)
    * DMC (Duff Moisture Code)
    * ISI (Initial Spread Index)
3. **Submit Prediction:** Click the "Predict FWI" button to submit your data.
4. **View Results:** The application will display the predicted FWI value based on the entered weather data.

**Disclaimer**

This is a research project and the predicted FWI should not be solely relied upon for critical fire prevention decisions. 

**Future Enhancements**

* Integrate real-time weather data acquisition.
* Develop a visual interface to display historical FWI data.
* Explore incorporating additional features like vegetation type and topography for potentially improved prediction accuracy.

**Technical Stack**

* Programming Language: Python
* Web Framework: Flask
* Machine Learning Library: scikit-learn
* Deployment Platform: AWS Elastic Beanstalk

**Getting Started (For Developers)**

1. **Clone the Repository:** (Provide your repository clone URL here)
2. **Set Up Environment:** Install required dependencies using `pip install -r requirements.txt`.
3. **Load Model and Scaler:** Load the pickled model and scaler objects from their respective files.
4. **Run the Application:** Run the Flask application using `python application.py`.

**Contributing**

We welcome contributions to this project. Feel free to fork the repository and submit pull requests with improvements or additional functionalities.

**License**

This project is licensed under the (Specify your chosen open-source license here).
