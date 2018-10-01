# FSImg
**«Анализ ИК-изображений с определением вероятности возникновения и существования очага самовозгорания, определения параметров эндогенного пожара»**

**Задача:**
Автоматическое определение очагов аномальных температур из собранной базы данных ИК-изображений. Для решения данной задачи был написан алгоритм ее решения и апробирован на экспериментальной базе данных.

*Блок–схема работы алгоритма программы анализа ИК-изображений с определением вероятности возникновения и существования очага самовозгорания, определения параметров эндогенного пожара.*
![Альтернативный текст](/блок%20схема.png)

**Описание интерфейса программы:**

![Альтернативный текст](/Безымянный.png)

**Выбор папки с фотографиями** - необходимо выбрать каталог со всеми фотографиями полученными с БПЛА в формате (jpg, png) 
**Выбор папки для пожаров** - необходимо выбрать каталог куда будут помещены уже обработанные фотографии с найденными очагами.
**Выберете папку для возможных пожаром** - необходимо выбрать каталог куда будут помещены уже обработанные фотографии где пожар был обнаружен только после первого анализа т.е. температура определенная на снимке была выше заданного предела, а площадь не соответствовала заданному пределу.
**Укажите интенсивность пожара** - Необходимо указать значения от 0 - 255 которое соответствует максимальной и минимальной температуре.
**Укажите площадь пожара** - необходимо указать площадь по превышению этого значения будем считать что на изображении - пожар.
**Метр квадратный на пиксель** - данное значение необходимо для корректного подсчета площади пожара. 
**Пуск** - Запуск обработки. 
**Окно Log** позволяет в реальном времени отслеживать такие параметры: 
 1. Имя изображения: Untitled006555.jpg
 2. Размер изображения: 704x576
 3. Максимальная интенсивность: 133.0
 4. Обработка по температуре: Возможен пожар
 5. Обработка по площади: Нет пожара
 6. Точка: 46, 491 интенсивность: 192
 
**Кнопка сохранить Log** - позволяет сохранить отчет о работе программы 
