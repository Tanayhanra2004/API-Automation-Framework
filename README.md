API Automation Framework (Python + Pytest)

 Features
- REST API Testing (CRUD)
- Data Driven Testing (JSON)
- Schema Validation
- Modular Framework Design
- Pytest Fixtures

 Tech Stack
- Python
- Pytest
- Requests
- JSONSchema

Run Tests
```bash

pytest
api-automation-framework/
│
├── tests/                # Test cases
├── data/                 # Test data (JSON/CSV)
├── utils/                # Helper functions
├── clients/              # API request layer
├── schemas/              # JSON schema validation
├── config/               # Base URLs, env configs
├── conftest.py           # pytest fixtures
├── requirements.txt
└── pytest.ini
