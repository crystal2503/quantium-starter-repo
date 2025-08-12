# Activate the virtual environment
& .\venv\Scripts\Activate.ps1

# Run the tests
pytest test.py
$TEST_RESULT = $LASTEXITCODE

# Deactivate the virtual environment
deactivate

# Exit with code 0 if tests passed, 1 otherwise
if ($TEST_RESULT -eq 0) {
    exit 0
} else {
    exit 1
}
