#include <Servo.h>

Servo serx;
Servo sery;

int anglex = 90;
int angley = 90;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  serx.attach(3);
  sery.attach(6);

  serx.write(90);
  sery.write(90);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {

    char c = Serial.read();
    if (c == 'l') {
      anglex = anglex - 5;
      Serial.println(anglex);
      serx.write(anglex);
    }
    else if (c == 'r') {
      anglex = anglex + 5;
      Serial.println(anglex);
      serx.write(anglex);
    }
    else if (c == 'u') {
      angley = angley - 5;
      Serial.println(angley);
      sery.write(angley);
    }
    else if (c == 'd'){
      angley = angley + 5;
      Serial.println(angley);
      sery.write(angley);
      }

    }
}
