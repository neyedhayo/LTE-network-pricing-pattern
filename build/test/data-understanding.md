# LTE Dataset Information

## Column names & Description

* **Timestamp:** timestamp of sample
  
* **Longitude and Latitude:** GPS coordinates of mobile device
  
* **Velocity:** velocity in kph of mobile device
  
* **Operatorname:** cellular operator name (anonymised)
  
* **CellId:** Serving cell for mobile device
  
* **NetworkMode:** mobile communication standard (2G/3G/4G)
  
* **RSRQ:** value for RSRQ. RSRQ Represents a ratio between RSRP and Received Signal Strength Indicator (RSSI). Signal strength (signal quality) is measured across all resource elements (RE), including interference from all sources (dB).
  
* **RSRP:** value for RSRP. RSRP Represents an average power over cell-specific reference symbols carried inside distinct RE. RSRP is used for measuring cell signal strength/coverage and therefore cell selection (dBm).
  
* **RSSI:** value for RSSI. RSSI represents a received power (wideband) including a serving cell and interference and noise from other sources. RSRQ, RSRP and RSSI are used for measuring cell strength/coverage and therefore cell selection (handover) (dBm).
  
* **SNR:** value for signal-to-noise ratio (dB).
  
* **CQI:** value for CQI of a mobile device. CQI is a feedback provided by UE to eNodeB. It indicates data rate that could be transmitted over a channel (highest MCS with a BLER probability less than 10%), as the function of SINR and UE’s receiver characteristics. Based on UE’s prediction of the channel, eNodeB selects an appropriate modulation scheme and coding rate.
  
* **DL_bitrate:** download rate measured at the device (application layer) (kbit/s)
  
* **UL_bitrate:** uplink rate measured at the device (application
layer) (kbit/s)

* **State:** state of the download process. It has two values, either
I (idle, not downloading) or D (downloading)

* **NRxRSRQ & NRxRSRP:** RSRQ and RSRP values for the neighbouring cell.
  
* **Cell_Longitude & Cell_Latitude:** GPS coordinates of serving
eNodeB. We use OpenCellid4 , the largest community open database providing GPS coordinates of cell towers.

* **Distance:** distance between the serving cell and mobile device in metres.
