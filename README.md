# pydrivehealth
pydrivehealth

This script shows show these attributes on all disks attached to your Linux system:
* SMART health
* capacity
* temperature
* age
* how many sectors in the disk have been reallocated
* model and serial numbers

## Show me

```
$ sudo ./pydrivehealth.py
9 devices detected
===  ======  ========  ==========  =============  ==========  =====================
  #  Name    Health    Capacity    Temperature    Age (on)      Reallocated Sectors
===  ======  ========  ==========  =============  ==========  =====================
  0  sda     PASS      4.00 TB     32.0C          0.22 years                      0
  1  sdb     PASS      4.00 TB     35.0C          4.34 years                      2
  2  sde     PASS      4.00 TB                    1.52 years                     10
  3  sdf     PASS      4.00 TB     31.0C          0.22 years                      0
  4  sdg     PASS      4.00 TB     36.0C          1.05 years                      0
  5  sdh     PASS      4.00 TB     38.0C          1.84 years                      0
  6  sdi     PASS      4.00 TB     34.0C          5.71 years                      0
  7  sdj     PASS      4.00 TB     31.0C          0.22 years                      0
  8  sdk     PASS      4.00 TB     30.0C          2.46 years                      0
===  ======  ========  ==========  =============  ==========  =====================
```

## Why
Personal yak shave project

## TODO

Keep track of disks, so disk failure is easy to track
