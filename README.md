Hishabee Web – QA Automation Scripts

1. Overview
This repository contains automated test scripts developed for the Hishabee Web (Dokan Management) platform as part of the Final QA Assessment Task for the Hishabee Internship selection process.

The goal of this automation project is to:
- Verify core functionalities of the platform through normal (happy path) tests.
- Validate system behavior under edge cases and unexpected inputs.
- Provide clear, repeatable, and maintainable automated tests for faster regression cycles.

2. Scope of Testing
The tests in this repository cover 10 selected test cases from my initial manual test case set:
- 5 Normal Tests: Validate core business flows that a user would perform daily.
- 5 Edge Cases: Test unusual or boundary conditions to ensure system robustness.

Test Case List:

#   Test Case Title                         Type
1   Login with valid credentials             Normal
2   Add a new product with all valid details Normal
3   Edit product name and price successfully Normal
4   Search for an existing product           Normal
5   Logout successfully                      Normal
6   Login with valid username but wrong password Edge
7   Add product without mandatory fields     Edge
8   Search for a product that doesn’t exist  Edge
9   Add a product with extremely long name   Edge
10  Try adding duplicate product name        Edge

3. Tools & Technologies Used
- Programming Language: Python 3.x
- Automation Framework: Selenium WebDriver
- Test Runner: Pytest
- Reporting: pytest-html (for HTML reports)
- Browser: Google Chrome
- Driver: ChromeDriver (version matching installed Chrome browser)

4. Prerequisites
Before running the tests, ensure the following are installed on your system:

1. Python 3.10
   Download & install from: https://www.python.org/downloads/

2. Google Chrome Browser
   Download & install from: https://www.google.com/chrome/

3. ChromeDriver
   - Download from: https://sites.google.com/chromium.org/driver/
   - Ensure the version matches your Chrome browser version.
   - Place the driver in a directory included in your system PATH.

4. Pip (Python package manager)
   Usually comes with Python installation.
   Verify by running:
   pip --version

5. Installation & Setup
1. Clone the Repository
   git clone https://github.com/yourusername/hishabeeWeb_autoTest.git
   cd hishabeeWeb_autoTest

2. Install Required Packages
   pip install -r requirements.txt

Example requirements.txt contents:
selenium
pytest
pytest-html

6. Folder Structure
hishabeeWeb_autoTest/
│
├── tests/
│   ├── test_add_purchase_entry.py
│   ├── test_login_invalid.py
│   ├── test_add_product_valid.py
│   ├── test_add_product_missing_fields.py
│   ├── test_edit_product.py
│   ├── test_search_existing_product.py
│   ├── test_search_nonexistent_product.py
│   ├── test_add_product_long_name.py
│   ├── test_add_duplicate_product.py
│   ├── test_logout.py
│
├── screenshots/
│   ├── login_valid.png
│   ├── login_invalid.png
│   └── ...
│
├── requirements.txt
├── README.txt
└── pytest.ini

7. How to Run the Tests
1. Run all tests
   pytest tests/ --html=report.html --self-contained-html

2. Run a specific test file
   pytest tests/test_login_valid.py --html=report.html --self-contained-html

3. View the Report
   Open report.html in your browser after test execution.

8. Test Results
- Screenshots of each test execution are stored in the screenshots/ folder.
- HTML report (report.html) contains:
  - Pass/Fail status
  - Duration of each test
  - Error messages (if any)

9. Suggestions for Test Process Improvement (Optional but Recommended)
- Integrate tests with CI/CD pipeline (e.g., GitHub Actions, Jenkins) for automated nightly runs.
- Expand automation to cover more edge cases and negative scenarios.
- Use Page Object Model (POM) for better code maintainability.
- Add cross-browser testing for Firefox and Edge.
- Implement data-driven testing using CSV or Excel files.

10. Author
Name: Abir Bhuiyan
Role: QA Automation Intern Applicant – Hishabee Technologies Ltd.
Contact: your.email@example.com
GitHub: https://github.com/yourusername
