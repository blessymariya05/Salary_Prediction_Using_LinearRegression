# Salary_Prediction_Using_LinearRegression
A beginner Machine Learning project demonstrating data preprocessing, train-test split, Linear Regression, and data visualization using Python.
The project demonstrates a basic Machine Learning workflow including:
- Data preprocessing
- Missing value handling
- Train-test split
- Model training
- Salary prediction
- Data visualization

# Technologies Used
- Python
- Pandas
- Matplotlib
- Sklearn

# Dataset
Dataset used:
- 'Salary_Data.csv' from kaggle
Columns:
- 'YearsExperience'
- 'Salary'

# Project Workflow
 1. Load Dataset:
      The dataset is loaded using Pandas.
      Python command:
	df = pd.read_csv("Salary_Data.csv")

 2. Handle Missing Values:
       A missing value is intentionally created for practice:
       df.loc[2,"Salary"] = None
       
       The missing value is replaced using the mean salary:
       df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

3. Feature Selection:
        Input Feature:- YearsExperience
        Target Variable:- Salary
        
        Command:
          X = df[["YearsExperience"]]
          Y = df["Salary"]

4. Train-Test Split

        The dataset is split into:
            - 80% training data
            - 20% testing data

        Command:
           train_test_split(X, Y, test_size=0.2, random_state=42)

5. Linear Regression Model

       The model is trained using Scikit-learn.
   
       Command:
          model = LinearRegression()
          model.fit(x_train, y_train)

6. Salary Prediction

       The model predicts salary values for test data.

       Command:
          prediction = model.predict(x_test)

7. Data Visualization

      Matplotlib is used to plot:
          - Actual data points
          - Regression line

      Command:
          plt.scatter(X, Y)
          plt.plot(X, model.predict(X))

Output:

     The model predicts salary based on employee experience.

     Example:
        - Higher experience generally results in higher predicted salary.

Visualization:

    The graph displays:
      - Scatter plot of actual salary data
      - Best-fit regression line


## Author
Blessy Mariya


