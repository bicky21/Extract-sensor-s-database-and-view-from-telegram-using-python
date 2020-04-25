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
    boltiot.begin(Serial); //Initialize the Bolt interface over serial uart. Serial could be replaced with Serial0 or Serial1 on Arduino mega boards.
         //In this example Tx pin of Bolt is connected to Rx pin of Arduino Serial Port
         //and Rx pin of Bolt is connected to tx pin of arduino Serial Port
    pinMode(2,INPUT); //Set pin 2 as input. We will send this pin's state as the data to the Bolt Cloud
  }

  void loop() {
     digitalWrite(trigPin, LOW);
     delayMicroseconds(2);
     digitalWrite(trigPin, HIGH);
     delayMicroseconds(10);
     digitalWrite(trigPin, LOW);
     duration = pulseIn(echoPin, HIGH);
     distanceCm = duration * 0.0340 / 2;
     Serial.print(distanceCm,DEC);
     Serial.print("\n");
     delay(5000);
  }
