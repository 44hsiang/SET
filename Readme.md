install package 
numpy matplotlib pyvisa qcode qcodes_contrib_drivers zhinst-qcodes  pyvisa-py

ZI related material
https://docs.zhinst.com/zhinst-qcodes/en/latest/index.html
https://docs.zhinst.com/labone_api_user_manual/index.html

QDAC related material
https://qm.quantum-machines.co/87kjeif6
https://qcodes.github.io/Qcodes_contrib_drivers/examples/QDevil/QDAC2/index.html

preamp IV converter
https://www.baspi.ch/low-noise-high-stab-itov-conv

Qcode:
https://microsoft.github.io/Qcodes/index.html
print_readable_snapshot() #useful command

plottr installation
1.	Run the following lines in the conda prompt
- conda activate qcodes
- pip install plottr==0.14.0
- pip install pyqt5
2.	Run the following command to show the plottr interface in the conda prompt
- conda activate qcodes
- plottr-inspectr
