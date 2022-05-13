# 4
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:

# Copy

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

#dollarize(123456.78901) -> "$123,456.80"
#dollarize(-123456.7801) -> "-$123,456.78"
#dollarize(1000000) -> "$1,000,000"


class MoneyFmt:

    def __init__(self, value):
        self.value = value
        self.str()

    def str(self):
        dollar = '${:,.2f}'.format(self.value)
        return dollar

    def __str__(self):
        return f'{self.str()}'

    def update(self, value):
        self.value = value
        return value

    def repr(self):
        return float(self.value)


cash = MoneyFmt(12345678.021)
print(cash)
cash.update(100000.4567)
print(cash)
cash.update(-0.3)
print(cash)
print(cash.repr())
