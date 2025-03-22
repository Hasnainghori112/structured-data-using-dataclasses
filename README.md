# 👤 Person Data Management

A Python project demonstrating the use of **dataclasses** for managing structured data, including addresses, contacts, and skills.

## 🚀 Features
- **Nested Dataclasses**: Address and Contact information are stored within the `Person` class.
- **JSON Serialization**: Convert objects into a readable JSON format.
- **Skill Management**: Add new skills dynamically to a person.
- **Default Values**: Provides default country for address and optional phone number for contact.

## 🏗️ Technologies Used
- **Python** 🐍
- **Dataclasses**
- **JSON Serialization**

## 📌 How to Use
1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```
2. **Run the script**
   ```bash
   python script.py
   ```

## 🛠️ Code Overview
### Example JSON Output
```json
{
  "name": "Hasnain",
  "age": 18,
  "adress": {
    "street": "123 main st",
    "city": "Karachi",
    "state": "Sindh",
    "zip_code": "00332",
    "country": "Pakistan"
  },
  "contact": {
    "email": "hasnain@gmail.com",
    "phone": "03022299-1"
  },
  "skills": ["python", "crewai", "fastapi"]
}
```

## 📜 Functions
- `hasnain()`: Creates and prints a `Person` instance for Hasnain.
- `ahmed()`: Creates a `Person` instance for Ahmed and adds an extra skill.
