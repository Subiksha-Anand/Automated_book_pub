def rl_ranked_search(query, documents):
    """
    Dummy RL-style search that ranks documents based on keyword match.
    Replace with real reinforcement learning algorithm if needed.
    """
    ranked = sorted(documents, key=lambda doc: query.lower() in doc.lower(), reverse=True)
    return ranked

