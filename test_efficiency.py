from efficiency import analyze_time_complexity

# Correct path to the file
file_path = "../uploads/test_code.py"

# Run complexity analysis
max_complexity, details = analyze_time_complexity(file_path)

print("Max Cyclomatic Complexity:", max_complexity)
print("Function complexities:")
for func in details:
    print(f"Function '{func['name']}' -> Complexity: {func['complexity']}")
