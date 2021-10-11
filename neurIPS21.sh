#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l mem=2g
#PBS -l walltime=24:00:00
#PBS -N bactXpat
#PBS -q cgsd
## conda install anndata, scanpy, scvelo, leidenalg

##curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
##unzip awscliv2.zip
##sudo ./aws/install
##aws s3 sync s3://openproblems-bio/public/ $HOME/data/ --no-sign-request
##cp -r ~/data/* /content/drive/MyDrive/
##wget https://github.com/openproblems-bio/neurips2021_multimodal_viash/releases/latest/download/starter_kit-match_modality-python.zip
##unzip starter_kit-match_modality-python.zip data/

python run/neurIPS.py