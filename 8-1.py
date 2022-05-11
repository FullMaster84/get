import numpy as np
import matplotlib.pyplot as plt

volt = []
data = np.loadtxt ('data.txt', dtype = int)
volt = [i / 256 * 3.3 for i in data]
with open ('settings.txt', mode = 'r') as setting:
    frequency = float(setting.read().split('\n')[0])
print (frequency)

x = np.linspace(0, len(volt)*frequency, len (volt))
volt = np.array(volt)
max_elem = np.argmax(volt)
zaryad = frequency * (max_elem + 1)
razryad = frequency * (len(volt) - max_elem - 1)
time = frequency * len(volt)




title = 'Процесс зарядки и разрядки конденсатора'

fig, ax = plt.subplots()
ax.plot(x, volt, 'r.-', label = 'V(t)')
ax.text(0.7 * time, 2.5, f'Время зарядки = {zaryad} c.')
ax.text(0.7 * time, 2.2, f'Время разрядки = {razryad} c.')
ax.minorticks_on()
ax.grid(which = 'major',
        color = 'k',
        linewidth = 1)
ax.grid(which = 'minor',
        color = 'k',
        linestyle = ':')
ax.set(xlim = (x.min(), x.max()), ylim = (volt.min(), volt.max()))
plt.title (title, wrap = True)
fig.set_figwidth(12)
fig.set_figheight(8)
plt.xlabel('Время, с')
plt.ylabel('Напряжение, В')
plt.legend()
plt.show()
fig.savefig('graph.svg')
fig.savefig('graph.png')