# ML-ADCIRC

## Table of Contents
- [ML-ADCIRC](#ml-adcirc)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Usage](#usage)
    - [Method 1: Docker](#method-1-docker)
    - [Method 2: SMS](#method-2-sms)
  - [Summary of weekly meeting](#summary-of-weekly-meeting)
    - [2025.1.22](#2025122)
    - [2025.1.15](#2025115)
    - [2025.1.8](#202518)
    - [2024.12.18](#20241218)
    - [2024.11.27](#20241127)
  - [Github Pages](#github-pages)
  - [License](#license)

## Introduction
ML-ADCIRC is a project aimed at integrating machine learning techniques with the ADCIRC coastal ocean model to improve predictions and analyses. 

![ADCIRC Demo](/docs/ADCIRC-demo-1218.gif)

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

### [2025.1.22](/docs/yl_Groupmeeting_0122.pdf)
- Literature review: Flood forecasting
  - Blog: https://sites.research.google/gr/floodforecasting/
  - Paper: https://www.nature.com/articles/s41586-024-07145-1
  - Talk: https://youtu.be/xskF3ggRxog?si=nN6N_D8yKPRvB7_x

- Towards a Science Exocortex 
  -  https://arxiv.org/pdf/2406.17809

### 2025.1.15
- Method 1: Visualization (Chengyi)
  - Visualization of ADCIRC Model Data in Vector Formats
  - https://github.com/ccht-ncsu/Kalpana

### [2025.1.8](/docs/yl_Groupmeeting_0108.pdf)
- Satellite
  - [Climate](/docs/climate_satellite.pptx)
  - [Sea level](/docs//sealevel_satellite.pptx)
- HindCast
  - https://www.designsafe-ci.org/data/browser/public/designsafe.storage.published/PRJ-3932
- Literature review: Flood forecasting
  - Blog: https://sites.research.google/gr/floodforecasting/
  - Paper: https://www.nature.com/articles/s41586-024-07145-1
  - Talk: https://youtu.be/xskF3ggRxog?si=nN6N_D8yKPRvB7_x

### [2024.12.18](/docs/yl_Groupmeeting_1218.pptx)
- Method 2: SMS ADCIRC demo 
- Output visualization
- Literature review and GitHub


### [2024.11.27](/docs/yl_Groupmeeting_1127.pptx)
- Method 1: Docker
- ADCIRC documents
  - [input file](https://adcirc.org/home/documentation/users-manual-v53/input-file-descriptions/
  )
  - [output file](https://adcirc.org/home/documentation/users-manual-v53/output-file-descriptions/
  )
- Literature review from Ruyi


## Github Pages

Coming soon.

<!-- ## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information. -->

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
