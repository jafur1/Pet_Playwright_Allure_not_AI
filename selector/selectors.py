class SelectMainPage:
    SELECT_MAIN_PAGE_ADD_REMOVE = 'a[href="/add_remove_elements/"]'
    SELECT_MAIN_PAGE_BROKEN_IMAGES = 'a[href="/broken_images"]'
    SELECT_MAIN_PAGE_CHECKBOXES = 'a[href="/checkboxes"]'
    SELECT_MAIN_PAGE_CONTEXT_MENU = 'a[href="/context_menu"]'
    SELECT_MAIN_PAGE_DRAG_AND_DROP = 'a[href="/drag_and_drop"]'
    SELECT_MAIN_PAGE_DROPDOWN_LIST = 'a[href="/dropdown"]'
    SELECT_MAIN_PAGE_KEY_PRESSES = 'a[href="/key_presses"]'

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