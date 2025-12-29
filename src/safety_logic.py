class SafetySystem:
    """
    PLC-style safety logic:
    - Emergency stop overrides everything
    - Fault latches until reset
    """

    def __init__(self):
        self.emergency_stop = False
        self.fault_latched = False

    def trigger_emergency_stop(self):
        self.emergency_stop = True

    def clear_emergency_stop(self):
        self.emergency_stop = False

    def trigger_fault(self):
        self.fault_latched = True

    def reset_fault(self):
        self.fault_latched = False

    def is_safe_to_run(self) -> bool:
        return (not self.emergency_stop) and (not self.fault_latched)
