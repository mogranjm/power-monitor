from pygoodwe import SingleInverter

from config.settings import env


inverter = SingleInverter(
	system_id=env('GOODWE_POWER_STATION_ID'),
	account=env('GOODWE_USERNAME'),
	password=env('GOODWE_PASSWORD')
)
