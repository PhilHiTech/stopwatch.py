Stopwatch.py
============
A simple stopwatch for Python.

Install
-------
Requires Python 3.5+

.. code:: sh

   pip install git+https://github.com/PhilHiTech/stopwatch.py.git

Usage
-----
.. code:: py

    from stopwatch import Stopwatch

    # Argument specifies decimal precision
    # e.g 2 digits = 1.00, 3 digits = 1.000
    # Optional, defaults to 2
    stopwatch = Stopwatch(2) # Start a stopwatch
    # It's just math with time.perf_counter_ns() so there isn't really a task
    # running in background

    stopwatch.stop() # Stop stopwatch, time freezes
    stopwatch.start() # Start it again
    stopwatch.reset() # Reset it back to 0
    stopwatch.restart() # Reset and start again
    stopwatch.running # Whether stopwatch is running
    stopwatch.duration_str_secs # Get the duration (in seconds) rounded to Stopwatch(n) digits, into string type
    str(stopwatch) # Get a friendly duration string

License
-------
MIT
