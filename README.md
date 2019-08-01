# Drone-AWE: Drone Applications in Weather Environments

This repository is being developed to advance the state of the art of drone performance predictions under a wide range of weather and battery conditions with mission planning in mind. An interactive GUI is available at http://droneecon.com. This README will explain general usage as well as the underlying theory for the models used, as currently implemented. Note that *Drone-AWE* is a work in progress (see **Future Work**). This document will explain general usage for the latter, as well as the engineering theory at work behind the scenes.

## Installation

Drone-AWE may be used in two ways: using the GUI available at http://droneecon.com, or by using the source code directly. To use the source code directly, install using

```python3
pip install drone_awe
```

## Usage

### Basic Usage

Base functionality is achieved by running the following:

```python3
import drone_awe
m = drone_awe.model(args)
m.simulate()
```

where `args` is a dictionary containing simulation parameters. Note that for every parameter not specified in `args`, a default value is used. It is possible to run the default simulation by passing an empty dictionary into the `drone_awe.model()` method:

```python3
import drone_awe
m = drone_awe.model({})
m.simulate()
```

Settable dictionary keys with example values for `args` include the following:

```python3
{
    "validation":False,
    "validationcase":"DiFranco2016",
    "dronename":"dji-Mavic2",
    "batterytechnology":"near-future",
    "stateofhealth":90.0,
    "startstateofcharge":100.0,
    "altitude":100.0,
    "rain":False,
    "dropsize":1.0,
    "liquidwatercontent":1.0,
    "temperature":15.0,
    "wind":False,
    "windspeed":10.0,
    "winddirection":0.0,
    "relativehumidity":0.0,
    "mission": {
            "missionspeed": 10.0
        },
    "timestep":1,
    "plot":True,
    "xlabel":"missionspeed",
    "ylabel":"power",
    "title":"First_test",
    "simulationtype":"simple",
    "model":"abdilla",
    "xvals":[0,1,2,3,4,5],
    "weathereffect":"temperature",
    "weathervals":[10,20,30,40]
}
```

These are explained further in **Settings**. After a `drone_awe.model` object is instantiated, settings can be changed by modifying the `input` class variable as:

```python3
m.input['xlabel'] = 'payload'
m.input['validationcase'] = 'Stolaroff2018'
```

The simulation must then be re-run using:

```python3
m.simulate()
```

### Plotting

An optional boolean may be set to produce a plot on runtime by running:

```python3
m = drone_awe.model({},plot=True)
```

when a `drone_awe.model` is instantiated. Alternatively, the `drone_awe.model`'s `plot` variable may be set at any time:

```python3
m.plot = True
```

### Settings

The following subsections explain the use of various settings of a `drone_awe.model` object.

#### `'dronename'`

`'dronename'` must be set to a string that is defined in the drone database. To access a dictionary containing all supported drones, use the following methods:

```python3
droneDictionary = m.getDrones()
```

If a drone or validation case does not exist in the drone database, it may still be used by setting a custom dictionary:

```python3
m.drone = droneDictionary
```

where `droneDictionary` is a dictionary with the same keys as the following:

```python3
{
    'id': 'dji-Mavic2',
    'wingtype': 'rotary',
    'diagonal': 0.354,
    'takeoffweight': 0.907,
    'speedmax': 20,
    'altitudemax': 6000,
    'endurancemax': 31,
    'endurancemaxspeed': 6.944,
    'endurancemaxhover': 29,
    'rangemax': 18000,
    'rangemaxspeed': 13.889,
    'temperaturemin': -10,
    'chargerpowerrating': 60,
    'batterytype': 'LiPo',
    'batterycapacity': 3850,
    'batteryvoltage': 15.4,
    'batterycells': 4,
    'batteryenergy': 59.29,
    'batterymass': 0.297,
    'waterproof': 'no',
    'windspeedmax': 10.8,
    'batteryrechargetime': 90,
    'rotorquantity': 4,
    'rotordiameter': 0.2,
    'cruisespeed': 6.94,
    'payload': 0.0,
    'length': 0.322,
    'width': 0.242,
    'height': 0.084
}
```

Note that not all parameters need be specified, but if a simulation is run that requires unspecified parameters, the model will not run.

#### `'validation'` and `'validationcase'`

To view validation cases for `drone_awe` models, set `'validation'=True` and `'validationcase'` to a string contained in the validation case database. To access a dictionary containing all supported validation cases, run the following:

```python3
validationDictionary = m.getValidationCases()
```

Additionally, `validationCaseDictionary` is a dictionary with the following format:

