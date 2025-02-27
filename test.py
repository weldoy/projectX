from datetime import datetime
import sys


while True:
    now = datetime.now()
    sys.stdout.write("\r{}".format(now.strftime("%H-%M-%S")))
    sys.stdout.flush()
