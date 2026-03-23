import pytest
from playwright.sync_api import Page
import os
from pytest_html import extras

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get('page')
        if isinstance(page, Page):
            os.makedirs('screenshots', exist_ok=True)
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)

            if not hasattr(report, 'extras'):
                report.extras = []
            report.extras.append(extras.image(screenshot_path))