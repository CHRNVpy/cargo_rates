import os

from tortoise import fields, models, Tortoise
from tortoise.transactions import in_transaction
import asyncio
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')


class CargoRate(models.Model):
    id = fields.IntField(pk=True)
    date = fields.CharField(max_length=50)
    cargo_type = fields.CharField(max_length=100)
    rate = fields.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        table = "cargo_rates"


async def init_db():
    await Tortoise.init(
        db_url=f'postgres://{db_user}:{db_password}@db/{db_name}',
        modules={'models': ['__main__']}
    )
    await Tortoise.generate_schemas()


async def create_tables():
    await init_db()
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


async def save_rates_to_db(rates_data):
    await init_db()
    for date_str, rates in rates_data.items():
        for rate_data in rates:
            async with in_transaction():
                await CargoRate.create(date=date_str, cargo_type=rate_data["cargo_type"], rate=rate_data["rate"])
    await Tortoise.close_connections()


async def get_rate(rates_data):
    await init_db()
    for date_str, rates in rates_data.items():
        result = await CargoRate.filter(date=date_str, cargo_type=rates["cargo_type"]).first()
        return result.rate
    await Tortoise.close_connections()
