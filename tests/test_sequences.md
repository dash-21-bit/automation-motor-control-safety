# Test Sequences (PLC-style)

## Test 1 — Normal Start/Stop
**Steps**
1. Press Start
2. Motor should RUN
3. Press Stop
4. Motor should go IDLE

**Expected**
- State transitions: IDLE -> RUNNING -> IDLE
- No faults or safety blocks

---

## Test 2 — Fault Latching Blocks Restart
**Steps**
1. Press Start (RUNNING)
2. Trigger fault
3. Try Start again (should be blocked)
4. Press Reset (fault clears)
5. Press Start (should run)

**Expected**
- Fault latches until Reset
- Cannot run while fault_latched = True

---

## Test 3 — Emergency Stop Highest Priority
**Steps**
1. Trigger E-Stop
2. Try Start (blocked)
3. Release E-Stop
4. Press Reset
5. Press Start (runs)

**Expected**
- E-Stop overrides everything
- Reset is blocked while E-Stop is active
