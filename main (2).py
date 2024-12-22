import colorama
help(colorama)
#Бібліотека Colorama у Python використовується для роботи з кольорами та стилями тексту в терміналі.
#Важливі атрибути Colorama:
#colorama.Fore: задає кольори тексту.
#colorama.Back: задає кольори фону.
#colorama.Style: задає стиль тексту.
#Важливі методи Colorama:
colorama.init()
#Ініціалізує бібліотеку. Це потрібно для коректної роботи кольорів на Windows.
colorama.deinit()
#Використовується для відключення і очищення змін, внесених init().
colorama.ansi.clear_screen()
#Видаляє весь текст з консолі (ефект очищення екрана).