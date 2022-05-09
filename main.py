import logging
import json
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from pygoodwe import SingleInverter

from config.settings import env


app = FastAPI()


inverter = SingleInverter(
	system_id=env('GOODWE_POWER_STATION_ID'),
	account=env('GOODWE_USERNAME'),
	password=env('GOODWE_PASSWORD')
)


@app.get('/', response_class=ORJSONResponse)
async def index():
	logging.warning("This is your first warning")
	return inverter.data

