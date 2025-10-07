# KU - Interactive Linear Regression Visualizer

This project is a Streamlit web application that allows users to interactively visualize simple linear regression. Users can adjust parameters such as the slope, intercept, number of data points, and noise level to see how these changes affect the data and the resulting regression line.

## Live App

The application is deployed on Streamlit Cloud and can be accessed here: [https://evbwqxxybnadwqmje2mmhw.streamlit.app/](https://evbwqxxybnadwqmje2mmhw.streamlit.app/)

## Motivation

This project was developed to provide an interactive and intuitive tool for understanding the fundamentals of linear regression. By allowing users to manipulate the underlying data parameters and see the immediate impact on the model, it helps build a stronger conceptual understanding of how linear regression works.

## Features

*   **Interactive Sliders:** Adjust the true slope (a), intercept (b), noise level, and number of data points.
*   **Real-time Visualization:** The scatter plot and the fitted regression line update instantly as parameters are changed.
*   **Model Evaluation:** The app displays the original (true) parameters and the parameters fitted by the linear regression model for comparison.
*   **Educational:** Built using the CRISP-DM framework (Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment) to structure the code and explanation.

## Quick Start

To run this application locally, ensure you have Python installed, then follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/harryku0311/HW1.git
    cd HW1
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit app:**
    ```bash
    streamlit run linear_regression.py
    ```

## Deployment on Streamlit Cloud

This application is deployed using Streamlit's free community cloud. To deploy your own version, follow these steps:

1.  Push your project to a GitHub repository.
2.  Go to [share.streamlit.io](https://share.streamlit.io/) and sign in.
3.  Click "**New app**" and select the repository.
    *   **Repository:** `harryku0311/HW1`
    *   **Branch:** `main`
    *   **Main file path:** `linear_regression.py`
4.  Set the **App name** (e.g., `KU`).
5.  Click "**Deploy!**".

## Required Files

The repository must contain the following files for successful deployment:

**1. `requirements.txt`:** Lists the Python libraries needed for the app.
```
numpy
scikit-learn
matplotlib
streamlit
```

**2. `.streamlit/config.toml`:** Configuration file for Streamlit. This example disables usage statistics gathering and enables headless mode, which is good practice for deployment.
```
[browser]
gatherUsageStats = false

[server]
headless = true
```

## Repository Structure
```
C:/Users/lab611/Desktop/HW1/
├── .streamlit/
│   └── config.toml
├── linear_regression.py
├── requirements.txt
└── README.md
```

## Troubleshooting

*   **`ModuleNotFoundError`:** Ensure you have installed all the packages from `requirements.txt` by running `pip install -r requirements.txt`.
*   **Streamlit Command Not Found:** If `streamlit run` is not recognized, make sure your Python scripts directory is in your system's PATH. Alternatively, you can run it as a module: `python -m streamlit run linear_regression.py`.
*   **Deployment Issues:** Check the logs in your Streamlit Cloud dashboard. The most common issue is a missing or incorrect `requirements.txt` file.