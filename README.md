# Multiway Classification with Real Data
Application of the R package **cpfa** to four real datasets.

Author: Matthew Asisgress

Package URL: <https://CRAN.R-project.org/package=cpfa>.

## Overview

We apply R package **cpfa** (Asisgress, 2026) to four real datasets. First, we 
apply the package to MNIST (LeCun, Cortes, and Burges, 1998; LeCun et al., 
2002)---showing how the package can be used to distinguish between images of the
digits 2 and 3. Second, we apply the package to Fashion MNIST (Xiao, Rasul, and 
Vollgraf, 2017)---distinguishing among images of tops, trousers, and sandals. 
Third, we apply the package to VesselMNIST3D (Yang et al., 2020) from the 
MedMNIST database (Yang et al., 2023; Yang, Shi, Ni, 2021). VesselMNIST3D 
contains three-dimensional representations of blood vessels, and we distinguish 
healthy blood vessels from aneurysm blood vessels. Finally, we apply the package 
to OrganMNIST3D (Bilic et al., 2023; Xu et al., 2019) from the MedMNIST database 
(Yang et al., 2023; Yang, Shi, Ni, 2021). OrganMNIST3D contains 
three-dimensional representations of abdominal organs, and we distinguish among 
four organs. For this project, the source file `mcrd.Rmd` contains original text 
and code used to produce the two reports `mcrd.pdf` and `mcrd.html`, which both 
contain results.

## License

This project is dual-licensed. All code and text, including the `mcrd.Rmd` 
source file and the `convert_npz_to_h5.py` file, is licensed under the MIT 
license. See the `LICENSE` file for details. Generated reports (`mcrd.pdf` and 
`mcrd.html`), as derivative works of the MNIST dataset, are licensed under the 
Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) license.

## R packages

This project uses the R programming language (R Core Team, 2025). In addition, 
this project directly uses four R packages found on The Comprehensive R Archive 
Network (CRAN) and one R package found on Bioconductor. Packages include: 
**cpfa** (Asisgress, 2026), **dslabs** (Irizarry and Gill, 2025), **keras3** 
(Kalinowski, Allaire, and Chollet, 2025), **rhdf5** (Fischer, Smith, and Pau, 
2025), and **plotly** (Sievert, 2020). Note that R package **cpfa** depends on 
R package **multiway** (Helwig, 2025), which itself depends on **CMLS** (Helwig, 
2025).

## Data

This project uses four datasets. First, it uses MNIST (LeCun, Cortes, and 
Burges, 1998; LeCun et al., 2002). Yann LeCun and Corinna Cortes hold the 
copyright of the MNIST dataset, which is a derivative work from the original 
NIST datasets. MNIST is made available under the terms of the CC BY-SA 3.0 
license, which can be viewed here: 
<https://creativecommons.org/licenses/by-sa/3.0/deed.en>. Second, this project 
uses Fashion MNIST (Xiao, Rasul, and Vollgraf, 2017). Zalando SE holds the 
copyright for Fashion MNIST, and the associated MIT license for this dataset can 
be found at the end of this README. Third, this project uses VesselMNIST3D 
(Yang et al., 2020) from the MedMNIST database (Yang et al., 2023; Yang, Shi, 
Ni, 2021). VesselMNIST3D is made available under the terms of the Creative 
Commons Attribution 4.0 International (CC BY 4.0) license, which can be viewed 
here: <https://creativecommons.org/licenses/by/4.0/deed.en>. Finally, this 
project uses OrganMNIST3D (Bilic et al., 2023; Xu et al., 2019) from the 
MedMNIST database (Yang et al., 2023; Yang, Shi, Ni, 2021). OrganMNIST3D is also 
made available under the terms of the CC BY 4.0 license.

