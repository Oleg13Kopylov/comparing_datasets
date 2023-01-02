# tn_bert

Описание вида "название файла – его содержание" для 
A compressed BERT model using tensor networks
(tn_bert).

1) **tn_bert_on_hotels_02_january.ipynb**
– модель tn_bert обучается на отзывах об отелях и
обученная модель сохраняется в google drive
2) **tn_bert_on_movies_02_january.ipynb**
– модель tn_bert обучается на отзывах о фильмах и 
обученная модель сохраняется в google drive
3) **tn_bert_loading_model_and_testing_02_january.ipynb**
– результаты тестирования модели tn_bert
(в том числе перекрестная проверка). Обучающая и тестовая
выборки фиксированные.
Модели загружаются из google drive, они уже обучены
(в файлах 1-2).
В конце ноутбука приведен dataframe
с результатами тестирования каждой из моделей tn_bert
на каждом из датасетов (один датасет с отзывами на отели, 
другой датасет – с отзывами на фильмы).


Ссылки на яндекс диск с моделями, которые я обучил:
1) tn_bert, обученная на отзывах на фильмы:
https://disk.yandex.com/d/rgKvu2y63KQGTg
2) tn_bert, обученная на отзывах на отели:
https://disk.yandex.com/d/LdpjPVg0KFi7-w
