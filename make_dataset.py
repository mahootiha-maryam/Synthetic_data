from monai.transforms import (
    RandBiasField,
    RandAdjustContrast,
    RandGaussianNoise,
    RandGaussianSmooth,
    RandGaussianSharpen,
    RandGibbsNoise,
    RandKSpaceSpikeNoise,
    Affine,
    Rotate90,
    Flip
)


import os
import numpy as np
import nibabel as nib
from pathlib import Path

def aug1(randomnumber, randforrot, randforflip):
    
    if randomnumber==0:
        changer1 = Affine(shear_params=(0, 0.5, 0), image_only=True, padding_mode='zeros' )
        
    if randomnumber==1:
        changer1 = Rotate90(k=randforrot, spatial_axes=(0, 1))
        
    if randomnumber==2:
        changer1 = Flip(spatial_axis= randforflip)
        
    return changer1

    
def aug2(randomnumber):

    if randomnumber==0:
        changer2 = RandBiasField(prob=1, coeff_range=(0.1, 0.3))
    if randomnumber==1:
        changer2 = RandAdjustContrast(prob=1, gamma=(1.5,2))
    
    return changer2

def aug3(randomnumber):
    if randomnumber==0:
        changer3 = RandGaussianNoise(prob=1, mean=0.0, std=0.1)
    if randomnumber==1:
        changer3 = RandGaussianSmooth(prob=1, sigma_x=(1,2))
    if randomnumber==2:
        changer3 = RandGaussianSharpen(prob=1)
    if randomnumber==3:
        changer3 = RandGibbsNoise(prob=1, alpha=(0.6, 0.8))
    if randomnumber==4:
        changer3 = RandKSpaceSpikeNoise(prob=1, intensity_range=(10,13))
        
    return changer3 


aug1list = ['RandAffine','RandRotate90','RandFlip']
aug2list = ['RandBiasField','RandAdjustContrast']
aug3list = ['RandGaussianNoise','RandGaussianSmooth','RandGaussianSharpen','RandGibbsNoise','RandKSpaceSpikeNoise']

######################################################################################
'class 0'
# source_dir_im = Path('/home/mary/Documents/kidney_ds/new_classes/class0/image')
# source_dir_lb = Path('/home/mary/Documents/kidney_ds/new_classes/class0/label')

# dest_dir_im = Path('/home/mary/Documents/kidney_ds/synthetic_data/class0/image')
# dest_dir_lb = Path('/home/mary/Documents/kidney_ds/synthetic_data/class0/label')

# names_class0 = sorted(os.listdir(source_dir_im))
# names_class0_lb = sorted(os.listdir(source_dir_lb))

# for i,item in enumerate(names_class0):
#     rannumaug1 = np.random.randint(len(aug1list))
#     rannumaug2 = np.random.randint(len(aug2list))
#     rannumaug3 = np.random.randint(len(aug3list))
    
#     randforrot = np.random.randint(1,4)
#     randforflip = np.random.randint(2)
    
#     changer1 = aug1(rannumaug1, randforrot, randforflip)
    
#     changer2 = aug2(rannumaug2)
    
#     changer3 = aug3(rannumaug3)

#     mydir = source_dir_im/item
#     nifti_image = nib.load(mydir)
#     nn = nifti_image.get_fdata()

#     mydir1 = source_dir_lb/names_class0_lb[i]
#     nifti_image1 = nib.load(mydir1)
#     nn1 = nifti_image1.get_fdata()
    
#     lb = changer1(nn1)
    
#     newim_L1 = changer1(nn)
#     newim_L2 = changer2(newim_L1)
#     newim_L3 = changer3(newim_L2)

#     name_im = names_class0[i][:12]+'_0'+'.nii.gz' 
#     name_lb = names_class0_lb[i][:10]+'_0'+'.nii.gz'
    
#     processed_nifti = nib.Nifti1Image(newim_L3, nifti_image.affine)
#     nib.save(processed_nifti, dest_dir_im/name_im)
    
#     processed_nifti1 = nib.Nifti1Image(lb, nifti_image.affine)
#     nib.save(processed_nifti1, dest_dir_lb/name_lb)
######################################################################################
'class 1'

