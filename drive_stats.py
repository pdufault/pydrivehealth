#!/usr/bin/env python
from __future__ import print_function
import pySMART
import tabulate


def get_smart_attribute(drive, attribute):
  for driveattribute in drive.attributes:
    if not driveattribute:
      continue

    if driveattribute.name == attribute:
      return float(driveattribute.raw)


def get_drive_age(drive):
  hours = get_smart_attribute(drive, 'Power_On_Hours')
  return str("%8.2f" % (hours / 24 / 365)) + ' years'


def get_drive_temperature(drive):
  return get_smart_attribute(drive, 'Temperature_Celsius')


def get_drive_reallocated_sectors(drive):
  return get_smart_attribute(drive, 'Reallocated_Sector_Ct')


def display_drive_information(devlist):
  header = [ 'Name', 'Health', 'Model', 'Serial', 'Capacity', 'Temperature', 'Age (on)', 'Reallocated Sectors']
  data = []
  for device in devlist.devices:
    data.append(get_drive_information(device))

  print(tabulate.tabulate(data, header, 'rst'))


def get_drive_information(drive):
  temp = get_drive_temperature(drive)
  age = get_drive_age(drive)
  reallocated_sectors = get_drive_reallocated_sectors(drive)
  data = [ drive.name, drive.assessment, drive.model, drive.serial, drive.capacity, temp, age, reallocated_sectors ]
  return data


def main():
  devlist = pySMART.DeviceList()
  display_drive_information(devlist)

if __name__ == "__main__":
  main()
