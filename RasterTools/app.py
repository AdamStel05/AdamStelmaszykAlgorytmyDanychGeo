from src.create_window import create_window
from src.create_menu_option import create_menu_option
from src.update_menu import update_menu
from src.menu_operations.close_program import close_program

window, canvas = create_window()

create_menu_option(canvas, 450, "Wyjdź", lambda: close_program(window))

window.mainloop()