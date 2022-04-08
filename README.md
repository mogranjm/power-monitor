# Power Monitor
An example Data Engineering project to capture the activity of my household solar array and generate insights for its productivity and to facilitate prediction of high-production periods for optimal use of high-power drawing appliances.

### Data Sources

| Source Name                                      | Data Type | Detail                                                                                                                                                                                                                                                                      |
|--------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Solar Inverter API (realtime production monitor) | JSON     | GoodWe Solar inverter logs production activity via WiFi. Data is available from an undocumented API,                                                                                                                                                                        
| Powerpal (realtime consumption monitor) "API"    | CSV      | Powerpal is a bluetooth IoT device connected to the smart meter at my property that records realtime power consumption by my house from the grid. Every time my phone is in range of its bluetooth receiver, the device will update the powerpal consumption record.        
| Power company consumption data                   | CSV      | The Powershop account portal allows rudimentary visualisation of power consumption. The data behind this dashboard is available through a form that allows the user to select a time-period with a slider and download the (CSV) data for that period via a download button |
| Power company solar production data              | CSV      | As above                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                            |
| Weather API                                      | ?? | TBD - Find a weather free API that can be used to estimate solar production                                                                                                                                                                                                 |

### Pipeline Description

#### Local Solar Production
The Solar Inverter logs production data continuously and is not operational overnight. So local solar production data is best processed in nightly batches. 

#### Local Power Consumption
Powerpal data is updated intermittently and infrequently. There is no true "downtime" as with the solar production data so this source will ideally be processed as a stream (pending ability to define a trigger).

i.e. Any time powerpal connects & updates, the local power consumption ETL should trigger

#### External Consumption & Production
Data from the power company (consumption & production) must be downloaded from the desktop portal so has to be scraped or downloaded manually

#### Weather Predictions
Weather Data is constantly updated as forecasts change. As the forecast date & time becomes closer, the predictions will be more accurate. Depending on the terms of a Weather API free tier, 7-day weather forecast data could be requested on a daily basis (morning) and stored in the Data Warehouse. A Data Mart could then be updated with the most recently issued forecast. It would also be interesting to know how much a forecast can change over a 7 day period.

## Acknowledgements
Thanks to Github user @yaleman for his work on [pygoodwe](https://www.github.com/yaleman/pygoodwe). Although it's not used in this project, the documentation there has been invaluable for deciphering the GoodWe API.