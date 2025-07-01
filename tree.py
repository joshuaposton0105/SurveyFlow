import streamlit as st
import pandas as pd
from graphviz import Digraph

# Load and clean
df = pd.read_excel("encoded_df.xlsx")
concat_col = df.columns[-1]
num_questions = 9
df[concat_col] = df[concat_col].astype(str).str.zfill(num_questions)
df = df[df[concat_col].str.len() == num_questions]
question_cols = [f"Q{i+1}" for i in range(num_questions)]
df[question_cols] = df[concat_col].apply(lambda x: pd.Series(list(x)))

# User input: create path
st.sidebar.title("Build a Response Path")
path = []
for q in question_cols:
    if st.sidebar.checkbox(q):
        options = sorted(df[q].dropna().unique())
        val = st.sidebar.selectbox(f"{q} value", options, key=q)
        path.append((q, val))

# Build flow graph
dot = Digraph()
filtered = df.copy()
prev_node = "Start"
dot.node(prev_node, f"Start\n[{len(filtered)}]")

for i, (q, val) in enumerate(path):
    filtered = filtered[filtered[q] == val]
    node_id = f"{q}={val}"
    dot.node(node_id, f"{q} = {val}\n[{len(filtered)}]")
    dot.edge(prev_node, node_id)
    prev_node = node_id

st.graphviz_chart(dot)

# Show filtered table if needed
with st.expander("Show Matching Rows"):
    st.dataframe(filtered[question_cols])
