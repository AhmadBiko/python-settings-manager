# Python Settings Manager ⚙️

A lightweight Python script to manage user configuration preferences using dictionaries and list comprehensions. 

## 🛠️ Technologies Used
* **Python 3:** Handles the core logic, string manipulation, and list comprehensions.
* **Data Structures:** Utilizes dictionaries for efficient key-value storage and tuples for structured data passing.

## 🗂️ Project Structure
* **`settings_manager.py`**: The main executable script containing all the functions to add, update, delete, and view settings, along with built-in test cases.

## 📊 Core Features
The script manages the dictionary through four primary operations:
* **`add_setting()`**: Validates inputs (verifying dictionary and tuple types) and inserts new unique configurations.
* **`update_setting()`**: Modifies existing setting values securely while checking for existing keys.
* **`delete_setting()`**: Safely removes a specific configuration key using the `.pop()` method.
* **`view_settings()`**: Iterates through the dictionary to display all current user settings in a clean, line-by-line capitalized text format.

## 🚀 How to Run
1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/ahmadbiko/python-settings-manager.git](https://github.com/ahmadbiko/python-settings-manager.git)