# source_dir_im = Path('/home/mary/Documents/kidney_ds/new_classes/class1/image')
# source_dir_lb = Path('/home/mary/Documents/kidney_ds/new_classes/class1/label')

# dest_dir_im = Path('/home/mary/Documents/kidney_ds/synthetic_data/class1/image')
# dest_dir_lb = Path('/home/mary/Documents/kidney_ds/synthetic_data/class1/label')

# names_class1 = sorted(os.listdir(source_dir_im))
# names_class1_lb = sorted(os.listdir(source_dir_lb))

# for j in range(3):
    
#     for i,item in enumerate(names_class1):
#         rannumaug1 = np.random.randint(len(aug1list))
#         rannumaug2 = np.random.randint(len(aug2list))
#         rannumaug3 = np.random.randint(len(aug3list))
        
#         randforrot = np.random.randint(1,4)
#         randforflip = np.random.randint(2)
        
#         changer1 = aug1(rannumaug1, randforrot, randforflip)
        
#         changer2 = aug2(rannumaug2)
        
#         changer3 = aug3(rannumaug3)
    
#         mydir = source_dir_im/item
#         nifti_image = nib.load(mydir)
#         nn = nifti_image.get_fdata()
    
#         mydir1 = source_dir_lb/names_class1_lb[i]
#         nifti_image1 = nib.load(mydir1)
#         nn1 = nifti_image1.get_fdata()
        
#         lb = changer1(nn1)
        
#         newim_L1 = changer1(nn)
#         newim_L2 = changer2(newim_L1)
#         newim_L3 = changer3(newim_L2)
    
#         name_im = names_class1[i][:12]+'_{}'.format(j)+'.nii.gz' 
#         name_lb = names_class1_lb[i][:10]+'_{}'.format(j)+'.nii.gz'
        
#         processed_nifti = nib.Nifti1Image(newim_L3, nifti_image.affine)
#         nib.save(processed_nifti, dest_dir_im/name_im)
        
#         processed_nifti1 = nib.Nifti1Image(lb, nifti_image.affine)
#         nib.save(processed_nifti1, dest_dir_lb/name_lb)
#         print(i)
######################################################################################
'class 2'

source_dir_im = Path('/home/mary/Documents/kidney_ds/new_classes/class2/image')
source_dir_lb = Path('/home/mary/Documents/kidney_ds/new_classes/class2/label')

dest_dir_im = Path('/home/mary/Documents/kidney_ds/synthetic_data/class2/image')
dest_dir_lb = Path('/home/mary/Documents/kidney_ds/synthetic_data/class2/label')

names_class2 = sorted(os.listdir(source_dir_im))
names_class2_lb = sorted(os.listdir(source_dir_lb))

for j in range(3):
    
    for i,item in enumerate(names_class2):
        rannumaug1 = np.random.randint(len(aug1list))
        rannumaug2 = np.random.randint(len(aug2list))
        rannumaug3 = np.random.randint(len(aug3list))
        
        randforrot = np.random.randint(1,4)
        randforflip = np.random.randint(2)
        
        changer1 = aug1(rannumaug1, randforrot, randforflip)
        
        changer2 = aug2(rannumaug2)
        
        changer3 = aug3(rannumaug3)
    
        mydir = source_dir_im/item
        nifti_image = nib.load(mydir)
        nn = nifti_image.get_fdata()
    
        mydir1 = source_dir_lb/names_class2_lb[i]
        nifti_image1 = nib.load(mydir1)
        nn1 = nifti_image1.get_fdata()
        
        lb = changer1(nn1)
        
        newim_L1 = changer1(nn)
        newim_L2 = changer2(newim_L1)
        newim_L3 = changer3(newim_L2)
    
        name_im = names_class2[i][:12]+'_{}'.format(j)+'.nii.gz' 
        name_lb = names_class2_lb[i][:10]+'_{}'.format(j)+'.nii.gz'
        
        processed_nifti = nib.Nifti1Image(newim_L3, nifti_image.affine)
        nib.save(processed_nifti, dest_dir_im/name_im)
        
        processed_nifti1 = nib.Nifti1Image(lb, nifti_image.affine)
        nib.save(processed_nifti1, dest_dir_lb/name_lb)
        print(i)