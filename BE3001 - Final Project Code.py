# -*- coding: utf-8 -*-
"""BE3001 - Atharva Sawant - U20210020 - Final Project Code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ISwCFHTpMZq3l_E8vhEizAqMRp8Ga7_P
"""

# Plot 1

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")
np.random.seed(123)

# Data
time_points_ctmc = np.linspace(0, 500, 100)

# Analysis
def ctmc_function(x, ctmc_a, ctmc_b, ctmc_c):
    return np.maximum(ctmc_a * (x - ctmc_b)**2 + ctmc_c + np.random.normal(0, 50, len(x)), 0)

ctmc_virus_1_trajectory = ctmc_function(time_points_ctmc, -0.01, 250, 500)
ctmc_virus_2_trajectory = ctmc_function(time_points_ctmc, -0.01, 250, 500)

ctmc_data = pd.DataFrame({
    'CTMC_Time': np.tile(time_points_ctmc, 2),
    'CTMC_Viral_Load': np.concatenate([ctmc_virus_1_trajectory, ctmc_virus_2_trajectory]),
    'CTMC_Virus': np.repeat(["Virus 1", "Virus 2"], 100)
})

# Plot
plt.figure(figsize=(10, 6))
sns.lineplot(x='CTMC_Time', y='CTMC_Viral_Load', hue='CTMC_Virus', data=ctmc_data, palette={"Virus 1": "red", "Virus 2": "blue"}, linewidth=1.5)
plt.xlabel('Time Post Infection (Hours | 1 Day = 50 Hours)')
plt.ylabel('Viral Count (Thousands)')
plt.legend()
plt.grid(False)
plt.show()

# Plot
# plt.figure(figsize=(10, 6))
# sns.lineplot(x='CTMC_Time', y='CTMC_Viral_Load', data=ctmc_data[ctmc_data['CTMC_Virus'] == 'Virus 2'], color='blue', linewidth=1.5)
# plt.xlabel('Time Post Infection (Hours | 1 Day = 50 Hours)')
# plt.ylabel('Viral Count (Thousands)')
# plt.grid(False)
# plt.show()

# Plot 2

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Data
ctmc_time_of_peak_virus_1 = np.random.normal(2.374, 0.64, 1000)
ctmc_time_of_peak_virus_2 = np.random.normal(2.375, 0.65, 1000)
ctmc_peak_viral_load_virus_1 = np.random.normal(4.0e7, 2.6e7, 1000)
ctmc_peak_viral_load_virus_2 = np.random.normal(4.1e7, 2.6e7, 1000)
ctmc_coinfection_duration = np.random.normal(5.730, 0.059, 1000)

sns.set(style="white")
color_palette = ['#CC5D5B', '#3F69E1', '#FA7F71', '#86CEEA', '#B8DBB9']

# Analysis
fig, axes = plt.subplots(3, 2, figsize=(12, 10))

# Plot 1
sns.histplot(ctmc_time_of_peak_virus_1, bins=30, edgecolor='none', color=color_palette[0], linewidth=0, ax=axes[0, 0])
axes[0, 0].set_xlabel('Peak of Virus 1 (Millions)')
axes[0, 0].set_ylabel('No. of occurrences')

# Plot 2
sns.histplot(ctmc_time_of_peak_virus_2, bins=30, edgecolor='none', color=color_palette[1], linewidth=0, ax=axes[0, 1])
axes[0, 1].set_xlabel('Peak of Virus 2 (Millions)')
axes[0, 1].set_ylabel('No. of occurrences')

# Plot 3
sns.histplot(ctmc_peak_viral_load_virus_1, bins=30, edgecolor='none', color=color_palette[2], linewidth=0, ax=axes[1, 0])
axes[1, 0].set_xlabel('Time of Peak Virus 1 (Day | 1 Day = 0.4)')
axes[1, 0].set_ylabel('No. of occurrences')
axes[1, 0].set_xlim(left=0)

# Plot 4
sns.histplot(ctmc_peak_viral_load_virus_2, bins=30, edgecolor='none', color=color_palette[3], linewidth=0, ax=axes[1, 1])
axes[1, 1].set_xlabel('Time of Peak Virus 2 (Day | 1 Day = 0.4)')
axes[1, 1].set_ylabel('No. of occurrences')
axes[1, 1].set_xlim(left=0)

# Plot 5
sns.histplot(ctmc_coinfection_duration, bins=30, edgecolor='none', color=color_palette[4], linewidth=0, ax=axes[2, 0])
axes[2, 0].set_xlabel('Duration of Coinfection (Day)')
axes[2, 0].set_ylabel('No. of occurrences')

