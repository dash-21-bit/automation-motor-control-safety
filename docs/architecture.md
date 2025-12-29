# Architecture

## Components
- **SafetySystem** (`src/safety_logic.py`)
  - Maintains emergency stop and fault latch state
  - Provides `is_safe_to_run()` gate for controller

- **MotorController** (`src/motor_control.py`)
  - Implements PLC-style scan cycle
  - Applies priority logic:
    1) Emergency stop
    2) Fault latch
    3) Stop
    4) Reset
    5) Start
  - Updates motor output + state

## Design Principles
- Safety overrides control commands
- Faults latch and require manual reset
- Inputs behave like momentary PLC signals
