class Battery:
    """Simple battery model to track energy and state of charge."""

    def __init__(self, capacity_mwh, power_mw, efficiency=0.9):
        # Battery characteristics
        self.capacity = capacity_mwh     # energy capacity [MWh]
        self.power = power_mw             # max charge/discharge power [MW]
        self.efficiency = efficiency      # round-trip efficiency

        # Dynamic state
        self.soc = 0.5 * self.capacity    # initial state of charge [MWh]

    def charge(self, p, dt=1):
        """Charge the battery by power p [MW] during dt [h]."""
        energy_added = self.efficiency * p * dt
        self.soc = min(self.capacity, self.soc + energy_added)

    def discharge(self, p, dt=1):
        """Discharge the battery by power p [MW] during dt [h]."""
        energy_removed = p * dt / self.efficiency
        self.soc = max(0, self.soc - energy_removed)

    def get_soc_percent(self):
        """Return SOC as a percentage of total capacity."""
        return 100 * self.soc / self.capacity
