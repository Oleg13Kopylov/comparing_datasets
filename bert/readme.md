# BERT

Описание вида "название файла – его содержание"

Первая серия экспериментов:

1) **11_december_applied_to_reviews_on_hotels.ipynb**
– модель bert обучается на отзывах об отелях и
обученная модель сохраняется в google drive
2) **11_december_applied_to_reviews_on_movies.ipynb**
– модель bert обучается на отзывах о фильмах и 
обученная модель сохраняется в google drive
3) **13_december_loading_model_and_testing.ipynb**
– результаты тестирования модели bert
(в том числе перекрестная проверка). Обучающая и тестовая
выборки фиксированные.
Модели загружаются из google drive, они уже обучены
(в файлах 1-2).
В конце ноутбука приведен dataframe
с результатами тестирования каждой из моделей bert на 
каждом из датасетов (один датасет с отзывами на отели, 
другой датасет – с отзывами на фильмы).


Вторая серия экспериментов:

4) **bert_on_spam_emails_19_january.ipynb** –
модель bert
обучается определять, является ли электронное письмо спамом
5) **bert_on_spam_sms_19_january.ipynb** –
модель bert
обучается определять, является ли sms спамом
6) **bert_loading_model_and_testing_on_spam_19_january.ipynb** – 
– результаты тестирования модели bert
(в том числе перекрестная проверка).

Ссылки на яндекс диск с моделями, которые я обучил:
1) bert, обученный на отзывах на фильмы:
https://disk.yandex.com/d/kTaDcVVXDvec0w
2) bert, обученный на отзывах на отели:
https://disk.yandex.com/d/EazMr_Q4nquOoA
3) bert, обученный определять спам в электронных письмах:
https://disk.yandex.com/d/Me8EBEMv4_WYyw
4) bert, обученный определять спам в sms:
https://disk.yandex.com/d/orFE-wQ2s1PmDg

