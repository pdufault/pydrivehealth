#!/usr/bin/env python
from __future__ import print_function
import pySMART
import tabulate
import os
import sys
import pwd
import argparse

def get_smart_attribute(drive, attribute):
  for driveattribute in drive.attributes:
    if not driveattribute:
      continue
    if driveattribute.name == attribute:
      return float(driveattribute.raw)


def get_drive_age(drive):
  hours = get_smart_attribute(drive, 'Power_On_Hours')
  return str('%8.2f' % (hours / 24 / 365)) + ' years'


def get_drive_temperature(drive):
  temp = get_smart_attribute(drive, 'Temperature_Celsius')
  if temp:
    temp = str(temp) + 'C'
  return temp


def get_drive_reallocated_sectors(drive):
  return get_smart_attribute(drive, 'Reallocated_Sector_Ct')


def display_drive_information(devlist, verbose):
  header = ['Name', 'Health', 'Model', 'Capacity', 'Temperature', 'Age (on)', 'Reallocated Sectors']
  if verbose:
    header = ['Name', 'Health', 'Model', 'Serial', 'Capacity', 'Temperature', 'Age (on)', 'Reallocated Sectors']
  data = [ header ]
  for device in devlist.devices:
    data.append(get_drive_information(device, verbose))

  print('{0} drives online'.format(len(devlist.devices)))
  print(tabulate.tabulate(data, 'firstrow' , 'rst'))


def get_drive_information(drive, verbose):
  '''
  Arguments are:
   * drive, a pySMART devicelist object, and
   * verbose, a boolean flag that increases the number of disk attributes this function returns
  Returns an array of 
  '''

  temp = get_drive_temperature(drive)
  age = get_drive_age(drive)
  reallocated_sectors = get_drive_reallocated_sectors(drive)

  if verbose:
    data = ( drive.name, drive.assessment, drive.model, drive.serial, drive.capacity, temp, age, reallocated_sectors )
#    data = [ drive.name, 'PASS', 'XXXXXXXXX', 'XXXXXXXXXXXXXX', drive.capacity, temp, age, reallocated_sectors ]
  else:
    data = ( drive.name, drive.assessment, drive.model, drive.capacity, temp, age, reallocated_sectors )
#    data = [ drive.name, 'PASS', '4.00 TB' , temp, age, reallocated_sectors ]

  return data


def main():
  '''
  Ensure this script is run as root, so that it can query disk information.
  Parse arguments and then display information on the disk drives in the system
  '''

  if os.getuid() != 0:
    raise RuntimeError('Run this script as root, as it needs to query disks.\nsudo {0}'.format(sys.argv[0]))

  parser = argparse.ArgumentParser(description='A script to display disk attributes')
  parser.add_argument('-v', '--verbose', action='store_true', help='Show verbose disk attributes view') 
  args = parser.parse_args()

  devlist = pySMART.DeviceList()
  display_drive_information(devlist, args.verbose)

if __name__ == '__main__':
  main()

