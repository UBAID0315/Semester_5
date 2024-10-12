# Food Association Analysis

This project is an interactive data exploration tool built using **Streamlit** for discovering frequent itemsets (patterns) and association rules from a food dataset. It uses the **FP-Growth** algorithm for pattern mining and **NetworkX** with **Plotly** for visualizing food item associations as a network graph.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Parameters](#parameters)
- [Visualizations](#visualizations)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)
- [How It Works](#how-it-works)
- [License](#license)

## Features

- **Frequent Pattern Mining**: Identify frequent food itemsets using the FP-Growth algorithm.
- **Association Rules**: Generate rules based on the relationships between food items.
- **Interactive Exploration**: Explore patterns and rules via a Streamlit web application.
- **Network Graph Visualization**: Display food item associations as an interactive network graph.
- **Adjustable Parameters**: Control sample size, minimum support, confidence, and top frequent patterns through the sidebar.

## Installation


1. **Install Dependencies: Install the required packages by running**:
    ```pip install -r requirements.txt```

    ```If you do not have a requirements.txt, create one with:```
    ```pandas```
    ```pyfpgrowth```
    ```streamlit```
    ```networkx```
    ```plotly```

# Usage
1. **Run the Streamlit App**:
streamlit run app.py
2. **Open the Browser:** Once the app is running, navigate to the URL shown in the terminal (usually http://localhost:8501).
3. Explore the Application: Use the sidebar to adjust the parameters for frequent pattern mining:

o Sample size
o Minimum support
o Minimum confidence
o Number of frequent patterns (top_n)

**Choose between the sections for:**

o Viewing Frequent Itemsets (Patterns)
o Viewing Association Rules
o Rules for a Specific Item

# Dataset
```The dataset must be in CSV format, with a column named Describe that contains lists of food items separated by commas.```

Example Data Format:
ID	Describe
1	apple, banana, milk
2	bread, butter
3	banana, milk, bread
...	...
Ensure that the Describe column contains comma-separated food items.

# Parameters

o Sample Size: Select the number of rows to sample for analysis.
o Minimum Support: The minimum number of times an itemset must appear to be considered frequent.
o Minimum Confidence: The minimum confidence level for association rules.
o Top Patterns: Control how many frequent itemsets are displayed in the results.

# Visualizations
o Frequent Itemsets (Patterns): Displays frequent itemsets and their support counts.
o Association Rules: Shows relationships between food items based on the specified confidence level.
o Network Graph: Displays a network graph of food items and their associations. Nodes represent items, and edges represent association rules with confidence values.

# File Structure

├── streamlit_app.py               # Main Streamlit application
├── requirements.txt      # List of required Python libraries
├── data  # Dataset file (place in root)
├── README.md             # Project documentation
├── code.ipynb
├── __pycache__

# Dependencies

o Python 3.x
o pandas: For data manipulation and loading the dataset.
o pyfpgrowth: For mining frequent patterns using the FP-Growth algorithm.
o Streamlit: For building the interactive web-based interface.
o NetworkX: For creating the network graph of associations.
o Plotly: For visualizing the network graph interactively.
o Install these dependencies using the requirements.txt provided.

# How It Works
1. The application loads the dataset and allows you to adjust parameters for frequent pattern mining.
2. It generates frequent patterns using the FP-Growth algorithm and identifies association rules.
3. You can explore:
    0 Frequent Patterns: Itemsets that commonly appear together.
    0 Association Rules: Relationships between items with a given confidence level.
    0 Network Graph: A visual representation of food items and their associations.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.