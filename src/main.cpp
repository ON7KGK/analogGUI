#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  analogReadResolution(12); // Résolution de 12 bits pour les entrées ADC
}

void loop() {
  int adcValue1 = analogRead(A0); // Lire la valeur analogique de la broche A0
  int adcValue2 = analogRead(A1); // Lire la valeur analogique de la broche A1

  // Envoyer les valeurs analogiques via le port série
  Serial.print("ADC1: ");
  Serial.print(adcValue1);
  Serial.print(" ADC2: ");
  Serial.println(adcValue2);

  delay(1000); // Attendre 1 seconde avant de lire à nouveau
}
