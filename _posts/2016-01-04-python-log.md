---
layout: post
title: Logging with python
---

I always forget how to configure logging with Python. So here is how:

	import logging
	logging.basicConfig(format='%(asctime)-%(levelname)s:%(message)s', level=logging.DEBUG)


This setup will allow you to print the time, followed by the debug level and the message, this is more or less what you need for basic logging in the console. Remember that printing messages on the screen is not a good practise contrary to logging. For more information about logging you can check [Python's documentation](https://docs.python.org/2/howto/logging.html) and Victor Lin's [excellent howto](http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python)