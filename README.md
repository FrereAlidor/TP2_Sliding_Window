# Cars Detection
IFI-VNU: Computer Vision Project : TP2

Implementation of a sliding window model using CNN for object detection in our case: cars.

* Data-set included - Vehicles and Non-Vehicles (approx 8k each).
* Sample test images included.
* Sample video included.

### Run instructions

* Download data zip files and code files.
* Extract vehicles and non-vehicles into `Data/`.

```shell
python3 ./preprocess.py# Détecteur de visage et d'pbjet avec la technique sliding windows



## Demarrage


### Cloner le project

Tout d'abord, vous devez cloner le projet sur votre ordinateur avec :


https://github.com/FrereAlidor/TP2_Sliding_Window.git


Vous pouvez maintenant vous déplacer dans le dossier nouvellement créé :

cd TP2_Sliding_Window


### Create a virtual environment


1. Create a new virtual environment

python3 -m venv venv


2. Activate the virtual environment

source env/bin/activate


Assurez-vous que l'environnement virtuel est activé chaque fois que vous voulez lancer le projet.

### Install all requirements

Les dépendances du projet sont stockées dans le fichier requirements.txt. Vous pouvez les installer avec la commande suivante :

*WARNING* :  Vérifiez que votre environnement virtuel est activé, sinon vous installerez les paquets à l'échelle du système.

pip install -r requirements.txt



### Start Project


python3 ./preprocess.py
python3 ./train.py
python3 ./sw_algorithm.py


*Note:* le projet utiliser Python3.


Vous pouvez maintenant visiter le rep "SW_Test_Output" pour voir les resultats.




