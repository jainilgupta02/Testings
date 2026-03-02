# 🧪 Python Testing & Coverage Project
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tests](https://img.shields.io/badge/tests-pytest-green)
![Coverage](https://img.shields.io/badge/coverage-enabled-brightgreen)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue)

This repository demonstrates **unit testing, code coverage analysis, and CI automation** using Python.

It is part of my **DevOps & Cloud Computing practice** to understand how testing integrates into real-world CI/CD pipelines.

---

## 🚀 What this project demonstrates

* Writing unit tests using **pytest**
* Measuring code coverage with **coverage.py**
* Generating HTML coverage reports
* Uploading coverage to CI tools (Codecov / GitHub Actions)
* Structuring Python projects for testing
* Automating tests in CI pipeline

---

## 📂 Project Structure

```
Testings/
│
├── src/              # Application source code
├── tests/            # Unit tests
├── .github/workflows # CI pipeline configuration
├── requirements.txt  # Dependencies
└── README.md
```

---

## 🧠 Application Example

A simple Python calculator supporting:

* Addition
* Subtraction
* Multiplication
* Division (with error handling)

---

## 🧪 Running Tests Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run tests:

```
pytest
```

Run tests with coverage:

```
pytest --cov=src
```

Generate HTML report:

```
pytest --cov=src --cov-report=html
```

Open coverage report:

```
htmlcov/index.html
```

---

## ⚙️ CI Integration

This repository uses **GitHub Actions** to:

* Install dependencies
* Run tests automatically
* Generate coverage report
* Upload results to coverage tools

You can view pipeline runs in:

**GitHub → Actions tab**

---

## 📊 Learning Outcomes

* Understood testing workflow in Python projects
* Learned coverage metrics and reports
* Practiced CI pipeline automation
* Improved code reliability mindset
* Built portfolio-ready DevOps project

---

## 👨‍💻 Author

**Jay Gupta**
DevOps & Cloud Learner (PW Skills)

---

⭐ Star this repo if you find it useful!
