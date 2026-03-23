import time

import pytest
from playwright.sync_api import sync_playwright, expect
@pytest.mark.smoke
def test_first(page):
    page.goto('https://demoqa.com/automation-practice-form')

    name = page.get_by_role('textbox', name='First Name')
    name.fill('QA')
    email = page.get_by_role('textbox', name='name@example.com')
    email.fill('text@text.ru')
    gender = page.locator("//input[@id = 'gender-radio-1']")
    gender.check()
    mobile = page.get_by_role('textbox', name='Mobile Number')
    mobile.fill('79999999999')
    last_name = page.get_by_role('textbox', name='Last Name')
    last_name.fill('QA2')
    button = page.get_by_role('button', name='Submit')
    button.click()
    text_succsess = page.locator('//div[@class="modal-title h4"]')
    expect(text_succsess).to_be_visible()
    expect(text_succsess).to_have_text('Thanks for submitting the form')
    modal = page.locator('//div[@class="modal-body"]')
    expect(modal).to_be_visible()
    close = page.get_by_role('button', name = 'Close')
    expect(close).to_be_visible()
    expect(close).to_have_text('Close')
    close.click()
