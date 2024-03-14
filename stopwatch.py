# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2018-2024 Ravener

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__author__ = "Ravener"
__version__ = "2.0.1"
__license__ = "MIT"

from time import monotonic as time_monotonic


class Stopwatch:
    digits: int

    def __init__(self, digits: int = 2):
        self.digits = digits

        self._start = time_monotonic()
        self._end = None

    @property
    def duration(self) -> float:
		if self._end:
			duration = self._end - self._start
		else:
			duration = time_monotonic() - self._start
		return round(duration, self.digits)

    @property
    def running(self) -> bool:
        return not self._end

    def restart(self) -> None:
        self._start = time_monotonic()
        self._end = None

    def reset(self) -> None:
        self._start = time_monotonic()
        self._end = self._start

    def start(self) -> None:
        if not self.running:
            self._start = time_monotonic() - self.duration
            self._end = None

    def stop(self) -> None:
        if self.running:
            self._end = time_monotonic()

    def __str__(self) -> str:
        time = self.duration

        if time >= 1.0:
            return "{:.{}f}s".format(time, self.digits)

        elif time >= 0.01:
            return "{:.{}f}ms".format(time * 1000, self.digits)

        return "{:.{}f}μs".format(time * 1000 * 1000, self.digits)
