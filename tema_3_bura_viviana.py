import csv
cars = []
# cars=[{"brand":"mercedes","model":"benz","hp":500,"price":6000},
#       {"brand":"opel","model":"astra","hp":100,"price":3000},
#       {"brand":"dacia","model":"logan","hp":150,"price":2000},
#       {"brand":"ford","model":"ka","hp":60,"price":1000} ]
with open ("input.csv","r")as my_file:
    csv_reader = csv.DictReader(my_file)
    while True:
        line=my_file.readline()
        print(line)
        my_cars=line
        if not line:
            break

print(my_cars)


for index in range(len(cars)):
    car = cars[index]
    price=cars[index]
    car['id'] = index
    print(index,cars[index])

print()

for car in cars:
    if car['hp'] < 120:
        print(f"{car['brand']},{car['model']} is slower car")
    elif car['hp'] >=180:
        print(f"{car['brand']},{car['model']} fast speed")
    else:
        print(f"{car['brand']},{car['model']} medium speed")
print("THE END OF HP CLASIFICATION\n")


for price in cars:
    if price['price']<120:
        print(f"{price['brand']},{price['model']} is a cheep car")
    elif price ["price"]>=5000:
        print(f"{price['brand']},{price['model']} is an expensive car")
    else:
        print(f"{price['brand']},{price['model']} is a medium price car")
print("THE END OF PRICE CLASIFICATION\n")

