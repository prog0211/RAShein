import json
import matplotlib.pyplot as plt
import numpy as np
from contextlib import redirect_stdout
import xml.etree.cElementTree as ET
import os

if __name__ == '__main__':
    A = 0
    x = np.linspace(-5.12,5.12,1000)
    y = (1+np.cos(12*np.sqrt(x**2+A**2)))/(0.5*(x**2+A**2)+2)
    plt.plot(x,y)
    plt.show()

    root = ET.Element("data")

    for i in range(len(x)):
        freq = ET.SubElement(root, "row")
        ET.SubElement(freq, "x").text = "{}".format(x[i])
        ET.SubElement(freq, "y").text = "{}".format(y[i])

if not os.path.exists('results'):
    os.mkdir('results')
    os.chdir(os.path.join(os.getcwd(), 'results'))
    tree = ET.ElementTree(root)
    ET.indent(tree, '  ')
    tree.write("prog0211.1.xml", encoding="utf-8", xml_declaration=True)
