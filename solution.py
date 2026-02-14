def check_numbers(lst):
    if not lst:
        return 0
    total = 0
    for n in lst:
        if n > 0:
            total += n
        else:
            total -= n
    return total

if __name__ == "__main__":
    import sys, ast
    lines = sys.stdin.read()
    lst = ast.literal_eval(lines)
    print(check_numbers(lst))
