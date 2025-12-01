money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
vsego = salary + money_capital
months = 0
while vsego > spend:
    months +=1
    vsego = vsego - spend
    spend +=spend*increase
    vsego+=salary
print("Количество месяцев, которое можно протянуть без долгов:", months)
