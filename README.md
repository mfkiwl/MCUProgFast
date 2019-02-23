# MCUProgFast
 MCU programmer using CMSIS-DAP (DAPLink), using Keil MDK's *.FLM Flashing Algorithm

to run this software, you need python 2.7 and pyqt4 
![](https://github.com/XIVN1987/MCUProgFast/blob/master/%E6%88%AA%E5%9B%BE.jpg)

FlashAlgo/flash_algo.py is used to parse Keil MDK's *.FLM file and extract code and its runing information into a python dict. And then you can modify the generated code to add new device support.
