cars = 100 #количество машин
space_in_a_car = 4 #мест в машине
drivers = 30 #количество водителей
passengers = 90 #количество пассажиров
cars_not_driven = cars - drivers #машины,которые не поедут
cars_driven = drivers # машины которые поедут
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
#average_passengers_per_car = carpool_capacity / passengers
# в этом случае мы делим 120-вместимость автомобиля на кол-во пассажиров
# а надо делить пассажиров на количество водятлов
print("В наличии", cars, "автомобилей.")
print("И только", drivers, "водителей вышли на работу.")
print("Получается, что", cars_not_driven, "машин пустуют.")
print("Мы можем перевезти сегодня", carpool_capacity, "человек.")
print("Сегодня нужно отвести", passengers, "человек.")
print("В каждой машине будет примерно", average_passengers_per_car, "человека")

x = 1
y = 2
print (x + y)