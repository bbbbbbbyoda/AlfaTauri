# #
# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.

# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.

class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun = None

    def __str__(self):
        return f'Рядовой {self.name} на месте, ваши указания?'

    def fire(self):
        if self.gun == None:
            print('Возьмите оружие, вы не умеете драться')
        else:
            self.gun.shoot()

    class Gun:
        def __init__(self, gun):
            self.gun = gun
            self.bullet_count = 0
            if self.gun == 'Ak-47':
                self.bullet_count = 5
            elif self.gun=='Glock-9':
                self.bullet_count = 18
            elif self.gun=='M4A1-S':
                self.bullet_count = 25
            else:
                print('В оружейной нет такого оружия. Возьмите одно их: Ak-47, M4A1-S, Glock-9')

        def __str__(self):
           return f"{self.gun} {self.bullet_count}"

        def shoot(self):
            a = self.bullet_count
            while True:
                s = input('Введите S для стрельбы: ')
                if s == 's' and self.bullet_count > 0:

                    print(f'тиги-тигитиш, осталовсь {self.bullet_count} патронов')
                    self.bullet_count -= 1
                elif s == 's' and self.bullet_count <= 0:
                    print('перезарядитесь')
                    self.bullet_count += a
                else:
                    raise ValueError('У вас нет патронов! Перезарядитесь!!!')


# class Act_of_shooting(Gun):




Piter = Soldier('Piter')
Piter.gun = Soldier('Piter').Gun('Ak-475')
print(Piter)
# Piter.gun.add_bullet

print(Piter.fire())









# # 2
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.

# class Furniture:
#     def __init__(self, f_name, area):
#         self.f_name = f_name
#         self.area = area
#
#     def __str__(self):
#         return f'{self.f_name} {self.area}'
#
# class House:
#     def __init__(self, house_type, area):
#         self.house_type = house_type
#         self.area = area
#         self.free_area = area
#         self.furniture_list = []
#
#     def __str__(self):
#         return f'{self.house_type} {self.area} {self.free_area} {self.furniture_list}'
#
#     def add_furniture(self, furniture):
#         if self.free_area > furniture.area:
#             self.free_area -= furniture.area
#             self.furniture_list.append(str(furniture))
#         elif self.free_area < furniture.area:
#             print(f'Площадь мебели {furniture} превышает оставшуюся площадь')
#
# bed = Furniture('bed', 4)
# cloakroom = Furniture('cloakroom', 2)
# table = Furniture('table', 1.5)
#
# print(bed)
# print(table)
# print(cloakroom)
#
# villa = House('Villa', 5)
#
# villa.add_furniture(bed)
# villa.add_furniture(cloakroom)
# villa.add_furniture(table)
#
# print(villa)

# # 3
# Students room:
# Реализуйте студенческую комнату с помощью ООП:

# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>



# # 4
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:

# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"

# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (количество) и 4 метода.
# Copy
#     "init" //конструктор инициализирует значение данных
#     "update" //метод заменяет значение данных новым
#     "repr" //методы возвращают значение с плавающей запятой
#     "str" //метод, реализующий логику метода dollarize ()

# Copy
# //Результат будет выглядеть так:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3



# # 5
# Deck of Cards:
# Создайте класс колоды карт. Внутри колода карт должна использовать другой класс - класс карт. Ваши требования:
# Класс Deck должен иметь метод раздачи для раздачи одной карты из колоды.
# После раздачи карты она удаляется из колоды.
# Должен быть метод «смешивания», который проверяет, что в колоде есть все 52 карты, а затем меняет их случайным образом.
# Класс должен иметь масть (червы, бубны, трефы, пики) и ценность карты (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# ПРИМЕЧАНИЕ: используйте случайное перемешивание

# Copy
# from random import shuffle



# # 6
# Спарсить сайт лалафо с недвижимостью (аренда посуточно)
# https://lalafo.kg/kyrgyzstan/nedvizhimost
# Название
# Цену
# Фото
# Адрес
# Дату
# Ссылку на пост

# Данные отдать в csv
