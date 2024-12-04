# Video Momment Retrieval for IID and OOD for Multimodal AI


### Charades-STA (ID) and (OOD)

| Method  | Rank1@0.3 | Rank1@0.5 | Rank1@0.7 | Rank5@0.3 | Rank5@0.5 | Rank5@0.7 |
| :-----: | :-------: | :-------: | :-------: | :-------: | :-------: | :-------: |
|   TVMR (ID)  |   66.40   |   49.24   |   22.39   |   96.99   |   84.71   |   52.37   |
| TVMR (OOD)    |   65.99   |   49.05   |   22.61   |   96.99   |   84.71   |   52.37   |

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

[Chrades_STA]
### Training
```bash
python train.py
```

### Inference
```bash
python train.py --eval --resume ./checkpoints/charades/my/model-best.pt 
```

This work was partly supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government(MSIT) (No. 2022R1A2C2012706)


