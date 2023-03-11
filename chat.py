import matplotlib.pyplot as plt
import numpy as np

# define the qualities and persons
qualities = ['MH', 'MN', 'MZ', 'ME']
persons = ['Ashish Pundir' ,'Vikas Sharma' , 'Kacper Paruch']

# define the data for each person
person1_data = [20, 40, 60, 80]
person2_data = [30, 50, 70, 90]
person3_data = [40, 60, 80, 100]

# create a figure and polar axis object
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# define the number of qualities and angles for the radar chart
num_qualities = len(qualities)
angles = np.linspace(0, 2*np.pi, num_qualities, endpoint=False)

# close the radar chart by appending the first angle to the end
angles = np.concatenate((angles, [angles[0]]))

# plot the radar chart for each person
ax.set_theta_offset(np.pi/2)
ax.set_theta_direction(-1)
for i, person_data in enumerate([person1_data, person2_data, person3_data]):
    data = np.concatenate((person_data, [person_data[0]]))
    ax.plot(angles, data, label=persons[i])
    ax.fill(angles, data, alpha=0.2)

# add the legend and title
plt.legend(loc='upper right')
plt.title("Comparison of Qualities")

# add the qualities to the radar chart
plt.xticks(angles[:-1], qualities)

# set the limit of the radar chart
plt.ylim(0, 100)

# display the radar chart
plt.show()
