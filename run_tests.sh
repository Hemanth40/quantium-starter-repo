#!/bin/bash

# Activate the virtual environment
source venv/Scripts/activate

# Run the test suite
pytest test_app.py

# Capture the exit code of pytest
EXIT_CODE=$?

# Return 0 if all tests passed, 1 if something went wrong
if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed!"
    exit 1
fi
```

**Step 3 - Save and close, then commit and push:**
```
git add .
git commit -m "Added CI bash script to run test suite"
git push origin main
```

---

**Explanation of the script:**

- `source venv/Scripts/activate` — activates your virtual environment
- `pytest test_app.py` — runs your 3 tests
- `EXIT_CODE=$?` — captures whether pytest passed or failed (`0` = success, anything else = failure)
- `exit 0` — tells the CI engine everything is fine
- `exit 1` — tells the CI engine something went wrong