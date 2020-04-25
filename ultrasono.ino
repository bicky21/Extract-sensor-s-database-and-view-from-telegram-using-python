#include<BoltIoT-Arduino-Helper.h>
#include <BoltDeviceCredentials.h>
#define trigPin 12
#define echoPin 13
float time=0,distance=0;
long duration;
int distanceCm;
int pin1;
void setup() {
    pinMode(trigPin,OUTPUT);
    pinMode(echoPin,INPUT);
    Serial.begin(9600);
    Serial.setTimeout(50);
    boltiot.begin(Serial); //Communication
    pinMode(2,INPUT);
  }

  void loop() {
     digitalWrite(trigPin, LOW);
     delayMicroseconds(2);
     digitalWrite(trigPin, HIGH);
     delayMicroseconds(10);
     digitalWrite(trigPin, LOW);
     duration = pulseIn(echoPin, HIGH);
     distanceCm = duration * 0.0340 / 2;
     Serial.print(distanceCm);
     Serial.print("\n");
     delay(5000);
  }
