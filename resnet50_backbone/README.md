# 🧬 Self-Supervised Cervical Image Pretraining (SimCLR + ResNet50)

This project implements a **SimCLR-based self-supervised learning pipeline** to pretrain a **ResNet50 encoder** on unlabeled cervical images. The learned representation is later reused as a backbone for downstream tasks like:

- VIA lesion segmentation  
- Cervical abnormality classification  

---

## 📁 Repository Structure

| File/Folder | Description |
|------------|-------------|
| `SimCLR_pretraining.ipynb` | Full SimCLR training workflow (augmentations, loss, checkpoints). |
| `checkpoints/` | Automatically saved encoder + projection head weights. |
| `data/` | *(Not included)* Expected directory for raw/unlabeled image dataset. |

---

## 🚀 Training Process

1. Apply SimCLR augmentations (crop, color jitter, blur, noise).  
2. Pass augmented pairs through:
   - **ResNet50 encoder**
   - **Projection MLP head**
3. Optimize using **NT-Xent (contrastive) loss** with cosine similarity.  
4. Save:
   - Full SSL checkpoint  
   - Backbone-only `.pth` file for downstream models  

---

## ⚙️ Requirements

- Python ≥ 3.9  
- PyTorch ≥ 2.0  
- GPU recommended (CUDA + AMP supported)

I ran this code on Colab GPU, which is why I have connected the drive. The code can be modified if you plan on running it locally. 

## 🎯 Using the Pretrained Encoder

After training, you can:

- Freeze the encoder for feature extraction  
- Finetune with classification or segmentation heads  
- Plug into YOLO / EfficientNet workflows  

---

## 📌 Citation

If you reference this work, please cite:

> Chen et al., *A Simple Framework for Contrastive Learning of Visual Representations (SimCLR)*, 2020.
