import signal
# Test signal.setitimer()
#
# This test is not very good, because it depends on the system clock,
# and the system clock may be too coarse to measure the timer.
#
# The test is also not very good because it depends on the system
# scheduler.  On some systems, the scheduler may be too busy to
# schedule the signal handler in time.
#
# On some systems, the system clock may be too coarse to measure
# the timer.
#
# On some systems, the system clock may jump backwards.
#
# On some systems, the system clock may jump forwards.
#
# On some systems, the system clock may be adjusted by NTP.
#
# On some systems, the system clock may be adjusted by the user.
#
# On some systems, the system clock may be adjusted by the kernel.
#
# On some systems, the system clock may be adjusted by the hardware.
#
# On some systems, the system clock may be adjusted by the BIOS.
#
# On some systems, the system clock may be adjusted by ACPI.
#
# On some systems, the system clock may be adjusted by the power supply
