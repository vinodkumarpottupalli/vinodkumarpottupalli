curl 'http://127.0.0.1:8080/api/cars?brand=ford'

curl 'http://127.0.0.1:8080/api/cars?model=7'

curl 'http://127.0.0.1:8080/api/cars?model=%7%'

curl 'http://127.0.0.1:8080/api/cars?brand=bmw&transmission=auto'

curl 'http://127.0.0.1:8080/api/cars?price_operator=lte&price=50000'

curl 'http://127.0.0.1:8080/api/cars?price_operator=lte&price=50000&page=2&size=20'


curl 'http://127.0.0.1:8080/api/cars?price_operator=between&price=30000&price_max=60000&brand=honda&size=5'

curl 'http://127.0.0.1:8080/api/cars?model=7'

curl 'http://127.0.0.1:8080/api/cars?brand=bmw&transmission=auto'

curl 'http://127.0.0.1:8080/api/cars?sort_by=price&size=5&page=1'

curl 'http://127.0.0.1:8080/api/cars?sort_by=price&size=5&page=20'

curl 'http://127.0.0.1:8080/api/cars?sort_by=price&sort_direction=desc&size=5&page=1'


curl 'http://127.0.0.1:8080/api/cars/multisort?brand=honda&sort_by=release_year,price&sort_direction=desc,asc&size=5&page=1'