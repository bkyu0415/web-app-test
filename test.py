import time
import tzlocal
from datetime import datetime

a = datetime.fromtimestamp(time.time(), tzlocal.get_localzone()).strftime("%A,%B %d,%Y %H:%M:%S %p %Z %z")

#t =time.strftime("%A,%B %d,%Y %H:%M:%S %p GMT %Z%z", time.gmtime())
print a