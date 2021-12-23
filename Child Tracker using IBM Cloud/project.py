import wiotp.sdk.device
import json
import time

myConfig={
    "identity": {
        "orgId":"dmj7hp",
        "typeId":"Device",
        "deviceId":"12345"
        
    },
    "auth":{
        "token":"12345678"
    }
}
client=wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
  
  #              in area
  #name="NAZIM ANSARI"
  #latitude=17.4226372
  #longitude=78.5456505
  #               out area
  name="pratham barot"
  latitude=17.4126772
  longitude=78.5479505
  myData={'name': name, 'lat': latitude, 'lon': longitude}
  client.publishEvent(eventId="status", msgFormat="json", data=myData, onPublish=None)
  print("data published", myData)
  time.sleep(3)
client.disconnect()