RPi-experiments
===============

Lots of experiments with my RaspberryPi (in Python)


Prerequisites
------------

Need to have the `RPi.GPIO` library installed from [here](http://pypi.python.org/pypi/RPi.GPIO). You can find installation instructions [here](http://www.raspberrypi-spy.co.uk/2012/05/install-rpi-gpio-python-library/).

Pinout Diagram:
---------------
Here's a basic pinout diagram of the RPi GPIO headers for quick reference:

```
	3.3V			( ) | ( )	5V
	GPIO0 (SDA)		( ) | ( ) 	--
	GPIO1 (SCL)		( ) | ( ) 	GND
	GPIO4 (GPCLK0)	( ) | ( ) 	GPIO14 (TXD)
	-- 				( ) | ( ) 	GPIO15 (RXD)
	GPIO17			( ) | ( ) 	GPIO18 (PCM_CLK)
	GPIO21(PCM_DOUT)( ) | ( ) 	--
	GPIO22			( ) | ( ) 	GPIO23
	-- 				( ) | ( )	GPIO24 
	GPIO10 (MOSI)	( ) | ( ) 	--
	GPIO9 (MISO)	( ) | ( )	GPIO25 
	GPIO11 (SCKL)	( ) | ( ) 	GPIO18 (CE0)
	-- 				( ) | ( ) 	GPIO17 (CE1)
```