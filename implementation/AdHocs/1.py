from graphviz import Digraph

# Create Digraph
dot = Digraph(comment="CTI-KG End-to-End Pipeline", format="png")
dot.attr(rankdir="LR", size="8,5")

# Phase nodes
phases = {
    "1": "Phase 1:\nThreat Data Acquisition",
    "2": "Phase 2:\nNormalization & Parsing",
    "3": "Phase 3:\nEntity Resolution & Enrichment",
    "4": "Phase 4:\nKnowledge Graph Construction",
    "5": "Phase 5:\nAdversary & Campaign Attribution",
    "6": "Phase 6:\nContext-Aware Analysis",
    "7": "Phase 7:\nAdversary Simulation & Hunting Prep",
    "8": "Phase 8:\nAutomation & Integration",
    "9": "Phase 9:\nVisualization & Analyst Workbench",
    "10": "Phase 10:\nNLP Chatbot Interface",
    "11": "Phase 11:\nCollaboration & Sharing",
    "12": "Phase 12:\nMonitoring, Evaluation & Maintenance",
}

# Add nodes
for pid, label in phases.items():
    dot.node(pid, label, shape="box", style="rounded,filled", fillcolor="lightblue")

# Sequential flow
for i in range(1, 12):
    dot.edge(str(i), str(i+1))

# Feedback loops (major)
dot.edge("12", "1", label="schema drift feedback", style="dashed")
dot.edge("12", "4", label="KG retraining", style="dashed")
dot.edge("12", "10", label="Chatbot tuning", style="dashed")
dot.edge("12", "11", label="Sharing compliance", style="dashed")
dot.edge("6", "7", label="attack paths", style="dashed")
dot.edge("7", "8", label="hunts → SOAR", style="dashed")
dot.edge("8", "6", label="incident feedback", style="dashed")
dot.edge("9", "10", label="UI → chatbot", style="dashed")
dot.edge("11", "1", label="partner feeds", style="dashed")

# Save and render
file_path = "cti_kg_full_pipeline"
dot.render(file_path)

file_path + ".png"