```python3
{
    'id': 'Stolaroff2018',
    'xvalid': [1.358974359,1.7179487179,1.6923076923,1.7692307692,1.7692307692,1.8205128205,1.8717948718,1.8974358974,1.9230769231,1.9743589744,2.0512820513,2.1025641026,2.1025641026,2.1794871795,2.2820512821,2.3076923077,2.3333333333,2.4358974359,2.5384615385,2.5384615385,2.6666666667,2.7948717949,2.9487179487,3.1025641026,3.2564102564,3.358974359,3.4615384615,3.641025641,3.7435897436,3.8717948718,4.0512820513,4.2564102564,4.358974359,4.641025641,4.8974358974,5.8461538462,6,6.2820512821,6.5384615385,7.1538461538,7.4871794872,7.8205128205,8.4871794872,9.1794871795,9.7692307692,10.2564102564,10.6923076923,11.1282051282,11.5897435897],
    'yvalid': [133.7510729614,149.2375075128,142.6477385276,144.5897859156,140.9450186657,141.7583868756,142.3874173587,140.4340604922,139.3656195241,139.5335348046,140.2321151941,139.9589946754,136.1689649626,138.3618186589,141.3711557508,139.4001574523,136.7492021569,136.5131929807,137.712167001,133.136399421,135.7755034665,136.58240428,141.8694500174,143.7278953027,145.8751386173,144.4503136349,143.5492800366,144.4966689523,140.8944307591,139.7885398414,140.0842115956,140.6905892611,140.7593265104,140.4412051028,148.3297356325,161.0751453894,160.7738527567,158.8079335653,157.0439596719,161.2248774665,165.1381601781,164.7032531681,177.1408013138,175.6982333173,190.095233258,197.4485952036,209.0736216573,203.7684942987,215.7551870381],
    'drone': {
        'validationcase':'Stolaroff2018',
        'wingtype': 'rotary',
        'rotorquantity': 4,
        'takeoffweight': 1.3,
        'batterytype': 'LiPo',
        'batteryvoltage': 11.1,
        'batterymass': 0.262,
        'props': '10x4.7',
        'endurancemaxhover': 16,
        'payloadmax': 0.4,
        'batterycapacity': 5500,
        'payload': 0.0,
        'rotordiameter': 0.254,
        'batterycells': 3,
        'length': 0.280,
        'width': 0.140,
        'height': 0.100,
        'waterproof': 'no'
        },
    'settings': {
        'dronename': 'drone',
        'stateofhealth': 100.0,
        'startstateofcharge': 100.0,
        'altitude': 100.0,
        'temperaturesealevel': 15.0,
        'rain': False,
        'dropsize': 0.0,
        'liquidwatercontent': 1.0,
        'temperature': 15.0,
        'wind': False,
        'windspeed': 0.0,
        'winddirection': 0.0,
        'relativehumidity': 85.0,
        'icing': False,
        "mission": {
            "missionspeed": 10.0
        },
        'timestep': 1,
        'xlabel': 'missionspeed',
        'ylabel': 'alpha',
        'title': 'Stolaroff',
        'simulationtype': 'simple',
        'model': 'abdilla',
        'xvals': [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0],
        'validation': False,
        'validationcase': 'Stolaroff2018',
        'batterytechnology': 'current'
        }
}
```

## Theory

`Drone AWE` is intended to predict performance parameters of rotary and fixed-wing drones based on readily-available specifications. To accomplish this, the power requirements for a given flight maneuver is calculated and used to predict battery drain behavior. Then, parameters such as range and endurance can be calculated. Comprehensive state data is collected at each step of a simulation, providing a versatile data set as output for study.

### Power

#### Rotary Drones

For rotary drones, power consumption is predicted in two steps. First, model parameters are calibrated based on known specifications, like maximum hover time and rotor diameter. Then, momentum theory is used to predict the power consumption.

#### Calibration

#### Momentum Theory

According to rotor momentum theory, five equations govern the flight of a rotorcraft:

1. $T = \sqrt{W^2 + D^2}$
2. $tan(\alpha) = \frac{D}{W}$
3. $D = \frac{1}{2} \rho V_\infty^2 C_D A_{\bot}$
4. $v_i = \frac{T}{2 A_{rotor} N_{rotor} \rho \sqrt{V_\infty^2 cos^2(\alpha) + (V_\infty sin(\alpha) + v_i^2)}}$
5. $A_{\bot} = A_{front} cos(\alpha) + A_{top} sin(\alpha)$

#### Fixed-Wing Drones

## Classes

This section contains a detailed description of each class, all contained in Classes.py.

* the `Drone` class

    * class variables contain:

        * data sheet specifications of specific drone models (e.g., the Mavic 2 Pro), including

			* battery size
			* battery type
			* range under specified conditions
			* fixed wing or rotary wing
			* etc.

	* methods calculate certain characteristics based on available information

* the `Battery` class

	* class variables describe:

		* properties of specific batteries used to model their discharge characteristics, including

			* battery type
			* number of cells
			* low, nominal, and charged cell voltages

		* Real-time discharge characteristics for simulation, including

			* instantaneous voltage
			* instantaneous current
			* instantaneous state of charge
			* current state of health

	* methods are used to update class variables using information from the `params/` directory

* the `Power` class

	* class variables describe

		* baseline power consumption
		* an array of 'correction' objects used to modify the power consumption class variable due to weather or other effects (these could be the weather effect classes, actually)
		* total power consumption

	* methods are used to

		* update the total power consumption class variable
		* append `PowerCorrection` objects to `Power` objects using the `addCorrection` method
		* throw an error if `addCorrection` attempts to append a time-variant `PowerCorrection` object to a time-invariant `Power` object
		* the `PowerCorrection` method
			* adjustments to the baseline power requirements of the drone
			* whether the simulation is time-variant or time-invariant
			* methods perform miscellaneous book-keeping functions

