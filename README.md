# Mock Framework

## Allure test reports

`pytest.ini` configures pytest to clear and write test results to `allure-results`
on each run. The project includes the official Allure Commandline 2.46.1 archive
at `tools/allure-2.46.1.zip` (SHA-256:
`d25c519bbde940dc953cff8901130ce18b73013dc19a8f8b90b8b4b1c5eb252f`). The
extracted CLI directory is ignored by Git.

On Windows, extract the CLI and generate/open the report with:

```powershell
Expand-Archive .\tools\allure-2.46.1.zip -DestinationPath .\tools -Force
python -m pytest
.\tools\allure-2.46.1\bin\allure.bat generate .\allure-results --clean -o .\allure-report
.\tools\allure-2.46.1\bin\allure.bat open .\allure-report
```

Allure Commandline requires Java. The GitHub Actions workflow sets up Java 17,
runs the tests, generates the report, and uploads both the results and report as
workflow artifacts.
