# Hishabee QA Internship Final Task - Test Automation Suite

## Repository Overview
This repository contains the submission for the Hishabee QA Internship final task - automated test scripts for the Hishabee web platform (Dokan Management System) using Selenium WebDriver with Python.

Repository URL:  
https://github.com/abirAbhuiyan/hishabee-internship-final-task.git

## Technical Specifications
- Platform: Hishabee Web (Dokan Management)
- Automation Tool: Selenium WebDriver
- Language: Python 3.x
- Browser: Chrome
- Test Framework: Custom implementation
- Reporting: Text log files with timestamps
- Execution: Sequential via run_test.py

## Test Cases Automated

### Purchase Module Tests
1. P001.py - Add a new purchase entry with valid data
2. P002.py - Attempt to add a purchase entry with missing required fields
3. P003.py - Edit the purchase value to a negative value
4. P005.py - Add large quantity purchase (10,000 units)
5. P006.py - Cancel adding product with partial data
6. P007.py - Edit an existing purchase entry
7. P010.py - Add product with an existing name

### Stock Book Module Tests
8. S003.py - Search Stock Book by item name
9. S004.py - Update stock after a purchase
10. S005.py - Update stock after a sale

## Setup Instructions

### Prerequisites
- Python 3.8 or later
- Chrome browser (latest stable version)
- ChromeDriver matching your Chrome version

### Installation Steps
1. Clone the repository:
   git clone https://github.com/abirAbhuiyan/hishabee-internship-final-task.git
2. Install required packages:
   pip install selenium
3. Download ChromeDriver and add to PATH or project directory

## Execution Instructions
To run all tests sequentially:
python run_test.py

To run individual tests:
python [test_script_name].py
Example: python P001.py

## Test Results
- Each test generates a dedicated log file (e.g., P001_log.txt)
- Logs include detailed execution steps with timestamps
- Final status is displayed in console output

## Test Data
- Test credentials are hardcoded in scripts (for evaluation purposes)
- Default test shop: "test"
- Test products: "product1", "product2"

## Technical Implementation Details
1. Framework Features:
   - Explicit waits using WebDriverWait
   - Comprehensive error handling
   - Detailed logging mechanism
   - Multi-language support (English/Bengali)

2. Common Functions:
   - Login sequence
   - Shop selection
   - Language setting (English)
   - Navigation helpers

## Known Limitations
1. Current Implementation:
   - Test data is hardcoded in scripts
   - No screenshot capture on failure
   - Sequential execution only

2. Recommended Improvements:
   - Implement Page Object Model pattern
   - Externalize test data to config files
   - Add screenshot capability
   - Generate HTML test reports

## Submission Details
- Platform: Hishabee Web (Dokan Management)
- Automation Tool: Selenium with Python
- Test Cases: 10 (as specified in requirements)
- Submitted via: GitHub Repository

## Contact Information
For any questions regarding this submission, please contact:
- Name: Abir Abhuiyan
- Repository: https://github.com/abirAbhuiyan/hishabee-internship-final-task.git
