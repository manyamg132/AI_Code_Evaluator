import difflib

def detect_plagiarism(code_text: str):
    # Dummy example: compare with a known solution (empty string here)
    known_solution = ""
    similarity = difflib.SequenceMatcher(None, code_text, known_solution).ratio()
    similarity_pct = round(similarity * 100)

    if similarity_pct > 80:
        message = f"High similarity detected ({similarity_pct}%) with existing solutions."
    else:
        message = f"No significant plagiarism detected ({similarity_pct}%)."

    return {"score": similarity_pct, "message": message}
