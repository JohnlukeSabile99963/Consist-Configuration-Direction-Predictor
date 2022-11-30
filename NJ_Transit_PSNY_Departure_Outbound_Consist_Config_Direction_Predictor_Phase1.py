import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import svm
from sklearn import tree
import random
import csv
import openpyxl
import numpy as np

# This program is responsible for predicting the configuration direction of
# outbound North Jersey Coast Line and Northeast Corridor
# NJ Transit Trains from Penn Station NY to Rahway, South Amboy,
# Long Branch, Bay Head, Jersey Avenue, and Trenton.


# Create Departure Dataframe for Outbound NJCL and NEC Trains
Outbound_NJCL_NEC_DPS_DF = pd.read_csv("NJ_Transit_Outbound_PSNY_Departures.csv")


# The Train ID, Line Served, Destination, Departure Timing, number of stops en route,
# and Service Class are all known. However, the Configuration Direction remains unknown.
# The passengers who board will only find out the configuration direction after they proceed
# to the announced boarding track number.
# Direction Configuration refers to whether a locomotive is pulling or pushing a set of Comets or Multi-Levels
# in the outbound direction per scheduled departure.
Outbound_NJCL_NEC_DPS_DF['Configuration Direction'] = pd.Series(random.choices(['R', 'W'],
                                                                               weights=[1, 1],
                                                                               k=len(Outbound_NJCL_NEC_DPS_DF)))

# Outbound_NJCL_NEC_DPS_DF.to_excel("NJT_NJCL_NEC_Outbound_Departures.xlsx", header=True)
# new_departure_df = pd.ExcelWriter("NJT_NJCL_NEC_Outbound_Departures.xlsx")
# Outbound_NJCL_NEC_DPS_DF.to_excel(new_departure_df, index=False)
# print(new_departure_df)
print(Outbound_NJCL_NEC_DPS_DF)

print("\nTotal # of Outbound PSNY Departures:", len(Outbound_NJCL_NEC_DPS_DF), "\n")

# Train ID is not necessary for visualizations.
# We will predict the Configuration Direction, so it is also not necessary to include in visualizations.

Outbound_NJCL_NEC_DPS_DF.drop(["Train ID:"], axis=1)
Outbound_NJCL_NEC_DPS_DF.drop(["Configuration Direction"], axis=1)


# Visualize Departure Data with Pairplot:


plt.figure(1)
sns.countplot(data=Outbound_NJCL_NEC_DPS_DF, x="Configuration Direction", hue="Line")

# Lines:
# M&E = Morris & Essex Line, or Morristown Line. Gladstone Branch Services included.
#  Termini include Summit, Dover, Peapack, and Gladstone.
# MOBO = Montclair-Boonton Line. Terminus is Montclair State University, or MSU.
# NJCL = North Jersey Coast Line. Termini include Rahway, South Amboy, Long Branch, and Bay Head.
# NEC = Northeast Corridor Line. Termini include Rahway, Jersey Avenue, and Trenton Transit Center.

plt.title("NJ Transit Outbound Departures from Penn Station")
plt.xlabel("Configuration Direction Class: R for 'Right' Consist Direction, W for 'Wrong' Consist Direction")
plt.ylabel("Trains Per Line")
plt.show()


plt.figure(2)
sns.countplot(data=Outbound_NJCL_NEC_DPS_DF, x="Configuration Direction", hue="Destination")
plt.title("NJ Transit Outbound Departures from Penn Station")
plt.xlabel("Configuration Direction Class: R for 'Right' Consist Direction, W for 'Wrong' Consist Direction")
plt.ylabel("Trains Per Destination from PSNY")
plt.show()


plt.figure(3)
sns.countplot(data=Outbound_NJCL_NEC_DPS_DF, x="Configuration Direction", hue="Service Day")
plt.title("NJ Transit Outbound Departures from Penn Station")
plt.xlabel("Configuration Direction Class: R for 'Right' Consist Direction, W for 'Wrong' Consist Direction")
plt.ylabel("Trains Per Service Period")
plt.show()


plt.figure(4)
sns.countplot(data=Outbound_NJCL_NEC_DPS_DF, x="Configuration Direction", hue="Departure Timing")
plt.title("NJ Transit Outbound Departures from Penn Station")
plt.xlabel("Configuration Direction Class: R for 'Right' Consist Direction, W for 'Wrong' Consist Direction")
plt.ylabel("Trains Per Departure Time")
plt.show()


plt.figure(5)
sns.countplot(data=Outbound_NJCL_NEC_DPS_DF, x="Configuration Direction", hue="Stations Stopped at En Route")
plt.title("NJ Transit Outbound Departures from Penn Station")
plt.xlabel("Configuration Direction Class: R for 'Right' Consist Direction, W for 'Wrong' Consist Direction")
plt.ylabel("Trains Per Stopped Station Count")
plt.show()


plt.figure(6)
sns.countplot(data=Outbound_NJCL_NEC_DPS_DF, x="Configuration Direction", hue="Service Class")
# If skipped stations < 3, Service Class = Local.
# Semi-Local and Express services may vary.
plt.title("NJ Transit Outbound Departures from Penn Station")
plt.xlabel("Configuration Direction Class: R for 'Right' Consist Direction, W for 'Wrong' Consist Direction")
plt.ylabel("Trains Per Service Class")
plt.show()


plt.figure(7)
sns.countplot(data=Outbound_NJCL_NEC_DPS_DF, x="Configuration Direction",
              hue="Expected Travel Time Range (Mins)")
# Expected Travel Time Range refers to time taken to operate from Penn Station to respective destination.
# In real time, time ranges often may vary due to circumstances beyond the crew control.
plt.title("NJ Transit Outbound Departures from Penn Station")
plt.xlabel("Configuration Direction Class: R for 'Right' Consist Direction, W for 'Wrong' Consist Direction")
plt.ylabel("Trains Per Service Class")
plt.show()


plt.figure(8)
sns.countplot(data=Outbound_NJCL_NEC_DPS_DF, x="Configuration Direction",
              hue="Distance Covered (Miles)")
# Distance Covered in intervals of 5.
plt.title("NJ Transit Outbound Departures from Penn Station")
plt.xlabel("Configuration Direction Class: R for 'Right' Consist Direction, W for 'Wrong' Consist Direction")
plt.ylabel("Trains Per Service Class")
plt.show()

