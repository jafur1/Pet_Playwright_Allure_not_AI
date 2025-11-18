import allure
from playwright.sync_api import expect
from selector.main_page import MainPage
from selector.selectors import *
from selector.links import Links


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


