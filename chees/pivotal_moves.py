def sort_by_score_diff(analysis):
    sorted_analysis = sorted(analysis, key=lambda x: abs(x["score_diff"]), reverse=True)
    result = []
    for i, item in enumerate(sorted_analysis):
        result.append({"position": analysis.index(item) + 1, "differential": item["score_diff"], "score": item["score"], "move": item["move"]})
    return result