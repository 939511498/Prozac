#include <Mouse.h>

void setup() {
  Serial.begin(115200);
  Mouse.begin();
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    processCommand(command);
  }
}

void processCommand(String command) {
  if (command == "CLICK") {
    Mouse.click();
  } else {
    int commaIndex = command.indexOf(",");
    if (commaIndex != -1) {
      int x = command.substring(0, commaIndex).toInt();
      int y = command.substring(commaIndex + 1).toInt();
      Mouse.move(x, y);
      Serial.write("ACK\n");
    }
  }
}
