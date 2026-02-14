import radon.complexity as rc

def score_efficiency(code_text: str, language="python"):
    try:
        blocks = rc.cc_visit(code_text)
        if blocks:
            avg_complexity = sum(b.complexity for b in blocks) / len(blocks)
        else:
            avg_complexity = 1

        if avg_complexity <= 5:
            score = 90
            message = "Excellent efficiency. Code structure is simple and clear."
        elif avg_complexity <= 10:
            score = 70
            message = "Moderate efficiency. Consider simplifying nested loops or functions."
        else:
            score = 50
            message = "Low efficiency. High cyclomatic complexity detected; refactor logic."
    except Exception:
        score = 60
        message = "Efficiency analysis unavailable."

    return {"score": score, "message": message}
