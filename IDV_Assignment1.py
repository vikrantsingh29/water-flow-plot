from matplotlib import pyplot as plt
import numpy as np

waterFlowDataArray = []
flowFigure = plt.figure()
plotAxes = plt.axes()

with open("field2.irreg", 'r') as file:
    for individualList in file:
        ListSplit = individualList.split(" ")
        dataArrayFromList = np.asarray(ListSplit, dtype=np.float)
        for x in dataArrayFromList[5:]:
            waterFlowDataArray.append(dataArrayFromList)

file.close()

for i in range(0, 6724):
    plotAxes.arrow(waterFlowDataArray[i][0], waterFlowDataArray[i][1],
                   waterFlowDataArray[i][3], waterFlowDataArray[i][4],
                   fc ='blue',clip_on = 1,
                   ec='red', head_length=0.01,
                   head_width=0.01,linewidth = 0.03)

plt.title("Water Particle Movement")
plt.grid()
plt.show()
flowFigure.savefig('dataPlot', dpi=500)
