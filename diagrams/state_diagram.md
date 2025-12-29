# Motor Control State Diagram (PLC-Style)

This diagram shows the high-level states and transitions for the motor controller.

## States
- IDLE
- RUNNING
- FAULT (latched)
- EMERGENCY_STOP

## State diagram


          +-------+
          | IDLE  |
          +---+---+
            |
       Start |
            v
      +-----+------+
      |  RUNNING   |
      +-----+------+
       |     |
  Stop |     | Fault
       v     v
    +--+--+  +---------+
    | IDLE |  |  FAULT  |
    +-----+  +----+-----+
                |
              Reset
                |
                v
              IDLE


    +------------------+
    | EMERGENCY_STOP   |
    +------------------+
## Control priority
1) Emergency Stop  
2) Fault latch  
3) Stop  
4) Reset  
5) Start  

