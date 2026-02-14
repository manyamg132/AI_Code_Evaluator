import subprocess, tempfile, os
from efficiency import score_efficiency
from readability import score_readability
from plagiarism import detect_plagiarism

def run_tests(code_text: str):
    """Run basic Python test cases (can be extended)."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp:
        tmp.write(code_text)
        tmp_path = tmp.name
    try:
        result = subprocess.run(
            ["python", tmp_path],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result
    except subprocess.TimeoutExpired:
        return None
    finally:
        os.remove(tmp_path)

def evaluate_code_text(code_text: str, language="python") -> str:
    """Generate human-readable feedback for a code submission."""
    # Correctness
    result = run_tests(code_text)
    if result is None:
        correctness_score = 0
        correctness_feedback = "Code did not run or timed out."
    elif result.returncode == 0:
        correctness_score = 100
        correctness_feedback = "Code ran successfully without runtime errors."
    else:
        correctness_score = 50
        correctness_feedback = f"Code ran with errors. Return code: {result.returncode}"

    # Efficiency
    eff = score_efficiency(code_text, language)

    # Readability
    read = score_readability(code_text, language)

    # Plagiarism
    plag = detect_plagiarism(code_text)

    # Overall score (weighted)
    overall = round((correctness_score*0.4 + eff["score"]*0.2 + read["score"]*0.2 + (100 - plag["score"])*0.2))

    # Human-readable feedback
    feedback = f"""
Overall Score: {overall}/100

Correctness: {correctness_score}/100
{correctness_feedback}

Time & Space Efficiency: {eff['score']}/100
{eff['message']}

Readability & Code Quality: {read['score']}/100
{read['message']}

Plagiarism Check: {plag['message']}

Suggestions:
- Improve logic, structure, and performance where necessary.
- Follow best practices for naming, modularity, and readability.
- Handle edge cases carefully.
- Optimize for time & space complexity based on efficiency feedback.
"""
    return feedback.strip()

async def evaluate_code_file(url, language="python") -> str:
    import requests
    r = requests.get(url)
    code_text = r.text
    return evaluate_code_text(code_text, language)
