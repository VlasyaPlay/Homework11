import requests
import pandas as pd
import matplotlib.pyplot as plt

#выполнение HTTP запроса к сайту, вывод полученных данных в консоль
response = requests.get('https://jsonplaceholder.typicode.com/users')

if response.status_code == 200:
    data = response.json()  # Преобразуем ответ в JSON
    for user in data:
        print(f"Имя: {user['name']}, Email: {user['email']}")
else:
    print(f"Ошибка при выполнении запроса: {response.status_code}")


# Использование класса Session
session = requests.Session()

# Устанавливаем базовый URL и общие параметры
base_url = 'https://jsonplaceholder.typicode.com'
session.headers.update({'User-Agent': 'Mozilla/5.0'})

# Выполняем первый запрос (GET)
response = session.get(f'{base_url}/posts/1')

if response.status_code == 200:
    print("Данные о посте:")
    print(response.json())

# Выполняем второй запрос с той же сессией (GET)
response2 = session.get(f'{base_url}/users/1')

if response2.status_code == 200:
    print("\nДанные о пользователе:")
    print(response2.json())

# Закрываем сессию после использования
session.close()


# Отправляем POST-запрос с данными, чтобы создать новый ресурс на сервере
url = 'https://jsonplaceholder.typicode.com/posts'

# Данные для отправки на сервер
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

try:
    # Отправляем POST-запрос
    response = requests.post(url, json=data)

    # Проверяем статус ответа
    if response.status_code == 201:
        print("Успешно создан новый пост:")
        print(response.json())
    else:
        print(f"Ошибка при создании поста: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка: {e}")


# Работа с библиотекой pandas

# Загрузка данных из CSV и вывод первых строк

data = pd.read_csv('data.csv')

print("Первые 5 строк данных:")
print(data.head())

# Класс для анализа данных с использованием DataFrame


class DataAnalyzer:
    def __init__(self, file_path):
        # Загрузка данных из CSV файла
        self.data = pd.read_csv(file_path)

    def show_head(self, n=5):
        """Выводит первые n строк данных."""
        print(self.data.head(n))

    def average_column(self, column_name):
        """Вычисляет среднее значение указанного столбца."""
        if column_name in self.data.columns:
            return self.data[column_name].mean()
        else:
            print(f"Столбец '{column_name}' не найден в данных.")
            return None

    def filter_by_condition(self, column_name, condition):
        """Фильтрует данные по заданному условию."""
        if column_name in self.data.columns:
            return self.data[self.data[column_name] > condition]
        else:
            print(f"Столбец '{column_name}' не найден в данных.")
            return None

    def count_by_group(self, column_name):
        """Подсчитывает количество элементов в каждой группе указанного столбца."""
        if column_name in self.data.columns:
            return self.data[column_name].value_counts()
        else:
            print(f"Столбец '{column_name}' не найден в данных.")
            return None


# Пример использования класса
if __name__ == "__main__":
    analyzer = DataAnalyzer('data.csv')

    print("Первые 5 строк данных:")
    analyzer.show_head()

    avg_age = analyzer.average_column('age')
    if avg_age is not None:
        print(f"Средний возраст: {avg_age:.2f}")

    high_salary_data = analyzer.filter_by_condition('salary', 50000)
    print("Сотрудники с зарплатой выше 50000:")
    print(high_salary_data)

    department_counts = analyzer.count_by_group('department')
    print("Количество сотрудников в каждом департаменте:")
    print(department_counts)


# анализ данных о продажах

import pandas as pd

# Загрузка данных из CSV файла
data = pd.read_csv('sales_data.csv')

# Выводим первые 5 строк данных
print("Первые 5 строк данных о продажах:")
print(data.head())

# Преобразование столбца Date в тип datetime
data['Date'] = pd.to_datetime(data['Date'])

# Создание нового столбца с месяцем
data['Month'] = data['Date'].dt.month

# Группировка данных по месяцу и продукту, и подсчет общего дохода
monthly_revenue = data.groupby(['Month', 'Product'])['Revenue'].sum().reset_index()

print("\nОбщий доход по месяцам и продуктам:")
print(monthly_revenue)

# Построение сводной таблицы (Pivot Table)
pivot_table = monthly_revenue.pivot(index='Month', columns='Product', values='Revenue').fillna(0)

print("\nСводная таблица дохода по месяцам:")
print(pivot_table)

# Вычисление общего дохода за весь период
total_revenue = data['Revenue'].sum()
print(f"\nОбщий доход за весь период: {total_revenue:.2f}")



# Работа с библиатекой matplotlib


# Класс для визуализации данных о продажах

class SalesVisualizer:
    def __init__(self, file_path):
        # Загрузка данных из CSV файла
        self.data = pd.read_csv(file_path)
        self.data['Date'] = pd.to_datetime(self.data['Date'])

    def plot_sales_trend(self):
        """Построение графика тренда продаж по датам."""
        sales_trend = self.data.groupby('Date')['Sales'].sum()

        plt.figure(figsize=(10, 5))
        plt.plot(sales_trend.index, sales_trend.values, marker='o')
        plt.title('Тренд продаж по датам')
        plt.xlabel('Дата')
        plt.ylabel('Количество продаж')
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.show()

    def plot_revenue_distribution(self):
        """Построение гистограммы распределения дохода."""
        plt.figure(figsize=(10, 5))
        plt.hist(self.data['Revenue'], bins=10, color='blue', alpha=0.7)
        plt.title('Распределение дохода')
        plt.xlabel('Выручка')
        plt.ylabel('Частота')
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

    def plot_monthly_revenue(self):
        """Построение столбчатой диаграммы дохода по месяцам."""
        self.data['Month'] = self.data['Date'].dt.month
        monthly_revenue = self.data.groupby('Month')['Revenue'].sum()

        plt.figure(figsize=(10, 5))
        monthly_revenue.plot(kind='bar', color='orange', alpha=0.7)
        plt.title('Доход по месяцам')
        plt.xlabel('Месяц')
        plt.ylabel('Выручка')
        plt.xticks(rotation=0)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()


# Пример использования класса
if __name__ == "__main__":
    visualizer = SalesVisualizer('sales_data.csv')

    visualizer.plot_sales_trend()
    visualizer.plot_revenue_distribution()
    visualizer.plot_monthly_revenue()






