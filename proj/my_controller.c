#include <stdio.h>
#include <webots/robot.h>
#include <webots/motor.h>
#include <webots/distance_sensor.h>
#include <webots/led.h>

#define TIME_STEP 256
#define QtddSensoresProx 8
#define QtddLeds 10

// Definindo a função para girar 90 graus
void virar90graus(WbDeviceTag MotorEsquerdo, WbDeviceTag MotorDireito, bool virar) {
  
  if(virar){
  
    // Para o robô:
    wb_motor_set_velocity(MotorEsquerdo, 0);
    wb_motor_set_velocity(MotorDireito, 0);
  
    // Faz com que o robô gire 90 graus para direita (aproximadamente 39 passos)
    for (float i = 0; i < 7.5; i++) {
      wb_robot_step(TIME_STEP);
      wb_motor_set_velocity(MotorEsquerdo, 6.28 * 1);
      wb_motor_set_velocity(MotorDireito, 6.28 * -1);
    }
    
    for (int j = 0; j < 5; j++) {
      wb_robot_step(TIME_STEP);
      wb_motor_set_velocity(MotorEsquerdo, 6.28 * 1);
      wb_motor_set_velocity(MotorDireito, 6.28 * 1);
    }
    
    for (float k = 0; k < 7; k++) {
      wb_robot_step(TIME_STEP);
      wb_motor_set_velocity(MotorEsquerdo, 6.28 * 1);
      wb_motor_set_velocity(MotorDireito, 6.28 * -1);
    }
  }
  
  else if(!virar){
  
    // Para o robô:
    wb_motor_set_velocity(MotorEsquerdo, 0);
    wb_motor_set_velocity(MotorDireito, 0);
  
    // Faz com que o robô gire 90 graus para esquerda (aproximadamente 39 passos)
    for (float i = 0; i < 7.5; i++) {
      wb_robot_step(TIME_STEP);
      wb_motor_set_velocity(MotorEsquerdo, 6.28 * -1);
      wb_motor_set_velocity(MotorDireito, 6.28 * 1);
    }
    
    for (int j = 0; j < 5; j++) {
      wb_robot_step(TIME_STEP);
      wb_motor_set_velocity(MotorEsquerdo, 6.28 * 1);
      wb_motor_set_velocity(MotorDireito, 6.28 * 1);
    }
    
    for (float k = 0; k < 7; k++) {
      wb_robot_step(TIME_STEP);
      wb_motor_set_velocity(MotorEsquerdo, 6.28 * -1);
      wb_motor_set_velocity(MotorDireito, 6.28 * 1);
    }
  }
}

int main(int argc, char **argv) {
  int i = 0;
  double LeituraSensorProx[QtddSensoresProx];
  double AceleradorDireito = 1.0, AceleradorEsquerdo = 1.0;
  bool sairDoQuadrado = true;
  
  wb_robot_init();

  // Motores:
  WbDeviceTag MotorEsquerdo = wb_robot_get_device("left wheel motor");
  WbDeviceTag MotorDireito = wb_robot_get_device("right wheel motor");

  wb_motor_set_position(MotorEsquerdo, INFINITY);
  wb_motor_set_position(MotorDireito, INFINITY);
  wb_motor_set_velocity(MotorEsquerdo, 0);
  wb_motor_set_velocity(MotorDireito, 0);

  // Sensores de Proximidade:
  WbDeviceTag SensorProx[QtddSensoresProx];
  SensorProx[0] = wb_robot_get_device("ps0");
  SensorProx[1] = wb_robot_get_device("ps1");
  SensorProx[2] = wb_robot_get_device("ps2");
  SensorProx[3] = wb_robot_get_device("ps3");
  SensorProx[4] = wb_robot_get_device("ps4");
  SensorProx[5] = wb_robot_get_device("ps5");
  SensorProx[6] = wb_robot_get_device("ps6");
  SensorProx[7] = wb_robot_get_device("ps7");

  for (i = 0; i < QtddSensoresProx; i++)
    wb_distance_sensor_enable(SensorProx[i], TIME_STEP);

  // LED:
  WbDeviceTag Leds[QtddLeds];
  Leds[0] = wb_robot_get_device("led0");
  wb_led_set(Leds[0], -1);

  while (wb_robot_step(TIME_STEP) != -1) {
    // Leitura dos sensores:
    printf("Sensor: ");
    for (i = 0; i < QtddSensoresProx; i++) {
      LeituraSensorProx[i] = wb_distance_sensor_get_value(SensorProx[i]) - 60;
      printf("%d: %.2f | ", i, LeituraSensorProx[i]);
    }
    printf("\n");

    wb_led_set(Leds[0], wb_led_get(Leds[0]) * -1);

    // Verifica o sensor da frente:
    if (LeituraSensorProx[0] > 100 && LeituraSensorProx[5] > 50){
      // Chama a função para girar 90 graus
      virar90graus(MotorEsquerdo, MotorDireito, true);
      sairDoQuadrado = false;
    } 
    
    else if(LeituraSensorProx[0] > 100 && LeituraSensorProx[2] > 50){
      // Chama a função para girar 90 graus
      virar90graus(MotorEsquerdo, MotorDireito, false);
      sairDoQuadrado = true;
    }
    
    else if(LeituraSensorProx[0] > 100 && sairDoQuadrado == true){
      virar90graus(MotorEsquerdo, MotorDireito, true);
      sairDoQuadrado = false;
      printf("Direita");
    }
    else if(LeituraSensorProx[0] > 100 && sairDoQuadrado == false){
      virar90graus(MotorEsquerdo, MotorDireito, false);
      sairDoQuadrado = true;
      printf("Esquerda");
    }
    else {
      // Continua o movimento para frente
      AceleradorDireito = 1;
      AceleradorEsquerdo = 1;
    }

    wb_motor_set_velocity(MotorEsquerdo, 6.28 * AceleradorEsquerdo);
    wb_motor_set_velocity(MotorDireito, 6.28 * AceleradorDireito);
  }

  wb_robot_cleanup();
  return 0;
}
