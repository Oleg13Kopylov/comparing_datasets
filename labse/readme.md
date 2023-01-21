# LaBSE

Описание вида "название файла – его содержание"

Первая серия экспериментов:

1) **labse_on_hotels_28_december.ipynb**
– модель labse обучается на отзывах об отелях и
обученная модель сохраняется в google drive
2) **labse_on_movies_28_december.ipynb**
– модель labse обучается на отзывах о фильмах и 
обученная модель сохраняется в google drive
3) **labse_loading_model_and_testing_28_december.ipynb**
– результаты тестирования модели labse
(в том числе перекрестная проверка). Обучающая и тестовая
выборки фиксированные.
Модели загружаются из google drive, они уже обучены
(в файлах 1-2).
В конце ноутбука приведен dataframe
с результатами тестирования каждой из моделей labse на 
каждом из датасетов (один датасет с отзывами на отели, 
другой датасет – с отзывами на фильмы).

Вторая серия экспериментов:

4) **labse_on_spam_emails_19_january.ipynb** – 
модель labse
обучается определять, является ли электронное письмо спамом
5) **labse_on_spam_sms_19_january.ipynb** – 
модель labse
обучается определять, является ли sms спамом
6) **labse_loading_model_and_testing_on_spam_19_january.ipynb** –
– результаты тестирования модели labse
(в том числе перекрестная проверка).


Ссылки на яндекс диск с моделями, которые я обучил:
1) labse, обученная на отзывах на фильмы:
https://disk.yandex.ru/d/o59rULabt6OE0A
2) labse, обученная на отзывах на отели:
https://disk.yandex.ru/d/1xckCLdpfWpwmg
3) labse, обученная определять спам в электронных письмах:
https://disk.yandex.com/d/1Sq6yPrlSG1nzA
4) labse, обученная определять спам в sms:
https://disk.yandex.com/d/swEPmDSbdvTtZg
