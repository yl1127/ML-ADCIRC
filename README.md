# ML-ADCIRC

## Table of Contents
- [ML-ADCIRC](#ml-adcirc)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Usage](#usage)
    - [Method 1: Docker](#method-1-docker)
    - [Method 2: SMS](#method-2-sms)
  - [Summary of weekly meeting](#summary-of-weekly-meeting)
  - [Github Pages](#github-pages)

## Introduction
ML-ADCIRC is a project aimed at integrating machine learning techniques with the ADCIRC coastal ocean model to improve predictions and analyses. 

More about ADCIRC: https://adcirc.org/

## Usage

### Method 1: Docker

```bash
# Download the docker container image for ADCIRC
sudo docker pull zcobell/adcirc_20200513

# Clone ADCIRC source code
git clone https://github.com/adcirc/adcirc.git

# Run the docker container
sudo docker run -it -v /your/path/to/adcirc/:/workspace zcobell/adcirc_20200513

# Enter ADCIRC directory
cd adcirc

# Create a build directory
mkdir build

# Enter the build directory
cd build

# From within the build directory, run CMake to configure the build environment
# Be sure to specify the parent directory (where CMakeLists.txt is located)
cmake .. -DBUILD_ADCIRC=ON -BUILD_ADCPREP=ON

# After configuring with CMake, compile the code
make -j4

# Test ADCIRC
./adcirc
```

### Method 2: SMS

SMS (Surface water Modeling System): https://www.aquaveo.com/software/sms-surface-water-modeling-system-introduction

Tutorials: https://www.aquaveo.com/software/sms-learning-tutorials

## Summary of weekly meeting

(2024.11.27) [Group Meeting Presentation](yl_Groupmeeting_1127.pptx)

## Github Pages

Coming soon.

<!-- ## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information. -->