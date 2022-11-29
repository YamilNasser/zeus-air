from amadeus import Client, ResponseError

amadeus = Client(
    client_id='qVGXBGiJqYwbLAQnxPi4QDxljsqVjdXu',
    client_secret='TFf9hWYPhqgVEmBG'
)

test = 'data'
try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='MIA',
        destinationLocationCode='MAD',
        departureDate='2022-12-12',
        adults=1)
    for x in response.data:
        print(x)
except ResponseError as error:
    print(error)

