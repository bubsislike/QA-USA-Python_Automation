import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:
    # Route inputs and taxi call button
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    CALL_TAXI_BUTTON = (By.XPATH, '//button[text()="Call a taxi"]')

    # Supportive plan
    SUPPORTIVE_PLAN_CARD = (By.XPATH, '//div[text()="Supportive"]/ancestor::div[contains(@class, "tcard")]')
    SUPPORTIVE_PLAN_CARD_TITLE = (By.XPATH, '//div[text()="Supportive"]')

    # Phone number flow
    PHONE_BUTTON = (By.CLASS_NAME, 'np-button')
    PHONE_INPUT = (By.ID, 'phone')
    SUBMIT_PHONE_BUTTON = (By.XPATH, '//button[text()="Next"]')
    SMS_CODE_INPUT = (By.ID, 'code')
    CONFIRM_SMS_BUTTON = (By.XPATH, '//button[text()="Confirm"]')
    PHONE_FIELD_VALUE = (By.CLASS_NAME, 'np-text')

    # Payment and card flow
    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, 'pp-button')
    ADD_CARD_ROW = (By.XPATH, '//div[text()="Add card"]')
    CARD_NUMBER_INPUT = (By.ID, 'number')
    CARD_CODE_INPUT = (By.XPATH, '//div[@class="card-code-input"]//input[@id="code"]')
    CARD_MODAL_TITLE = (By.CLASS_NAME, 'card-wrapper')
    LINK_CARD_BUTTON = (By.XPATH, '//button[text()="Link"]')
    CLOSE_PAYMENT_MODAL_BUTTON = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    PAYMENT_METHOD_VALUE = (By.CLASS_NAME, 'pp-value-text')

    # Driver message
    COMMENT_INPUT = (By.ID, 'comment')

    # Blanket and handkerchiefs switch
    BLANKET_SWITCH_CLICK = (By.XPATH, '//div[text()="Blanket and handkerchiefs"]/following-sibling::div//span[contains(@class, "slider")]')
    BLANKET_INPUT_CHECK = (By.XPATH, '//div[text()="Blanket and handkerchiefs"]/..//input')

    # Ice cream counter
    ICE_CREAM_PLUS_BUTTON = (By.XPATH, '//div[text()="Ice cream"]/following-sibling::div//div[contains(@class, "counter-plus")]')
    ICE_CREAM_VALUE = (By.XPATH, '//div[text()="Ice cream"]/following-sibling::div//div[contains(@class, "counter-value")]')

    # Final order button and search modal
    SMART_ORDER_BUTTON = (By.CLASS_NAME, 'smart-button-main')
    ORDER_MODAL = (By.CLASS_NAME, 'order-body')

    def __init__(self, driver):
        self.driver = driver

    # Address Methods
    def set_from_address(self, address_from):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FROM_FIELD))
        field.clear()
        field.send_keys(address_from)

    def set_to_address(self, address_to):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.TO_FIELD))
        field.clear()
        field.send_keys(address_to)

    def click_call_taxi(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CALL_TAXI_BUTTON)).click()

    def set_route(self, address_from, address_to):
        self.set_from_address(address_from)
        self.set_to_address(address_to)
        self.click_call_taxi()

    def get_from_value(self):
        return self.driver.find_element(*self.FROM_FIELD).get_property('value')

    def get_to_value(self):
        return self.driver.find_element(*self.TO_FIELD).get_property('value')

    # Tariff Methods
    def select_supportive_plan(self):
        card = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SUPPORTIVE_PLAN_CARD))
        if 'active' not in card.get_attribute('class'):
            self.driver.find_element(*self.SUPPORTIVE_PLAN_CARD_TITLE).click()

    def is_supportive_plan_selected(self):
        card = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SUPPORTIVE_PLAN_CARD))
        return 'active' in card.get_attribute('class')

    # Phone Methods
    def open_phone_modal(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PHONE_BUTTON)).click()

    def enter_phone_number(self, phone):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PHONE_INPUT))
        field.clear()
        field.send_keys(phone)

    def submit_phone(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SUBMIT_PHONE_BUTTON)).click()

    def enter_sms_code(self, code):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SMS_CODE_INPUT))
        field.clear()
        field.send_keys(code)

    def confirm_sms(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CONFIRM_SMS_BUTTON)).click()

    def get_phone_value(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PHONE_FIELD_VALUE)).text

    # Payment Methods
    def open_payment_modal(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PAYMENT_METHOD_BUTTON)).click()

    def click_add_card(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADD_CARD_ROW)).click()

    def enter_card_number(self, card_number):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CARD_NUMBER_INPUT))
        field.clear()
        field.send_keys(card_number)

    def enter_card_code(self, card_code):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CARD_CODE_INPUT))
        field.clear()
        field.send_keys(card_code)
        field.send_keys(Keys.TAB)

    def click_link_card(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LINK_CARD_BUTTON)).click()

    def close_payment_modal(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CLOSE_PAYMENT_MODAL_BUTTON)).click()

    def get_payment_method_text(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PAYMENT_METHOD_VALUE)).text

    # Driver Comment Methods
    def set_driver_comment(self, comment):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.COMMENT_INPUT))
        field.clear()
        field.send_keys(comment)

    def get_driver_comment_value(self):
        return self.driver.find_element(*self.COMMENT_INPUT).get_property('value')

    # Blanket and Handkerchief Methods
    def click_blanket_switch(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BLANKET_SWITCH_CLICK)).click()

    def is_blanket_switch_selected(self):
        input_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.BLANKET_INPUT_CHECK))
        return input_element.is_selected() or input_element.get_property('checked') is True

    # Ice Cream Counter Methods
    def order_ice_creams(self, count=2):
        plus_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ICE_CREAM_PLUS_BUTTON))
        for _ in range(count):
            plus_btn.click()
            time.sleep(0.5)

    def get_ice_cream_count(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ICE_CREAM_VALUE)).text

    # Order Modal Methods
    def click_order_taxi(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SMART_ORDER_BUTTON)).click()

    def is_order_modal_displayed(self):
        modal = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ORDER_MODAL))
        return modal.is_displayed()