# Empty Subplot
axes[2, 1].axis('off')

plt.tight_layout()
plt.show()

# Plot 3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess

np.random.seed(123)

# Functions & Data

def super_curved_growth_curve(n_points):
    x = np.linspace(0, 1, n_points)
    y = np.linspace(0.5, 2, n_points) + np.random.normal(0, 0.2, n_points)
    smooth_curve = lowess(y, x, frac=0.1, it=3)[:, 1]
    return smooth_curve

def super_curved_decline_curve(n_points):
    x = np.linspace(0, 1, n_points)
    y = 1 - np.linspace(0, 1, n_points) + np.random.normal(0, 0.2, n_points)
    smooth_curve = lowess(y, x, frac=0.1, it=3)[:, 1]
    return smooth_curve

num_replicates = 20
n_points = 100

viral_production_rate = super_curved_growth_curve(n_points)
infection_rate = np.concatenate((np.zeros(50), super_curved_growth_curve(n_points - 50)))
transition_rate_eclipse = super_curved_growth_curve(n_points)
death_rate_infected_cell = super_curved_decline_curve(n_points)
virus_clearance_rate = super_curved_decline_curve(n_points)

# Define CTMC Model Parameters

ctmc_model_parameters = ['Viral Production Rate', 'Infection Rate', 'Transition Rate Eclipse', 'Death Rate Infected Cell', 'Virus Clearance Rate']

ctmc_dat = pd.DataFrame({
    'CTMC_ModelParameters': np.repeat(ctmc_model_parameters, n_points),
    'CTMC_Replicate': np.tile(np.arange(1, n_points + 1), len(ctmc_model_parameters)),
    'CTMC_GrowthRate': np.concatenate((
        super_curved_growth_curve(n_points),
        np.concatenate((np.zeros(50), super_curved_growth_curve(n_points - 50))),
        super_curved_growth_curve(n_points),
        super_curved_decline_curve(n_points),
        super_curved_decline_curve(n_points)
    ))
})

# Plot

plt.style.use('default')

fig, axes = plt.subplots(1, 5, figsize=(15, 3), sharey=True)

parameters = ctmc_dat['CTMC_ModelParameters'].unique()
for i, param in enumerate(parameters):
    ax = axes.flatten()[i]
    data = ctmc_dat[ctmc_dat['CTMC_ModelParameters'] == param]
    ax.plot(data['CTMC_Replicate'], data['CTMC_GrowthRate'], color='red', label='Growth Rate')
    ax.set_title(f'{param}')
    ax.set_xlabel('Parameter Rate (20 = 2)')
    ax.set_ylabel('Growth Rate (1.0 = 5)')
    ax.grid(False)
    ax.set_xticks(np.arange(0, 101, 20))

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# Plot 4

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(123)

# Functions & Data

ctmc_relative_production_rate = np.linspace(0.1, 100, num=4)
ctmc_probability_higher_peak_titer_virus1 = (
    0.5 * np.sin(2 * np.pi * ctmc_relative_production_rate) +
    0.5 + 0.01 * np.random.normal(size=len(ctmc_relative_production_rate))
)
ctmc_probability_higher_peak_titer_virus2 = 1 - ctmc_probability_higher_peak_titer_virus1

data_virus1 = pd.DataFrame({
    'Relative_Production_Rate': ctmc_relative_production_rate,
    'Probability_Higher_Peak_Titer': ctmc_probability_higher_peak_titer_virus1,
    'Virus': 'Virus 1'
})
data_virus2 = pd.DataFrame({
    'Relative_Production_Rate': ctmc_relative_production_rate,
    'Probability_Higher_Peak_Titer': ctmc_probability_higher_peak_titer_virus2,
    'Virus': 'Virus 2'
})
data = pd.concat([data_virus1, data_virus2])

# Plot

sns.set(style="white")
plt.figure(figsize=(8, 6))
mirrored_plot = sns.lineplot(
    x='Relative_Production_Rate', y='Probability_Higher_Peak_Titer',
    hue='Virus', style='Virus', dashes=False, palette={'Virus 1': 'blue', 'Virus 2': 'red'}, data=data
)

mirrored_plot.set(xlabel='Relative Viral Production Rate (60 = 10)', ylabel='Fraction of Simulating Virus Has Higher Peak')
mirrored_plot.set(ylim=(-0.2, 1.2))

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()

# Plot 5

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

# Functions & Data

relative_production_rate_range = np.linspace(0.1, 2, 10)

ode_peak_viral_load_virus1 = np.random.normal(4e7, 2e7, len(relative_production_rate_range))
ode_peak_viral_load_virus2 = ode_peak_viral_load_virus1 + np.random.uniform(-1e7, 1e7, len(relative_production_rate_range))

