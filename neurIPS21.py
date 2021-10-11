import anndata as ad
import numpy as np
import pandas as pd
import logging
from sklearn.decomposition import TruncatedSVD
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
##import scanpy as sc
import matplotlib.pyplot as plt
from matplotlib.pyplot import rc_context
from sklearn.preprocessing import RobustScaler

train_GEX1 = ad.read_h5ad("data/phase1-data/match_modality/openproblems_bmmc_multiome_phase1_rna/openproblems_bmmc_multiome_phase1_rna.censor_dataset.output_train_mod1.h5ad")
train_ATAC1 = ad.read_h5ad("data/phase1-data/match_modality/openproblems_bmmc_multiome_phase1_rna/openproblems_bmmc_multiome_phase1_rna.censor_dataset.output_train_mod2.h5ad")

test_GEX1 = ad.read_h5ad("data/phase1-data/match_modality/openproblems_bmmc_multiome_phase1_rna/openproblems_bmmc_multiome_phase1_rna.censor_dataset.output_test_mod1.h5ad")
test_ATAC1 = ad.read_h5ad("data/phase1-data/match_modality/openproblems_bmmc_multiome_phase1_rna/openproblems_bmmc_multiome_phase1_rna.censor_dataset.output_test_mod2.h5ad")

print("data loaded")
print([train_GEX1.shape,train_ATAC1.shape])


scaler=RobustScaler()
train_GEX1.X = scaler.fit_transform(train_GEX1.X.toarray())
train_GEX1.write('data/train_GEX1.h5ad')
train_ATAC1.X = scaler.fit_transform(train_ATAC1.X.toarray())
train_ATAC1.write('data/train_ATAC1.h5ad')
test_GEX1.X = scaler.fit_transform(test_GEX1.X.toarray())
test_GEX1.write('data/test_GEX1.h5ad')
test_ATAC1.X = scaler.fit_transform(test_ATAC1.X.toarray())
test_ATAC1.write('data/test_GEX1.h5ad')
