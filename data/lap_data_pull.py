import matplotlib.pyplot as plt
import fastf1 as ff
import fastf1.plotting as ffp

ffp.setup_mpl(misc_mpl_mods=False, color_scheme="fastf1")

session = ff.get_session(2019, "Monza", "Q")

session.load()

fast_leclerc = session.laps.pick_drivers("LEC").pick_fastest()
lec_car_data = fast_leclerc.get_car_data()
t = lec_car_data["Time"]
vCar = lec_car_data["Speed"]

# plotting
fig, ax = plt.subplots()
ax.plot(t, vCar, label="Fast")
ax.set_xlabel("Time")
ax.set_ylabel("Speed [km/h]")
ax.set_title("Leclerc's Lap Timings")
ax.legend()
plt.show()
