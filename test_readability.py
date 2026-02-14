from readability import analyze_readability

file_path = "../uploads/test_code.py"
score, feedback = analyze_readability(file_path)

print("Readability Score:", score)
print("Feedback:")
for f in feedback:
    print("-", f)
