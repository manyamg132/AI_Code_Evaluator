import re

def score_readability(code_text: str, language="python"):
    variable_names = re.findall(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\b", code_text)
    short_names = [v for v in variable_names if len(v) <= 2]

    if len(variable_names) == 0:
        score = 60
        message = "No variables detected; ensure meaningful identifiers."
    elif len(short_names)/len(variable_names) > 0.3:
        score = 50
        message = "Many short or unclear variable names detected. Consider descriptive names."
    else:
        score = 85
        message = "Variable names and structure are mostly clear."

    # Check docstring presence
    if '"""' not in code_text and "'''" not in code_text:
        message += "\nMissing docstring in functions or modules."
        score -= 5

    return {"score": score, "message": message}
