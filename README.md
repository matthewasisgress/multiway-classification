# multiway-classification
Application of the R package **cpfa** to the MNIST and Fashion MNIST datasets. A 
demonstration of multiway classification with real data.

Author: Matthew Asisgress

## License

This project is dual-licensed. R code, including the `mcrd.Rmd` source file, 
is licensed under the MIT license. See the `LICENSE` file for details. The 
generated report (`mcrd.pdf`), as a derivative work of the MNIST dataset, is 
licensed under the Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) 
license.

## R packages

This project uses the R programming language (R Core Team, 2025). In addition, 
this project uses three R packages found on The Comprehensive R Archive Network 
(i.e., CRAN) including: **cpfa** (Asisgress, 2025), **dslabs** (Irizarry and 
Gill, 2025), and **keras3** (Kalinowski, Allaire, and Chollet, 2025). Note that 
R package **cpfa** depends on R package **mulitway** (Helwig, 2025), which 
itself depends on R package **CMLS** (Helwig, 2025).

## Data

This project uses the MNIST dataset (LeCun, Cortes, and Burges, 1998; LeCun 
et al., 2002). Yann LeCun and Corinna Cortes hold the copyright of the MNIST 
dataset, which is a derivative work from original NIST datasets. The MNIST 
dataset is made available under the terms of the CC BY-SA 3.0 license, which can 
be viewed here: <https://creativecommons.org/licenses/by-sa/3.0/deed.en>. 
Moreover, this project uses the Fashion MNIST dataset (Xiao, Rasul, and 
Vollgraf, 2017). Zalando SE holds the copyright for the Fashion MNIST dataset,
and the associated MIT license for this dataset can be found at the end of this
README. Note that both datasets are automatically downloaded when `mcrd.Rmd` 
runs.

## References

Asisgress, M. (2025). cpfa: Classification with Parallel Factor Analysis. 
R package version 1.2-2, <https://CRAN.R-project.org/package=cpfa>.

Helwig, N. (2025). CMLS: Constrained Multivariate Least Squares.
R package version 1.1, <https://CRAN.R-project.org/package=CMLS>.

Helwig, N. (2025). multiway: Component Models for Multi-Way Data. 
R package version 1.0-7, <https://CRAN.R-project.org/package=multiway>.

Irizarry, R., Gill, A. (2025). dslabs: Data Science Labs.
R package version 0.9.0, <https://CRAN.R-project.org/package=dslabs>.

Kalinowski, T., Allaire, J., and Chollet, F. (2025). keras3: R Interface to 
'Keras'. R package version 1.4.0, <https://CRAN.R-project.org/package=keras3>.

LeCun, Y., Bottou, L., Bengio, Y., and Haffner, P. (2002). Gradient-based 
learning applied to document recognition. Proceedings of the IEEE, 86(11), 
2278–2324. <https://doi.org/10.1109/5.726791>.

LeCun, Y., Cortes, C., and Burges, C. (1998). The MNIST database of handwritten 
digits. <http://yann.lecun.com/exdb/mnist/>.

R Core Team (2025). R: A Language and Environment for Statistical Computing. R 
Foundation for Statistical Computing, Vienna, Austria. 
<https://www.R-project.org/>.

Xiao, H., Rasul, K., and Vollgraf, R. (2017). Fashion-mnist: a novel image 
dataset for benchmarking machine learning algorithms. arXiv preprint 
arXiv:1708.07747.

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