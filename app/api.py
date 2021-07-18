import asyncio
import datetime

import httpx

partner: str = "finn"


async def get_price(
    fly_from: str, fly_to: str, date_from: datetime.date, date_to: datetime.date
):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.skypicker.com/flights?fly_from={fly_from}&to={fly_to}&date_from={date_from}&date_to={date_to}&adults=1&partner={partner}",
            timeout=None,
        )
        response_dict = response.json()

        flight = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date": date_to,
            "price": response_dict["data"][0]["price"],
            "booking_token": response_dict["data"][0]["booking_token"],
        }

        return flight


async def check_price(booking_token: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://booking-api.skypicker.com/api/v0.1/check_flights?v=2&booking_token={booking_token}&bnum=1&pnum=1&affily={partner}_us&currency=EUR&adults=1&children=0&infants=1",
            timeout=None,
        )
        response_dict = response.json()
        if response_dict["price_change"]:
            price = response_dict["flights_price"]
            return price
        return


async def check_valid(booking_token: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://booking-api.skypicker.com/api/v0.1/check_flights?v=2&booking_token={booking_token}&bnum=1&pnum=1&affily={partner}_us&currency=EUR&adults=1&children=0&infants=1",
            timeout=None,
        )
        response_dict = response.json()
        if response_dict["flights_checked"]:
            valid = response_dict["flights_invalid"]
            return valid
        return


def run(fly_from: str, fly_to: str, date_from: datetime.date):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    data: list = []
    for i in range(1, 31, 1):
        data.append(
            get_price(fly_from, fly_to, date_from, date_from + datetime.timedelta(i))
        )
    all_groups = asyncio.gather(*data)
    results = loop.run_until_complete(all_groups)
    loop.close()

    return results
