# ML-ADCIRC

## Table of Contents
- [ML-ADCIRC](#ml-adcirc)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [To do:](#to-do)
  - [Usage](#usage)
    - [Method 1: Docker](#method-1-docker)
    - [Method 2: SMS](#method-2-sms)
  - [Summary of weekly meeting](#summary-of-weekly-meeting)
    - [2025.3.7](#202537)
    - [2025.1.31](#2025131)
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

## To do:
- **Benchmark** Find the state-of-the-art costal Flood forecasting as benchmark
  - ~~SOMAS(0213)~~
    - ~~Stony Brook Storm Surge Research Group~~ https://stormy.msrc.sunysb.edu/
  <!-- - NOAA (prediction)
    - Tide Predictions https://tidesandcurrents.noaa.gov/tide_predictions.html
    - Water Levels https://tidesandcurrents.noaa.gov/stations.html?type=Water+Levels
    - Coastal Inundation Dashboard https://tidesandcurrents.noaa.gov/inundationdb_info.html
  - Physical models (Ocean Global Circulation Models OGCMs)
    - NEMO ocean engine https://zenodo.org/records/3248739
  - Data-driven models
    - XiHe https://arxiv.org/abs/2402.02995
    - GLONET https://arxiv.org/abs/2412.05454
    - Statistics-free interpolation of ocean observations with deep spatio-temporal prior https://ceur-ws.org/Vol-3343/paper1.pdf
    - Multimodal unsupervised spatiotemporal interpolation of satellite ocean altimetry maps https://www.scitepress.org/PublishedPapers/2023/116201/116201.pdf
    - Synthesizing Sea Surface Temperature and Satellite Altimetry Observations Using Deep Learning Improves the Accuracy and Resolution of Gridded Sea Surface Height Anomalies https://doi.org/10.1029/2022MS003589
    - Pre-training and Fine-tuning Attention Based Encoder Decoder Improves Sea Surface Height Multi-variate Inpainting https://hal.sorbonne-universite.fr/hal-04475205
    - ORCAst https://arxiv.org/abs/2501.12054
  - Hybrid -->

- **Model**
  - ~~Run the open source [code](https://github.com/google-research-datasets/global_streamflow_model_paper)(0204)~~
    - ~~Figure out how it works(0212)~~
    - ~~Run the neuralhydrology models(0211)~~ https://github.com/neuralhydrology/neuralhydrology
    ~~- Train a LSTM [model](https://github.com/neuralhydrology/neuralhydrology) using CORA [dataset](https://github.com/NOAA-CO-OPS/CORA-Coastal-Ocean-ReAnalysis-CORA).~~


- **Dataset** (Train&Eval)
  ~~- CORA (Target)~~ https://tidesandcurrents.noaa.gov/cora.html
    - ~~Download the CORA dataset(0205)~~
    - ~~Figure it out~~
  - ERA5 (Other weather variables)
  <!-- - Satellite
    - DUACS DT2018 https://os.copernicus.org/articles/15/1207/2019/
    - Surface Water and Ocean Topography (SWOT) https://swot.jpl.nasa.gov/
    - Daily NeurOST L4 Sea Surface Height and Surface Geostrophic Currents https://podaac.jpl.nasa.gov/dataset/NEUROST_SSH-SST_L4_V2024.0
    - Global Ocean Along Track L 3 Sea Surface Heights Nrt https://data.marine.copernicus.eu/product/SEALEVEL_GLO_PHY_L3_NRT_008_044/description -->


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

### [2025.3.7](/docs/yl_Groupmeeting_0307.pdf)
- Recent progress
- Plan
- Challenges

### [2025.1.31](/docs/yl_Groupmeeting_0131.pdf)
- A Web-tool for Regional Sea Level Forecast for All Global Coastal Communities (Prof Zhu's email)
- Dataset: CORA
  - link: https://tidesandcurrents.noaa.gov/cora.html
  - code: https://github.com/NOAA-CO-OPS/CORA-Coastal-Ocean-ReAnalysis-CORA



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
