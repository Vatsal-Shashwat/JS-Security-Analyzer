<h1 align="center">JavaScript Sensitive Information Finder 🕵️‍♂️</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</p>

<p align="center">Discover and secure sensitive data in JavaScript files</p>

---

## Features

🔍 **Automated Analysis**: Quickly scan JavaScript files for potential sensitive data.

⚙️ **Customizable Patterns**: Configure detection patterns to match specific types of information.

📝 **Detailed Reporting**: Get comprehensive reports with identified sensitive information.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/js-sensitive-information-finder.git

   cd js-sensitive-information-finder

   pip install -r requirements.txt
   
 ## Usage

1. **Add sample JavaScript files:** Add your JavaScript files containing potential sensitive information to the `sample_files` directory.

2. **Run the script:**
   ```sh
   python find_sensitive_info.py

<details>
<summary>Click to expand</summary>
Scanning file: sample_files/file1.js
Sensitive information found:
API keys: YOUR_API_KEY
Credentials: admin:password123
Sensitive URLs: https://api.example.com

Scanning file: sample_files/file2.js
Sensitive information found:
API keys: YOUR_ACCESS_TOKEN
Sensitive URLs: https://example.com/login
</details>
