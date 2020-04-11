uint32_t tme_duration;
uint32_t tme_pre;
uint32_t tme_well_us;
uint16_t tme_rec;
uint16_t tme_well;
boolean current_state;
boolean pre_state;
boolean venture_inside;
boolean non_vent_inside;
const uint16_t x=2000;
const uint32_t y=2000000;
uint16_t RPM;
uint8_t counter;
float kmph;
float temp_kmph;

void setup() {
  
pinMode(8,INPUT);
Serial.begin(115200);
pre_state=HIGH;
venture_inside=false;
tme_pre=0;
temp_kmph=0;

}

void loop() {

 current_state = digitalRead(8);
  if (pre_state != current_state)
  {
    if ( current_state == LOW)
    {
      tme_duration = (micros() - tme_pre);
      RPM = (60000000/tme_duration);
      venture_inside=true;
      non_vent_inside = false;
      counter++;
      tme_pre = micros();
     }
    else 
    {
      venture_inside =false;
      non_vent_inside = true;
      tme_rec=millis();
    }
  }
  pre_state = current_state;
  tme_well_us = micros() - tme_pre;
  tme_well=millis()- tme_rec;
  
  if (venture_inside== false && tme_well > x)  //This checks if the motor has stopped
    {
      RPM=0;
    }
    
     if (non_vent_inside== false && tme_well_us > y)  //This if clause checks if the motor has stopped in fromt of the sensor
    {
      RPM=0;
    }
    
  kmph=RPM*0.12; //Assuming a circumference of the wheel = 2m, converting RPM to KMPH
  
  if (kmph != temp_kmph & counter%2==0)
  {
    Serial.println(kmph);
    temp_kmph=kmph;
  }
 
  if (counter=255) counter=0;
 
}
