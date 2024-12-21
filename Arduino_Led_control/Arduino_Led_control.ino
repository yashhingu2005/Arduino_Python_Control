const int led = 3;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    char command = Serial.read();
    if (command == '1') {
      digitalWrite(led, HIGH);
    }
    else if (command == '0') {
      digitalWrite(led, LOW);
    }
  }
}
