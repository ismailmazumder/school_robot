#include <ESP8266WiFi.h>

// SSID and password for the access point
const char *ssid = "ESP8266_Chat";
const char *password = "12345678";

// Create a Wi-Fi server on port 1234
WiFiServer server(1234);

void setup() {
  // Start serial communication
  Serial.begin(9600);
  Serial.println();

  // Configure the ESP8266 as an access point
  WiFi.softAP(ssid, password);

  // Start the TCP server
  server.begin();
  Serial.println("TCP Server started");

  // Get and display the IP address of the access point
  IPAddress IP = WiFi.softAPIP();
  Serial.print("Access Point IP address: ");
  Serial.println(IP);
}

void loop() {
  // Check if a client has connected
  WiFiClient client = server.available();
  if (client) {
    Serial.println("New Client Connected");

    while (client.connected()) {
      // Check if the client has sent any data
      if (client.available()) {
        // Read the message sent by the client
        String message = client.readStringUntil('\n');

        // Print the message to the Serial Monitor
        Serial.print("Received from client: ");
        Serial.println(message);

        // Echo the message back to the client
        client.print("ESP: ");
        client.println(message);
      }
    }

    // Close the connection
    client.stop();
    Serial.println("Client Disconnected");
  }
}
