class SelectMainPage:
    SELECT_MAIN_PAGE_ADD_REMOVE = 'a[href="/add_remove_elements/"]'
    SELECT_MAIN_PAGE_BROKEN_IMAGES = 'a[href="/broken_images"]'
    SELECT_MAIN_PAGE_CHECKBOXES = 'a[href="/checkboxes"]'
    SELECT_MAIN_PAGE_CONTEXT_MENU = 'a[href="/context_menu"]'
    SELECT_MAIN_PAGE_DRAG_AND_DROP = 'a[href="/drag_and_drop"]'
    SELECT_MAIN_PAGE_DROPDOWN_LIST = 'a[href="/dropdown"]'
    SELECT_MAIN_PAGE_KEY_PRESSES = 'a[href="/key_presses"]'
    SELECT_MAIN_PAGE_DISAPPEARING_ELEMENTS = 'a[href="/disappearing_elements"]'
    SELECT_MAIN_PAGE_DYNAMIC_CONTENT = 'a[href="/dynamic_content"]'
    SELECT_MAIN_PAGE_DYNAMIC_LOADING = 'a[href="/dynamic_loading"]'
    SELECT_MAIN_PAGE_ENTRY_AD = 'a[href="/entry_ad"]'
    SELECT_MAIN_PAGE_EXIT_INTENT = 'a[href="/exit_intent"]'
    SELECT_MAIN_PAGE_FRAMES = 'a[href="/frames"]'
    SELECT_MAIN_PAGE_FRAMES_NESTED = 'a[href="/nested_frames"]'
    SELECT_MAIN_PAGE_FROM_AUTH = 'a[href="/login"]'
    SELECT_MAIN_PAGE_JS_ALERTS = 'a[href="/javascript_alerts"]'
    SELECT_MAIN_PAGE_MILTIPLE_WINDOWS = 'a[href="/windows"]'
    SELECT_MAIN_PAGE_STATUS_CODES = 'a[href="/status_codes"]'

class AddRemoveElement:
    SELECT_ADD_BUTTON = 'button[onclick="addElement()"]'
    SELECT_REMOVE_BUTTON = 'button.added-manually[onclick="deleteElement()"]'

class BrokenImagesElement:
    SELECT_IMAGE_asdf = 'img[src="asdf.jpg"]'
    SELECT_IMAGE_hjkl = 'img[src="hjkl.jpg"]'
    SELECT_IMAGE_avatar_blank = 'img[src="img/avatar-blank.jpg"]'

class CheckboxesElement:
    SELECT_CHECKBOXES_1 = 'input[type="checkbox"] >> nth=0'
    SELECT_CHECKBOXES_2 = 'input[type="checkbox"] >> nth=1'

class ContextMenuElement:
    SELECT_CONTEXT_MENU_BUTTON = '#hot-spot'

class DragAndDropElement:
    SELECT_DROP_BUTTON_A = '#column-a'
    SELECT_DROP_BUTTON_B = '#column-b'

class DropdownListElement:
    SELECT_DROPDOWN_LIST = '#dropdown'
    SELECT_DROPDOWN_OPTION_1 = 'option[value="1"]'
    SELECT_DROPDOWN_OPTION_2 = 'option[value="2"]'

class KeyPressesElement:
    SELECT_KEY_PRESSES_TARGET = '#target'
    SELECT_KEY_PRESSES_RESULT = '#result'

class DisappearElement:
    SELECT_DISAPPEARING_MISSING_ELEMENTS = 'a[href="/gallery"]'

class DynamicContentElement:
    SELECT_DYNAMIC_CONTENT_TEXT = 'div[class="large-10 columns"]'

class DynamicLoadingElement:
    SELECT_DYNAMIC_LOADING_LINK_PAGE_2 = 'a[href="/dynamic_loading/2"]'
    SELECT_DYNAMIC_LOADING_BUTTON_START = "button"
    SELECT_DYNAMIC_LOADING_BUTTON_LOADING = '#loading'
    SELECT_DYNAMIC_LOADING_BUTTON_FINISH = "#finish"

class EntryAdElement:
    SELECT_ENTRY_AD_MODAL_WINDOW_TITLE = '.modal-title'
    SELECT_ENTRY_AD_MODAL_WINDOW_BUTTON_CLOSE = '.modal-footer >> text=Close'
    SELECT_ENTRY_AD_WINDOW_BAN = '#restart-ad'

class NestedFramesElement:
    SELECT_FRAME_TOP = 'frame[name="frame-top"]'
    SELECT_FRAME_LEFT = 'frame[src="/frame_left"]'
    SELECT_FRAME_MIDDLE = '#target'
    SELECT_FRAME_RIGHT = '#target'
    SELECT_FRAME_LEFT_HEADING = "text=LEFT"

class FromAuthElement:
    SELECT_FROM_AUTH_BUTTON = 'button[class="radius"]'
    SELECT_FROM_AUTH_INPUT_USERNAME = '#username'
    SELECT_FROM_AUTH_INPUT_PASSWORD = '#password'
    SELECT_FROM_AUTH_ERROR_MESS = '#flash-messages'

class JsAlertsElement:
    SELECT_JS_BUTTON_ALERT = 'button[onclick="jsAlert()"]'
    SELECT_JS_BUTTON_CONFIRM = 'button[onclick="jsConfirm()"]'
    SELECT_JS_BUTTON_PROMPT = 'button[onclick="jsPrompt()"]'
    SELECT_JS_RESULT = '#result'
    SELECT_JS_BUTTON_ALERT_CLOSE = "button:has-text('Click for JS Alert')"
    SELECT_JS_BUTTON_CONFIRM_OK = "button:has-text('Click for JS Confirm')"
    SELECT_JS_BUTTON_PROMPT_OK = "button:has-text('Click for JS Prompt')"

class MiltipleWindowsElement:
    SELECT_MILTIPLE_WINDOW_BUTTON = 'a[href="/windows/new"]'

class NewWindowsElement:
    SELECT_NEW_WINDOW_TITLE = 'div[class="example"]'

class StatusCodesElement:
    SELECT_STATUS_CODES_BACK = 'a[href="/status_codes"]'