MNIST and Fashion MNIST are downloaded when `mcrd.Rmd` runs. VesselMNIST3D and 
OrganMNIST3D are provided in the project GitHub repository in both their 
original .npz file format and new .h5 file format. Specifically, the Python 
script 'convert_npz_to_h5.py' was used to convert VesselMNIST3D and OrganMNIST3D 
from .npz to .h5. This script is made available in the project repository. When 
`mcrd.Rmd` runs, it subsets a given dataset, builds a classification rule 
between data and class labels, and provides summaries of these analyses. Results 
can be viewed within output files `mcrd.pdf` or `mcrd.html`.

## References

Asisgress, M. (2026). cpfa: Classification with Parallel Factor Analysis. 
R package version 1.2-6. <https://CRAN.R-project.org/package=cpfa>.

Bilic, P., Christ, P., Li, H., Vorontsov, E., Ben-Cohen, A., Kaissis, G., ...
and Menze, B. (2023). The liver tumor segmentation benchmark (lits). Medical 
Image Analysis, 84, 102680.

Fischer, B., Smith, M., and Pau, G. (2025). rhdf5: R Interface to HDF5. 
R package version 2.54.1, <https://bioconductor.org/packages/rhdf5>.

Helwig, N. (2025). CMLS: Constrained Multivariate Least Squares.
R package version 1.1, <https://CRAN.R-project.org/package=CMLS>.

Helwig, N. (2025). multiway: Component Models for Multi-Way Data. 
R package version 1.0-7, <https://CRAN.R-project.org/package=multiway>.

Irizarry, R., Gill, A. (2025). dslabs: Data Science Labs.
R package version 0.9.1, <https://CRAN.R-project.org/package=dslabs>.

Kalinowski, T., Allaire, J., and Chollet, F. (2025). keras3: R Interface to 
'Keras'. R package version 1.5.0, <https://CRAN.R-project.org/package=keras3>.

LeCun, Y., Bottou, L., Bengio, Y., and Haffner, P. (2002). Gradient-based 
learning applied to document recognition. Proceedings of the IEEE, 86(11), 
2278–2324. <https://doi.org/10.1109/5.726791>.

LeCun, Y., Cortes, C., and Burges, C. (1998). The MNIST database of handwritten 
digits. <http://yann.lecun.com/exdb/mnist/>.

R Core Team (2025). R: A Language and Environment for Statistical Computing. R 
Foundation for Statistical Computing, Vienna, Austria. 
<https://www.R-project.org/>.

Sievert, C. (2020). Interactive web-based data visualization with R, plotly, 
and shiny. Chapman and Hall/CRC.

Xiao, H., Rasul, K., and Vollgraf, R. (2017). Fashion-mnist: a novel image 
dataset for benchmarking machine learning algorithms. arXiv preprint 
arXiv:1708.07747.

Xu, X., Zhou, F., Liu, B., Fu, D., and Bai, X. (2019). Efficient multiple organ 
localization in CT image using 3D region proposal network. IEEE Transactions on 
Medical Imaging, 38(8), 1885-1898.

Yang, J., Shi, R., and Ni, B. (April 2021). Medmnist classification decathlon: 
A lightweight automl benchmark for medical image analysis. In 2021 IEEE 18th 
International Symposium on Biomedical Imaging (ISBI) (pp. 191-195). IEEE.

Yang, J., Shi, R., Wei, D., Liu, Z., Zhao, L., Ke, B., ... and Ni, B. (2023). 
Medmnist v2-a large-scale lightweight benchmark for 2d and 3d biomedical image 
classification. Scientific Data, 10(1), 41.

Yang, X., Xia, D., Kin, T., and Igarashi, T. (2020). Intra: 3d intracranial 
aneurysm dataset for deep learning. In Proceedings of the IEEE/CVF conference 
on computer vision and pattern recognition (pp. 2656-2666).

## Fashion MNIST License

The MIT License (MIT) Copyright © 2017 Zalando SE, https://tech.zalando.com 
Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the “Software”), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of 
the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS 
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER 
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.