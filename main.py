from battery.core import Battery

def main():
    # Create a battery object
    bat = Battery(capacity_mwh=2, power_mw=2, efficiency=0.9)

    print("Initial SOC:", bat.get_soc_percent(), "%")

    # Simulate 1 hour of charging
    bat.charge(p=0.5, dt=1)
    print("After charging 0.5 MW for 1h:", bat.get_soc_percent(), "%")

    # Simulate 1 hour of discharging
    bat.discharge(p=1, dt=1)
    print("After discharging 1 MW for 1h:", bat.get_soc_percent(), "%")

if __name__ == "__main__":
    main()
