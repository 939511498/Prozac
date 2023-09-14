#include <Mouse.h>

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    ;
  }
  Mouse.begin();
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    processCommand(command);
  }
}

void processCommand(String command) {
  if (command.length() > 0) {
    if (command[0] == 'M') {
      int commaIndex = command.indexOf(",");
      if (commaIndex != -1) {
        int x = command.substring(1, commaIndex).toInt();
        int y = command.substring(commaIndex + 1).toInt();
        moveMouse(x, y);
      }
    }
  }
}

void moveMouse(int x, int y) {
  Mouse.move(x, y);
  Serial.write("ACK\n");
}
