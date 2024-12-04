# Video Momment Retrieval for IID and OOD for Multimodal AI



## Requiments

- pytorch
- h5py
- nltk
- fairseq

## Quick Start

### Data Preparation

```
data
├── activitynet
│   ├── sub_activitynet_v1-3.c3d.hdf5
│   ├── glove.pkl
│   ├── train_data.json
│   ├── val_data.json
│   ├── test_data.json
├── charades
│   ├── i3d_features.hdf5
│   ├── glove.pkl
│   ├── train.json
│   ├── test.json
```

## [Chrades_STA ID and OOD]
### Training
```bash
python train.py
```

### Inference
```bash
python train.py --eval --resume ./checkpoints/charades/my/model-best.pt 
```

This work was partly supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government(MSIT) (No. 2022R1A2C2012706)