* the `Weather` class

	* class variables describe

		* an instance of each weather effect to be modeled

	* methods may be used to check for icing, or other miscellaneous needs

* the `WeatherType` class

	* class consists of the following sub-classes:

		* the `Rain` class

			* class variables describe 

				* droplet size
				* Liquid Water Content (LWC)
				* other parameters needed to model rain

		* the `Temperature` class

			* class variables describe 

				* new temperature?

		* the `Humidity` class

			* class variables describe 

				* relative humidity

		* the `Wind` class

			* class variables describe 

				* wind speed
				* wind direction
				* amount of turbulence?
				* variation in speed and/or direction?
		
		* the `Gust` class

			* class variables describe

				* frequency
				* amplitude
		
		* the `Ice` class
			
			* Because of modeling difficulty, this class does not attempt yet to model icing effects. It may in the future be used to identify if icing conditions are present. 

* the `Mission` class

	* class variables describe
		
		* mission speed

* the `Simulation` class

  * class variables describe
	* start time
	* end time
	* timestep
	* current timestep index
	* current time
	* methods are used to run and store simulation information, including procedures to get range and endurance

NOTE: the model is based on power consumption to accomodate future development. The `Power` class is designed to receive an indefinite number of modifications based on weather effects

* the `Plotter` class

	* plots results according to labels and titles specified by the user in the `settings.txt` file. Methods can plot a line or scatter plots. The validation method plots results on top of specified validation data.

## Units

Properties and their respective units are converted within the simulation to SI units, and then converted back. Those units are:

<!-- These could probably be better organized -->

### Electricity

* Capacity: _milliamp-hours [mAh]_
* Voltage: _volts [V]_
* Current: _amperes [A]_
* Resistance: _ohms [&Omega;]_

### Mechanics

* Velocity/Speed: _meters per second [m/s]_
* Power: _watts [W]_
* Endurance or Flight time: _minutes [min]_
* Altitude: _meters [m]_
* mass: _kilograms [kg]_

	* note that "takeoff weight" is measured in mass units <!-- I feel weird quoting a weight in mass units, but I put this here because the .param files seem to use kg. Which may be fine. Let me know if you have any thoughts. :)  Yeah, that is kind of strange. -->

### Miscellaneous

* Temperature: _degrees Celcius [&deg;C]_
* Wind Resistance: _meters per second [m/s]_

	*refers to the maximum wind speed the drone can resist

* Battery re-charge time: _minutes [min]_

## Parameter Files

### Simulation

* The settings list file contains all the necessary simulation parameters the code will look through before running simulations. These include:

	* validation (True/False)

		* If validation is True, the program reads in the next value, validationcase, and looks for the settings file under that directory in params/Validation/, and ignores the rest of the current settings file.

	* validationcase
		
		* Specifies which validation case is being tested. Irrelevant if validation is False.
	
	* drone (True/False)
	* dronename
	* battery state of health
	* battery beginning state of charge
	* altitude
	* sea level temperature
	* rain (True/False)

		* droplet size
		* LWC

	* Temperature

		* New temperature

	* Humidity

		* Relative humidity

	* Wind

		* Wind speed
		* Wind direction

	* Icing
	* Timestep
	* plot (True/False)

		* xlabel
		* ylabel
		* axis title

	* simulation type

		* simple is the only option for now

	* range of vx-values

		* xbegin
		* xend
		* xnumber

			* the simulation will loop through xnumber of the model from xbeginning to xend, according to what is put as the xlabel (also the x-variable)

NOTE: For the plotting x- and y-labels, choose from the following parameters to plot:

* range
* endurance
* payload

### Drone

There are `.param` files in the Drone directory each contain parameters specific to each drone. They are labled with the company's name or abbreviation in lowercase letters followed by a dash (-) and then the name of the drone (e.g., dji-Mavic2). New drones needing to be tested can follow similar formats, with a space (`" "`) delimiter.

### Batteries

Similar to the Drone `.param` files, battery `.param` files exist for each type of battery tested. These parameters assist in determining the discharge rate over time and amount of specific energy and power available for different types of batteries.

## functions.py - Commonly used functions

* `getparams` reads in a .txt or .csv file and outputs a dictionary with keys from a specified list and values from the specified parameter file.
* `getXandY()` reads in data from a validation case and saves the contents to lists for x and y. This function assumes the first row contains labels and ignores them.
* `interpolate()` does a simple linear interpolation with inputs of 2 x-values, 2 y-values, and the x-value of the parameter you are seeking.

## Testing
* test_power.py
* test_drone.py
* test_plotter.py

## Future Work

This section is to be used to record ideas for future development that cannot be immediately implemented due to time constraints.

* calculate propulsive efficiency at max range and max endurance and interpolate between the two
* go weather by weather and determine the appropriate model to be used