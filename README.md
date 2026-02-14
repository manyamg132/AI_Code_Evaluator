# AI Coding Assignment Evaluator

## Overview
This project is an AI-powered coding assignment evaluator that allows students and educators to automatically assess Python code submissions beyond correctness. It provides human-like feedback including code quality, efficiency, readability, edge cases, and plagiarism detection.

## Features
- Correctness Analysis: Checks if code runs successfully and detects test case pass/fail.
- Efficiency Scoring: Evaluates time and space complexity using cyclomatic complexity.
- Readability & Code Quality: Assesses naming conventions, modularity, and docstring usage.
- Edge Case Handling: Detects potential runtime issues and suggests improvements.
- Plagiarism Detection: Highlights similarity with known solutions and reports percentage.
- Human-like Feedback Engine: Generates constructive suggestions for improvement.
- Frontend Interface: Clean web interface for file upload and GitHub URL evaluation.

## Project Structure
AI_Code_Evaluator/
├─ backend/
│ ├─ main.py
│ ├─ evaluate.py
│ ├─ efficiency.py
│ ├─ readability.py
│ └─ plagiarism.py
├─ frontend/
│ └─ index.html
├─ requirements.txt
├─ README.md


## Demo / Screen Recording
[Watch the working demo](https://drive.google.com/file/d/1RNGnpKlWUB-CQt3I04tPKmTmswL4sNAC/view?usp=sharing)


Clone the repository (optional if using locally):
git clone https://github.com/manyamg132/AI_Code_Evaluator.git


## Installation
1. Navigate to the backend folder:
cd backend

2. Create a virtual environment:
python -m venv venv

3. Activate the virtual environment:
-in Windows CMD:
venv\Scripts\activate.bat

-in PowerShell:
.\venv\Scripts\Activate.ps1

4. Install dependencies:
pip install -r ../requirements.txt


## Running the Project
uvicorn main:app --reload

Open frontend/index.html in your browser.

