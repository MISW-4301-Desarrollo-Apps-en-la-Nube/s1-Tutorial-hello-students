
import time
from datetime import datetime

print("Bienvenidos al curso desarrollo de aplicaciones nativas en la nube versión 0.0.3")
while True:
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(f"Consulta de logs contenedora versión 0.0.3 a las {current_time}")
  time.sleep(2)