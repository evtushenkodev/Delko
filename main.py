import calendar as cal

russian_months = [
    "января", "февраля", "марта", "апреля", "мая", "июня",
    "июля", "августа", "сентября", "октября", "ноября", "декабря"
]


class CalendarIterator:
    def __init__(self, year):
        self.year = year
        self.months = range(1, 13)
        self.current_month = 1
        self.current_day = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_month <= 12:
            day = f"{self.current_day} {russian_months[self.current_month - 1]}"
            if self.current_day < cal.monthrange(self.year, self.current_month)[1]:
                self.current_day += 1
            else:
                self.current_month += 1
                self.current_day = 1
            return day
        else:
            raise StopIteration


calendar = CalendarIterator(2023)

# Пример использования итератора с вызовом next()
for _ in range(100):  # Получить 100 дней
    print(next(calendar))

for _ in range(200):  # Получить следующие 200 дней
    print(next(calendar))

for _ in range(100):  # Получить следующие 100 дней (приведет к выводу исключения StopIteration)
    print(next(calendar))