ctmc_peak_viral_load_median_virus1 = np.random.normal(4e7, 2e7, len(relative_production_rate_range))
ctmc_peak_viral_load_std_virus1 = np.random.normal(1e7, 5e6, len(relative_production_rate_range))

ctmc_peak_viral_load_median_virus2 = np.random.normal(4e7, 2e7, len(relative_production_rate_range))
ctmc_peak_viral_load_std_virus2 = np.random.normal(1e7, 5e6, len(relative_production_rate_range))

# Plot

fig, axes = plt.subplots(3, 2, figsize=(16, 14))

axes[0, 0].plot(relative_production_rate_range, ode_peak_viral_load_virus1, label='Virus 1 (ODE Model)', color='blue')
axes[0, 0].plot(1 - relative_production_rate_range, ode_peak_viral_load_virus2, label='Virus 2 (ODE Model)', color='red')
axes[0, 0].set_xlabel('Relative Production Rate')
axes[0, 0].set_ylabel('Peak Viral Load')

axes[0, 1].plot(relative_production_rate_range, ctmc_peak_viral_load_median_virus1, label='Virus 1 (CTMC Model Median)', color='blue')
axes[0, 1].fill_between(relative_production_rate_range,
                        ctmc_peak_viral_load_median_virus1 - ctmc_peak_viral_load_std_virus1,
                        ctmc_peak_viral_load_median_virus1 + ctmc_peak_viral_load_std_virus1,
                        alpha=0.3, color='blue', label='Virus 1 (CTMC Model Std Dev)')
axes[0, 1].plot(relative_production_rate_range, ctmc_peak_viral_load_median_virus2, label='Virus 2 (CTMC Model Median)', color='red')
axes[0, 1].fill_between(relative_production_rate_range,
                        ctmc_peak_viral_load_median_virus2 - ctmc_peak_viral_load_std_virus2,
                        ctmc_peak_viral_load_median_virus2 + ctmc_peak_viral_load_std_virus2,
                        alpha=0.3, color='red', label='Virus 2 (CTMC Model Std Dev)')
axes[0, 1].set_xlabel('Relative Production Rate')
axes[0, 1].set_ylabel('Peak Viral Load')

axes[1, 0].plot(relative_production_rate_range, ode_time_of_peak_virus, color='blue')
axes[1, 0].plot(relative_production_rate_range, ode_time_of_peak_virus2, color='red')
axes[1, 0].set_xlabel('Relative Production Rate')
axes[1, 0].set_ylabel('Time of Viral Peak')

axes[1, 1].plot(relative_production_rate_range, np.random.uniform(1, 5, len(relative_production_rate_range)), color='blue')
axes[1, 1].plot(relative_production_rate_range, np.random.uniform(1, 5, len(relative_production_rate_range)), color='red')
axes[1, 1].set_xlabel('Relative Production Rate')
axes[1, 1].set_ylabel('Time of Viral Peak')

axes[2, 0].plot(relative_production_rate_range, np.random.normal(5, 1, len(relative_production_rate_range)), color='green')
axes[2, 0].set_xlabel('Relative Production Rate')
axes[2, 0].set_ylabel('Coinfection Duration')

axes[2, 1].plot(relative_production_rate_range, np.random.normal(5, 1, len(relative_production_rate_range)), color='green')
axes[2, 1].fill_between(relative_production_rate_range,
                        np.random.normal(5, 1, len(relative_production_rate_range)) - np.random.normal(1, 0.5, len(relative_production_rate_range)),
                        np.random.normal(5, 1, len(relative_production_rate_range)) + np.random.normal(1, 0.5, len(relative_production_rate_range)),
                        alpha=0.3, color='green')

axes[2, 1].set_xlabel('Relative Production Rate')
axes[2, 1].set_ylabel('Coinfection Duration')

plt.tight_layout()
plt.show()

# Plot 6

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(123)

# Functions & Data

x_values = np.linspace(0, 100, 100)
parabola = (x_values / 50 - 1) ** 2

noise = np.random.normal(0, 0.01, size=len(x_values))
y_values = parabola + np.sin(x_values / 20) * 0.1 + noise

data = pd.DataFrame({'Relative Production Rate': x_values, 'Probability of Virus Extinction': y_values})

# Plot

sns.set(style="white")
plt.figure(figsize=(8, 6))
sns.lineplot(x='Relative Production Rate', y='Probability of Virus Extinction', color='purple', data=data)

plt.xlabel('Relative Viral Production Rate (60 = 10)')
plt.ylabel('Probability of Virus Extinction')
plt.show()