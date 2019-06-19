# Drone-Models

Development of drone models accounting for weather and battery characteristics.

## Instructions

This section contains instructions for how to run awesomeModelName.py.

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

* the `Simulation` class

  * class variables describe
	* start time
	* end time
	* timestep
	* current timestep index
	* current time
	* an instance of the `Drone` class
	* an instance of the `Battery` class
	* an instance of the `Power` class
	* an instance of the `Weather` class
	* methods are used to run and store simulation information

NOTE: the model is based on power consumption to accomodate future development. The `Power` class is designed to receive an indefinite number of modifications based on weather effects

## Units

Properties and their respective units include:

<!-- These could probably be better organized -->
### Electricity
* Capacity: _milliamp-hours [mAh]_
* Voltage: _Volts [V]_
* Current: _Amperes [A]_
* Resistance: _Ohms [&Omega;]_

### Mechanics

* Velocity/Speed: _meters per second [m/s]_
* Power: _watts [W]_
* Endurance or Flight time: _minutes [min]_
* Altitude: _meters [m]_
* Weight: _kilograms [kg]_ <!-- I feel weird quoting a weight in mass units, but I put this here because the .param files seem to use kg. Which may be fine. Let me know if you have any thoughts. :) -->

### Miscellaneous
* Temperature: _degrees Celcius [&deg;C]_
* Wind Resistance: _meters per second [m/s]_ (referring to the maximum wind speed the drone can resist)
* Battery re-charge time: _minutes [min]_

## Parameter Files

### Simulation
	* The settings list file contains all the necessary simulation parameters the code will look through before running simulations. These include: 
		* drone (True/False)
		* dronename
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
			* axistitle

NOTE: For the plotting x- and y-labels, choose from the following parameters to plot:
	* range
	* endurance
	* payload

### Drone
There are `.param` files in the Drone directory each contain parameters specific to each drone. They are labled with the company's name or abbreviation in lowercase letters followed by a dash (-) and then the name of the drone (e.g., dji-Mavic2). New drones needing to be tested can follow similar formats, with a space (`" "`) delimiter.

### Batteries
Similar to the Drone `.param` files, battery `.param` files exist for each type of battery tested. These parameters assist in determining the discharge rate over time and amount of specific energy and power available for different types of batteries.

## functions.py - Commonly used functions
	* `getparams()` reads in a .txt or .csv file and outputs a dictionary with keys from a specified list and values from the specified parameter file.
	* More here...

## Testing
	* test_power.py
	* test_drone.py
	* test_plotter.py

<!--
## Directories Overview

### Drone/

This directory contains the following:

* the `Drone` class

	* class variables contain:

		* data sheet specifications of specific drone models (e.g., the Mavic 2 Pro), including

			* battery size
			* battery type
			* range under specified conditions
			* fixed wing or rotary wing
			* etc.

	* methods calculate certain characteristics based on available information

* the `params/` directory

	* contains `.param` text files containing specifications of each drone to be modeled

* a test script entitled `test_Drones.py`

### Batteries/

This directory contains the following:

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

* the `params/` directory

	* contains `.param` text files containing information about different battery types

### Power/

This directory contains the following:

* the `Power` class

	* class variables describe

		* baseline power consumption
		* an array of 'correction' objects used to modify the power consumption class variable due to weather or other effects (these could be the weather effect classes, actually)
		* total power consumption

	* methods are used to

		* update the total power consumption class variable
		* append `PowerCorrection` objects to `Power` objects using the `addCorrection` method
		* throw an error if `addCorrection` attempts to append a time-variant `PowerCorrection` object to a time-invariant `Power` object

* the `PowerCorrection` class

	* class variables desribe

		* adjustments to the baseline power requirements of the drone
		* whether the simulation is time-variant or time-invariant

	* methods perform miscellaneous book-keeping functions

### Weather/

This directory contains the following:

* scripts used to model weather effects on drones
* classes corresponding to each weather effect (e.g., rain, icing (though this might be a function of temperature and humidity- maybe it has a class that checks to see if icing is likely based on other weather characteristics), wind, etc.) that contain the following:

    * class variables characterizing the weather (e.g., )
    * methods used to modify the `Power` class
		* these probably take an instance of the `Drone` class as an argument

* the `Weather` class

	* class variables describe

		* an instance of each weather effect to be modeled

	* methods may be used to check for icing, or other miscellaneous needs

* the `params/` directory

	* contains `.param` text files containing information about different weather phenomena

### Simulation/

This directory contains the following:

* scripts used to model the range of a particular drone
* the `Simulation` class

  * class variables describe

	  * start time
		* end time
		* timestep
		* current timestep index
		* current time
		* an instance of the `Drone` class
		* an instance of the `Battery` class
		* an instance of the `Power` class
		* an instance of the `Weather` class

	* methods are used to run and store simulation information
NOTE: the model is based on power consumption to accomodate future development. The `Power` class is designed to receive an indefinite number of modifications based on weather effects
	* settings.csv
		* A csv file will input all the necessary information for a given simulation with the following rows (see settings_example.csv for reference):
			* Drone - true/false
			* Drone name
			* Rain - true/false
			* Drop size 
			* LWC
			* Timestep (for time-variant cases)
			* plot - specifies the next rows as plotting parameters
			* x-label 
			* y-label
			* axis title
		* for the x- and y-labels, choose two from the following parameters:
			* range
			* endurance
			* payload

* the `Plotter` class

	* class variables describe

		* x-axis variable
		* x-axis label
		* y-axis variable
		* y-axis label
		* other miscellaneous plotting parameters

	* methods are used to make plots
		* line plot
		* scatter plot
		* others to be decided (subplots, multiple plots per figure, etc.)
	* a test script entitled `test_plotter.py`
	* to use this you need to install matplotlib:
		* 'pip install matplotlib' (in the terminal)

* an `awesomeModelName_importer.py` module importer script

	* this script imports the classes and definitions defined above
	* after this script is run, classes and functions can be accessed and used to start simulations

* an `awesomeModelName_exe.py` script

	* this script is a sample simulation script containing

		* the module importer script
		* a sample simulation setup, where the following are specified:

			* the drone
			* weather
			* other variables

NOTE: `awesomeModelName_importer.py` and `awesomeModelName_exe.py` should be simple since data describing drone specifications, weather effects, battery parameters, etc. should already be contained `params/` directories
-->
