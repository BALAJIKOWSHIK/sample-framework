import pytest
import allure
from pathlib import Path
from playwright.sync_api import Page, BrowserContext
from pages.login_page import LoginPage

# Start tracing per test
@pytest.fixture(autouse=True)
def trace_context(context: BrowserContext, request: pytest.Item):
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield
    # If the test failed, save the trace file and attach to Allure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        trace_path = Path("test-results") / f"{request.node.name}_trace.zip"
        trace_path.parent.mkdir(parents=True, exist_ok=True)
        context.tracing.stop(path=str(trace_path))
        allure.attach.file(str(trace_path), name="Playwright Trace", extension="zip")
    else:
        context.tracing.stop()

# Capture test status for fixtures
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login_pg = LoginPage(page)
    login_pg.navigate()
    return login_pg