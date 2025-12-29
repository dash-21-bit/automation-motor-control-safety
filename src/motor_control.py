from safety_logic import SafetySystem
class MotorController:
    """
    Simple PLC-style motor controller using safety interlocks.
    Priority order:
      1) E-Stop
      2) Fault
      3) Stop
      4) Start
    """

    def __init__(self):
        self.safety = SafetySystem()
        self.motor_running = False
        self.state = "IDLE"

    def start(self):
        if self.safety.is_safe_to_run():
            self.motor_running = True
            self.state = "RUNNING"
            print("[START] Motor running")
        else:
            print("[BLOCKED] Cannot start: E-Stop or Fault active")

    def stop(self):
        self.motor_running = False
        self.state = "IDLE"
        print("[STOP] Motor stopped")

    def emergency_stop(self):
        self.safety.trigger_emergency_stop()
        self.motor_running = False
        self.state = "EMERGENCY_STOP"
        print("[E-STOP] Emergency stop activated. Motor OFF.")

    def fault_trip(self):
        self.safety.trigger_fault()
        self.motor_running = False
        self.state = "FAULT"
        print("[FAULT] Fault latched. Motor OFF.")

def reset(self):
    if self.safety.emergency_stop:
        print("[RESET BLOCKED] Release E-Stop first.")
        return

    if self.safety.fault_latched:
        self.safety.reset_fault()
        print("[RESET] Fault cleared. Ready to start.")
    else:
        print("[RESET] No fault active. System ready.")

    self.state = "IDLE"
    

def demo_sequence():
    mc = MotorController()

    print("\n--- Normal Start/Stop ---")
    mc.start()
    mc.stop()

    print("\n--- Fault Latching Demo ---")
    mc.start()
    mc.fault_trip()
    mc.start()          # should be blocked
    mc.reset()
    mc.start()          # should start

    print("\n--- Emergency Stop Demo ---")
    mc.emergency_stop()
    mc.start()          # blocked
    mc.safety.clear_emergency_stop()
    mc.reset()
    mc.start()          # should start


if __name__ == "__main__":
    demo_sequence()
