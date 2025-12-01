salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
salary_sum = salary
spend_sum = spend
for i in range(months-1):
    salary_sum += salary
    spend = spend*(increase+1)
    spend_sum += spend
money_capital = spend_sum-salary_sum
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
