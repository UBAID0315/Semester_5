import pandas as pd
import pyfpgrowth
import streamlit as st
import networkx as nx
import plotly.graph_objects as go
import warnings
from collections import Counter

warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(page_title="Food Association Analysis", layout="wide")

# Custom CSS to improve the app's appearance
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    font-weight: bold;
}
.stButton>button {
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    food_items = pd.read_csv("1662574418893344.csv")
    return food_items

@st.cache_data
def generate_patterns_and_rules(data, sample_size=400, min_support=7, min_confidence=0.5, top_n=100):
    # Adjusting the sample and pattern generation
    subset = data.sample(sample_size, replace=True)
    subset["Describe"] = subset["Describe"].apply(lambda x: x.split(","))
    
    # Find the frequent patterns with the given minimum support
    patterns = pyfpgrowth.find_frequent_patterns(subset["Describe"], min_support)
    rules = pyfpgrowth.generate_association_rules(patterns, min_confidence)
    sorted_patterns = dict(sorted(patterns.items(), key=lambda item: item[1], reverse=True)[:top_n])
    
    return sorted_patterns, rules

@st.cache_data
def get_top_items(data, patterns, top_n=50):
    all_items = [item.strip() for items in data["Describe"] for item in items.split(",")]
    unique_items = set([item for item in all_items if item])
    items_in_patterns = set()
    for pattern in patterns:
        items_in_patterns.update(pattern)

    return list(items_in_patterns)


def create_network_graph(rules):
    G = nx.Graph()
    for antecedent, (consequent, confidence) in rules.items():
        for item in antecedent:
            G.add_edge(item, consequent, weight=confidence)
    return G

def plot_network_graph(G):
    pos = nx.spring_layout(G)
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    node_adjacencies = []
    node_text = []
    for node, adjacencies in enumerate(G.adjacency()):
        node_adjacencies.append(len(adjacencies[1]))
        node_text.append(f'{adjacencies[0]}<br># of connections: {len(adjacencies[1])}')

    node_trace.marker.color = node_adjacencies
    node_trace.text = node_text

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='<br>Network graph of Food Item Associations',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20,l=5,r=5,t=40),
                        annotations=[dict(
                            text="Python code: <a href='https://plotly.com/ipython-notebooks/network -graphs/'> Network Graphs</a>",
                            showarrow=False,
                            xref="paper",
                            yref="paper",
                            x=0.005,
                            y=-0.002)],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

    st.plotly_chart(fig, use_container_width=True)

def display_patterns(patterns):
    st.header("Frequent Itemsets (Patterns)")
    for pattern in patterns:
        st.write(f"Pattern: {pattern} (Support: {patterns[pattern]})")

def display_rules(rules):
    st.header("Association Rules")
    for rule in rules:
        antecedent = rule
        consequent = rules[rule][0]
        confidence = rules[rule][1]
        st.write(f"Rule: {antecedent} -> {consequent} (Confidence: {confidence:.2f})")

def display_rules_for_itemset(rules, item_name, patterns):
    st.write(f"\nAssociation rules related to '{item_name}':")
    found = False
    item_name = item_name.strip().lower() 
    
    # Check if the item is part of the patterns
    item_in_patterns = any(item_name in pattern for pattern in patterns)
    
    for rule in rules:
        antecedent = tuple(x.strip().lower() for x in rule)
        consequent = rules[rule][0]
        consequent = consequent.strip().lower() if isinstance(consequent, str) else tuple(x.strip().lower() for x in consequent)  # Clean up consequent items
        confidence = rules[rule][1]
        
        if item_name in antecedent or item_name in consequent:
            found = True
            st.write(f"Rule: {antecedent} -> {consequent} (Confidence: {confidence:.2f})")

def call_graph(rules):
    st.header("Network Graph of Food Item Associations")
    G = create_network_graph(rules)
    plot_network_graph(G)

def main():
    st.title("Food Association Analysis")
    st.header("Data Overview")
    data = load_data()
    st.write(data.head())

    st.header("Data Statistics")
    st.write(data.describe())

    # Add header to the sidebar
    st.sidebar.header("Association Rule Mining")

    # Add sliders to the sidebar
    sample_size = st.sidebar.slider("Sample Size", 10, 400, 290)
    min_support = st.sidebar.slider("Minimum Support", 1, 10, 6)
    min_confidence = st.sidebar.slider("Minimum Confidence", 0.1, 1.0, 0.5)
    top_n = st.sidebar.slider("Number of Frequent Patterns", 10, 100, 15)  # Added top_n slider for patterns

    # Generate patterns and rules
    patterns, rules = generate_patterns_and_rules(data, sample_size, min_support, min_confidence, top_n)

    # Get unique items from the dataset
    unique_items = get_top_items(data,patterns)

    # Add a sidebar selector for the user to choose between sections
    option = st.sidebar.selectbox(
        "Choose a section to display:",
        ("Frequent Itemsets (Patterns)", "Association Rules", "Rules for Specific Item")
    )

    if option == "Frequent Itemsets (Patterns)":
        display_patterns(patterns)

    elif option == "Association Rules":
        display_rules(rules)

    elif option == "Rules for Specific Item":
        st.header("Rules for Specific Item")
        item_name = st.selectbox("Select an item for association rule analysis", unique_items)
        display_rules_for_itemset(rules, item_name, patterns)
    
    if option != "Frequent Itemsets (Patterns)":
        call_graph(rules)

if __name__ == "__main__":
    main()
