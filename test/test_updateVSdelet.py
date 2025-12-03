import allure
import pytest
from playwright.sync_api import expect
from selector.main_page import MainPage
from selector.selectors import *
from selector.links import Links
from selector.data_test_user import *


@allure.feature("Главная страница")
class TestMainPage:
    @allure.title("ADD/REMOVE страница")
    def test_add_remove(self, main_page: MainPage):
        with allure.step("Открываем основную страницу"):
            main_page.navigate()

        with allure.step("Открываем страницу ADD/REMOVE"):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_ADD_REMOVE)
            expect(main_page.page).to_have_url(Links.ADD_REMOVE)

        with allure.step("Добавляем 2 элемента"):
            main_page.page.click(AddRemoveElement.SELECT_ADD_BUTTON)
            main_page.page.click(AddRemoveElement.SELECT_ADD_BUTTON)
            expect(main_page.page.locator(AddRemoveElement.SELECT_REMOVE_BUTTON)).to_have_count(2)

        with allure.step("удаляем 1 элемент"):
            main_page.page.click(AddRemoveElement.SELECT_REMOVE_BUTTON)
            expect(main_page.page.locator(AddRemoveElement.SELECT_REMOVE_BUTTON)).to_have_count(1)

    @allure.title("BROKEN IMAGES страница")
    def test_broken_images(self, main_page: MainPage):
        with allure.step("Открываем основную страницу"):
            main_page.navigate()

        with allure.step("Открываем страницу BROKEN IMAGES"):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_BROKEN_IMAGES)
            expect(main_page.page).to_have_url(Links.BROKEN_IMAGES)

        with allure.step("Видно 3 фотографии"):
            expect(main_page.page.locator(BrokenImagesElement.SELECT_IMAGE_asdf)).to_be_visible()
            expect(main_page.page.locator(BrokenImagesElement.SELECT_IMAGE_hjkl)).to_be_visible()
            expect(main_page.page.locator(BrokenImagesElement.SELECT_IMAGE_avatar_blank)).to_be_visible()

    @allure.title("CHECKBOXES страница")
    def test_checkboxes(self, main_page: MainPage):
        with allure.step("Открываем основную страницу"):
            main_page.navigate()

        with allure.step("Открываем страницу CHECKBOXES"):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_CHECKBOXES)
            expect(main_page.page).to_have_url(Links.CHECKBOXES)

        with allure.step("Первый чекбокс не активированный, второй активированный"):
            expect(main_page.page.locator(CheckboxesElement.SELECT_CHECKBOXES_1)).not_to_be_checked()
            expect(main_page.page.locator(CheckboxesElement.SELECT_CHECKBOXES_2)).to_be_checked()

        with allure.step("Меняет на первый активный, второй не активный"):
            main_page.page.click(CheckboxesElement.SELECT_CHECKBOXES_1)
            main_page.page.click(CheckboxesElement.SELECT_CHECKBOXES_2)
            expect(main_page.page.locator(CheckboxesElement.SELECT_CHECKBOXES_1)).to_be_checked()
            expect(main_page.page.locator(CheckboxesElement.SELECT_CHECKBOXES_2)).not_to_be_checked()

    @allure.title("CONTEXT MENU страница")
    def test_context_menu(self, main_page: MainPage):
        with allure.step("Открываем основную страницу"):
            main_page.navigate()

        with allure.step("Открываем страницу CONTEXT MENU"):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_CONTEXT_MENU)
            expect(main_page.page).to_have_url(Links.CONTEXT_MENU)

        with allure.step("Первый чекбокс не активированный, второй активированный"):
            main_page.page.locator(ContextMenuElement.SELECT_CONTEXT_MENU_BUTTON).click(button="right")

    @allure.title("DRAG AND DROP страница")
    def test_checkboxes(self, main_page: MainPage):
        with allure.step("Открываем основную страницу"):
            main_page.navigate()

        with allure.step("Открываем страницу DRAG AND DROP"):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_DRAG_AND_DROP)
            expect(main_page.page).to_have_url(Links.DRAG_AND_DROP)

        with allure.step("Наличие на странице column-a и column-b"):
            expect(main_page.page.locator(DragAndDropElement.SELECT_DROP_BUTTON_A)).to_be_visible()
            expect(main_page.page.locator(DragAndDropElement.SELECT_DROP_BUTTON_B)).to_be_visible()
            expect(main_page.page.locator(DragAndDropElement.SELECT_DROP_BUTTON_A)).to_have_text('A')
            expect(main_page.page.locator(DragAndDropElement.SELECT_DROP_BUTTON_B)).to_have_text('B')

        with allure.step("Перемещение из A в B"):
            main_page.page.locator(DragAndDropElement.SELECT_DROP_BUTTON_A).drag_to(
                main_page.page.locator(DragAndDropElement.SELECT_DROP_BUTTON_B))

        with allure.step("Проверка изменения положения A и B"):
            expect(main_page.page.locator(DragAndDropElement.SELECT_DROP_BUTTON_A)).to_have_text('B')
            expect(main_page.page.locator(DragAndDropElement.SELECT_DROP_BUTTON_B)).to_have_text('A')

    @allure.title("Dropdown List страница")
    def test_dropdown_list(self, main_page: MainPage):

        select = main_page.page.locator(DropdownListElement.SELECT_DROPDOWN_LIST)

        with allure.step("Открываем основную страницу"):
            main_page.navigate()

        with allure.step("Открываем страницу Dropdown List"):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_DROPDOWN_LIST)
            expect(main_page.page).to_have_url(Links.DROPDOWN_LIST)

        with allure.step("Оба варианта не выбраны"):
            expect(main_page.page.locator(DropdownListElement.SELECT_DROPDOWN_OPTION_1)).not_to_have_attribute('selected', 'selected')
            expect(main_page.page.locator(DropdownListElement.SELECT_DROPDOWN_OPTION_2)).not_to_have_attribute('selected', 'selected')

        with allure.step("Выбор первого варианта"):
            select.select_option('1')

        with allure.step("Проверка что первый элемент выбран, а второй нет"):
            expect(main_page.page.locator(DropdownListElement.SELECT_DROPDOWN_OPTION_1)).to_have_attribute('selected', 'selected')
            expect(main_page.page.locator(DropdownListElement.SELECT_DROPDOWN_OPTION_2)).not_to_have_attribute('selected','selected')

        with allure.step("Выбор второго варианта"):
            select.select_option('2')

        with allure.step("Проверка что второй элемент выбран, а первый нет"):
            expect(main_page.page.locator(DropdownListElement.SELECT_DROPDOWN_OPTION_1)).not_to_have_attribute('selected', 'selected')
            expect(main_page.page.locator(DropdownListElement.SELECT_DROPDOWN_OPTION_2)).to_have_attribute('selected','selected')

    @allure.title("KEY PRESSES страница")
    def test_key_presses(self, main_page: MainPage):
        with allure.step("Открываем основную страницу"):
            main_page.navigate()

        with allure.step("Открываем страницу KEY PRESSES"):
            main_page.page.locator(SelectMainPage.SELECT_MAIN_PAGE_KEY_PRESSES).scroll_into_view_if_needed()
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_KEY_PRESSES)
            expect(main_page.page).to_have_url(Links.KEY_PRESSES)

        with allure.step("Нажатие на Space и проверка что появляется надпись с You entered: SPACE"):
            main_page.page.locator(KeyPressesElement.SELECT_KEY_PRESSES_TARGET).press('Space')
            expect(main_page.page.locator(KeyPressesElement.SELECT_KEY_PRESSES_RESULT)).to_have_text('You entered: SPACE')

        with allure.step("Нажатие на Delete и проверка что появляется надпись с You entered: DELETE"):
            main_page.page.locator(KeyPressesElement.SELECT_KEY_PRESSES_TARGET).press('Delete')
            expect(main_page.page.locator(KeyPressesElement.SELECT_KEY_PRESSES_RESULT)).to_have_text('You entered: DELETE')

    @allure.title("DISAPPEARING ELEMENTS страница")
    def test_disappearing_elements(self, main_page: MainPage):
        with allure.step("Открываем основную страницу"):
            main_page.navigate()

        with allure.step("Открываем страницу DISAPPEARING ELEMENTS"):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_DISAPPEARING_ELEMENTS)
            expect(main_page.page).to_have_url(Links.DISAPPEARING_ELEMENTS)

        with allure.step("Создаём цикл из 8 перезагрузок сайта"):
            error_count = 0

            for _ in range(8):
                element = main_page.page.locator(DisappearElement.SELECT_DISAPPEARING_MISSING_ELEMENTS).count()
                if element > 0:
                    with allure.step("Элемент появился"):
                        expect(element).to_be_visible()
                    error_count += 1
                    break
                main_page.page.reload()

            if error_count <= 0:
                with allure.step("Элемент не появился"):
                    expect(main_page.page.locator(DisappearElement.SELECT_DISAPPEARING_MISSING_ELEMENTS)).to_have_count(0)

    @allure.title("DYNAMIC CONTENT страница")
    def test_dynamic_content(self, main_page: MainPage):
        with allure.step("Открываем основную страницу"):
            main_page.navigate()

        with allure.step("Открываем страницу DYNAMIC CONTENT"):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_DYNAMIC_CONTENT)
            expect(main_page.page).to_have_url(Links.DYNAMIC_CONTENT)

        with allure.step("Записываем актуальное значение"):
            old_value = main_page.page.locator(DynamicContentElement.SELECT_DYNAMIC_CONTENT_TEXT).nth(2).text_content()

        with allure.step("Перезагружаем страницу"):
            main_page.page.reload()

        with allure.step("Записываем новое значение и сравниваем со старым"):
            next_value = main_page.page.locator(DynamicContentElement.SELECT_DYNAMIC_CONTENT_TEXT).nth(2).text_content()
            assert old_value != next_value, {f"Ранее текст был {old_value}, а сейчас {next_value}"}

    @allure.title("DYNAMIC LOADING страница")
    def test_dynamic_loading(self, main_page: MainPage):
        with allure.step("Открываем основную страницу"):
            main_page.navigate()

        with allure.step("Открываем страницу DYNAMIC LOADING"):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_DYNAMIC_LOADING)
            expect(main_page.page).to_have_url(Links.DYNAMIC_LOADING)

        with allure.step("Открываем страницу DYNAMIC LOADING 2"):
            main_page.page.click(DynamicLoadingElement.SELECT_DYNAMIC_LOADING_LINK_PAGE_2)
            expect(main_page.page).to_have_url(Links.DYNAMIC_LOADING_2)

        with allure.step("Запускаем динамическую загрузку"):
            main_page.page.locator(DynamicLoadingElement.SELECT_DYNAMIC_LOADING_BUTTON_START).click()

        with allure.step("Ждем завершения загрузки"):
            main_page.page.locator(DynamicLoadingElement.SELECT_DYNAMIC_LOADING_BUTTON_FINISH).wait_for(state="visible", timeout=15000)

        with allure.step("Проверяем результат"):
            result_text = main_page.page.locator(DynamicLoadingElement.SELECT_DYNAMIC_LOADING_BUTTON_FINISH).text_content()
            assert result_text == "Hello World!", {f"Ожидался текст Hello World!, был получен {result_text}"}

    @allure.title("DYNAMIC LOADING страница")
    def test_dynamic_loading(self, main_page: MainPage):
        with allure.step("Открываем основную страницу"):
            main_page.navigate()

        with allure.step("Открываем страницу DYNAMIC LOADING"):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_ENTRY_AD)
            expect(main_page.page).to_have_url(Links.ENTRY_AD)

        with allure.step("Проверка видимости модального окна"):
            expect(main_page.page.locator(EntryAdElement.SELECT_ENTRY_AD_MODAL_WINDOW_TITLE)).to_be_visible()

        with allure.step("Закрытие модального окна"):
            main_page.page.locator(EntryAdElement.SELECT_ENTRY_AD_MODAL_WINDOW_BUTTON_CLOSE).click()

        with allure.step("Нажатие на кнопку отключения модального окна"):
            main_page.page.locator(EntryAdElement.SELECT_ENTRY_AD_WINDOW_BAN).click()

        with allure.step("Перезагрузка страницы"):
            main_page.page.reload()

        with allure.step("Проверка отсутствия модального окна"):
            expect(main_page.page.locator(EntryAdElement.SELECT_ENTRY_AD_MODAL_WINDOW_TITLE)).not_to_be_visible()

    @allure.step('FRAMES NESTED страница')
    def test_frame_loading(self, main_page: MainPage):
        with allure.step('Открываем основную страницу'):
            main_page.navigate()

        with allure.step('Открываем страницу FRAMES'):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_FRAMES)
            expect(main_page.page).to_have_url(Links.FRAMES)

        with allure.step('Открываем страницу FRAMES NESTED'):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_FRAMES_NESTED)
            expect(main_page.page).to_have_url(Links.FRAMES_NESTED)

        with allure.step('Определяемся переменную для работы с top frame'):
            frame_locator_top = main_page.page.frame_locator(NestedFramesElement.SELECT_FRAME_TOP)

        with allure.step('Определяемся переменную для работы с left frame'):
            frame_locator_left = frame_locator_top.frame_locator(NestedFramesElement.SELECT_FRAME_LEFT)

        with allure.step('Находим тестк заголовка frame и сравниваем его с ранее заданным'):
            text_left_frame = frame_locator_left.locator(NestedFramesElement.SELECT_FRAME_LEFT_HEADING).text_content().strip()
            assert text_left_frame == "LEFT", f"Ожидался текст LEFT, был получен {text_left_frame}"

    @allure.step('FROM AUTH страница авторизация с неверным логином')
    def test_from_auth_invalid_login(self, main_page: MainPage):
        with allure.step('Открываем основную страницу'):
            main_page.navigate()

        with allure.step('Открываем страницу FROM AUTH'):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_FROM_AUTH)
            expect(main_page.page).to_have_url(Links.FROM_AUTH)

        with allure.step('Открываем страницу FRAMES NESTED'):
            main_page.page.locator(FromAuthElement.SELECT_FROM_AUTH_INPUT_USERNAME).fill(InvalidLoginDateUser.USER_LOGIN)
            main_page.page.locator(FromAuthElement.SELECT_FROM_AUTH_INPUT_PASSWORD).fill(InvalidLoginDateUser.USER_PASSWORD)
            main_page.page.click(FromAuthElement.SELECT_FROM_AUTH_BUTTON)

        with allure.step('Отображение сообщения об ошибке'):
            mess = main_page.page.locator(FromAuthElement.SELECT_FROM_AUTH_ERROR_MESS).text_content().strip().split('\n')[0].strip()
            assert mess == 'Your username is invalid!', f"Ожидался текст Your username is invalid!, был получен {mess}"

    @allure.step('FROM AUTH страница авторизация с неверным паролем')
    def test_from_auth_invalid_pass(self, main_page: MainPage):
        with allure.step('Открываем основную страницу'):
            main_page.navigate()

        with allure.step('Открываем страницу FROM AUTH'):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_FROM_AUTH)
            expect(main_page.page).to_have_url(Links.FROM_AUTH)

        with allure.step('Открываем страницу FRAMES NESTED'):
            main_page.page.locator(FromAuthElement.SELECT_FROM_AUTH_INPUT_USERNAME).fill(InvalidPassDateUser.USER_LOGIN)
            main_page.page.locator(FromAuthElement.SELECT_FROM_AUTH_INPUT_PASSWORD).fill(InvalidPassDateUser.USER_PASSWORD)
            main_page.page.click(FromAuthElement.SELECT_FROM_AUTH_BUTTON)

        with allure.step('Отображение сообщения об ошибке'):
            mess = main_page.page.locator(FromAuthElement.SELECT_FROM_AUTH_ERROR_MESS).text_content().strip().split('\n')[0].strip()
            assert mess == 'Your password is invalid!', f"Ожидался текст Your password is invalid!, был получен {mess}"

    @allure.step('FROM AUTH страница с верными данными')
    def test_from_auth_valid(self, main_page: MainPage):
        with allure.step('Открываем основную страницу'):
            main_page.navigate()

        with allure.step('Открываем страницу FROM AUTH'):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_FROM_AUTH)
            expect(main_page.page).to_have_url(Links.FROM_AUTH)

        with allure.step('Открываем страницу FRAMES NESTED'):
            main_page.page.locator(FromAuthElement.SELECT_FROM_AUTH_INPUT_USERNAME).fill(ValidDateUser.USER_LOGIN)
            main_page.page.locator(FromAuthElement.SELECT_FROM_AUTH_INPUT_PASSWORD).fill(ValidDateUser.USER_PASSWORD)
            main_page.page.click(FromAuthElement.SELECT_FROM_AUTH_BUTTON)

        with allure.step('Отображение сообщения об успешной авторизации'):
            mess = main_page.page.locator(FromAuthElement.SELECT_FROM_AUTH_ERROR_MESS).text_content().strip().split('\n')[0].strip()
            assert mess == 'You logged into a secure area!', f"Ожидался текст You logged into a secure area!, был получен {mess}"

    @allure.step('JS ALERTS страница')
    def test_js_alert(self, main_page: MainPage):
        with allure.step('Открываем основную страницу'):
            main_page.navigate()

        with allure.step('Открываем страницу JS ALERTS'):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_JS_ALERTS)
            expect(main_page.page).to_have_url(Links.JS_ALERT)

        with allure.step('Открывает Alert и нажатие на закрытие Alert'):
            main_page.page.click(JsAlertsElement.SELECT_JS_BUTTON_ALERT)
            main_page.page.once("dialog", lambda dialog: dialog.dismiss())  # Cancel
            main_page.page.click(JsAlertsElement.SELECT_JS_BUTTON_ALERT_CLOSE)

        with allure.step('Получаем результирующие сообщение и сравниваем'):
            result_mess = main_page.page.locator(JsAlertsElement.SELECT_JS_RESULT).text_content()
            assert result_mess == 'You successfully clicked an alert', f"Ожидался текст You successfully clicked an alert, был получен {result_mess}"

    @allure.step('JS CONFIRM страница')
    def test_js_confirm_ok(self, main_page: MainPage):
        with allure.step('Открываем основную страницу'):
            main_page.navigate()

        with allure.step('Открываем страницу JS ALERTS'):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_JS_ALERTS)
            expect(main_page.page).to_have_url(Links.JS_ALERT)

        with allure.step('Открывает Confirm и нажатие на Ok Confirm'):
            main_page.page.click(JsAlertsElement.SELECT_JS_BUTTON_CONFIRM)
            main_page.page.once("dialog", lambda dialog: dialog.accept())
            main_page.page.click(JsAlertsElement.SELECT_JS_BUTTON_CONFIRM_OK)

        with allure.step('Получаем результирующие сообщение и сравниваем'):
            result_mess = main_page.page.locator(JsAlertsElement.SELECT_JS_RESULT).text_content()
            assert result_mess == 'You clicked: Ok', f"Ожидался текст You clicked: Ok, был получен {result_mess}"

    @allure.step('JS CONFIRM страница')
    def test_js_confirm_cansel(self, main_page: MainPage):
        with allure.step('Открываем основную страницу'):
            main_page.navigate()

        with allure.step('Открываем страницу JS ALERTS'):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_JS_ALERTS)
            expect(main_page.page).to_have_url(Links.JS_ALERT)

        with allure.step('Открывает Confirm и нажатие на Cancel Confirm'):
            main_page.page.click(JsAlertsElement.SELECT_JS_BUTTON_CONFIRM)
            main_page.page.once("dialog", lambda dialog: dialog.dismiss())
            main_page.page.click(JsAlertsElement.SELECT_JS_BUTTON_CONFIRM_OK)

        with allure.step('Получаем результирующие сообщение и сравниваем'):
            result_mess = main_page.page.locator(JsAlertsElement.SELECT_JS_RESULT).text_content()
            assert result_mess == 'You clicked: Cancel', f"Ожидался текст You clicked: Cancel, был получен {result_mess}"

    @allure.step('JS PROMPT страница')
    def test_js_prompt_ok(self, main_page: MainPage):
        with allure.step('Открываем основную страницу'):
            main_page.navigate()

        with allure.step('Открываем страницу JS PROMPT'):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_JS_ALERTS)
            expect(main_page.page).to_have_url(Links.JS_ALERT)

        with allure.step('Открывает Confirm и нажатие на OK Confirm'):
            main_page.page.click(JsAlertsElement.SELECT_JS_BUTTON_PROMPT)
            main_page.page.once("dialog", lambda dialog: dialog.accept("Привет тому, кто читает мой код)"))
            main_page.page.click(JsAlertsElement.SELECT_JS_BUTTON_PROMPT_OK)

        with allure.step('Получаем результирующие сообщение и сравниваем'):
            result_mess = main_page.page.locator(JsAlertsElement.SELECT_JS_RESULT).text_content()
            assert result_mess == 'You entered: Привет тому, кто читает мой код)', f"Ожидался текст You entered: Привет тому, кто читает мой код), был получен {result_mess}"

    @allure.step('JS PROMPT страница')
    def test_js_prompt_cansel(self, main_page: MainPage):
        with allure.step('Открываем основную страницу'):
            main_page.navigate()

        with allure.step('Открываем страницу JS PROMPT'):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_JS_ALERTS)
            expect(main_page.page).to_have_url(Links.JS_ALERT)

        with allure.step('Открывает Confirm и нажатие на Cancel Confirm'):
            main_page.page.click(JsAlertsElement.SELECT_JS_BUTTON_PROMPT)
            main_page.page.once("dialog", lambda dialog: dialog.dismiss())
            main_page.page.click(JsAlertsElement.SELECT_JS_BUTTON_PROMPT_OK)

        with allure.step('Получаем результирующие сообщение и сравниваем'):
            result_mess = main_page.page.locator(JsAlertsElement.SELECT_JS_RESULT).text_content()
            assert result_mess == 'You entered: null', f"Ожидался текст You entered: null, был получен {result_mess}"

    @allure.step('NEW WINDOW страница')
    def test_new_window(self, main_page: MainPage):
        with allure.step('Открываем основную страницу'):
            main_page.navigate()

        with allure.step('Открываем страницу JS PROMPT'):
            main_page.page.locator(SelectMainPage.SELECT_MAIN_PAGE_MILTIPLE_WINDOWS).scroll_into_view_if_needed()
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_MILTIPLE_WINDOWS)
            expect(main_page.page).to_have_url(Links.MILTIPLE_WINDOWS)

        with allure.step('Открываем основную страницу'):
            with main_page.page.expect_popup() as new_window:
                main_page.page.click(MiltipleWindowsElement.SELECT_MILTIPLE_WINDOW_BUTTON)
            new_page = new_window.value

        with allure.step('Открываем основную страницу'):
            expect(new_page.locator(NewWindowsElement.SELECT_NEW_WINDOW_TITLE)).to_be_visible()

    @allure.step('STATUS CODES страница')
    @pytest.mark.parametrize("status_code", [200, 301, 404, 500])
    def test_status_codes_with_http_check(self, main_page: MainPage, status_code):
        with allure.step('Открываем основную страницу'):
            main_page.navigate()

        with allure.step('Открываем страницу STATUS CODES'):
            main_page.page.click(SelectMainPage.SELECT_MAIN_PAGE_STATUS_CODES)

        with allure.step('Переход на страницу с возвратным кодом'):
            with main_page.page.expect_response(lambda r: str(status_code) in r.url) as response_info:
                main_page.page.click(f"a[href*='{status_code}']")

        with allure.step('Проверяем HTTP статус'):
            response = response_info.value
            assert response.status == status_code, f"Ожидался код {status_code}, был получен {response.status}"

        with allure.step('Возврат на страницу со всем статус кодами'):
            main_page.page.click(StatusCodesElement.SELECT_STATUS_CODES_BACK)
            expect(main_page.page).to_have_url(Links.STATUS_CODES_MAIN)

    @pytest.mark.parametrize("username, password, status_auth", [
    ("admin", "admin", True),
    ("admin", "wrong", False),
    ("wrong", "admin", False),
    ("", "", False)])
    @allure.step('BASIC AUTH страница')
    def test_all_basic_auth(self, username, password, status_auth, main_page,make_auth_page):
        with allure.step('Создание контекста с тестовыми данными'):
            auth_page, context = make_auth_page(username, password)

        with allure.step('Переход на страницу авторизации'):
            auth_page.goto(Links.BASIC_AUTH)

        with allure.step('Проверка видимости элементов или их отсутствия'):
            if status_auth:
                expect(auth_page.locator('#content')).to_be_visible()
            else:
                body = auth_page.locator("body").text_content()
                assert "Congratulations" not in body
        context.close()