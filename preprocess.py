import os
import torch
import torchvision
import numpy as np
from torchvision.transforms import Resize, ToTensor, Compose

# Définir la transformation pour redimensionner et convertir les images en tenseurs
transform = Compose([
    Resize((64, 64)),  # Redimensionner toutes les images à 64x64
    ToTensor()         # Convertir les images en tenseurs
])

# Charger les images et les labels sous forme de tuples (imageTensor, label)
images = torchvision.datasets.ImageFolder(
    root='Data',
    transform=transform
)

# Mélanger les tuples
idx = np.arange(len(images))
np.random.shuffle(idx)
img = [images[i] for i in idx]

# Diviser les données
Total_samples = len(images)
Train_samples = int(Total_samples * 0.6)
CV_samples = int(Total_samples * 0.2)
Test_samples = Total_samples - Train_samples - CV_samples

print(Total_samples, Train_samples, CV_samples, Test_samples)

def save_as_tensor(images, start, samples, Itname, Ltname):
    # Créer le répertoire si nécessaire
    os.makedirs(os.path.dirname(Itname), exist_ok=True)
    
    # Initialiser les tenseurs pour les images et les labels
    imgt = torch.zeros((samples, *images[0][0].shape))
    lblt = torch.zeros((samples, 1))
    
    for i in range(samples):
        imgt[i] = images[start + i][0]
        lblt[i] = images[start + i][1]
    
    # Sauvegarder les tenseurs
    torch.save(imgt, Itname)
    torch.save(lblt, Ltname)

# Sauvegarder les images et les labels dans les fichiers spécifiés
save_as_tensor(img, 0, Train_samples, 'Tensors/train_img.pt', 'Tensors/train_lbl.pt')
save_as_tensor(img, Train_samples, CV_samples, 'Tensors/val_img.pt', 'Tensors/val_lbl.pt')
save_as_tensor(img, CV_samples, Test_samples, 'Tensors/test_img.pt', 'Tensors/test_lbl.pt')
