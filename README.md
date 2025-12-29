# PLC Motor Control & Safety System (Simulation)

This project simulates a PLC-style motor control system with industrial safety logic.
It demonstrates start/stop control, emergency stop behaviour, fault latching, and safe restart conditions.

## Objectives
- Implement PLC-style control logic and safety interlocks
- Model emergency stop priority and fault handling
- Document system design clearly for automation interviews

## Inputs
- Start button
- Stop button
- Emergency Stop (E-Stop)
- Fault signal (e.g., overload)
- Reset button

## Outputs
- Motor ON/OFF
- Fault indicator
- System state (IDLE / RUNNING / FAULT / EMERGENCY_STOP)

## Tech
- Python (logic simulation)
- State-based control design (PLC-style thinking)

## Run
```bash
python src/motor_control.py#
## Test Scenarios
- Normal start/stop
- Fault latching and reset (restart blocked until reset)
- Emergency stop override (restart blocked until E-stop released)
