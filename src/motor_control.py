from src.safety_logic import SafetySystem


class MotorController:
    """
    PLC-style motor controller using safety interlocks.
    Priority order:
      1) E-Stop
      2) Fault
      3) Stop
      4) Reset
      5) Start
    """

    def __init__(self):
        self.safety = SafetySystem()
        self.motor_running = False
        self.state = "IDLE"

        # Momentary input signals (like PLC inputs)
        self.start_button = False
        self.stop_button = False
        self.reset_button = False

    def scan_cycle(self):
        """Simulates a PLC scan cycle: read inputs -> apply priority logic -> update outputs"""

        # 1) Emergency stop has highest priority
        if self.safety.emergency_stop:
            self.motor_running = False
            self.state = "EMERGENCY_STOP"
            self._clear_buttons()
            return

        # 2) Fault latching has second priority
        if self.safety.fault_latched:
            self.motor_running = False
            self.state = "FAULT"
            # Allow reset button to clear fault (if E-stop is not active)
            if self.reset_button:
                self.reset()
            self._clear_buttons()
            return

        # 3) Normal stop
        if self.stop_button:
            self.stop()

        # 4) Reset (when no fault latched, reset just returns to IDLE)
        if self.reset_button:
            self.reset()

        # 5) Start
        if self.start_button:
            self.start()

        # Clear momentary inputs after scan
        self._clear_buttons()

    def _clear_buttons(self):
        self.start_button = False
        self.stop_button = False
        self.reset_button = False

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

    def release_emergency_stop(self):
        self.safety.clear_emergency_stop()
        print("[E-STOP] Emergency stop released")

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

    print("\n--- Normal Start/Stop (Scan Cycle) ---")
    mc.start_button = True
    mc.scan_cycle()
    mc.stop_button = True
    mc.scan_cycle()

    print("\n--- Fault Latching Demo (Scan Cycle) ---")
    mc.start_button = True
    mc.scan_cycle()
    mc.fault_trip()
    mc.start_button = True
    mc.scan_cycle()  # should remain blocked

    mc.reset_button = True
    mc.scan_cycle()  # clears fault

    mc.start_button = True
    mc.scan_cycle()  # should start

    print("\n--- Emergency Stop Demo (Scan Cycle) ---")
    mc.emergency_stop()
    mc.start_button = True
    mc.scan_cycle()  # blocked

    mc.release_emergency_stop()
    mc.reset_button = True
    mc.scan_cycle()

    mc.start_button = True
    mc.scan_cycle()


if __name__ == "__main__":
    demo_sequence()

