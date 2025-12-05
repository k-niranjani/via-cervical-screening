# 🧪 Model Testing Suite

This folder contains a complete testing pipeline for evaluating both segmentation and classification models used in the VIA Cervical Screening project. These notebooks allow any user to load models, run inference on test images, generate metrics, and visualize predictions — all without needing the original training scripts.

---

## 📁 Folder Structure

```
for_testing/
│
├── testing_segmentation.ipynb        # Notebook for YOLOv8 segmentation model testing
├── testing_classification.ipynb      # Notebook for ResNet50 + EfficientHead classifier testing
│
├── models/                           # Folder for your model weights (NOT tracked in GitHub)
│     └── README.md                   # Instructions for placing model .pt/.pth files here
│
└── testing_images/                   # Folder for testing images + CSV labels
      ├── README.md                   # Instructions for placing test images + test_tags.csv
      ├── *.jpg / *.png               # Test images
      └── test_tags.csv               # Ground-truth labels for classification testing
```

---

### ⚠️ Note

The `models/` and `testing_images/` folders are intentionally empty in the remote repo (GitHub).  
Place your local model files and images in these folders before running the notebooks.

---

## 🚀 1. Segmentation Testing (YOLOv8)

**Notebook:** `testing_segmentation.ipynb`

This notebook:

- Loads YOLOv8-based segmentation models  
  - `best_yolov8m_resnet.pt`  
  - `best_yolov8s.pt`
- Runs inference on all images inside `testing_images/`
- Saves annotated outputs (masks + bounding boxes) into:

```
for_testing/segmentation_testing_outputs/<model_name>/
```

- Provides utilities to:
  - Visualize predictions for single images  
  - Compare two models side-by-side  
  - Evaluate segmentation quality qualitatively  

### Requirements

```
pip install ultralytics matplotlib pillow
```

---

## 🔍 2. Classification Testing (ResNet50 + EfficientHead)

**Notebook:** `testing_classification.ipynb`

This notebook:

- Loads a ResNet50 classifier with a custom Efficient-style head  
- Loads ground-truth labels from `testing_images/test_tags.csv`
- Runs prediction on each test image  
- Produces:
  - Accuracy  
  - Classification report  
  - Confusion matrix (raw + normalized)  
  - Visualizations of correct/misclassified examples  
  - Probability histograms per image  

### Requirements

```
pip install torch torchvision pandas scikit-learn matplotlib pillow
```

---

## 📥 Placing Your Models and Test Data

### Put segmentation models here:

```
for_testing/models/
  ├── best_yolov8m_resnet.pt
  └── best_yolov8s.pt
```

### Put classification model here:

```
for_testing/models/
  └── resnet_backbone_efficient_head_best.pth
```

### Put your testing images + CSV here:

```
for_testing/testing_images/
  ├── via_img_001.jpg
  ├── via_img_002.jpg
  ├── ...
  └── test_tags.csv
```

The `image` column in `test_tags.csv` must match the exact filenames in this folder.

---

## 💡 Notes

- The testing notebooks do *not* require the training pipeline.  
- The notebooks automatically detect and validate missing files.  
- Large model files and images are intentionally ignored by Git to avoid repository size issues.  

---

## ✅ Summary

This folder provides a reproducible, simple, and portable environment to evaluate:

- **Segmentation performance** (mask quality, visualization)  
- **Classification performance** (accuracy, precision/recall/F1, confusion matrix)

Use these notebooks as your standardized testing framework for all future models in the VIA Cervical Screening project.
