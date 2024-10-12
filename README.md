# **Food Association Analysis**

This project is an interactive data exploration tool built using **Streamlit** for discovering frequent itemsets (patterns) and association rules from a food dataset. It uses the **FP-Growth** algorithm for pattern mining and **NetworkX** with **Plotly** for visualizing food item associations as a network graph.

## **Table of Contents**

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

## **Features**

- **Frequent Pattern Mining**: Identify frequent food itemsets using the FP-Growth algorithm.
- **Association Rules**: Generate rules based on the relationships between food items.
- **Interactive Exploration**: Explore patterns and rules via a Streamlit web application.
- **Network Graph Visualization**: Display food item associations as an interactive network graph.
- **Adjustable Parameters**: Control sample size, minimum support, confidence, and top frequent patterns through the sidebar.

## **Installation**

**Install Dependencies: Install the required packages by running**:
    ```pip install -r requirements.txt```

If you do not have a requirements.txt, create one with:
- pandas
- pyfpgrowth
- streamlit
- networkx
- plotly

**Choose between the sections for:**

- Viewing Frequent Itemsets (Patterns)
- Viewing Association Rules
- Rules for a Specific Item

# Dataset
```The dataset must be in CSV format, with a column named Describe that contains lists of food items separated by commas.```


# Parameters

- Sample Size: Select the number of rows to sample for analysis.
- Minimum Support: The minimum number of times an itemset must appear to be considered frequent.
- Minimum Confidence: The minimum confidence level for association rules.
- Top Patterns: Control how many frequent itemsets are displayed in the results.

# Visualizations
- Frequent Itemsets (Patterns): Displays frequent itemsets and their support counts.
- Association Rules: Shows relationships between food items based on the specified confidence level.
- Network Graph: Displays a network graph of food items and their associations. Nodes represent items, and edges represent association rules with confidence values.

# File Structure

- streamlit_app.py      
- requirements.txt      
- data                  
- README.md             
- code.ipynb
- __pycache__

# Dependencies

- Python 3.x
- pandas: For data manipulation and loading the dataset.
- pyfpgrowth: For mining frequent patterns using the FP-Growth algorithm.
- Streamlit: For building the interactive web-based interface.
- NetworkX: For creating the network graph of associations.
- Plotly: For visualizing the network graph interactively.
- Install these dependencies using the requirements.txt provided.

# How It Works
1. The application loads the dataset and allows you to adjust parameters for frequent pattern mining.
2. It generates frequent patterns using the FP-Growth algorithm and identifies association rules.
3. You can explore:
    - Frequent Patterns: Itemsets that commonly appear together.
    - Association Rules: Relationships between items with a given confidence level.
    - Network Graph: A visual representation of food items and their associations.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Live Demo
- [website][#https://semester5-4zmlc2neazjpqsbtw2tug8.streamlit.app/]
